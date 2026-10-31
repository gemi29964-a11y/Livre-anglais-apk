#!/usr/bin/env python3
"""Production des voix créées (7.5, 7.8, 7.9) — interface unique, un adaptateur par moteur.

Le registre `voix/registre/creations.jsonl` consigne chaque prise : identifiant d'énoncé, voix, moteur, version,
réglages, graine (ou rang de tentative), texte envoyé, indication de jeu, empreinte SHA-256, verdict du contrôle.
Toutes les commandes sont reprenables sans doublon : un énoncé dont une prise est acceptée n'est jamais recréé.

Moteurs
  gemini  — Gemini 2.5 Pro TTS (voix intégrée de l'environnement). L'appel se fait hors de Python (outil de
            synthèse de la plateforme) : `preparer` écrit les lots (texte d'appel + lignes), `integrer` découpe la
            génération reçue, contrôle chaque segment et l'inscrit.
  kokoro  — Kokoro v1.0 (Apache 2.0) via kokoro-onnx, exécuté localement : `kokoro` crée, contrôle et inscrit.

Usage
  creer.py preparer --script voix/scripts/c01.s01/UK-F1.jsonl --rythme pose [--taille 12]
  creer.py integrer --lot voix/travail/<lot> --audio <fichier rendu>
  creer.py etat [--scene c01.s01]
"""
from __future__ import annotations
import argparse, datetime as dt, hashlib, json, os, shutil, sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
RACINE = ICI.parents[1]
sys.path.insert(0, str(ICI))
REGISTRE = RACINE / "voix/registre/creations.jsonl"
TRAVAIL = RACINE / "voix/travail"           # lots en cours (hors dépôt)
PRISES = RACINE / "voix/prises"             # prises acceptées, WAV natif (hors dépôt)
FICHES = RACINE / "voix/fiches"

GEMINI = {"nom": "gemini-2.5-pro-tts", "version": "gemini-2.5-pro-preview-tts (outil de synthèse intégré, figé au 2026-10-31)"}
TAILLE_MAX_OCTETS = 3900


def maintenant():
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def lire_jsonl(p):
    p = Path(p)
    if not p.exists():
        return []
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]


def ajouter_registre(o):
    REGISTRE.parent.mkdir(parents=True, exist_ok=True)
    with open(REGISTRE, "a", encoding="utf-8") as f:
        f.write(json.dumps(o, ensure_ascii=False) + "\n")


def cle(line_id, voix, rythme):
    return f"{line_id}|{voix}|{rythme}"


def acceptees():
    return {cle(o["line_id"], o["voix"], o["rythme"]): o for o in lire_jsonl(REGISTRE) if o.get("statut") == "acceptee"}


def tentatives():
    n = {}
    for o in lire_jsonl(REGISTRE):
        k = cle(o["line_id"], o["voix"], o["rythme"]); n[k] = n.get(k, 0) + 1
    return n


def fiche(voix):
    import yaml
    p = FICHES / f"{voix}.yaml"
    if p.exists():
        return yaml.safe_load(p.read_text(encoding="utf-8"))
    p = FICHES / "candidats" / f"{voix}.yaml"
    return yaml.safe_load(p.read_text(encoding="utf-8"))


# ------------------------------------------------------------------ Gemini : texte d'appel
RYTHMES_EN = {
    "pose": ("Careful pace, about 130 words per minute: say each line clearly and unhurriedly, as if to someone you "
             "want to be sure understands you, without treating them like a child. Natural weak forms and the "
             "contractions of writing; light pauses only between word groups. Never sound like a textbook, never "
             "over-articulate the small words."),
    "spontane": ("Natural fast pace, about 190 words per minute: say each line the way you would to a friend in real "
                 "life, without thinking about it. Weak forms and connected speech pushed, the reductions of speech "
                 "where written, no pause inside a line except for acting. Never rushed artificially, never swallowed "
                 "so much that a native speaker could not follow."),
    "sens": ("Natural, warm, unhurried French, never didactic; in the tone of the expression it explains."),
}


def texte_appel(f, lignes, rythme):
    desc = " ".join(f["description"].split())
    regle = ("Speak only the quoted lines, in order. Each line is preceded by an acting note in square brackets: use "
             "it to act the line, never read it aloud. Leave a two-second silence between lines.")
    if rythme == "sens":
        tete = f"Voice direction (do not read aloud): {desc} {RYTHMES_EN['sens']} {regle} The lines are in French.\n\n"
    else:
        tete = f"Voice direction (do not read aloud): {desc} {RYTHMES_EN[rythme]} {regle}\n\n"
    corps = []
    for l in lignes:
        note = " ".join(x.strip().rstrip(".") + "." for x in (l.get("context"), l.get("emotion"), l.get("pronunciation_note")) if x)
        dit = l.get("play_text") or l["text"]
        corps.append(f"[{note}] \"{dit}\"")
    return tete + "\n\n".join(corps)


def preparer(a):
    L = [l for l in lire_jsonl(a.script) if l["rythme"] == a.rythme]
    if not L:
        print(json.dumps({"lots": []})); return
    voix = L[0]["voice"]; f = fiche(voix)
    deja = acceptees(); nt = tentatives()
    reste = [l for l in L if cle(l["line_id"], voix, a.rythme) not in deja]
    # lots en cours non intégrés : leurs lignes ne sont pas reprises en double
    en_cours = set()
    for d in TRAVAIL.glob("*/lot.json"):
        o = json.loads(d.read_text(encoding="utf-8"))
        if not o.get("integre") and o["voix"] == voix and o["rythme"] == a.rythme:
            en_cours |= {l["line_id"] for l in o["lignes"]}
    reste = [l for l in reste if l["line_id"] not in en_cours]
    lots, cur = [], []
    for l in reste:
        essai = cur + [l]
        if cur and (len(essai) > a.taille or len(texte_appel(f, essai, a.rythme).encode()) > TAILLE_MAX_OCTETS):
            lots.append(cur); cur = [l]
        else:
            cur = essai
    if cur:
        lots.append(cur)
    sortie = []
    for lot in lots:
        tent = max(nt.get(cle(l["line_id"], voix, a.rythme), 0) for l in lot) + 1
        nom = f"{voix}.{a.rythme}.{lot[0]['line_id']}.t{tent}"
        d = TRAVAIL / nom; d.mkdir(parents=True, exist_ok=True)
        t = texte_appel(f, lot, a.rythme)
        (d / f"{nom}.txt").write_text(t, encoding="utf-8")
        (d / "lot.json").write_text(json.dumps({"nom": nom, "voix": voix, "rythme": a.rythme, "moteur": GEMINI,
                                                 "voix_moteur": f["moteur"]["voix"], "tentative": tent,
                                                 "lignes": lot, "integre": False, "cree_le": maintenant()},
                                                ensure_ascii=False, indent=1), encoding="utf-8")
        sortie.append({"lot": str(d), "texte": str(d / f"{nom}.txt"), "voix_moteur": f["moteur"]["voix"], "n": len(lot)})
    print(json.dumps({"lots": sortie}, ensure_ascii=False))


def integrer(a):
    import soundfile as sf
    import controler as C
    import decouper as D
    d = Path(a.lot); o = json.loads((d / "lot.json").read_text(encoding="utf-8"))
    if o.get("integre"):
        print(json.dumps({"lot": o["nom"], "deja": True})); return
    f = fiche(o["voix"])
    audio = Path(a.audio)
    brut = d / f"{o['nom']}.brut{audio.suffix}"
    if audio.resolve() != brut.resolve():
        shutil.move(str(audio), brut)
    x, sr = sf.read(brut, dtype="float32", always_2d=True); x = x.mean(axis=1)
    langue = "fr" if o["rythme"] == "sens" else "en"
    M = C.Modeles()
    textes = [l.get("play_text") or l["text"] for l in o["lignes"]]
    segs, diag = D.decouper_asr(x, sr, textes, M=M, langue=langue)
    seuils = C.charger_seuils()
    ref = f.get("reference")
    ref = str(RACINE / ref) if ref and (RACINE / ref).exists() else None
    bilan = {"acceptees": 0, "refusees": 0, "manquantes": 0}
    for l, s, dg in zip(o["lignes"], segs, diag):
        base = {"line_id": l["line_id"], "voix": o["voix"], "rythme": o["rythme"], "moteur": o["moteur"]["nom"],
                "version": o["moteur"]["version"], "voix_moteur": o["voix_moteur"], "graine": None,
                "tentative": o["tentative"], "lot": o["nom"], "texte_envoye": l.get("play_text") or l["text"],
                "texte": l["text"], "jeu": {k: l.get(k) for k in ("context", "emotion", "register", "pronunciation_note")},
                "brut_sha256": sha256(brut), "horodatage": maintenant()}
        if s is None:
            ajouter_registre({**base, "statut": "manquante", "bloquants": ["énoncé omis par le moteur"]})
            bilan["manquantes"] += 1; continue
        cible = PRISES / o["voix"] / f"{l['line_id']}.{o['rythme']}.t{o['tentative']}.wav"
        cible.parent.mkdir(parents=True, exist_ok=True)
        sf.write(cible, s, sr, subtype="PCM_16")
        e = {"id": l["line_id"], "f": str(cible), "texte": l["text"], "voix": o["voix"],
             "accent": "fr" if langue == "fr" else l["accent"], "rythme": o["rythme"], "reference": ref,
             "asr_lot": dg.get("asr"), "mots_lot": dg.get("mots")}
        r = C.mesurer(M, e, seuils, avec_asr=True)
        r.pop("_emb", None)
        if o["rythme"] == "spontane" and r.get("nb_mots", 0) >= 4:
            # rapport de durée spontané / posé (7.7) contre la prise posée acceptée
            p = acceptees().get(cle(l["line_id"], o["voix"], "pose"))
            if p is None:
                r["bloquants"].append("rapport spontané/posé : aucune prise posée acceptée")
            else:
                dp = p["mesures"].get("parole") or p["mesures"]["d"]
                ds = r.get("parole") or r["d"]
                r["rapport_duree"] = round(ds / max(dp, 1e-3), 3)
                if not (0.55 <= r["rapport_duree"] <= 0.90):
                    r["bloquants"].append(f"rapport spontané/posé {r['rapport_duree']} hors 0,55–0,90")
        ok = not r["bloquants"]
        r["ok"] = ok
        ajouter_registre({**base, "statut": "acceptee" if ok else "refusee", "f": str(cible.relative_to(RACINE)),
                          "sha256": sha256(cible), "mesures": r, "bloquants": r["bloquants"]})
        bilan["acceptees" if ok else "refusees"] += 1
        if not ok:
            cible.unlink()
    o["integre"] = True; o["integre_le"] = maintenant(); o["bilan"] = bilan
    (d / "lot.json").write_text(json.dumps(o, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({"lot": o["nom"], **bilan}, ensure_ascii=False))


def etat(a):
    R = lire_jsonl(REGISTRE)
    par = {}
    for o in R:
        if a.scene and not o["line_id"].startswith(a.scene):
            continue
        k = (o["voix"], o["rythme"]); par.setdefault(k, {"acceptee": 0, "refusee": 0, "manquante": 0})
        par[k][o["statut"]] = par[k].get(o["statut"], 0) + 1
    print(json.dumps({f"{v}.{r}": c for (v, r), c in sorted(par.items())}, ensure_ascii=False, indent=1))


def main():
    ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("preparer"); p.add_argument("--script", required=True); p.add_argument("--rythme", required=True)
    p.add_argument("--taille", type=int, default=12)
    p = sp.add_parser("integrer"); p.add_argument("--lot", required=True); p.add_argument("--audio", required=True)
    p = sp.add_parser("etat"); p.add_argument("--scene")
    a = ap.parse_args()
    {"preparer": preparer, "integrer": integrer, "etat": etat}[a.cmd](a)


if __name__ == "__main__":
    main()
