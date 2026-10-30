"""Contrôle des contrastes des quatre thèmes (9.2, 9.9, 11.2).

Lit app/src/lib/design/themes.css. Pour chaque thème, chaque couleur de texte (encre, encre-douce,
accent, voix-am, voix-brit, ton-*) doit atteindre 4,5:1 sur --fond et --surface, et 7:1 dans le
thème Contraste. Écrit le tableau mesuré dans pilotage/portes/contrastes.md. Code 1 si un seuil manque.
"""
from __future__ import annotations

import re
import sys

from commun import APP, RACINE

TEXTES = ["encre", "encre-douce", "accent", "voix-am", "voix-brit",
          "ton-courant", "ton-complice", "ton-cru", "ton-soutenu"]


def lum(h: str) -> float:
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))
    f = lambda c: c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def ratio(a: str, b: str) -> float:
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def themes() -> dict[str, dict[str, str]]:
    css = (APP / "src/lib/design/themes.css").read_text(encoding="utf-8")
    sortie = {}
    for m in re.finditer(r"\[data-theme='(\w+)'\]\s*\{([^}]*)\}", css):
        if m.group(1) in sortie:
            continue
        sortie[m.group(1)] = dict(re.findall(r"--([\w-]+):\s*(#[0-9A-Fa-f]{6})", m.group(2)))
    return sortie


def main() -> int:
    t = themes()
    lignes = ["# Porte : contrastes des thèmes (9.2)", "",
              "| Thème | Couleur | sur --fond | sur --surface | Seuil | Verdict |", "|---|---|---|---|---|---|"]
    echecs = 0
    for nom in ("papier", "ambre", "nuit", "contraste"):
        j = t[nom]
        seuil = 7.0 if nom == "contraste" else 4.5
        for c in TEXTES:
            rf, rs = ratio(j[c], j["fond"]), ratio(j[c], j["surface"])
            ok = min(rf, rs) >= seuil
            echecs += not ok
            lignes.append(f"| {nom} | --{c} {j[c]} | {rf:.2f}:1 | {rs:.2f}:1 | {seuil}:1 | {'conforme' if ok else 'ÉCHEC'} |")
    lignes += ["", f"Résultat : {'conforme' if not echecs else f'{echecs} échec(s)'}."]
    porte = RACINE / "pilotage/portes/contrastes.md"
    porte.parent.mkdir(parents=True, exist_ok=True)
    porte.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    print("\n".join(lignes[-1:]))
    if echecs:
        print("\n".join(l for l in lignes if "ÉCHEC" in l))
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
