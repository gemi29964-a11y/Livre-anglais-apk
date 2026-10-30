"""Fonctions partagées par les outils de la chaîne de contenu (section 10.5)."""
from __future__ import annotations

import pathlib
import re
import unicodedata
from typing import Any, Iterator

RACINE = pathlib.Path(__file__).resolve().parents[1]
CORPUS = RACINE / "corpus"
APP = RACINE / "app"

# Liste fermée de la charte du lexique (3.3), reprise mot pour mot.
MOTS_BANNIS = [
    "module", "sous-module", "fiche", "exercice", "quiz", "test", "score", "points", "xp", "niveau débloqué",
    "débloquer", "valider", "soumettre", "erreur", "bug", "chargement", "télécharger", "téléchargement",
    "synchroniser", "synchronisation", "cliquer", "bouton", "menu", "paramètre", "paramètres", "utilisateur",
    "apprenant", "élève", "leçon", "cours", "contenu", "fichier", "données", "audio", "mode", "item", "input",
    "output", "tts", "synthèse vocale", "algorithme", "automatiser", "génératif", "pivot", "étape suivante",
    "prochaine étape", "réponse suivante", "widget", "statistiques", "tableau de bord", "tutoriel",
    "onboarding", "notification", "profil", "compte", "dictée", "playlist", "feedback",
]

# Balisage des fragments anglais dans les champs français du corpus : <en>…</en> (décision D-012).
BALISE_EN = re.compile(r"<en>.*?</en>", re.S)

# Champs du corpus dont la langue est le français (lus par le lecteur ou dits par la voix du sens).
CHAMPS_FR = {"titre", "intention", "sens", "motAMot", "usage", "coulisses", "pourquoi", "pourQui"}
# Champs anglais (jamais soumis au lexique français).
CHAMPS_EN = {"texte", "jeu", "phrase", "expert", "entendu", "fautif", "naturel", "contexte", "emotion"}


def sans_accents(t: str) -> str:
    t = unicodedata.normalize("NFD", t)
    return "".join(c for c in t if unicodedata.category(c) != "Mn")


def normaliser(t: str) -> str:
    t = sans_accents(t).lower()
    t = t.replace("’", "'").replace("\u00a0", " ").replace("\u202f", " ")
    return t


def _motif(terme: str) -> re.Pattern[str]:
    n = re.escape(normaliser(terme)).replace(r"\ ", r"[\s\-]+").replace(r"\-", r"[\s\-]")
    # Le mot entier : pas de lettre avant ni après (les apostrophes et traits d'union séparent).
    return re.compile(rf"(?<![a-z0-9]){n}(?![a-z0-9])")


MOTIFS_BANNIS = [(t, _motif(t)) for t in MOTS_BANNIS]

# Locutions où le mot n'a pas le sens scolaire banni, et que le Plan emploie lui-même dans des textes
# visibles (8.2 « Itinéraire en cours », 8.3 état « en cours ») : décision D-021, la règle la plus précise prime.
LOCUTIONS_PERMISES = [re.compile(r"(?<![a-z])(en|au) cours(?![a-z])")]


def termes_bannis(texte: str) -> list[str]:
    """Renvoie les termes bannis présents dans un texte français (hors fragments balisés anglais)."""
    propre = BALISE_EN.sub(" ", texte)
    propre = re.sub(r"<[^>]*lang=[\"']en[\"'][^>]*>.*?</[^>]+>", " ", propre, flags=re.S)
    n = normaliser(propre)
    for loc in LOCUTIONS_PERMISES:
        n = loc.sub(" ", n)
    return [t for t, m in MOTIFS_BANNIS if m.search(n)]


def parcourir(objet: Any, chemin: str = "") -> Iterator[tuple[str, str, str]]:
    """Parcourt un objet YAML et renvoie (chemin, clé, valeur) pour chaque chaîne."""
    if isinstance(objet, dict):
        for k, v in objet.items():
            yield from parcourir_cle(v, f"{chemin}/{k}" if chemin else str(k), str(k))
    elif isinstance(objet, list):
        for i, v in enumerate(objet):
            yield from parcourir_cle(v, f"{chemin}/{i}", None)


def parcourir_cle(v: Any, chemin: str, cle: str | None) -> Iterator[tuple[str, str, str]]:
    if isinstance(v, str):
        yield chemin, cle or chemin.rsplit("/", 2)[-2], v
    else:
        yield from parcourir(v, chemin)


def champs_francais(objet: Any) -> Iterator[tuple[str, str]]:
    """Renvoie (chemin, texte) des champs français d'un fichier de corpus."""
    for chemin, cle, valeur in parcourir(objet):
        parties = chemin.split("/")
        if any(p in CHAMPS_EN for p in parties):
            continue
        if cle in CHAMPS_FR or "rituel" in parties or "etapes" in parties and cle == "titre":
            yield chemin, valeur
        elif parties[-2:-1] == ["declinaisons"] and cle == "sens":
            yield chemin, valeur
