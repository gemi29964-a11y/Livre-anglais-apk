"""Validation du corpus : les douze règles de la section 10.4.

Usage :
  python3 tools/valider_corpus.py              # mode publication : toute violation bloque
  python3 tools/valider_corpus.py --brouillon  # mode rédaction : phrasés manquants et densité
                                               # sous le minimum signalés sans bloquer (D-014)
Sortie : rapport lisible ; code 1 si une règle bloquante est violée.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter

import yaml
from jsonschema import Draft202012Validator

from commun import BALISE_EN, CORPUS, RACINE, champs_francais, termes_bannis

RE_ID = re.compile(r"^c\d{2}\.s\d{2}\.[A-Z]\d{1,2}(\.(e|d)\d{1,2})?$")
RE_REPLIQUE = re.compile(r"^c\d{2}\.s\d{2}\.sv\.l\d{2}$")

# Normes de densité (4.5) : (minimum, cible, maximum).
DENSITE = {
    "moments": (8, 12, 15),
    "expressions": (40, 55, 75),
    "par_moment": (3, 5, 8),
    "enonces": (1, 1, 3),
    "declinaisons": (3, 5, 6),
    "repliques": (10, 14, 20),
    "incontournables": (10, 10, 10),
    "faux_pas": (6, 8, 10),
}

# Mots anglais courants qui n'existent pas en français : leur présence non balisée dans `sens`
# trahit un fragment anglais (règle 12). Liste fermée, révisable par décision.
MOTS_ANGLAIS = set(
    """the you your yours i'm you're it's don't doesn't didn't can't won't isn't aren't wasn't what's
    that's there's let's i've i'll i'd we're they're he's she's what when where who why how which
    with without this that these those have has had been being would could should will shall
    and but or not my our their his her its they them we us me of to for from into onto about
    get got gonna wanna gotta yeah yes okay please thanks thank sorry morning night good bad
    up down off out over again just really very much many some any every all one two three""".split()
)
EXCEPTIONS_FR = {"or", "on", "me", "un", "us", "a", "est", "ont", "ma", "ok"}  # homographes français


class Rapport:
    def __init__(self, brouillon: bool) -> None:
        self.brouillon = brouillon
        self.blocages: list[str] = []
        self.avertissements: list[str] = []

    def bloquer(self, ou: str, quoi: str, souple: bool = False) -> None:
        (self.avertissements if souple and self.brouillon else self.blocages).append(f"{ou} : {quoi}")

    def avertir(self, ou: str, quoi: str) -> None:
        self.avertissements.append(f"{ou} : {quoi}")


def mots(t: str) -> int:
    return len(re.findall(r"[A-Za-zÀ-ÿ0-9’']+", t))


def densite(r: Rapport, ou: str, cle: str, n: int) -> None:
    mini, cible, maxi = DENSITE[cle]
    if n < mini:
        r.bloquer(ou, f"densité {cle} = {n} < minimum {mini} (4.5)", souple=True)
    elif n > maxi:
        r.bloquer(ou, f"densité {cle} = {n} > maximum {maxi} (4.5)")
    elif n < cible:
        r.avertir(ou, f"densité {cle} = {n} sous la cible {cible} (4.5)")


def quatre_phrases(p: dict | None) -> bool:
    try:
        return all(p[a][rt]["phrase"] and p[a][rt]["expert"] for a in ("uk", "us") for rt in ("pose", "spontane"))
    except (KeyError, TypeError):
        return False


def anglais_non_balise(t: str) -> list[str]:
    nu = BALISE_EN.sub(" ", t).replace("’", "'").lower()
    return [m for m in re.findall(r"[a-z']+", nu) if m in MOTS_ANGLAIS and m not in EXCEPTIONS_FR]


def typographie(t: str) -> bool:
    nu = BALISE_EN.sub(" ", t)
    return not re.search(r"[^\u202f\u00a0]([;:!?])", nu)


def valider(brouillon: bool) -> Rapport:
    r = Rapport(brouillon)
    schema = json.loads((CORPUS / "schema/scene.schema.json").read_text(encoding="utf-8"))
    validateur = Draft202012Validator(schema)
    personnages = yaml.safe_load((CORPUS / "personnages.yaml").read_text(encoding="utf-8"))["personnages"]
    chapitres = yaml.safe_load((CORPUS / "chapitres.yaml").read_text(encoding="utf-8"))["chapitres"]
    connus: Counter[str] = Counter()
    expressions: set[str] = set()
    renvois: list[tuple[str, str]] = []
    scenes = sorted(CORPUS.glob("c[0-9][0-9]/s[0-9][0-9].yaml"))

    for f in scenes:
        rel = str(f.relative_to(RACINE))
        s = yaml.safe_load(f.read_text(encoding="utf-8"))
        attendu = f"{f.parent.name}.{f.stem}"
        # Règle 1 : schéma
        for e in sorted(validateur.iter_errors(s), key=lambda e: list(e.path)):
            r.bloquer(rel, f"schéma : {'/'.join(map(str, e.path))} — {e.message}")
        if not isinstance(s, dict):
            continue
        if s.get("id") != attendu:
            r.bloquer(rel, f"identifiant {s.get('id')} ≠ {attendu}")
        prelude = attendu.startswith("c00.")
        moments = s.get("moments", [])
        if not prelude:
            densite(r, rel, "moments", len(moments))
        total = 0
        for m in moments:
            exps = m.get("expressions", [])
            total += len(exps)
            if not prelude:
                densite(r, f"{rel}:{m.get('lettre')}", "par_moment", len(exps))
            for x in exps:
                xid = x.get("id", "")
                connus[xid] += 1
                expressions.add(xid)
                if not xid.startswith(f"{attendu}.{m.get('lettre')}"):
                    r.bloquer(rel, f"{xid} n’appartient pas au moment {m.get('lettre')}")
                densite(r, xid, "enonces", len(x.get("enonces", [])))
                densite(r, xid, "declinaisons", len(x.get("declinaisons", [])))
                for e in x.get("enonces", []):
                    connus[e.get("id", "")] += 1
                    if not quatre_phrases(e.get("phrases")):  # Règle 6
                        r.bloquer(e.get("id", xid), "quatre phrasés absents", souple=True)
                    for a, t in (e.get("texte") or {}).items():  # Règle 7
                        if mots(t) > 18:
                            r.bloquer(e.get("id", xid), f"énoncé {a} de {mots(t)} mots > 18 (5.2)")
                for d in x.get("declinaisons", []):  # Règle 5
                    connus[d.get("id", "")] += 1
                    if not d.get("sens"):
                        r.bloquer(d.get("id", xid), "déclinaison sans sens")
                    if not quatre_phrases(d.get("phrases")):
                        r.bloquer(d.get("id", xid), "quatre phrasés de la déclinaison absents", souple=True)
                    if d.get("renvoi"):
                        renvois.append((d["id"], d["renvoi"]))
                    for a, t in (d.get("texte") or {}).items():
                        if mots(t) > 12:
                            r.bloquer(d.get("id", xid), f"déclinaison {a} de {mots(t)} mots > 12 (5.1)")
                if mots(BALISE_EN.sub(lambda m: m.group(0)[4:-5], x.get("usage", ""))) > 70:
                    r.bloquer(xid, "« L’usage » dépasse 70 mots")
                if mots(BALISE_EN.sub(lambda m: m.group(0)[4:-5], x.get("coulisses", ""))) > 50:
                    r.bloquer(xid, "« En coulisses » dépasse 50 mots")
                if x.get("motAMot") and mots(x["motAMot"]) > 12:
                    r.bloquer(xid, "« Mot à mot » dépasse 12 mots (5.1)")
                if x.get("ton") == "cru" and "réserver" not in x.get("usage", "").lower():
                    r.bloquer(xid, "ton cru sans avertissement d’usage (5.2 règle 6)")
                for cible in x.get("renvois", []):
                    renvois.append((xid, cible))
                for champ in ("sens",):  # Règle 12
                    for d in [x] + x.get("declinaisons", []):
                        intrus = anglais_non_balise(d.get(champ, ""))
                        if intrus:
                            r.bloquer(d.get("id", xid), f"anglais non balisé dans le sens : {', '.join(intrus)}")
        if not prelude:
            densite(r, rel, "expressions", total)
            ess = s.get("essentiel", {})
            densite(r, rel, "incontournables", len(ess.get("incontournables", [])))
            densite(r, rel, "faux_pas", len(ess.get("fauxPas", [])))
            for i in ess.get("incontournables", []):
                renvois.append((f"{rel}:incontournables", i))
        sv = s.get("sceneVivante", {})
        reps = sv.get("repliques", [])
        if not prelude:
            densite(r, rel, "repliques", len(reps))
        for rep in reps:  # Règles 2 et 10
            if not RE_REPLIQUE.match(rep.get("id", "")):
                r.bloquer(rel, f"réplique {rep.get('id')} au format invalide")
            connus[rep.get("id", "")] += 1
            if rep.get("personnage") not in personnages:
                r.bloquer(rep.get("id", rel), f"personnage inconnu « {rep.get('personnage')} »")
        # Règles 8 et 9 : typographie et lexique des champs français
        for chemin, texte in champs_francais(s):
            if not typographie(texte):
                r.bloquer(f"{rel}:{chemin}", "espace insécable manquante avant ; : ! ? (3.4)")
            for t in termes_bannis(texte):
                r.bloquer(f"{rel}:{chemin}", f"terme banni « {t} » (3.3)")

    # Règle 2 : unicité et format des identifiants
    for i, n in connus.items():
        if n > 1:
            r.bloquer("ouvrage", f"identifiant en double : {i}")
        if not (RE_ID.match(i) or RE_REPLIQUE.match(i)):
            r.bloquer("ouvrage", f"identifiant au format invalide : {i}")
    # Règle 3 : renvois
    for source, cible in renvois:
        if cible not in expressions:
            r.bloquer(source, f"renvoi vers un identifiant inexistant : {cible}")
    # Règle 11 : itinéraires et moments de la journée
    it_f = CORPUS / "itineraires.yaml"
    if it_f.exists():
        for it in yaml.safe_load(it_f.read_text(encoding="utf-8")) or []:  # liste (annexe C.9)
            if not 4 <= len(it.get("etapes", [])) <= 8:
                r.bloquer(f"itinéraire {it.get('id')}", "4 à 8 étapes attendues (8.17)", souple=True)
            for et in it.get("etapes", []):
                n = len(et.get("expressions", []))
                if not 12 <= n <= 25:
                    r.bloquer(f"itinéraire {it.get('id')}", f"étape « {et.get('titre')} » : {n} expressions (12 à 25)", souple=True)
                for x in et.get("expressions", []):
                    if x not in expressions:
                        r.bloquer(f"itinéraire {it.get('id')}", f"expression inexistante {x}", souple=True)
    mo_f = CORPUS / "moments.yaml"
    if mo_f.exists():
        ids_scenes = {f"{f.parent.name}.{f.stem}" for f in scenes}
        attendus = {"petit-matin", "matinee", "midi", "apres-midi", "soiree", "nuit", "week-end"}
        table = yaml.safe_load(mo_f.read_text(encoding="utf-8")) or {}  # moment → scènes (annexe C.10)
        if set(table) != attendus:
            r.bloquer("moments.yaml", f"moments attendus {sorted(attendus)} (8.20)")
        for nom, liste in table.items():
            for sc in liste or []:
                if sc not in ids_scenes:
                    r.bloquer(f"moments {nom}", f"scène inexistante {sc}", souple=True)
    # Cohérence avec la table des chapitres (4.4)
    for f in scenes:
        ch = int(f.parent.name[1:])
        if ch not in {c["numero"] for c in chapitres}:
            r.bloquer(str(f.relative_to(RACINE)), "chapitre absent de la table 4.4")
    r.nb_scenes = len(scenes)  # type: ignore[attr-defined]
    r.nb_expressions = len(expressions)  # type: ignore[attr-defined]
    return r


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--brouillon", action="store_true")
    ap.add_argument("--strict", action="store_true", help="tout avertissement devient bloquant (annexe E)")
    a = ap.parse_args()
    r = valider(a.brouillon)
    if a.strict and r.avertissements:
        r.blocages += [f"(strict) {x}" for x in r.avertissements]
    print(f"corpus : {r.nb_scenes} scène(s), {r.nb_expressions} expression(s)")  # type: ignore[attr-defined]
    for x in r.avertissements[:100]:
        print("  ⚠", x)
    if r.blocages:
        print(f"corpus : ÉCHEC — {len(r.blocages)} violation(s) bloquante(s)")
        for x in r.blocages[:300]:
            print("  ✗", x)
        return 1
    print(f"corpus : conforme — 0 violation bloquante, {len(r.avertissements)} avertissement(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
