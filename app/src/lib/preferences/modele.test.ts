import { describe, expect, it } from 'vitest';
import { DEFAUT, lire, selonNiveau, usageOuvert } from './modele';

describe('préférences (8.10)', () => {
  it('rend les valeurs par défaut pour une sauvegarde vide ou abîmée', () => {
    expect(lire(undefined)).toEqual(DEFAUT);
    expect(lire('n’importe quoi')).toEqual(DEFAUT);
  });
  it('borne les valeurs hors limites et écarte les inconnues', () => {
    const p = lire({ passagesEcho: 9, tailleCran: -3, retention: 99.4, nouvellesParJour: 'x', accent: 'fr', theme: 'nuit',
      formesEcartees: ['miroir', 'inconnue'], rendezVous: { heure: 25, minute: 7.6, jours: [0, 9, 3] }, ecranAccueil: { origine: 'ouvrage' } });
    expect(p.passagesEcho).toBe(5);
    expect(p.tailleCran).toBe(0);
    expect(p.retention).toBe(95);
    expect(p.nouvellesParJour).toBe(DEFAUT.nouvellesParJour);
    expect(p.accent).toBe('uk');
    expect(p.theme).toBe('nuit');
    expect(p.formesEcartees).toEqual(['miroir']);
    expect(p.rendezVous).toEqual({ actif: false, heure: 23, minute: 8, jours: [0, 3] });
    expect(p.ecranAccueil.origine).toBe('ouvrage');
  });
  it('déduit les réglages du niveau choisi à l’accueil (8.11)', () => {
    const f = selonNiveau(DEFAUT, 'fondations');
    expect([f.rythme, f.voixDuSens, f.courbe, usageOuvert(f)]).toEqual(['pose', true, false, true]);
    const a = selonNiveau(DEFAUT, 'aisance');
    expect([a.rythme, a.voixDuSens, a.courbe, usageOuvert(a)]).toEqual(['pose', true, true, false]);
    const m = selonNiveau(DEFAUT, 'maitrise');
    expect([m.rythme, m.voixDuSens, m.courbe]).toEqual(['spontane', false, true]);
  });
});
