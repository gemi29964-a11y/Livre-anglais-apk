import { beforeEach, describe, expect, it, vi } from 'vitest';

const stock = new Map<string, string>();
vi.mock('@capacitor/preferences', () => ({
  Preferences: {
    get: vi.fn(async ({ key }: { key: string }) => {
      if (key === 'casse') throw new Error('stockage');
      return { value: stock.get(key) ?? null };
    }),
    set: vi.fn(async ({ key, value }: { key: string; value: string }) => void stock.set(key, value))
  }
}));

import { preferences } from './magasin.svelte';
import { DEFAUT } from './modele';

describe('magasin des préférences', () => {
  beforeEach(() => stock.clear());
  it('ouvre avec les valeurs par défaut puis enregistre chaque changement', async () => {
    await preferences.ouvrir();
    expect(preferences.pret).toBe(true);
    expect(preferences.valeur.accent).toBe(DEFAUT.accent);
    await preferences.changer({ accent: 'us', passagesEcho: 12 });
    expect(JSON.parse(stock.get('preferences')!).accent).toBe('us');
    expect(preferences.valeur.passagesEcho).toBe(5);
    await preferences.ouvrir();
    expect(preferences.valeur.accent).toBe('us');
  });
  it('se rabat sur les valeurs par défaut si la sauvegarde est illisible', async () => {
    stock.set('preferences', '{abîmé');
    await preferences.ouvrir();
    expect(preferences.valeur).toEqual(DEFAUT);
  });
});
