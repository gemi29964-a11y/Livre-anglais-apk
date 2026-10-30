// Options MiniSearch partagées par l'index pré-calculé (tools/index_recherche.mjs) et l'application
// (8.9) : insensible aux accents et à la casse, préfixe, distance d'édition 1 dès cinq lettres.

/** @param {string} terme */
export function normaliserTerme(terme) {
  return terme
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/[’']/g, "'")
    .toLowerCase();
}

/** @type {import('minisearch').Options} */
export const OPTIONS = {
  idField: 'ref',
  fields: ['texte', 'complement'],
  storeFields: ['ref', 'genre', 'texte', 'sens', 'scene', 'numero', 'moment', 'lien'],
  processTerm: (terme) => normaliserTerme(terme),
  tokenize: (texte) => texte.split(/[\s\-–—.,;:!?«»"()…/]+/u).filter(Boolean),
  searchOptions: {
    prefix: true,
    fuzzy: (terme) => (terme.length >= 5 ? 1 : 0),
    boost: { texte: 2 },
    processTerm: (terme) => normaliserTerme(terme)
  }
};
