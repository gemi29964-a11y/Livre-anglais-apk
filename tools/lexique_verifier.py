"""Contrôle automatique de la charte du lexique (section 3).

Usage :
  python3 tools/lexique_verifier.py                 # corpus + textes de l'interface + gabarits Svelte
  python3 tools/lexique_verifier.py --construit DIR # texte visible du livre construit (HTML et corpus JSON)

Bloquant : tout terme banni (3.3), tout « TODO », tout texte de remplissage, toute chaîne française
écrite en dur dans un gabarit Svelte, tout manquement typographique aux textes de l'interface (3.4).
Code de sortie 1 en cas d'échec : la compilation s'arrête.
"""
from __future__ import annotations

import argparse
import html
import json
import pathlib
import re
import sys

import yaml

from commun import APP, CORPUS, RACINE, champs_francais, parcourir, termes_bannis

# Marqueurs de remplissage interdits dans tout ce qui est livré (2 et 7.1 : aucun contenu factice).
REMPLISSAGE = re.compile(
    r"\b(todo|fixme|xxx|tbd|lorem|ipsum|placeholder|à compléter|a completer|texte provisoire|contenu factice)\b",
    re.I,
)
EMOJI = re.compile("[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F2FF]")


class Rapport:
    def __init__(self) -> None:
        self.fautes: list[str] = []
        self.textes = 0

    def faute(self, ou: str, quoi: str) -> None:
        self.fautes.append(f"{ou} : {quoi}")

    def examiner(self, ou: str, texte: str, interface: bool = False) -> None:
        self.textes += 1
        for t in termes_bannis(texte):
            self.faute(ou, f"terme banni « {t} »")
        if REMPLISSAGE.search(texte):
            self.faute(ou, "texte de remplissage")
        if EMOJI.search(texte):
            self.faute(ou, "émoji")
        if interface:
            self.typographie(ou, texte)
        else:
            nu = re.sub(r"<en>.*?</en>", " ", texte, flags=re.S)
            if re.search(r"[A-Za-zÀ-ÿ]'[A-Za-zÀ-ÿ]", nu):
                self.faute(ou, "apostrophe droite : employer ’ (3.4)")
            if "..." in nu:
                self.faute(ou, "trois points : employer … (3.4)")

    def typographie(self, ou: str, texte: str) -> None:
        nu = re.sub(r"<en>.*?</en>|<[^>]+>|\$\{[^}]*\}|\{[^}]*\}", " ", texte)
        if "!" in nu:
            self.faute(ou, "point d’exclamation dans la voix de l’accompagnement (3.4)")
        if "'" in nu:
            self.faute(ou, "apostrophe droite : employer ’ (3.4)")
        if "..." in nu:
            self.faute(ou, "trois points : employer … (3.4)")
        sans_liens = re.sub(r"https?://\S+", " ", nu)
        m = re.search(r"[^\u202f\u00a0]([;:?])", sans_liens)
        if m:
            self.faute(ou, f"espace insécable manquante avant « {m.group(1)} » (3.4)")
        if re.search(r"«(?![\u202f\u00a0])|(?<![\u202f\u00a0])»", nu):
            self.faute(ou, "espace insécable manquante à l’intérieur des guillemets (3.4)")
        for phrase in re.split(r"(?<=[.?…])\s+", nu):
            if len(re.findall(r"[\wÀ-ÿ’]+", phrase)) > 22:
                self.faute(ou, "phrase de plus de 22 mots (3.4)")
                break


def textes_interface(r: Rapport) -> None:
    """Textes de l'interface : app/src/lib/textes/fr.ts (seule source des chaînes françaises)."""
    fr = APP / "src/lib/textes/fr.ts"
    if not fr.exists():
        r.faute(str(fr), "fichier des textes de l’interface absent")
        return
    source = fr.read_text(encoding="utf-8")
    motif = re.compile(r"//[^\n]*|/\*.*?\*/|(['\"`])((?:\\.|(?!\1)[^\\])*)\1", re.S)
    for m in motif.finditer(source):
        if m.group(1) is None:  # commentaire
            continue
        valeur = m.group(2)
        if re.fullmatch(r"[\w./:-]*", valeur):  # identifiants techniques (clés, codes de langue)
            continue
        ligne = source.count("\n", 0, m.start()) + 1
        r.examiner(f"fr.ts:{ligne}", valeur, interface=True)


def gabarits(r: Rapport) -> None:
    """Aucune chaîne française en dur dans les gabarits Svelte, hors anglais balisé lang="en"."""
    for f in sorted((APP / "src").rglob("*.svelte")):
        s = f.read_text(encoding="utf-8")
        s = re.sub(r"<script.*?</script>|<style.*?</style>|<!--.*?-->", " ", s, flags=re.S)
        s = re.sub(r"<(\w+)[^>]*lang=\"en\"[^>]*>.*?</\1>", " ", s, flags=re.S)
        while True:  # expressions imbriquées : on retire les accolades de l'intérieur vers l'extérieur
            s2 = re.sub(r"\{[^{}]*\}", " ", s)
            if s2 == s:
                break
            s = s2
        texte = re.sub(r"<[^>]*>", " ", s)
        for ligne in texte.splitlines():
            ligne = html.unescape(ligne).strip()
            if re.search(r"[A-Za-zÀ-ÿ]{2,}", ligne):
                r.faute(str(f.relative_to(RACINE)), f"chaîne en dur « {ligne[:60]} » (passer par textes/fr.ts)")
        for m in re.finditer(r"(aria-label|title|alt|placeholder)=\"([^\"{]+)\"", f.read_text(encoding="utf-8")):
            r.faute(str(f.relative_to(RACINE)), f"attribut {m.group(1)} en dur « {m.group(2)} »")


def corpus(r: Rapport) -> None:
    for f in sorted(CORPUS.rglob("*.yaml")):
        donnees = yaml.safe_load(f.read_text(encoding="utf-8"))
        rel = f.relative_to(RACINE)
        scene = re.fullmatch(r"c\d{2}", f.parent.name) is not None
        valeurs = champs_francais(donnees) if scene else ((c, v) for c, _, v in parcourir(donnees))
        for chemin, texte in valeurs:
            r.examiner(f"{rel}:{chemin}", texte)
        brut = f.read_text(encoding="utf-8")
        if REMPLISSAGE.search(brut):
            r.faute(str(rel), "texte de remplissage")


def construit(r: Rapport, dossier: pathlib.Path) -> None:
    """Texte réellement visible du livre construit : HTML rendu et corpus JSON."""
    for f in sorted(dossier.rglob("*.html")):
        s = f.read_text(encoding="utf-8")
        s = re.sub(r"<script.*?</script>|<style.*?</style>|<!--.*?-->", " ", s, flags=re.S)
        s = re.sub(r"<(\w+)[^>]*lang=\"en\"[^>]*>.*?</\1>", " ", s, flags=re.S)
        visibles = [html.unescape(m) for m in re.findall(r">([^<]+)<", s)]
        visibles += [html.unescape(m) for m in re.findall(r"(?:aria-label|title|alt|content)=\"([^\"]+)\"", s)]
        for t in visibles:
            if t.strip():
                r.examiner(str(f.relative_to(dossier)), t)
    for f in sorted(dossier.rglob("*.json")):
        try:
            donnees = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        for chemin, texte in champs_francais(donnees):
            r.examiner(f"{f.relative_to(dossier)}:{chemin}", texte)
    for f in sorted(dossier.rglob("*.js")):
        s = f.read_text(encoding="utf-8")
        if re.search(r"\bTODO\b|\bFIXME\b|lorem ipsum", s, re.I):
            r.faute(str(f.relative_to(dossier)), "texte de remplissage dans le code livré")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--construit", type=pathlib.Path)
    a = ap.parse_args()
    r = Rapport()
    if a.construit:
        d = a.construit if a.construit.is_absolute() else pathlib.Path.cwd() / a.construit
        construit(r, d)
    else:
        textes_interface(r)
        gabarits(r)
        corpus(r)
    if r.fautes:
        print(f"lexique : ÉCHEC — {len(r.fautes)} manquement(s) sur {r.textes} textes examinés")
        for x in r.fautes[:200]:
            print("  ✗", x)
        return 1
    print(f"lexique : conforme — {r.textes} textes examinés, 0 terme banni")
    return 0


if __name__ == "__main__":
    sys.exit(main())
