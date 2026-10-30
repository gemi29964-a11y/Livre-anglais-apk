// Index MiniSearch pré-calculé (10.5, étape 5) : index-fr.json et index-en.json.
// Lit app/static/corpus/sommaire.json et les scènes compilées ; écrit les deux index sérialisés.
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import MiniSearch from '../app/node_modules/minisearch/dist/es/index.js';
import { OPTIONS } from '../app/src/lib/recherche/options.js';

const racine = join(dirname(fileURLToPath(import.meta.url)), '..');
const dossier = join(racine, 'app/static/corpus');
const sommaire = JSON.parse(readFileSync(join(dossier, 'sommaire.json'), 'utf-8'));
const sansBalise = (s = '') => s.replace(/<\/?en>/g, '');
const fr = [], en = [];

for (const ch of sommaire.chapitres) {
  fr.push({ ref: ch.id, genre: 'chapitre', texte: sansBalise(ch.titre), complement: '', lien: `/livre/${ch.id}/`, numero: String(ch.numero) });
  for (const sc of ch.scenes) {
    fr.push({ ref: sc.id, genre: 'scene', texte: sansBalise(sc.titre), complement: sansBalise(sc.intention ?? ''), scene: sc.id, numero: sc.numero, lien: sc.disponible ? `/scene/${sc.id}/` : `/livre/${ch.id}/` });
    const f = join(dossier, `${sc.id}.json`);
    if (!sc.disponible || !existsSync(f)) continue;
    const s = JSON.parse(readFileSync(f, 'utf-8'));
    for (const m of s.moments) {
      for (const x of m.expressions) {
        const lien = `/scene/${s.id}/#${x.id}`;
        const principal = x.enonces[0];
        fr.push({ ref: `${x.id}#fr`, genre: 'expression', texte: sansBalise(x.sens), complement: sansBalise(`${x.usage} ${x.coulisses ?? ''} ${x.fonctions.join(' ')} ${x.situations.join(' ')}`), sens: x.sens, scene: s.id, numero: sc.numero, moment: m.lettre, lien, enonce: principal.id });
        for (const e of x.enonces) {
          en.push({ ref: e.id, genre: 'enonce', texte: `${e.texte.uk} ${e.texte.us === e.texte.uk ? '' : e.texte.us}`, complement: '', sens: x.sens, scene: s.id, numero: sc.numero, moment: m.lettre, lien });
        }
        for (const d of x.declinaisons) {
          en.push({ ref: d.id, genre: 'declinaison', texte: `${d.texte.uk} ${d.texte.us === d.texte.uk ? '' : d.texte.us}`, complement: '', sens: d.sens, scene: s.id, numero: sc.numero, moment: m.lettre, lien });
          fr.push({ ref: `${d.id}#fr`, genre: 'declinaison', texte: sansBalise(d.sens), complement: '', sens: d.sens, scene: s.id, numero: sc.numero, moment: m.lettre, lien });
        }
      }
    }
  }
}

for (const [nom, docs] of [['index-fr.json', fr], ['index-en.json', en]]) {
  const index = new MiniSearch(OPTIONS);
  index.addAll(docs);
  writeFileSync(join(dossier, nom), JSON.stringify(index));
  console.log(`${nom} : ${docs.length} entrées`);
}
