#!/usr/bin/env python3
"""Écrit le script d'essai de chaque candidat (7.4) : voix/scripts/essai/{candidat}.jsonl, format 7.8.

Voix anglaises : les 40 lignes de script_essai.yaml, chacune en posé puis en spontané.
Voix du sens : 40 sens de la scène étalon (c01.s01), dits une fois chacun.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
import yaml

RACINE = Path(__file__).resolve().parents[2]
REGISTRE = {"courant": "everyday", "complice": "casual", "cru": "slang", "soutenu": "formal"}


def sens_scene(scene="c01/s01"):
    d = yaml.safe_load((RACINE / f"corpus/{scene}.yaml").read_text(encoding="utf-8"))
    out = []
    for m in d["moments"]:
        for x in m["expressions"]:
            out.append({"id": x["id"], "sens": x["sens"], "ton": x.get("ton", "courant")})
    return out


def main():
    S = yaml.safe_load((RACINE / "voix/scripts/essai/script_essai.yaml").read_text(encoding="utf-8"))["lignes"]
    assert len(S) == 40, len(S)
    dossier = RACINE / "voix/scripts/essai"
    for p in sorted((RACINE / "voix/fiches/candidats").glob("*.yaml")):
        f = yaml.safe_load(p.read_text(encoding="utf-8"))
        cid = f["id"]; lignes = []
        if f["accent"].startswith("fr"):
            sens = sens_scene()
            # 40 sens répartis sur toute la scène, tons variés
            pas = len(sens) / 40
            for k in range(40):
                s = sens[int(k * pas)]
                lignes.append({"line_id": f"essai.{s['id']}", "voice": cid, "accent": "fr", "text": s["sens"],
                               "context": "Explaining to a French friend what an English expression means.",
                               "emotion": "natural, warm" if s["ton"] == "courant" else "natural, with a smile",
                               "register": REGISTRE.get(s["ton"], "everyday"), "rhythm": "natural", "rythme": "sens",
                               "genre": "sens"})
        else:
            acc = "uk" if f["accent"] == "en-GB" else "us"
            for l in S:
                for ry, rh in (("pose", "careful"), ("spontane", "natural")):
                    o = {"line_id": f"essai.{l['id']}", "voice": cid, "accent": acc, "text": l[acc],
                         "context": l["contexte"], "emotion": l["emotion"], "register": REGISTRE[l["ton"]],
                         "rhythm": rh, "rythme": ry, "genre": "essai", "trait": l["trait"]}
                    if ry == "spontane" and l.get(f"spontane_{acc}"):
                        o["play_text"] = l[f"spontane_{acc}"]
                    lignes.append(o)
        (dossier / f"{cid}.jsonl").write_text("".join(json.dumps(o, ensure_ascii=False) + "\n" for o in lignes),
                                              encoding="utf-8")
    print(json.dumps({"candidats": len(list((RACINE / 'voix/fiches/candidats').glob('*.yaml')))}))


if __name__ == "__main__":
    sys.exit(main())
