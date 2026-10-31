#!/usr/bin/env python3
"""Bilan de l'épreuve par candidat : lignes acceptées par rythme, prises, réussite en 1re prise, causes de refus."""
import json, collections, re, sys
from pathlib import Path
R = [json.loads(l) for l in open(Path(__file__).resolve().parents[1] / "registre/creations.jsonl", encoding="utf-8")]
filtre = re.compile(sys.argv[1]) if len(sys.argv) > 1 else None
par = collections.defaultdict(list)
for r in R:
    if r["line_id"].startswith("essai.") and (not filtre or filtre.search(r["voix"])):
        par[(r["voix"], r["rythme"])].append(r)
for (v, ry), L in sorted(par.items()):
    acc = {r["line_id"] for r in L if r["statut"] == "acceptee"}
    pre = [r for r in L if r["tentative"] == min(x["tentative"] for x in L if x["line_id"] == r["line_id"])]
    causes = collections.Counter()
    for r in L:
        for b in r.get("bloquants") or []:
            causes[b.split(" ")[0]] += 1
    ut = [r["mesures"]["utmos"] for r in L if r["statut"] == "acceptee"]
    print(f"{v:10s} {ry:8s} lignes_ok={len(acc):2d}/40 prises={len(L):3d} 1re={sum(r['statut']=='acceptee' for r in pre)}/{len(pre)} "
          f"utmos={sum(ut)/len(ut) if ut else 0:.2f} causes={dict(causes.most_common(5))}")
