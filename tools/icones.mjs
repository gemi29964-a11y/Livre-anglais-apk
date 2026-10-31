// Icônes et écrans d'ouverture (10.9, annexe C.7) : sources SVG « Encre & Voix » → PNG pour @capacitor/assets,
// plus les drawables vectoriels (monochrome, notification, raccourcis) écrits directement dans android/.
// Usage : node tools/icones.mjs   (depuis la racine ; utilise sharp, installé avec @capacitor/assets)
import { createRequire } from 'node:module';
import { mkdirSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const racine = join(dirname(fileURLToPath(import.meta.url)), '..');
const require = createRequire(join(racine, 'app', 'package.json'));
const sharp = require('sharp');

const ENCRE = '#1F3A5F', VOIX = '#2B5C8A', PAPIER = '#FBF8F3', NUIT = '#121314', ENCRE_NUIT = '#A9C1E6', VOIX_NUIT = '#8DB6E0';

// Le motif, sur la grille de l'icône adaptative (108 × 108, zone sûre de 66 de diamètre centrée) :
// un livre ouvert d'où montent deux ondes — le livre qui parle.
const LIVRE = 'M54 52.4c-4.6-3.7-11.3-4.8-19.1-3.5v29c7.8-1.4 14.5-.2 19.1 3.5 4.6-3.7 11.3-4.9 19.1-3.5v-29c-7.8-1.3-14.5-.2-19.1 3.5Z';
const DOS = 'M54 52.4v29';
const LIGNES = 'M40.6 58.6h8M40.6 65h8M59.4 58.6h8M59.4 65h8';
const ONDES = ['M47.6 40.6a9 9 0 0 1 12.8 0', 'M42.6 35.4a16.2 16.2 0 0 1 22.8 0'];

const motif = (encre, voix, trait = 3.6) => `
  <g fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="${trait}">
    <path d="${LIVRE}" stroke="${encre}"/><path d="${DOS}" stroke="${encre}"/><path d="${LIGNES}" stroke="${encre}"/>
    ${ONDES.map((d) => `<path d="${d}" stroke="${voix}"/>`).join('')}
  </g>`;

const svg = (taille, vue, contenu, fond) =>
  `<svg xmlns="http://www.w3.org/2000/svg" width="${taille}" height="${taille}" viewBox="${vue}">${fond ? `<rect x="-1000" y="-1000" width="3000" height="3000" fill="${fond}"/>` : ''}${contenu}</svg>`;

const sorties = join(racine, 'app', 'assets');
mkdirSync(join(sorties, 'sources'), { recursive: true });
const ecrire = async (nom, source) => {
  writeFileSync(join(sorties, 'sources', nom.replace('.png', '.svg')), source);
  await sharp(Buffer.from(source)).png().toFile(join(sorties, nom));
};

await ecrire('icon-foreground.png', svg(1024, '0 0 108 108', motif(ENCRE, VOIX)));
await ecrire('icon-background.png', svg(1024, '0 0 108 108', '', PAPIER));
await ecrire('icon-only.png', svg(1024, '0 0 108 108', motif(ENCRE, VOIX), PAPIER));
// Écran d'ouverture : le motif seul, petit, au centre (2732 × 2732) ; la marge est laissée au système.
await ecrire('splash.png', svg(2732, '-108 -108 324 324', motif(ENCRE, VOIX, 3.2), PAPIER));
await ecrire('splash-dark.png', svg(2732, '-108 -108 324 324', motif(ENCRE_NUIT, VOIX_NUIT, 3.2), NUIT));
// Icône de la fiche Play (512 × 512, 10.15 / annexe E).
await sharp(Buffer.from(svg(512, '0 0 108 108', motif(ENCRE, VOIX), PAPIER))).png().toFile(join(sorties, 'icone-fiche-512.png'));

// Drawables vectoriels Android.
const res = join(racine, 'android', 'app', 'src', 'main', 'res', 'drawable');
mkdirSync(res, { recursive: true });
const vecteur = (taille, vue, chemins, couleur, trait) => `<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="${taille}dp" android:height="${taille}dp"
    android:viewportWidth="${vue}" android:viewportHeight="${vue}">
${chemins.map((d) => `    <path android:pathData="${d}" android:strokeColor="${couleur}" android:strokeWidth="${trait}"
        android:strokeLineCap="round" android:strokeLineJoin="round" android:fillColor="#00000000" />`).join('\n')}
</vector>
`;
// Icône à thème (Android 13+) : le même motif, d'une seule teinte.
writeFileSync(join(res, 'ic_launcher_monochrome.xml'), vecteur(108, 108, [LIVRE, DOS, LIGNES, ...ONDES], '#FFFFFFFF', 3.6));
// Petite icône de notification : la plume, blanc sur transparent, 24 dp.
const PLUME = ['M19.5 4.5c-6.2.4-10.6 4.6-12 11.3L5 20', 'M19.5 4.5c.3 6.5-4.4 10.9-11 11.4', 'M11 13l3.6-3.6'];
writeFileSync(join(res, 'ic_stat_plume.xml'), vecteur(24, 24, PLUME, '#FFFFFFFF', 1.75));
// Raccourcis : livre, carnet, casque, loupe (jeu d'icônes de l'interface, 9.6), encre sur papier.
const rond = (contenu) => `<?xml version="1.0" encoding="utf-8"?>
<layer-list xmlns:android="http://schemas.android.com/apk/res/android">
    <item><shape android:shape="oval"><solid android:color="${PAPIER}" /></shape></item>
    <item android:drawable="@drawable/${contenu}" android:left="12dp" android:top="12dp" android:right="12dp" android:bottom="12dp" />
</layer-list>
`;
const RACCOURCIS = {
  livre: ['M12 6.8c-2-1.6-4.9-2.1-8.3-1.5v12.6c3.4-.6 6.3-.1 8.3 1.5 2-1.6 4.9-2.1 8.3-1.5V5.3c-3.4-.6-6.3-.1-8.3 1.5Z', 'M12 6.8v12.6', 'M6.3 9.2c1.3-.1 2.5.1 3.4.6M14.3 9.8c.9-.5 2.1-.7 3.4-.6'],
  carnet: ['M7 3.2h9.6a2 2 0 0 1 2 2v13.6a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V5.2a2 2 0 0 1 2-2Z', 'M8.6 3.2v17.6', 'M15.6 3.2v17.6', 'M11.2 8.2h2.4M11.2 11.2h2.4'],
  casque: ['M4.2 15.5v-3.2a7.8 7.8 0 0 1 15.6 0v3.2', 'M4.8 14h1a1.6 1.6 0 0 1 1.6 1.6v3a1.6 1.6 0 0 1-1.6 1.6h-1a1.6 1.6 0 0 1-1.6-1.6v-3A1.6 1.6 0 0 1 4.8 14Z', 'M18.2 14h1a1.6 1.6 0 0 1 1.6 1.6v3a1.6 1.6 0 0 1-1.6 1.6h-1a1.6 1.6 0 0 1-1.6-1.6v-3a1.6 1.6 0 0 1 1.6-1.6Z'],
  loupe: ['M16.5 10.5a6 6 0 1 1-12 0 6 6 0 0 1 12 0Z', 'M15 15l5.2 5.2', 'M8 9.2a2.8 2.8 0 0 1 2.4-1.6']
};
for (const [nom, chemins] of Object.entries(RACCOURCIS)) {
  writeFileSync(join(res, `rac_${nom}_trait.xml`), vecteur(24, 24, chemins, ENCRE, 1.75));
  writeFileSync(join(res, `rac_${nom}.xml`), rond(`rac_${nom}_trait`));
}
console.log('icônes : sources SVG, PNG et drawables écrits');
