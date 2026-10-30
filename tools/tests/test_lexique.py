"""Contrôle du lexique (3.3) : un terme banni, un texte de remplissage ou une faute typographique bloquent."""
import lexique_verifier as lv
from commun import termes_bannis


def test_terme_banni_detecte():
    assert termes_bannis("Validez votre score pour débloquer le niveau suivant.") == ["score", "débloquer"]
    assert "téléchargement" in termes_bannis("Téléchargement en cours")
    assert termes_bannis("Les voix arrivent… 42 %") == []


def test_anglais_balise_ignore():
    assert termes_bannis("On dit <en>Take the test</en> au bureau.") == []
    assert termes_bannis('Dire <span lang="en">test</span> ici.') == []
    assert termes_bannis("Passer un test.") == ["test"]


def test_locutions_permises_D021():
    assert termes_bannis("Itinéraire en cours") == []
    assert termes_bannis("au cours de la journée") == []
    assert termes_bannis("Un cours d’anglais") == ["cours"]


def test_remplissage_et_emoji():
    r = lv.Rapport()
    r.examiner("x", "TODO écrire le sens")
    r.examiner("y", "Lorem ipsum dolor")
    r.examiner("z", "Bravo 🎉")
    assert len(r.fautes) == 3


def test_typographie_interface():
    r = lv.Rapport()
    r.examiner("a", "Bravo !", interface=True)
    r.examiner("b", "l'anglais", interface=True)
    r.examiner("c", "Attendez...", interface=True)
    r.examiner("d", "Quelle heure ?", interface=True)
    r.examiner("e", "«\u00a0Bonjour»", interface=True)
    assert len(r.fautes) == 5
    r = lv.Rapport()
    r.examiner("f", "Quelle heure\u00a0? «\u00a0Bonjour\u00a0»", interface=True)
    assert r.fautes == []


def test_typographie_corpus():
    r = lv.Rapport()
    r.examiner("a", "C'est l'heure.")
    r.examiner("b", "On dit <en>it's fine</en> ici.")
    assert len(r.fautes) == 1


def test_construit(tmp_path):
    (tmp_path / "index.html").write_text('<p>Votre score</p><p lang="en">test</p><button aria-label="Cliquer ici">x</button>', encoding="utf-8")
    (tmp_path / "a.js").write_text("// TODO", encoding="utf-8")
    r = lv.Rapport()
    lv.construit(r, tmp_path)
    assert any("score" in f for f in r.fautes)
    assert any("cliquer" in f for f in r.fautes)
    assert any("remplissage" in f for f in r.fautes)
    assert not any("« test »" in f for f in r.fautes)


def test_depot_conforme():
    r = lv.Rapport()
    lv.textes_interface(r)
    lv.gabarits(r)
    lv.corpus(r)
    assert r.fautes == []
    assert r.textes > 500
