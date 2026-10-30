"""Vérificateur du phrasé (6.2 à 6.4)."""
from phrase_verifier import verifier_ensemble, verifier_phrase


def test_exemple_du_plan_conforme():
    assert verifier_phrase("x", {"phrase": "maï ə·LÂMZ gəou·ing OF ↘", "expert": "/maɪ əˈlɑːmz ˌɡəʊɪŋ ˈɒf/"}) == []


def test_graphies_proscrites():
    assert verifier_phrase("x", {"phrase": "aï DOWN nəou", "expert": "/aɪ dəʊnt nəʊ/"})
    assert verifier_phrase("x", {"phrase": "guÈS", "expert": "/ɡes/"})
    assert verifier_phrase("x", {"phrase": "KISS", "expert": "/kɪs/"})
    assert verifier_phrase("x", {"phrase": "DAT", "expert": "/ðæt/"})          # /ð/ sans dh


def test_sans_syllabe_forte_ou_expert_mal_forme():
    assert any("accentuée" in f for f in verifier_phrase("x", {"phrase": "hè·lo", "expert": "/həˈləʊ/"}))
    assert any("barres" in f for f in verifier_phrase("x", {"phrase": "hə·LO", "expert": "həˈləʊ"}))
    assert any("hors liste" in f for f in verifier_phrase("x", {"phrase": "hə·LO#", "expert": "/həˈləʊ/"}))


def test_quatre_transcriptions_recopiees():
    p = {"phrase": "gʊd MÔ·ning", "expert": "/ɡʊd ˈmɔːnɪŋ/"}
    f = verifier_ensemble("x", {"uk": {"pose": p, "spontane": p}, "us": {"pose": p, "spontane": p}})
    assert any("une seule transcription" in x for x in f)
    assert verifier_ensemble("x", None) == []
