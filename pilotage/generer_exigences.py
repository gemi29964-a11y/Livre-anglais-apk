#!/usr/bin/env python3
"""Construit pilotage/exigences.csv à partir de docs/MEGA_GOD_PLAN.md.

Une ligne par exigence vérifiable :
  * les 205 fonctionnalités de la section 14 (identifiants F001 à F205) ;
  * chaque élément normatif du Plan : ligne de tableau, élément de liste,
    ou phrase portant une obligation (DOIT, jamais, aucun, ≤, ≥, bloquant…),
    dans toutes les sections 0 à 21 et les annexes A, B, C et E.

Le statut de chaque exigence vient de pilotage/statuts.csv (id;statut;preuve),
tenu à jour à chaque tranche ; à défaut, le statut est « à faire » avec la
tranche prévue par le découpage de la mission.

Usage : python3 pilotage/generer_exigences.py [--verifier]
  --verifier : échoue si une fonctionnalité manque ou si le total diffère de 205.
"""
from __future__ import annotations

import csv
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parents[1]
PLAN = RACINE / "docs" / "MEGA_GOD_PLAN.md"
SORTIE = RACINE / "pilotage" / "exigences.csv"
STATUTS = RACINE / "pilotage" / "statuts.csv"

# Sections exclues de l'extraction normative : sommaire, glossaire (D), sources (F, une seule ligne).
EXCLUES = {"Sommaire", "D", "F"}

MOTS_NORMATIFS = re.compile(
    r"\b(DOIT|DOIVENT|NE DOIT PAS|DEVRAIT|doit|doivent|jamais|aucun|aucune|toujours|obligatoire|"
    r"exig|bloqu|interdit|refus|uniquement|seul|seule|chaque|tout|toute|tous|toutes|minimum|maximum)\b"
    r"|[≤≥]|\d+\s?%|\d+\s?(ms|s|Mo|Go|Ko|dp|px|LUFS|dBTP|Hz|kHz)\b",
    re.I,
)

TYPE_PAR_SECTION = {
    "0": "décision figée", "1": "volume", "2": "principe", "3": "lexique", "4": "architecture du contenu",
    "5": "contenu", "6": "phrasé", "7": "voix", "8": "expérience", "9": "design", "10": "ingénierie",
    "11": "qualité", "12": "production éditoriale", "13": "risque", "14": "fonctionnalité", "15": "science",
    "16": "module avancé", "17": "module avancé", "18": "module avancé", "19": "module avancé",
    "20": "industrialisation", "21": "volume", "A": "scène étalon", "B": "schéma", "C": "configuration",
    "E": "mise en production",
}

PORTE_PAR_SECTION = {
    "0": "P7", "1": "P6", "2": "P6", "3": "P1", "4": "P1", "5": "P1", "6": "P5", "7": "P3", "8": "P6",
    "9": "P6", "10": "P7", "11": "P7", "12": "P2", "13": "P7", "14": "P7", "15": "P6", "16": "P6",
    "17": "P6", "18": "P6", "19": "P6", "20": "P7", "21": "P6", "A": "P1-P6", "B": "P1", "C": "P7", "E": "P7",
}

# Portes plus précises pour certaines sous-sections.
PORTE_PAR_SOUS_SECTION = {
    "7.9": "P4", "7.10": "P3", "7.11": "P4", "7.12": "P7", "10.4": "P1", "10.5": "P1", "10.22": "P4",
    "6.7": "P5", "5.4": "P2", "12.3": "P2", "11.1": "P1-P7", "9.2": "P6", "9.9": "P6",
}

PREUVE_PAR_TYPE = {
    "décision figée": "Contrôle automatique de la configuration (capacitor.config.ts, build.gradle, aapt2 dump badging) consigné dans le rapport de porte",
    "volume": "Comptage produit par tools/construire.py (sommaire.json, rapport-couverture.md) comparé à la cible",
    "principe": "Revue d'intégration P6 consignée (écrans, parcours) et absence de contre-exemple",
    "lexique": "Rapport tools/lexique_verifier.py : 0 terme banni (corpus, fr.ts, build/)",
    "architecture du contenu": "Rapport tools/valider_corpus.py (schéma, densité, renvois) sans erreur",
    "contenu": "Rapport tools/valider_corpus.py + rapport de relecture P2",
    "phrasé": "Rapport tools/phrase_verifier.py + rapport de contre-écoute P5",
    "voix": "Registre voix/registre/creations.jsonl + rapport voix/outils/controler.py (seuils 7.10)",
    "expérience": "Test de composant ou parcours Playwright/Maestro vert + capture d'écran archivée",
    "design": "Rapport tools/contrastes.py + captures des quatre thèmes",
    "ingénierie": "Fichier présent et conforme + compilation/tests verts (journal d'exécution archivé)",
    "qualité": "Rapport de test automatique ou de porte archivé dans pilotage/portes/",
    "production éditoriale": "Rapport de porte P1/P2 de la scène concernée",
    "risque": "Mesure d'atténuation en place, vérifiée et consignée",
    "fonctionnalité": "Fonctionnalité présente dans l'édition, démontrée par test automatique ou capture, rapport P6/P7",
    "science": "Mécanisme appliqué présent (fonctionnalité liée) et page « Ce que l'ouvrage ne promet pas » conforme",
    "module avancé": "Module présent, voix couvertes, test automatique vert, rapport P6",
    "industrialisation": "Procédure outillée exécutée, rapport consigné",
    "scène étalon": "Scène c01.s01 conforme : portes P1 à P6 franchies, mesures consignées",
    "schéma": "corpus/schema/scene.schema.json identique à l'annexe B ; valider_corpus.py appliqué",
    "configuration": "Fichier de configuration présent, conforme à l'annexe C, utilisé par la compilation",
    "mise en production": "Case de la check-list E cochée avec sa preuve (Tranche 10)",
}


def tranche_prevue(section: str, sous: str) -> str:
    """Tranche de la mission où l'exigence doit être satisfaite (découpage en 10 tranches)."""
    if section in {"0", "3", "9", "10", "11", "B", "C"}:
        return "T1"
    if section in {"7", "6"}:
        return "T2"
    if section == "A":
        return "T2"
    if section in {"16", "17", "18", "19"}:
        return "T9"
    if section in {"E", "20", "13"}:
        return "T10"
    if section in {"4", "5", "12", "1", "21"}:
        return "T2-T8"
    return "T2-T10"


def nettoyer(t: str) -> str:
    t = re.sub(r"\*\*|`", "", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def lire_plan():
    lignes = PLAN.read_text(encoding="utf-8").splitlines()
    section, sous, titre_sous = "", "", ""
    dans_code = False
    for n, ligne in enumerate(lignes, 1):
        if ligne.startswith("```"):
            dans_code = not dans_code
            continue
        m = re.match(r"^## (\d+)\. ", ligne)
        if m:
            section, sous, titre_sous = m.group(1), m.group(1), ligne[3:].strip()
            continue
        m = re.match(r"^## Annexe ([A-F])", ligne)
        if m:
            section, sous, titre_sous = m.group(1), m.group(1), ligne[3:].strip()
            continue
        if ligne.startswith("## Sommaire"):
            section, sous = "Sommaire", "Sommaire"
            continue
        m = re.match(r"^### (\d+\.\d+|[A-F]\.\d+) ?(.*)", ligne)
        if m:
            sous, titre_sous = m.group(1), m.group(2).strip()
            continue
        yield n, section, sous, titre_sous, ligne, dans_code


def fonctionnalites():
    rows = []
    for n, section, sous, titre, ligne, code in lire_plan():
        if section != "14" or code:
            continue
        m = re.match(r"^\| (\d+) \| \*\*(.+?)\*\* \| (.+?) \| (.+?) \|$", ligne)
        if m:
            num, nom, apport, ref = m.groups()
            rows.append((int(num), nettoyer(nom), nettoyer(apport), nettoyer(ref), n))
    return rows


def exigences_normatives():
    rows = []
    compteur: dict[str, int] = {}
    entete_tableau = None
    for n, section, sous, titre, ligne, code in lire_plan():
        if not section or section in EXCLUES or section == "14":
            continue
        brut = ligne.strip()
        if not brut or brut.startswith("#") or brut == "---":
            entete_tableau = None if not brut.startswith("|") else entete_tableau
            continue
        texte = None
        if brut.startswith("|"):
            cellules = [c.strip() for c in brut.strip("|").split("|")]
            if all(re.fullmatch(r":?-{3,}:?", c) for c in cellules):
                continue
            if entete_tableau is None:
                entete_tableau = cellules
                continue
            paires = [f"{entete_tableau[i]} : {c}" if i < len(entete_tableau) and i > 0 else c
                      for i, c in enumerate(cellules) if c]
            texte = " — ".join(paires)
        else:
            entete_tableau = None
            if code:
                continue  # le code des annexes est couvert par une exigence de fichier (voir plus bas)
            if re.match(r"^(\d+\.|-|\*) ", brut) or MOTS_NORMATIFS.search(brut):
                texte = re.sub(r"^(\d+\.|-|\*) ", "", brut)
        if not texte:
            continue
        texte = nettoyer(texte)
        if len(texte) < 12:
            continue
        cle = sous or section
        compteur[cle] = compteur.get(cle, 0) + 1
        rid = f"R-{cle}-{compteur[cle]:03d}"
        rows.append((rid, section, sous, titre, texte, n))
    return rows


def fichiers_imposes():
    """Chaque fichier dont le Plan donne le contenu intégral devient une exigence."""
    rows = []
    texte = PLAN.read_text(encoding="utf-8")
    vus = set()
    for m in re.finditer(r"^(?://|#) ((?:app|android|tools|corpus|voix|\.github)/[\w./\-\[\]+]+)", texte, re.M):
        chemin = m.group(1).rstrip(".")
        if chemin in vus:
            continue
        vus.add(chemin)
        rows.append(chemin)
    for chemin in ["corpus/schema/scene.schema.json", "app/package.json", "app/src/routes/+layout.ts",
                   "app/playwright.config.ts", "tools/requirements.txt", "tools/voix_recuperer.py",
                   "tools/generer_paquets.py", "android/app/src/main/res/mipmap-anydpi-v26/ic_launcher.xml",
                   ".gitignore", "corpus/itineraires.yaml", "corpus/moments.yaml"]:
        if chemin not in vus:
            vus.add(chemin)
            rows.append(chemin)
    return rows


def charger_statuts():
    statuts = {}
    if STATUTS.exists():
        with STATUTS.open(encoding="utf-8") as f:
            for r in csv.reader(f, delimiter=";"):
                if r and not r[0].startswith("#") and len(r) >= 2:
                    statuts[r[0]] = (r[1], r[2] if len(r) > 2 else "")
    return statuts


def section_de_reference(ref: str) -> str:
    m = re.match(r"(\d+|[A-F])", ref)
    return m.group(1) if m else "14"


def main():
    statuts = charger_statuts()
    sortie = []
    feats = fonctionnalites()
    for num, nom, apport, ref, n in feats:
        s = section_de_reference(ref)
        sous = ref.split(",")[0].strip()
        porte = PORTE_PAR_SOUS_SECTION.get(sous, PORTE_PAR_SECTION.get(s, "P6"))
        fid = f"F{num:03d}"
        st, preuve = statuts.get(fid, (f"à faire ({tranche_prevue(s, sous)})", ""))
        sortie.append([fid, f"14 → {ref}", f"Fonctionnalité {num} « {nom} » : {apport}", "fonctionnalité", porte,
                       preuve or PREUVE_PAR_TYPE["fonctionnalité"], st])
    for rid, section, sous, titre, texte, n in exigences_normatives():
        typ = TYPE_PAR_SECTION.get(section, "exigence")
        porte = PORTE_PAR_SOUS_SECTION.get(sous, PORTE_PAR_SECTION.get(section, "P7"))
        st, preuve = statuts.get(rid, (f"à faire ({tranche_prevue(section, sous)})", ""))
        sortie.append([rid, f"{sous} {titre}".strip(), texte, typ, porte, preuve or PREUVE_PAR_TYPE.get(typ, ""), st])
    for i, chemin in enumerate(fichiers_imposes(), 1):
        rid = f"FICH-{i:03d}"
        st, preuve = statuts.get(rid, ("à faire (T1)" if not chemin.startswith("voix/") else "à faire (T2)", ""))
        sortie.append([rid, "10.3 / annexes B–C", f"Le fichier {chemin} existe et reprend le contenu imposé par le Plan",
                       "fichier imposé", "P7", preuve or "Fichier présent dans le dépôt, utilisé par la compilation", st])
    sources = "Annexe F — Sources citées"
    st, preuve = statuts.get("R-F-001", ("à faire (T10)", ""))
    sortie.append(["R-F-001", sources, "Chaque source citée dans l'ouvrage figure avec son adresse complète (61 sources)",
                   "sources", "P7", preuve or "Page « Les sources » de l'ouvrage avec les 61 adresses", st])

    with SORTIE.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "section", "exigence", "type", "porte", "preuve_attendue", "statut"])
        w.writerows(sortie)

    nb_f = len(feats)
    print(f"{len(sortie)} exigences écrites dans {SORTIE.relative_to(RACINE)} (dont {nb_f} fonctionnalités)")
    if "--verifier" in sys.argv:
        nums = sorted(x[0] for x in feats)
        if nums != list(range(1, 206)):
            manquantes = sorted(set(range(1, 206)) - set(nums))
            print(f"Fonctionnalités manquantes : {manquantes}", file=sys.stderr)
            sys.exit(1)
        ids = [r[0] for r in sortie]
        if len(ids) != len(set(ids)):
            print("Identifiants en double", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
