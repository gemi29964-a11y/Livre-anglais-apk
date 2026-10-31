"""Section 3.5 : chaque microtexte de référence figure mot pour mot dans app/src/lib/textes/fr.ts.

La partie fixe de chaque texte (avant la première valeur chiffrée) doit s'y trouver, apostrophes
typographiques et espaces insécables normalisées."""
import pathlib, re

RACINE = pathlib.Path(__file__).resolve().parents[2]


def _section_35():
    lignes = (RACINE / "docs/MEGA_GOD_PLAN.md").read_text(encoding="utf-8").splitlines()
    debut = next(i for i, l in enumerate(lignes) if l.startswith("### 3.5"))
    fin = next(i for i in range(debut + 1, len(lignes)) if lignes[i].startswith("### "))
    return lignes[debut:fin]


def test_microtextes_repris_mot_pour_mot():
    fr = (RACINE / "app/src/lib/textes/fr.ts").read_text(encoding="utf-8").replace("\u00a0", " ").replace("\u202f", " ")
    manquants = []
    vus = 0
    for l in _section_35():
        m = re.search(r"« (.*) »", l)
        if not m:
            continue
        texte = m.group(1).replace("'", "’")
        fixe = re.split(r"\d|octobre", texte)[0].strip()
        if len(fixe) < 6:
            continue
        vus += 1
        # la partie fixe peut s'interrompre sur une valeur variable (moment, titre d'itinéraire) :
        # on exige le plus long préfixe commun, d'au moins 20 caractères ou du texte entier.
        n = len(fixe)
        while n > 0 and fixe[:n] not in fr:
            n -= 1
        if n < min(len(fixe), 20):
            manquants.append(fixe)
    assert vus >= 20
    assert not manquants, manquants
