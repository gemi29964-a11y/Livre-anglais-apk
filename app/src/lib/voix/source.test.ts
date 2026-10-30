import { beforeEach, describe, expect, it, vi } from 'vitest';

const etat = vi.fn();
vi.mock('@capacitor/core', () => ({
  registerPlugin: () => ({ etat: (o: unknown) => etat(o) }),
  Capacitor: { convertFileSrc: (c: string) => `https://localhost/_capacitor_file_${c}` }
}));

import { nomFichier, oublierBase, urlSens, urlVoix } from './source';

describe('source des voix (10.6, 10.20)', () => {
  beforeEach(() => { etat.mockReset(); oublierBase('c05'); oublierBase('c06'); });
  it('nomme les fichiers selon la convention du manifeste', () => {
    expect(nomFichier('c01.s01.A1.e1', 'uk', 'pose')).toBe('c01s01-A1-e1.uk.pose.opus');
    expect(nomFichier('c12.s03.sv.l04', 'us', 'spontane')).toBe('c12s03-sv-l04.us.spontane.opus');
  });
  it('sert le socle (Prélude, chapitres 1 et 2) depuis le livre lui-même', async () => {
    expect(await urlVoix('c01.s01.A1.e1', 'uk', 'pose')).toBe('/voix/c01/s01/c01s01-A1-e1.uk.pose.opus');
    expect(await urlSens('c00.s02.A1')).toBe('/voix/c00/s02/c00s02-A1.fr.sens.opus');
    expect(etat).not.toHaveBeenCalled();
  });
  it('sert un chapitre installé depuis son paquet, une seule interrogation par chapitre', async () => {
    etat.mockResolvedValue({ etat: 'installe', base: '/data/paquet', taille: 10 });
    const u = await urlVoix('c05.s01.A1.e1', 'us', 'pose');
    expect(u).toBe('https://localhost/_capacitor_file_/data/paquet/voix/c05/s01/c05s01-A1-e1.us.pose.opus');
    await urlVoix('c05.s01.A2.e1', 'us', 'pose');
    expect(etat).toHaveBeenCalledTimes(1);
    expect(await urlSens('c05.s01.A1')).toBe('https://localhost/_capacitor_file_/data/paquet/voix/c05/s01/c05s01-A1.fr.sens.opus');
  });
  it('rend null pour un chapitre absent', async () => {
    etat.mockResolvedValue({ etat: 'absent', taille: 10 });
    expect(await urlVoix('c06.s01.A1.e1', 'uk', 'pose')).toBeNull();
    expect(await urlSens('c06.s01.A1')).toBeNull();
    oublierBase('c06');
    expect(await urlSens('c06.s01.A1')).toBeNull();
  });
});
