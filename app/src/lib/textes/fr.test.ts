import { describe, expect, it } from 'vitest';
import { duree, enLettres, heure, pluriel, romain, t } from './fr';
import { en } from './en';

/** Les espaces insécables (3.4) sont vérifiées à part ; ici on compare le texte. */
const n = (x: string) => x.replace(/[\u00a0\u202f]/g, ' ');

describe('voix de l’éditeur (3.5)', () => {
  it('écrit les nombres en toutes lettres', () => {
    expect(enLettres(0)).toBe('zéro');
    expect(enLettres(4)).toBe('quatre');
    expect(enLettres(17)).toBe('dix-sept');
    expect(enLettres(20)).toBe('vingt');
    expect(enLettres(21)).toBe('vingt et une');
    expect(enLettres(45)).toBe('quarante-cinq');
    expect(enLettres(70)).toBe('70');
    expect(enLettres(-1)).toBe('-1');
    expect(enLettres(2.5)).toBe('2.5');
  });
  it('accorde, met l’heure et la durée à la française', () => {
    expect(pluriel(1, 'jour', 'jours')).toBe('1 jour');
    expect(pluriel(12, 'jour', 'jours')).toBe('12 jours');
    expect(n(heure(7, 30))).toBe('7 h 30');
    expect(n(heure(18, 0))).toBe('18 h');
    expect(n(heure(7, 5))).toBe('7 h 05');
    expect(duree(25)).toBe('25 minutes');
    expect(duree(1)).toBe('1 minute');
    expect(n(duree(120))).toBe('2 h');
    expect(n(duree(580))).toBe('9 h 40');
  });
  it('place les espaces insécables de la typographie française (3.4)', () => {
    expect(heure(7, 30)).toBe('7\u00a0h\u00a030');
    expect(t.aujourdhui.momentPresent(7, 10, '1.1', 'Le réveil')).toContain('1.1\u00a0:');
    expect(t.voix.arrivent(42)).toContain('42\u00a0%');
  });
  it('numérote les chapitres en chiffres romains', () => {
    expect([1, 4, 9, 14, 19, 26].map(romain)).toEqual(['I', 'IV', 'IX', 'XIV', 'XIX', 'XXVI']);
  });
  it('produit les microtextes du Plan mot pour mot', () => {
    expect(t.aujourdhui.retrouvailles(9, 4)).toBe('9 expressions vous attendent aujourd’hui. Environ quatre minutes.');
    expect(t.aujourdhui.retrouvailles(1, 1)).toBe('1 expression vous attend aujourd’hui. Environ une minute.');
    expect(t.aujourdhui.constance(12)).toBe('12 jours de constance');
    expect(n(t.aujourdhui.momentPresent(7, 10, '1.1', 'Le réveil'))).toBe('Il est 7 h 10. C’est l’heure de la Scène 1.1 : Le réveil.');
    expect(t.aujourdhui.salutation(8)).toBe('Bonjour');
    expect(t.aujourdhui.salutation(14)).toBe('Bon après-midi');
    expect(t.aujourdhui.salutation(21)).toBe('Bonsoir');
    expect(t.aujourdhui.salutation(2)).toBe('Bonsoir');
    expect(n(t.voix.arrivent(42))).toBe('Les voix arrivent… 42 %');
    expect(n(t.carnet.regardArriereMois(9, 63, 580))).toBe('En octobre, 63 expressions vous sont devenues familières. Vous avez écouté 9 h 40 de voix.');
    expect(t.carnet.regardArriereMois(0, 1, 25)).toContain('1 expression vous est devenue familière');
  });
  it('couvre toutes les fonctions de textes', () => {
    const appels: [unknown, unknown[]][] = [
      [t.ouvrage.edition, ['1.0.0']], [t.aujourdhui.reprise, ['1.1', 'Le réveil']], [t.aujourdhui.expressionsRestantes, [3]],
      [t.accueil.ecran, [2]], [t.voix.ecouterAnnonce, ['Britannique', 'Posé']], [t.voix.nonInstallees, [38]],
      [t.voix.faireVenirChapitre, [3]], [t.voix.reparees, [3]], [t.voix.ecouteDuMot, ['going']], [t.voix.confirmationMobile, [40]],
      [t.livre.chapitre, [3]], [t.livre.chapitreRomain, [3]], [t.livre.scenes, [7]], [t.livre.scene, ['1.1']],
      [t.livre.cheminParcouru, [1, 163]], [t.livre.cheminParcouru, [2, 163]], [t.livre.dureeEcoute, [45]],
      [t.scene.moment, ['A', 'Le réveil']], [t.scene.rang, ['A', 1, 4]], [t.scene.declinaisons, [4]], [t.scene.renvoi, ['B']],
      [t.scene.annonceCarte, ['Mon réveil sonne', 'Ton courant']], [t.promenade.minutes, [20]],
      [t.recherche.trouveDans, ['1.1', 'A']], [t.recherche.trouveDansScene, ['1.1']], [t.recherche.parcoursFonction, ['s’excuser']],
      [t.preferences.pourcentage, [90]], [t.preferences.crans, [3, 7]], [t.lireCeLivre.page, [1, 6]]
    ];
    for (const [f, args] of appels) expect(typeof (f as (...a: unknown[]) => string)(...args)).toBe('string');
    expect(en.accueilQuatreVoix).toMatch(/alarm/);
  });
});
