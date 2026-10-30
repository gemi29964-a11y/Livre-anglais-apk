import { beforeEach, describe, expect, it, vi } from 'vitest';
import { chapitreDe, chargerScene, chargerSommaire, fragments, oublierCache, sceneDe, type Sommaire } from './chargeur';

const SOMMAIRE: Sommaire = { chapitres: [{ id: 'c01', numero: 1, titre: 'Le matin', tailleVoix: 0, scenes: [{ id: 'c01.s01', numero: '1.1', titre: 'Le réveil', disponible: true, intention: null, expressions: 0 }] }] };
const reponse = (ok: boolean, corps: unknown) => Promise.resolve({ ok, status: ok ? 200 : 404, json: () => Promise.resolve(corps) } as Response);

describe('chargeur du corpus', () => {
  beforeEach(() => oublierCache());
  it('charge le sommaire une seule fois et retrouve chapitres et scènes', async () => {
    const f = vi.fn(() => reponse(true, SOMMAIRE));
    const s = await chargerSommaire(f);
    await chargerSommaire(f);
    expect(f).toHaveBeenCalledTimes(1);
    expect(chapitreDe(s, 'c01')?.titre).toBe('Le matin');
    expect(sceneDe(s, 'c01.s01')?.scene.numero).toBe('1.1');
    expect(sceneDe(s, 'c09.s09')).toBeUndefined();
  });
  it('réessaie le sommaire après un échec', async () => {
    await expect(chargerSommaire(() => reponse(false, null))).rejects.toThrow('sommaire 404');
    await expect(chargerSommaire(() => reponse(true, SOMMAIRE))).resolves.toEqual(SOMMAIRE);
  });
  it('charge une scène, refuse un identifiant invalide, rend null si absente', async () => {
    expect(await chargerScene('../secret')).toBeNull();
    const f = vi.fn(() => reponse(true, { id: 'c01.s01' }));
    expect(await chargerScene('c01.s01', f)).toEqual({ id: 'c01.s01' });
    await chargerScene('c01.s01', f);
    expect(f).toHaveBeenCalledTimes(1);
    expect(await chargerScene('c01.s02', () => reponse(false, null))).toBeNull();
    expect(await chargerScene('c01.s03', () => Promise.reject(new Error('réseau')))).toBeNull();
  });
  it('sépare l’anglais balisé du français (règle 6)', () => {
    expect(fragments('Dire <en>Good morning</en> au voisin.')).toEqual([
      { en: false, texte: 'Dire ' }, { en: true, texte: 'Good morning' }, { en: false, texte: ' au voisin.' }
    ]);
    expect(fragments('<en>Hi</en>')).toEqual([{ en: true, texte: 'Hi' }]);
  });
});
