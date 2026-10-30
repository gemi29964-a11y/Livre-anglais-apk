"""Correction typographique française proposée (règle 8 de 10.4, 3.4) : espaces insécables.

Usage : python3 tools/typographie.py FICHIER [--ecrire]
Dans les littéraux de chaîne (TS) ou les valeurs (YAML) : espace insécable avant ; : ! ? %,
à l'intérieur des guillemets « », et entre un nombre et son unité « h », « Mo ».
Sans --ecrire, affiche les corrections proposées et sort en 1 s'il y en a.
"""
from __future__ import annotations

import pathlib
import re
import sys

NBSP = "\u00a0"


def corriger(s: str) -> str:
    s = re.sub(r"[ \u202f]([;:!?%»])", NBSP + r"\1", s)
    s = re.sub(r"«[ \u202f]", "«" + NBSP, s)
    s = re.sub(r"(\d|\})[ ](h|Mo|min)\b", r"\1" + NBSP + r"\2", s)
    return s


def traiter(texte: str, ts: bool) -> str:
    if not ts:
        return corriger(texte)
    # Analyse lexicale minimale : commentaires laissés tels quels, seuls les littéraux de chaîne sont corrigés.
    motif = re.compile(r"//[^\n]*|/\*.*?\*/|(['\"`])((?:\\.|(?!\1)[^\\])*)\1", re.S)
    sortie, i = [], 0
    for m in motif.finditer(texte):
        sortie.append(texte[i:m.start()])
        if m.group(1) is None:
            sortie.append(m.group(0))
        else:
            contenu = m.group(2)
            if not re.fullmatch(r"[\w./:-]*", contenu) and not contenu.startswith("http"):
                contenu = corriger(contenu)
            sortie.append(m.group(1) + contenu + m.group(1))
        i = m.end()
    sortie.append(texte[i:])
    return "".join(sortie)


def main() -> int:
    f = pathlib.Path(sys.argv[1])
    avant = f.read_text(encoding="utf-8")
    apres = traiter(avant, f.suffix == ".ts")
    if "--ecrire" in sys.argv:
        f.write_text(apres, encoding="utf-8")
        return 0
    if apres != avant:
        print(f"{f} : corrections typographiques proposées (relancer avec --ecrire)")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
