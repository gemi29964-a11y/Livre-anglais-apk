import { describe, expect, it } from 'vitest';
import { decouper, nombreSyllabes } from './phrase';

describe('le phrasé (6.2 à 6.4)', () => {
  it('découpe l’exemple du Plan : syllabes, forte en capitales, frontières, intonation', () => {
    const s = decouper('maï ə·LÂMZ gəou·ing OF ↘');
    expect(s.filter((x) => x.genre === 'syllabe').map((x) => (x as { texte: string }).texte)).toEqual(['maï', 'ə', 'lâmz', 'gəou', 'ing', 'of']);
    const fortes = s.filter((x) => x.genre === 'syllabe' && x.forte).map((x) => (x as { texte: string }).texte);
    expect(fortes).toEqual(['lâmz', 'of']);
    expect(s.filter((x) => x.genre === 'frontiere')).toHaveLength(2);
    expect(s.at(-1)).toEqual({ genre: 'intonation', texte: '↘' });
    expect(nombreSyllabes(s)).toBe(6);
  });

  it('reconnaît liaison, son retenu, coup de glotte, t battu, r de liaison', () => {
    const s = decouper('WO‿tə(t) bʌʔ·n LÂɾə FÔʳ ↗↘');
    const genres = s.map((x) => x.genre);
    expect(genres).toContain('lien');
    expect(genres).toContain('retenu');
    expect(genres).toContain('glotte');
    expect(genres).toContain('battu');
    expect(genres).toContain('liaisonR');
    expect(s.at(-1)).toEqual({ genre: 'intonation', texte: '↗↘' });
    expect(s.find((x) => x.genre === 'retenu')).toEqual({ genre: 'retenu', texte: 't' });
  });

  it('écarte les espaces multiples et finales, garde une parenthèse orpheline sans planter', () => {
    const s = decouper('  HÈ·lo   (  ');
    expect(s[0].genre).toBe('syllabe');
    expect(s.at(-1)?.genre).not.toBe('espace');
    expect(s.filter((x) => x.genre === 'espace').length).toBeLessThanOrEqual(1);
  });

  it('numérote les syllabes dans l’ordre pour la synchronisation', () => {
    const idx = decouper('A·BI·cə').filter((x) => x.genre === 'syllabe').map((x) => (x as { index: number }).index);
    expect(idx).toEqual([0, 1, 2]);
  });
});
