"""Contrastes des thèmes (9.2, 9.9) : WCAG AA au minimum pour chaque paire texte/fond."""
import contrastes


def test_formule_wcag():
    assert round(contrastes.ratio("#000000", "#FFFFFF"), 1) == 21.0
    assert round(contrastes.ratio("#777777", "#FFFFFF"), 2) == 4.48


def test_quatre_themes_definis():
    t = contrastes.themes()
    assert {"papier", "ambre", "nuit", "contraste"} <= set(t)


def test_rapport_conforme():
    assert contrastes.main() == 0
