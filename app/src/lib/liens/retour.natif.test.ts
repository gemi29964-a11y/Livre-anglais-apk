import { describe, expect, it, vi } from 'vitest';

let ecouteur: ((e: { canGoBack: boolean }) => void) | null = null;
const minimiser = vi.fn(async () => undefined);
vi.mock('@capacitor/core', () => ({ Capacitor: { isNativePlatform: () => true } }));
vi.mock('@capacitor/app', () => ({
  App: { minimizeApp: () => minimiser(), addListener: vi.fn(async (_n: string, f: (e: { canGoBack: boolean }) => void) => { ecouteur = f; }) }
}));

import { installerRetour } from './retour';

describe('retour arrière sur Android', () => {
  it('installe un seul écouteur et traite le geste et le plan B', () => {
    installerRetour(() => '/', vi.fn());
    installerRetour(() => '/', vi.fn());
    ecouteur?.({ canGoBack: false });
    expect(minimiser).toHaveBeenCalledTimes(1);
    window.dispatchEvent(new Event('retourDemande'));
    expect(minimiser).toHaveBeenCalledTimes(2);
  });
});
