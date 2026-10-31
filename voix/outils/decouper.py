#!/usr/bin/env python3
"""Découpe une génération groupée (plusieurs énoncés séparés par des silences) en un fichier par énoncé.

Chaque énoncé reste une seule coulée de voix (7.1.7) : on coupe uniquement dans les silences qui séparent
les énoncés, jamais à l'intérieur d'un énoncé. Les n−1 plus longs silences sont retenus comme frontières ;
si le nombre de segments obtenus ne correspond pas au nombre d'énoncés attendus, la génération est rejetée.
La vérification de la correspondance texte ↔ segment est faite ensuite par la transcription (controler.py).
"""
from __future__ import annotations
import numpy as np, soundfile as sf

def trames(x, sr, pas=0.01):
    h = int(sr * pas); n = len(x) // h
    e = np.sqrt(np.mean(x[: n * h].reshape(n, h) ** 2, axis=1) + 1e-12)
    return 20 * np.log10(e), h

def decouper(x: np.ndarray, sr: int, n: int, marge_avant=0.10, marge_apres=0.25, silence_min=0.35):
    db, h = trames(x, sr)
    ref = np.percentile(db, 95)
    actif = db > max(ref - 40, -55)
    # silences : suites de trames inactives
    sil, i = [], 0
    while i < len(actif):
        if not actif[i]:
            j = i
            while j < len(actif) and not actif[j]:
                j += 1
            if i > 0 and j < len(actif):
                sil.append((j - i, i, j))
            i = j
        else:
            i += 1
    sil = [s for s in sil if s[0] * h / sr >= silence_min]
    if len(sil) < n - 1:
        raise ValueError(f"{len(sil)+1} segments trouvés pour {n} énoncés")
    choisis = sorted(sorted(sil, reverse=True)[: n - 1], key=lambda s: s[1])
    idx = np.flatnonzero(actif)
    bornes, debut = [], idx[0]
    for _, a, b in choisis:
        bornes.append((debut, a)); debut = b
    bornes.append((debut, idx[-1] + 1))
    out = []
    for k, (a, b) in enumerate(bornes):
        # marges prises dans le silence voisin, sans jamais déborder sur l'énoncé suivant ou précédent
        lim_a = 0 if k == 0 else (choisis[k - 1][1] + choisis[k - 1][2]) // 2
        lim_b = len(actif) if k == len(bornes) - 1 else (choisis[k][1] + choisis[k][2]) // 2
        s0 = max(lim_a, a - int(marge_avant / 0.01)) * h
        s1 = min(lim_b, b + int(marge_apres / 0.01)) * h
        out.append(x[s0:s1].copy())
    return out

if __name__ == "__main__":
    import argparse, json, os
    ap = argparse.ArgumentParser(); ap.add_argument("audio"); ap.add_argument("ids"); ap.add_argument("dossier")
    a = ap.parse_args()
    ids = [l.strip() for l in open(a.ids) if l.strip()]
    x, sr = sf.read(a.audio, dtype="float32", always_2d=True); x = x.mean(axis=1)
    os.makedirs(a.dossier, exist_ok=True)
    for i, seg in zip(ids, decouper(x, sr, len(ids))):
        sf.write(os.path.join(a.dossier, f"{i}.wav"), seg, sr, subtype="PCM_16")
    print(json.dumps({"segments": len(ids)}))
