"""generer_paquets.remplacer_bloc : marqueurs seuls sur leur ligne, idempotence, refus d'un bloc absent."""
import importlib.util, pathlib, pytest

_spec = importlib.util.spec_from_file_location("generer_paquets", pathlib.Path(__file__).resolve().parents[1] / "generer_paquets.py")
gp = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(gp)

GRADLE = """android {
    // la produit entre les marqueurs // <liste-paquets> (annexe C.6).
    signingConfigs { release { } }
}

// <liste-paquets>
// </liste-paquets>

repositories { }
"""

def test_mention_en_commentaire_ignoree(tmp_path):
    f = tmp_path / "build.gradle"; f.write_text(GRADLE, encoding="utf-8")
    gp.remplacer_bloc(f, "// <liste-paquets>", "// </liste-paquets>", 'android { assetPacks = [":voix_c03"] }')
    t = f.read_text(encoding="utf-8")
    assert "signingConfigs { release { } }" in t
    assert '// <liste-paquets>\nandroid { assetPacks = [":voix_c03"] }\n// </liste-paquets>\n' in t

def test_idempotent_et_retour_a_vide(tmp_path):
    f = tmp_path / "build.gradle"; f.write_text(GRADLE, encoding="utf-8")
    for _ in range(2):
        gp.remplacer_bloc(f, "// <liste-paquets>", "// </liste-paquets>", "android { assetPacks = [] }")
    once = f.read_text(encoding="utf-8")
    gp.remplacer_bloc(f, "// <liste-paquets>", "// </liste-paquets>", "android { assetPacks = [] }")
    assert f.read_text(encoding="utf-8") == once
    gp.remplacer_bloc(f, "// <liste-paquets>", "// </liste-paquets>", "")
    assert f.read_text(encoding="utf-8") == GRADLE

def test_bloc_absent_refuse(tmp_path):
    f = tmp_path / "settings.gradle"; f.write_text("include ':app'\n", encoding="utf-8")
    with pytest.raises(SystemExit):
        gp.remplacer_bloc(f, "// <paquets-voix>", "// </paquets-voix>", "")
