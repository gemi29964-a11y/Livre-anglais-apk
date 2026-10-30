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
    texte = fichier.read_text(encoding="utf-8")
    motif = re.compile(re.escape(debut) + r".*?" + re.escape(fin), re.S)
    nouveau = f"{debut}\n{contenu}\n{fin}"
    texte = motif.sub(lambda _: nouveau, texte) if motif.search(texte) else texte + "\n" + nouveau + "\n"
    fichier.write_text(texte, encoding="utf-8")

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
                   "android { assetPacks = [" + ", ".join(f'":voix_{ch}"' for ch in chapitres) + "] }")
    print(f"{len(chapitres)} paquets de voix générés")

if __name__ == "__main__":
    main()
