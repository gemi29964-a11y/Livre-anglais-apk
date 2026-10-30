"""Validation du corpus (10.4) : densité, phrasés complets, anglais balisé, typographie."""
import valider_corpus as vc


def test_densite():
    r = vc.Rapport(brouillon=False)
    vc.densite(r, "s", "moments", 7)
    vc.densite(r, "s", "moments", 16)
    vc.densite(r, "s", "moments", 10)
    assert len(r.blocages) == 2 and len(r.avertissements) == 1
    b = vc.Rapport(brouillon=True)
    vc.densite(b, "s", "moments", 7)
    assert b.blocages == [] and len(b.avertissements) == 1      # D-014 : souple en rédaction seulement


def test_quatre_phrases():
    p = {"phrase": "HÈ·lo", "expert": "/ˈhel.əʊ/"}
    assert vc.quatre_phrases({"uk": {"pose": p, "spontane": p}, "us": {"pose": p, "spontane": p}})
    assert not vc.quatre_phrases({"uk": {"pose": p}})
    assert not vc.quatre_phrases(None)


def test_anglais_non_balise_et_typographie():
    assert vc.anglais_non_balise("Dire thank you au serveur") == ["thank", "you"]
    assert vc.anglais_non_balise("Dire <en>thank you</en> au serveur") == []
    assert vc.typographie("Quelle heure\u00a0?")
    assert not vc.typographie("Quelle heure ?")


def test_corpus_actuel_valide_en_redaction():
    r = vc.valider(brouillon=True)
    assert r.blocages == []
