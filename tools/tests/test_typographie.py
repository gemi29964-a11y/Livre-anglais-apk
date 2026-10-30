"""Correcteur typographique (3.4) : insécables dans les chaînes, jamais dans le code ni les commentaires."""
from typographie import corriger, traiter


def test_insecables():
    assert corriger("Quelle heure ? « Oui »") == "Quelle heure\u00a0? «\u00a0Oui\u00a0»"
    assert corriger("7 h 30, 42 %, 38 Mo") == "7\u00a0h 30, 42\u00a0%, 38\u00a0Mo"


def test_code_et_commentaires_intacts():
    source = "/** Durée d'écoute : « 9 h » */\nconst m = a % 60;\nconst x = b ? 'Oui ?' : 'Non';\n"
    sortie = traiter(source, ts=True)
    assert "Durée d'écoute : « 9 h » */" in sortie
    assert "a % 60" in sortie
    assert "b ? 'Oui\u00a0?' : 'Non'" in sortie
