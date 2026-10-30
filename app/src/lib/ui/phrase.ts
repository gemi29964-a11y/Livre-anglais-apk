// Transforme une chaîne du Phrasé (6.2 à 6.4) en segments typographiques (10.6, composant Phrase).
export type Segment =
  | { genre: 'syllabe'; texte: string; forte: boolean; index: number }
  | { genre: 'frontiere' }                         // ·  point médian discret
  | { genre: 'lien' }                              // ‿  les mots se collent
  | { genre: 'espace' }
  | { genre: 'retenu'; texte: string }             // (t) son retenu
  | { genre: 'glotte' }                            // ʔ  coup de glotte → ’
  | { genre: 'battu'; index: number }              // ɾ  t battu → d pointillé
  | { genre: 'liaisonR' }                          // ʳ  r de liaison → r en exposant
  | { genre: 'intonation'; texte: string };        // ↗ ↘ ↗↘

const LETTRE = /[A-Za-zÀ-ÖØ-öø-ÿəƏ]/;

export function decouper(phrase: string): Segment[] {
  const sortie: Segment[] = [];
  let i = 0, index = 0, courant = '';
  const fermer = () => {
    if (!courant) return;
    const forte = courant !== courant.toLowerCase() && courant === courant.toUpperCase();
    sortie.push({ genre: 'syllabe', texte: forte ? courant.toLowerCase() : courant, forte, index: index++ });
    courant = '';
  };
  while (i < phrase.length) {
    const c = phrase[i];
    if (LETTRE.test(c)) { courant += c; i++; continue; }
    if (c === '(' ) {
      const fin = phrase.indexOf(')', i);
      if (fin > i) { fermer(); sortie.push({ genre: 'retenu', texte: phrase.slice(i + 1, fin) }); i = fin + 1; continue; }
    }
    if (c === 'ɾ') {
      // le t battu fait partie de la syllabe qui suit : il s'affiche comme un d pointillé
      fermer(); sortie.push({ genre: 'battu', index }); i++; continue;
    }
    fermer();
    if (c === '·') sortie.push({ genre: 'frontiere' });
    else if (c === '‿') sortie.push({ genre: 'lien' });
    else if (c === 'ʔ') sortie.push({ genre: 'glotte' });
    else if (c === 'ʳ') sortie.push({ genre: 'liaisonR' });
    else if (c === '↗' || c === '↘') {
      const dernier = sortie[sortie.length - 1];
      if (dernier && dernier.genre === 'intonation') dernier.texte += c;
      else sortie.push({ genre: 'intonation', texte: c });
    } else if (c === ' ') {
      if (sortie.length && sortie[sortie.length - 1].genre !== 'espace') sortie.push({ genre: 'espace' });
    }
    i++;
  }
  fermer();
  while (sortie.length && sortie[sortie.length - 1].genre === 'espace') sortie.pop();
  return sortie;
}

/** Nombre de syllabes indexées (pour la synchronisation avec le champ `syllabes` du manifeste). */
export function nombreSyllabes(segments: Segment[]): number {
  return segments.filter((s) => s.genre === 'syllabe').length;
}
