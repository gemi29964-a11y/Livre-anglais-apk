// Une page par scène compilée (app/static/corpus/cNN.sNN.json), produite à la construction.
import type { EntryGenerator } from './$types';

// « auto » : tant qu'aucune entrée n'existe (scènes non encore écrites), la page reste servie par le repli index.html.
export const prerender = 'auto';

const compilees = import.meta.glob('/static/corpus/c[0-9][0-9].s[0-9][0-9].json');

export const entries: EntryGenerator = () =>
  Object.keys(compilees).map((f) => ({ id: f.replace(/^.*\/(c\d{2}\.s\d{2})\.json$/, '$1') }));

export function load({ params }) {
  return { id: params.id };
}
