#!/usr/bin/env python3
"""Découpe une génération groupée (plusieurs énoncés séparés par des silences) en un fichier par énoncé.

Chaque énoncé reste une seule coulée de voix (7.1.7) : on coupe uniquement dans les silences qui séparent
les énoncés, jamais à l'intérieur d'un énoncé.

Méthode (D-040) : la génération entière est transcrite (Whisper, horodatage par mot) ; les mots entendus
sont alignés sur la suite des textes attendus. Pour deux énoncés consécutifs, la frontière est le plus long
silence situé entre le dernier mot du premier et le premier mot du second. Un énoncé dont aucun mot n'est
retrouvé (omis par le moteur) est déclaré manquant : il sera recréé, jamais comblé. Chaque segment est
ensuite contrôlé isolément par controler.py (texte, accent, naturel…).

Repli sans transcription (`--sans-asr`) : les n−1 plus longs silences, rejet si le compte ne tombe pas juste.
"""
from __future__ import annotations
import difflib, json, os, sys
import numpy as np, soundfile as sf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

PAS = 0.01


def trames(x, sr, pas=PAS):
    h = int(sr * pas); n = len(x) // h
    e = np.sqrt(np.mean(x[: n * h].reshape(n, h) ** 2, axis=1) + 1e-12)
    return 20 * np.log10(e), h


def activite(x, sr):
    db, h = trames(x, sr)
    ref = np.percentile(db, 95)
    return db > max(ref - 40, -55), h


def silences(actif, min_trames=1):
    sil, i = [], 0
    while i < len(actif):
        if not actif[i]:
            j = i
            while j < len(actif) and not actif[j]:
                j += 1
            if i > 0 and j < len(actif) and j - i >= min_trames:
                sil.append((i, j))
            i = j
        else:
            i += 1
    return sil


def extraire(x, actif, h, bornes, marge_avant=0.10, marge_apres=0.25):
    """bornes : [(debut_trame, fin_trame, lim_gauche, lim_droite)] → segments avec marges prises dans le silence."""
    out = []
    for a, b, la, lb in bornes:
        s0 = max(la, a - int(marge_avant / PAS)) * h
        s1 = min(lb, b + int(marge_apres / PAS)) * h
        out.append(x[s0:s1].copy())
    return out


def decouper_silences(x, sr, n, silence_min=0.35):
    actif, h = activite(x, sr)
    sil = [s for s in silences(actif) if (s[1] - s[0]) * PAS >= silence_min]
    if len(sil) < n - 1:
        raise ValueError(f"{len(sil)+1} segments trouvés pour {n} énoncés")
    choisis = sorted(sorted(sil, key=lambda s: s[1] - s[0], reverse=True)[: n - 1])
    idx = np.flatnonzero(actif)
    cuts = [(a + b) // 2 for a, b in choisis]
    starts = [idx[0]] + [b for _, b in choisis]
    ends = [a for a, _ in choisis] + [idx[-1] + 1]
    lims = [0] + cuts + [len(actif)]
    return extraire(x, actif, h, [(starts[k], ends[k], lims[k], lims[k + 1]) for k in range(n)]), [None] * n


def decouper_asr(x, sr, textes, M=None, langue="en"):
    """Retourne (segments, diagnostics). segments[k] vaut None si l'énoncé k est introuvable."""
    import controler as C
    import scipy.signal as ss
    if M is None:
        M = C.Modeles(avec=("whisper",))
    x16 = ss.resample_poly(x, 16000, sr).astype("float32") if sr != 16000 else x.astype("float32")
    _, mots = M.transcrire(x16, langue)
    # jetons entendus → indice du mot Whisper
    hyp, hyp_mot = [], []
    for k, (w, t0, t1, _) in enumerate(mots):
        for tok in C.normaliser(w, langue):
            hyp.append(tok); hyp_mot.append(k)
    att, att_ligne = [], []
    for i, t in enumerate(textes):
        for tok in C.normaliser(t, langue):
            att.append(tok); att_ligne.append(i)
    sm = difflib.SequenceMatcher(a=att, b=hyp, autojunk=False)
    t_deb = [None] * len(textes); t_fin = [None] * len(textes); couverts = [0] * len(textes)
    ligne_mot = {}  # mot Whisper → énoncé auquel l'alignement le rattache
    for blk in sm.get_matching_blocks():
        for d in range(blk.size):
            i = att_ligne[blk.a + d]; w = mots[hyp_mot[blk.b + d]]
            ligne_mot[hyp_mot[blk.b + d]] = i
            couverts[i] += 1
            t_deb[i] = w[1] if t_deb[i] is None else min(t_deb[i], w[1])
            t_fin[i] = w[2] if t_fin[i] is None else max(t_fin[i], w[2])
    actif, h = activite(x, sr)
    sil = silences(actif)
    presents = [i for i in range(len(textes)) if t_deb[i] is not None]
    # frontières entre énoncés présents consécutifs
    coupe = {}
    for u, v in zip(presents, presents[1:]):
        g, d = int(t_fin[u] / PAS), int(t_deb[v] / PAS)
        cand = [s for s in sil if s[1] > g - 15 and s[0] < d + 15]
        if cand:
            a, b = max(cand, key=lambda s: s[1] - s[0])
        else:
            a = b = (g + d) // 2
        coupe[(u, v)] = (a, b)
    idx = np.flatnonzero(actif)
    segments, diag = [None] * len(textes), []
    asr = [None] * len(textes)
    for n, i in enumerate(presents):
        prev = presents[n - 1] if n else None; nxt = presents[n + 1] if n + 1 < len(presents) else None
        debut = coupe[(prev, i)][1] if prev is not None else int(idx[0])
        fin = coupe[(i, nxt)][0] if nxt is not None else int(idx[-1] + 1)
        la = (sum(coupe[(prev, i)]) // 2) if prev is not None else 0
        lb = (sum(coupe[(i, nxt)]) // 2) if nxt is not None else len(actif)
        segments[i] = extraire(x, actif, h, [(debut, fin, la, lb)])[0]
        s0 = max(la, debut - int(0.10 / PAS)) * h / sr; s1 = min(lb, fin + int(0.25 / PAS)) * h / sr
        dedans = [w for k, w in enumerate(mots) if ligne_mot.get(k, -1) == i
                  or (k not in ligne_mot and s0 <= (w[1] + w[2]) / 2 < s1)]
        asr[i] = (" ".join(w[0] for w in dedans), [(w[0], round(w[1] - s0, 3), round(w[2] - s0, 3), w[3]) for w in dedans])
    for i, t in enumerate(textes):
        n_att = len(C.normaliser(t, langue))
        diag.append({"i": i, "mots_attendus": n_att, "mots_retrouves": couverts[i],
                     "debut": t_deb[i], "fin": t_fin[i], "present": t_deb[i] is not None,
                     "asr": asr[i][0] if asr[i] else None, "mots": asr[i][1] if asr[i] else None})
    return segments, diag


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("audio"); ap.add_argument("lignes", help="JSONL : {id, text|texte} dans l'ordre de la génération")
    ap.add_argument("dossier"); ap.add_argument("--langue", default="en"); ap.add_argument("--sans-asr", action="store_true")
    a = ap.parse_args()
    L = [json.loads(l) for l in open(a.lignes, encoding="utf-8") if l.strip()]
    textes = [l.get("text") or l.get("texte") for l in L]
    x, sr = sf.read(a.audio, dtype="float32", always_2d=True); x = x.mean(axis=1)
    os.makedirs(a.dossier, exist_ok=True)
    if a.sans_asr:
        segs, diag = decouper_silences(x, sr, len(L))
    else:
        segs, diag = decouper_asr(x, sr, textes, langue=a.langue)
    manquants = []
    for l, s in zip(L, segs):
        if s is None:
            manquants.append(l["id"]); continue
        sf.write(os.path.join(a.dossier, f"{l['id']}.wav"), s, sr, subtype="PCM_16")
    print(json.dumps({"segments": len(L) - len(manquants), "manquants": manquants, "diag": diag}, ensure_ascii=False))
