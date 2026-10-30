import { describe, expect, it, vi } from 'vitest';

const minimiser = vi.fn(async () => undefined);
vi.mock('@capacitor/app', () => ({ App: { minimizeApp: () => minimiser(), addListener: vi.fn() } }));
vi.mock('@capacitor/core', () => ({ Capacitor: { isNativePlatform: () => false } }));

import { decider, traiterRetour, voletOuvert, installerRetour } from './retour';

describe('retour arrière (10.8)', () => {
  it('décide : volet, puis historique, puis refermer le livre depuis Aujourd’hui', () => {
    expect(decider(1, '/', true)).toBe('volet');
    expect(decider(0, '/livre/', true)).toBe('historique');
    expect(decider(0, '/livre/', false)).toBe('historique');
    expect(decider(0, '/', true)).toBe('quitter');
  });
  it('ferme le volet le plus récent d’abord', () => {
    const a = vi.fn(), b = vi.fn();
    voletOuvert(a); const retirerB = voletOuvert(b);
    expect(traiterRetour('/scene/c01.s01/', true, vi.fn())).toBe('volet');
    expect(b).toHaveBeenCalled();
    retirerB();
    expect(traiterRetour('/scene/c01.s01/', true, vi.fn())).toBe('volet');
    expect(a).toHaveBeenCalled();
  });
  it('remonte l’historique ou revient à Aujourd’hui, et minimise depuis Aujourd’hui', () => {
    const back = vi.spyOn(history, 'back').mockImplementation(() => undefined);
    traiterRetour('/livre/', true, vi.fn());
    expect(back).toHaveBeenCalled();
    const aller = vi.fn();
    traiterRetour('/livre/', false, aller);
    expect(aller).toHaveBeenCalled();
    traiterRetour('/', false, vi.fn());
    expect(minimiser).toHaveBeenCalled();
    installerRetour(() => '/', vi.fn());                      // hors Android : aucun écouteur
  });
});
