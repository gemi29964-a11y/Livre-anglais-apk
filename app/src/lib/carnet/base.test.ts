import { describe, expect, it } from 'vitest';
import { BaseCarnet, constance, jourDePratique } from './base';

describe('mon carnet (8.8)', () => {
  it('fait basculer la journée de pratique à 4 h du matin', () => {
    expect(jourDePratique(new Date(2026, 9, 30, 3, 59))).toBe('2026-10-29');
    expect(jourDePratique(new Date(2026, 9, 30, 4, 0))).toBe('2026-10-30');
  });
  it('compte la constance avec un jour de grâce par semaine', () => {
    expect(constance([], '2026-10-30')).toBe(0);
    expect(constance(['2026-10-28', '2026-10-29', '2026-10-30'], '2026-10-30')).toBe(3);
    expect(constance(['2026-10-28', '2026-10-29'], '2026-10-30')).toBe(2);           // aujourd'hui pas encore pratiqué
    expect(constance(['2026-10-26', '2026-10-27', '2026-10-29', '2026-10-30'], '2026-10-30')).toBe(4); // un oubli pardonné
    expect(constance(['2026-10-24', '2026-10-27', '2026-10-30'], '2026-10-30')).toBe(1); // deux oublis rapprochés
  });
  it('enregistre et relit marque-pages, pratique et reprise', async () => {
    const b = new BaseCarnet('essai');
    await b.marquePages.put({ id: 'c01.s01.A1', genre: 'expression', scene: 'c01.s01', date: 1 });
    await b.pratique.put({ jour: '2026-10-30', scenes: 1, retrouvailles: 0, minutes: 6 });
    await b.lecture.put({ cle: 'reprise', scene: 'c01.s01', moment: 'A', expression: 'c01.s01.A1', date: 2 });
    expect(await b.marquePages.count()).toBe(1);
    expect((await b.lecture.get('reprise'))?.scene).toBe('c01.s01');
    expect(constance((await b.pratique.toArray()).map((p) => p.jour), '2026-10-30')).toBe(1);
    await b.delete();
  });
});
