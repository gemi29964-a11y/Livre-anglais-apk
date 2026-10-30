"""Chaîne de compilation du contenu (Plan, 10.5). Reprenable : chaque étape réécrit ses sorties.

Usage :
  python3 tools/construire.py               # publication : toute violation bloque, voix à 100 %
  python3 tools/construire.py --brouillon   # rédaction : manques signalés sans bloquer (D-014)

Étapes, dans l'ordre du Plan :
 1. valider_corpus.py   2. lexique_verifier.py   3. phrase_verifier.py
 4. YAML → JSON par scène (app/static/corpus/) + sommaire.json
 5. index_recherche (index-fr.json, index-en.json)
 6. contrôle de couverture vocale → pilotage/portes/rapport-couverture.md
 7. scripts des voix : sur demande, par tools/scripts_voix.py (Phase 2)
 8. itineraires.yaml, moments.yaml → JSON
 9. expression-du-jour.json (lu par l'écran d'accueil natif, 10.20)
"""
from __future__ import annotations

import argparse
import json
import pathlib
import shutil
import subprocess
import sys

import yaml

from commun import APP, CORPUS, RACINE

OUTILS = RACINE / "tools"
SORTIE = APP / "static/corpus"
ENCODES = RACINE / "voix/encodes"
ACCENTS, RYTHMES = ("uk", "us"), ("pose", "spontane")


def etape(nom: str, commande: list[str]) -> None:
    print(f"— {nom}")
    r = subprocess.run(commande, cwd=RACINE)
    if r.returncode:
        print(f"construire : arrêt à l’étape « {nom} »")
        sys.exit(r.returncode)


def nom_fichier(ident: str, accent: str, rythme: str) -> str:
    c, s, *reste = ident.split(".")
    return f"{c}{s}-{'-'.join(reste)}.{accent}.{rythme}.opus"


def nom_sens(ident: str) -> str:
    c, s, *reste = ident.split(".")
    return f"{c}{s}-{'-'.join(reste)}.fr.sens.opus"


def manifeste(ch: str, sc: str) -> dict:
    f = ENCODES / ch / sc / "manifeste.json"
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}


def couverture(scenes: dict[str, dict]) -> tuple[list[str], dict[str, float]]:
    """Étape 6 : quatre fichiers par énoncé, déclinaison et réplique ; voix du sens ; manifeste complet."""
    manques: list[str] = []
    taux: dict[str, float] = {}
    for sid, s in scenes.items():
        ch, sc = sid.split(".")
        man = manifeste(ch, sc).get("fichiers", {})
        attendus, presents = 0, 0
        elements = []
        for m in s["moments"]:
            for x in m["expressions"]:
                elements += [e["id"] for e in x["enonces"]] + [d["id"] for d in x["declinaisons"]]
                for porteur in [x] + x["declinaisons"]:
                    attendus += 1
                    nom = nom_sens(porteur["id"])
                    if (ENCODES / ch / sc / nom).exists():
                        presents += 1
                    else:
                        manques.append(f"{sid} : voix du sens absente — {nom}")
        elements += [r["id"] for r in s["sceneVivante"]["repliques"]]
        for ident in elements:
            for a in ACCENTS:
                for r in RYTHMES:
                    attendus += 1
                    nom = nom_fichier(ident, a, r)
                    entree = man.get(nom, {})
                    if (ENCODES / ch / sc / nom).exists() and all(k in entree for k in ("mots", "syllabes", "courbe")):
                        presents += 1
                    else:
                        manques.append(f"{sid} : {nom}")
        taux[sid] = 100.0 * presents / attendus if attendus else 100.0
    return manques, taux


def taille_chapitre(ch: str) -> int:
    d = ENCODES / ch
    return sum(f.stat().st_size for f in d.rglob("*.opus")) if d.exists() else 0


def main() -> int:
    sys.stdout.reconfigure(line_buffering=True)
    ap = argparse.ArgumentParser()
    ap.add_argument("--brouillon", action="store_true")
    ap.add_argument("--strict", action="store_true", help="publication : aucun avertissement toléré (10.14, annexe E)")
    ap.add_argument("--valider", action="store_true", help="étapes 1 à 3 seulement (rapport P1, 15.x)")
    a = ap.parse_args()
    if a.strict and a.brouillon:
        ap.error("--strict et --brouillon s'excluent")
    py = sys.executable
    drapeau = ["--brouillon"] if a.brouillon else (["--strict"] if a.strict else [])
    etape("1. validation du corpus", [py, str(OUTILS / "valider_corpus.py"), *drapeau])
    etape("2. lexique", [py, str(OUTILS / "lexique_verifier.py")])
    etape("3. phrasé", [py, str(OUTILS / "phrase_verifier.py")])
    if a.valider:
        print("construire : validations conformes")
        return 0

    print("— 4. corpus JSON et sommaire")
    if SORTIE.exists():
        shutil.rmtree(SORTIE)
    SORTIE.mkdir(parents=True)
    chapitres = yaml.safe_load((CORPUS / "chapitres.yaml").read_text(encoding="utf-8"))["chapitres"]
    personnages = yaml.safe_load((CORPUS / "personnages.yaml").read_text(encoding="utf-8"))["personnages"]
    scenes: dict[str, dict] = {}
    for f in sorted(CORPUS.glob("c[0-9][0-9]/s[0-9][0-9].yaml")):
        s = yaml.safe_load(f.read_text(encoding="utf-8"))
        ch = int(s["id"][1:3])
        s["chapitre"], s["numero"] = ch, int(s["id"][5:7])
        scenes[s["id"]] = s
        (SORTIE / f"{s['id']}.json").write_text(json.dumps(s, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    sommaire = {"chapitres": []}
    for c in chapitres:
        entree = {"id": c["id"], "numero": c["numero"], "titre": c["titre"],
                  "tailleVoix": taille_chapitre(c["id"]), "scenes": []}
        for sc in c["scenes"]:
            s = scenes.get(sc["id"])
            numero = f"P.{sc['numero']}" if c["numero"] == 0 else f"{c['numero']}.{sc['numero']}"
            entree["scenes"].append({
                "id": sc["id"], "numero": numero, "titre": sc["titre"], "disponible": s is not None,
                "intention": s["intention"] if s else None,
                "expressions": sum(len(m["expressions"]) for m in s["moments"]) if s else 0,
            })
        sommaire["chapitres"].append(entree)
    (SORTIE / "sommaire.json").write_text(json.dumps(sommaire, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    (SORTIE / "personnages.json").write_text(json.dumps(
        {k: {"nom": v["nom"]} for k, v in personnages.items()}, ensure_ascii=False), encoding="utf-8")
    print(f"   {len(scenes)} scène(s) compilée(s), sommaire de {len(chapitres)} chapitres")

    etape("5. index de recherche", ["node", str(OUTILS / "index_recherche.mjs")])

    print("— 6. couverture vocale")
    manques, taux = couverture(scenes)
    porte = RACINE / "pilotage/portes/rapport-couverture.md"
    porte.parent.mkdir(parents=True, exist_ok=True)
    lignes = ["# Rapport de couverture vocale (10.5, étape 6)", "", "| Scène | Couverture |", "|---|---|"]
    lignes += [f"| {sid} | {v:.1f} % |" for sid, v in taux.items()] or ["| (aucune scène compilée) | — |"]
    lignes += ["", f"Manques : {len(manques)}", ""] + [f"- {m}" for m in manques[:2000]]
    porte.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    incompletes = [sid for sid, v in taux.items() if v < 100.0]
    print(f"   {len(scenes) - len(incompletes)} scène(s) à 100 %, {len(manques)} manque(s)")
    if incompletes and not a.brouillon:
        print(f"construire : couverture vocale incomplète pour {', '.join(incompletes)} (toute scène publiée doit être à 100 %)")
        return 1

    print("— 8. itinéraires et moments")
    for nom in ("itineraires", "moments"):
        src = CORPUS / f"{nom}.yaml"
        donnees = yaml.safe_load(src.read_text(encoding="utf-8")) if src.exists() else ([] if nom == "itineraires" else {})
        (SORTIE / f"{nom}.json").write_text(json.dumps(donnees, ensure_ascii=False), encoding="utf-8")

    print("— 9. expression du jour")
    jour = []
    for sid, s in scenes.items():
        for m in s["moments"]:
            for x in m["expressions"]:
                e = x["enonces"][0]
                jour.append({"id": x["id"], "enonce": e["id"], "texte": e["texte"], "sens": x["sens"], "frequence": x["frequence"]})
    (SORTIE / "expression-du-jour.json").write_text(json.dumps(jour, ensure_ascii=False), encoding="utf-8")
    print(f"   {len(jour)} expression(s) candidates")
    print("construire : terminé")
    return 0


if __name__ == "__main__":
    sys.exit(main())
