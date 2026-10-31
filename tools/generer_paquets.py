#!/usr/bin/env python3
"""Crée un module de paquet de voix Android par chapitre hors socle, et met à jour Gradle."""
import pathlib, re, shutil

RACINE = pathlib.Path(__file__).resolve().parent.parent
ENCODES = RACINE / "voix" / "encodes"
ANDROID = RACINE / "android"
SOCLE = {"c00", "c01", "c02"}

GABARIT = """plugins {{ id 'com.android.asset-pack' }}

assetPack {{
    packName = "voix_{ch}"
    dynamicDelivery {{ deliveryType = "on-demand" }}
}}
"""

def remplacer_bloc(fichier, debut, fin, contenu):
    """Remplace le contenu compris entre deux marqueurs placés chacun seul sur sa ligne.

    Une simple mention du marqueur dans un commentaire n'est jamais prise pour le marqueur ;
    deux exécutions successives donnent un fichier identique ; un marqueur absent est une erreur.
    """
    texte = fichier.read_text(encoding="utf-8")
    motif = re.compile(r"^" + re.escape(debut) + r"[ \t]*\n(?:.*?\n)??" + re.escape(fin) + r"[ \t]*$", re.S | re.M)
    trouves = motif.findall(texte)
    if len(trouves) != 1:
        raise SystemExit(f"{fichier.name} : {len(trouves)} bloc(s) {debut} … {fin} trouvé(s), un seul attendu")
    nouveau = f"{debut}\n{contenu}\n{fin}" if contenu else f"{debut}\n{fin}"
    fichier.write_text(motif.sub(lambda _: nouveau, texte), encoding="utf-8")

def main():
    chapitres = sorted(p.name for p in ENCODES.glob("c[0-9][0-9]") if p.name not in SOCLE)
    for ch in chapitres:
        module = ANDROID / f"voix_{ch}"
        if module.exists():
            shutil.rmtree(module)
        (module / "src/main/assets/voix").mkdir(parents=True)
        shutil.copytree(ENCODES / ch, module / "src/main/assets/voix" / ch)
        (module / "build.gradle").write_text(GABARIT.format(ch=ch), encoding="utf-8")
    remplacer_bloc(ANDROID / "settings.gradle", "// <paquets-voix>", "// </paquets-voix>",
                   "\n".join(f"include ':voix_{ch}'" for ch in chapitres))
    remplacer_bloc(ANDROID / "app/build.gradle", "// <liste-paquets>", "// </liste-paquets>",
                   ("android { assetPacks = [" + ", ".join(f'":voix_{ch}"' for ch in chapitres) + "] }") if chapitres else "")
    print(f"{len(chapitres)} paquets de voix générés")

if __name__ == "__main__":
    main()
