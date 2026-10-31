import { describe, expect, it } from 'vitest';
import { chemin } from './liens';
import type { Sommaire } from '$lib/corpus/chargeur';

const S: Sommaire = { chapitres: [{ id: 'c01', numero: 1, titre: 'Le matin', tailleVoix: 0, scenes: [
  { id: 'c01.s01', numero: '1.1', titre: 'Le réveil', disponible: true, intention: null, expressions: 1 },
  { id: 'c01.s02', numero: '1.2', titre: 'La salle de bains', disponible: false, intention: null, expressions: 0 }] }] };

describe('adresses de l’ouvrage (10.20)', () => {
  it('ouvre expression, scène et destinations', () => {
    expect(chemin('vivrelanglais://expression/c01.s01.A1', S)).toBe('/scene/c01.s01/#c01.s01.A1');
    expect(chemin('vivrelanglais://expression/c01.s01.A1?ecouter=1', S)).toBe('/scene/c01.s01/?ecouter=1#c01.s01.A1');
    expect(chemin('https://vivrelanglais.com/e/c01.s01.A1', S)).toBe('/scene/c01.s01/#c01.s01.A1');
    expect(chemin('vivrelanglais://scene/c01.s01', S)).toBe('/scene/c01.s01/');
    expect(chemin('vivrelanglais://retrouvailles', S)).toBe('/?retrouvailles=1');
    expect(chemin('vivrelanglais://promenade', S)).toBe('/promenade/?programme=reprendre');
    expect(chemin('vivrelanglais://reprendre', S)).toBe('/?reprendre=1');
    expect(chemin('vivrelanglais://recherche', S)).toBe('/recherche/');
  });
  it('toute adresse inconnue ou invalide ouvre Aujourd’hui', () => {
    for (const a of ['vivrelanglais://scene/c01.s02', 'vivrelanglais://scene/../x', 'vivrelanglais://expression/c09.s01.A1',
      'vivrelanglais://inconnu', 'https://ailleurs.com/e/c01.s01.A1', 'pas une adresse', 'vivrelanglais://expression/zzz'])
      expect(chemin(a, S)).toBe('/');
  });
});
