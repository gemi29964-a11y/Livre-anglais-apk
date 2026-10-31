#!/usr/bin/env python3
"""Scripts de production des voix (Plan 7.8), générés depuis le corpus.

Usage :
  python3 tools/scripts_voix.py corpus/c01/s01.yaml [--sortie voix/scripts]
Produit un fichier JSONL par voix et par scène : voix/scripts/{scene}/{voix}.jsonl, une ligne par
énoncé et par rythme (careful puis natural), plus les sens français pour FR-F1.
L'attribution des voix suit 7.4 : chaque expression reçoit une voix principale par accent, la même pour
ses énoncés et ses déclinaisons et pour les deux rythmes (7.1.4) ; les répliques de la scène vivante
reçoivent la voix de leur personnage (corpus/personnages.yaml).
"""
from __future__ import annotations
import argparse, json, pathlib, re, sys
import yaml

RACINE = pathlib.Path(__file__).resolve().parent.parent
VOIX = {"uk": ["UK-F1", "UK-M1", "UK-F2", "UK-M2"], "us": ["US-F1", "US-M1", "US-F2", "US-M2"]}
REGISTRE = {"courant": "everyday", "complice": "casual", "cru": "slang", "soutenu": "formal"}
RYTHMES = [("pose", "careful"), ("spontane", "natural")]

# Réductions de l'oral que la voix peut réaliser en spontané (7.7, texte de jeu) ; le texte affiché ne change pas.
JEU_SPONTANE = [
    (r"\bgoing to (?=[a-z])", "gonna "), (r"\bwant to\b", "wanna"),
]

def personnages():
    p = yaml.safe_load((RACINE / "corpus" / "personnages.yaml").read_text(encoding="utf-8"))
    return p.get("personnages", p)

def sans_balises(t: str) -> str:
    return re.sub(r"</?en>", "", t)

def texte_jeu(t: str) -> str | None:
    s = t
    for a, b in JEU_SPONTANE:
        s = re.sub(a, b, s)
    return s if s != t else None

def lignes(scene: dict):
    pers = personnages()
    rang = 0
    for m in scene["moments"]:
        for x in m["expressions"]:
            voix = {a: VOIX[a][rang % 4] for a in VOIX}
            rang += 1
            reg = REGISTRE[x["ton"]]
            for e in x["enonces"]:
                for a in ("uk", "us"):
                    for ry, nom in RYTHMES:
                        l = {"line_id": e["id"], "voice": voix[a], "accent": a, "text": e["texte"][a],
                             "context": e["jeu"]["contexte"], "emotion": e["jeu"]["emotion"], "register": reg,
                             "rhythm": nom, "rythme": ry, "genre": "enonce"}
                        if ry == "spontane" and (tj := texte_jeu(e["texte"][a])):
                            l["play_text"] = tj
                        yield l
            ctx = x["enonces"][0]["jeu"]
            for d in x["declinaisons"]:
                for a in ("uk", "us"):
                    for ry, nom in RYTHMES:
                        l = {"line_id": d["id"], "voice": voix[a], "accent": a, "text": d["texte"][a],
                             "context": f"Variation on the same pattern. {ctx['contexte']}", "emotion": "natural, everyday",
                             "register": reg, "rhythm": nom, "rythme": ry, "genre": "declinaison"}
                        if ry == "spontane" and (tj := texte_jeu(d["texte"][a])):
                            l["play_text"] = tj
                        yield l
            yield {"line_id": x["id"], "voice": "FR-F1", "accent": "fr", "text": sans_balises(x["sens"]),
                   "context": "Sens français de l'expression, dit naturellement, dans le ton de l'expression.",
                   "emotion": {"courant": "naturel", "complice": "souriant", "cru": "franc", "soutenu": "posé"}[x["ton"]],
                   "rhythm": "sens", "rythme": "sens", "genre": "sens"}
    sv = scene["sceneVivante"]["repliques"]
    for i, r in enumerate(sv):
        fiche = pers.get(r["personnage"], {})
        for a in ("uk", "us"):
            v = (fiche.get("voix") or {}).get(a)
            for ry, nom in RYTHMES:
                l = {"line_id": r["id"], "voice": v, "accent": a, "text": r["texte"][a],
                     "context": f"Live scene, {r['personnage']} speaking.", "emotion": r["emotion"], "register": "everyday",
                     "rhythm": nom, "rythme": ry, "genre": "replique",
                     "scene_partner": sv[i - 1]["personnage"] if i else sv[1]["personnage"]}
                yield l
        yield {"line_id": r["id"], "voice": "FR-F1", "accent": "fr", "text": sans_balises(r["sens"]),
               "context": "Sens français de la réplique.", "emotion": "naturel", "rhythm": "sens", "rythme": "sens",
               "genre": "sens"}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("scene"); ap.add_argument("--sortie", default=str(RACINE / "voix" / "scripts"))
    a = ap.parse_args()
    scene = yaml.safe_load(open(a.scene, encoding="utf-8"))
    out = pathlib.Path(a.sortie) / scene["id"]; out.mkdir(parents=True, exist_ok=True)
    par_voix: dict[str, list] = {}
    for l in lignes(scene):
        par_voix.setdefault(l["voice"] or "SANS-VOIX", []).append(l)
    for v, ls in sorted(par_voix.items()):
        with open(out / f"{v}.jsonl", "w", encoding="utf-8") as f:
            for l in ls:
                f.write(json.dumps(l, ensure_ascii=False) + "\n")
    print(json.dumps({v: len(ls) for v, ls in sorted(par_voix.items())}, ensure_ascii=False))
    if "SANS-VOIX" in par_voix:
        sys.exit("personnage sans voix attitrée dans corpus/personnages.yaml")

if __name__ == "__main__":
    main()
