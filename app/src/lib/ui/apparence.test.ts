import { describe, expect, it, vi } from 'vitest';
vi.mock('@capacitor/core', () => ({ Capacitor: { isNativePlatform: () => true } }));
const setStyle = vi.fn(async () => undefined);
vi.mock('@capacitor/status-bar', () => ({ StatusBar: { setStyle: (o: unknown) => setStyle(o) }, Style: { Dark: 'DARK', Light: 'LIGHT' } }));

import { appliquer, themeEffectif } from './apparence';
import { DEFAUT } from '$lib/preferences/modele';

describe('apparence (9.2, 9.3)', () => {
  it('résout le thème automatique selon le système', () => {
    expect(themeEffectif('automatique', true, false)).toBe('nuit');
    expect(themeEffectif('automatique', false, false)).toBe('papier');
    expect(themeEffectif('automatique', false, true)).toBe('contraste');
    expect(themeEffectif('ambre', true, true)).toBe('ambre');
  });
  it('applique thème, taille, interligne et police d’aide à la racine', () => {
    const r = document.createElement('html');
    appliquer({ ...DEFAUT, theme: 'nuit', tailleCran: 6, interligneCran: 2, aideLecture: true }, r);
    expect(r.dataset.theme).toBe('nuit');
    expect(r.dataset.aideLecture).toBe('oui');
    expect(r.style.getPropertyValue('--base')).toBe('26px');
    expect(r.style.getPropertyValue('--interligne')).toBe('1.75');
    expect(setStyle).toHaveBeenCalledWith({ style: 'DARK' });
  });
});
