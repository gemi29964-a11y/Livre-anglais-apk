import { describe, expect, it, vi } from 'vitest';

let ecouteur: ((e: { url: string }) => void) | null = null;
vi.mock('@capacitor/core', () => ({ Capacitor: { isNativePlatform: () => true } }));
vi.mock('@capacitor/app', () => ({
  App: {
    getLaunchUrl: vi.fn(async () => ({ url: 'vivrelanglais://recherche' })),
    addListener: vi.fn(async (_n: string, f: (e: { url: string }) => void) => { ecouteur = f; })
  }
}));

import { ecouterLiens } from './liens';

describe('écoute des adresses sur Android', () => {
  it('suit l’adresse de lancement puis celles reçues en cours de lecture', async () => {
    const aller = vi.fn();
    await ecouterLiens(async () => ({ chapitres: [] }), aller);
    expect(aller).toHaveBeenCalledWith('/recherche/');
    ecouteur?.({ url: 'vivrelanglais://promenade' });
    await new Promise((r) => setTimeout(r, 0));
    expect(aller).toHaveBeenLastCalledWith('/promenade/?programme=reprendre');
  });
  it('ne navigue pas si le sommaire est illisible', async () => {
    const aller = vi.fn();
    await ecouterLiens(async () => null, aller);
    expect(aller).not.toHaveBeenCalled();
  });
});
