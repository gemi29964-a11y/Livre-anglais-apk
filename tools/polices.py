"""Réduction des polices embarquées (9.3) : WOFF2, jeux de caractères utilisés, aucun appel réseau.

Usage : python3 tools/polices.py SOURCE_DIR
SOURCE_DIR contient les TTF officiels (google/fonts, licence SIL OFL) : Literata[opsz,wght].ttf,
Inter[opsz,wght].ttf, CharisSIL-Regular.ttf, CharisSIL-Bold.ttf, AtkinsonHyperlegible-*.ttf.
Vérifie que chaque police couvre les signes qu'elle doit rendre (phrasé : ə ʔ ɾ ʳ ‿ ↗ ↘ ·).
"""
from __future__ import annotations

import pathlib
import shutil
import sys

from fontTools import subset
from fontTools.ttLib import TTFont

from commun import APP

PLAGES = (
    "U+0020-007E,U+00A0-00FF,U+0100-017F,U+0180-024F,U+0250-02AF,U+02B0-02FF,U+0300-036F,"
    "U+1E00-1EFF,U+2000-206F,U+20AC,U+2122,U+2190-21FF,U+2026,U+202F,U+25CC,U+03B8,U+03C7"
)
POLICES = {
    "Literata[opsz,wght].ttf": "literata.woff2",
    "Inter[opsz,wght].ttf": "inter.woff2",
    "CharisSIL-Regular.ttf": "charis-sil.woff2",
    "CharisSIL-Bold.ttf": "charis-sil-gras.woff2",
    "AtkinsonHyperlegible-Regular.ttf": "atkinson.woff2",
    "AtkinsonHyperlegible-Bold.ttf": "atkinson-gras.woff2",
}
# Signes que chaque police doit porter (6.2 à 6.4 pour le phrasé, API pour Charis SIL).
EXIGES = {
    "inter.woff2": "əƏʔɾʳ‿↗↘·’«»…\u202f\u00a0éèàçœ",
    "literata.woff2": "’«»…\u00a0éèàçœÉÀ",
    "charis-sil.woff2": "ɑɒɔəɚɛɜɝɪʊʌθðʃʒŋɡɾʔˈˌː",
    "atkinson.woff2": "’«»…éèàç",
}


def main(source: pathlib.Path) -> int:
    dest = APP / "static/polices"
    dest.mkdir(parents=True, exist_ok=True)
    manques = []
    for src, nom in POLICES.items():
        sortie = dest / nom
        opts = ["--flavor=woff2", f"--unicodes={PLAGES}", "--layout-features=*", f"--output-file={sortie}"]
        subset.main([str(source / src), *opts])
        cmap = TTFont(sortie).getBestCmap()
        absents = [c for c in EXIGES.get(nom, "") if ord(c) not in cmap]
        if absents:
            manques.append(f"{nom} : {''.join(absents)}")
        print(f"{nom} : {sortie.stat().st_size // 1024} Kio")
    for lic in source.rglob("OFL.txt"):
        shutil.copy(lic, dest / f"OFL-{lic.parent.name}.txt")
    if manques:
        print("polices : glyphes absents —", "; ".join(manques))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(pathlib.Path(sys.argv[1])))
