// app/src/lib/voix/moteur.ts
import { urlVoix } from './source';
import type { Accent, Rythme } from '$lib/corpus/types';

type Cle = string;
export type Issue = 'fini' | 'interrompu' | 'absent';
export interface Lecture {
  id: string; accent: Accent; rythme: Rythme;
  mots?: [string, number, number][];
  syllabes?: [number, number, 0 | 1][];
  /** segment à lire, en secondes (écoute au mot) */
  de?: number; a?: number;
}

class MoteurVoix {
  private ctx: AudioContext | null = null;
  private tampons = new Map<Cle, AudioBuffer>();          // cache LRU
  private enCours = new Map<Cle, Promise<AudioBuffer | null>>();
  private source: AudioBufferSourceNode | null = null;
  private gain: GainNode | null = null;
  private terminer: ((i: Issue) => void) | null = null;    // résout la lecture en cours
  private debut = 0;
  private decalage = 0;
  private raf = 0;
  private generation = 0;                                  // invalide les enchaînements interrompus
  private static readonly MAX = 96;
  onMot: (index: number) => void = () => {};
  onSyllabeForte: () => void = () => {};                   // branché sur le battement (8.15)
  onTemps: (t: number) => void = () => {};                 // dessine la courbe (8.15)

  private contexte(): AudioContext {
    if (!this.ctx) this.ctx = new AudioContext({ latencyHint: 'interactive', sampleRate: 48000 });
    if (this.ctx.state === 'suspended') void this.ctx.resume();
    return this.ctx;
  }

  private cle(id: string, a: Accent, r: Rythme): Cle { return `${id}|${a}|${r}`; }

  async preparer(id: string, a: Accent, r: Rythme): Promise<AudioBuffer | null> {
    const k = this.cle(id, a, r);
    const t = this.tampons.get(k);
    if (t) { this.tampons.delete(k); this.tampons.set(k, t); return t; }  // rafraîchit l'ordre LRU
    if (this.enCours.has(k)) return this.enCours.get(k)!;
    const p = (async () => {
      try {
        const url = await urlVoix(id, a, r);
        if (!url) return null;
        const rep = await fetch(url);
        if (!rep.ok) return null;
        const tampon = await this.contexte().decodeAudioData(await rep.arrayBuffer());
        this.tampons.set(k, tampon);
        while (this.tampons.size > MoteurVoix.MAX) this.tampons.delete(this.tampons.keys().next().value!);
        return tampon;
      } catch { return null; }                              // fichier abîmé : signalé par 10.21
    })().finally(() => this.enCours.delete(k));
    this.enCours.set(k, p);
    return p;
  }

  /** Joue une voix ; la promesse se résout quand elle finit, est interrompue, ou est absente. */
  async jouer(l: Lecture): Promise<Issue> {
    const ctx = this.contexte();
    const tampon = await this.preparer(l.id, l.accent, l.rythme);
    if (!tampon) return 'absent';
    this.arreter();
    const g = ctx.createGain();
    const t0 = ctx.currentTime;
    const fondu = l.de !== undefined ? 0.015 : 0.005;
    g.gain.setValueAtTime(0, t0);
    g.gain.linearRampToValueAtTime(1, t0 + fondu);
    const s = ctx.createBufferSource();
    s.buffer = tampon;
    s.connect(g).connect(ctx.destination);
    this.decalage = Math.max(0, l.de ?? 0);
    const duree = l.a !== undefined ? Math.max(0.05, l.a - this.decalage) : undefined;
    if (duree !== undefined) {                                // fondu de sortie du segment
      g.gain.setValueAtTime(1, t0 + duree - fondu);
      g.gain.linearRampToValueAtTime(0, t0 + duree);
    }
    this.debut = t0;
    const issue = new Promise<Issue>((ok) => (this.terminer = ok));
    s.onended = () => {
      if (this.source !== s) return;
      this.source = null; cancelAnimationFrame(this.raf);
      this.terminer?.('fini'); this.terminer = null;
    };
    s.start(0, this.decalage, duree);
    this.source = s; this.gain = g;
    this.suivre(l);
    return issue;
  }

  /** Écoute au mot (8.14) : le mot tel qu'il a été dit dans la phrase. */
  async jouerMot(l: Lecture, index: number): Promise<Issue> {
    const m = l.mots?.[index];
    if (!m) return 'absent';
    let [, de, a] = m;
    if (a - de < 0.18 && l.mots) {                           // mot faible : son groupe de souffle
      const voisins = l.mots.slice(Math.max(0, index - 1), index + 2);
      de = voisins[0][1]; a = voisins[voisins.length - 1][2];
    }
    return this.jouer({ ...l, de, a, mots: undefined, syllabes: undefined });
  }

  private suivre(l: Lecture) {
    let dernierMot = -1, derniereSyllabe = -1;
    const pas = () => {
      if (!this.ctx || !this.source) return;
      const t = this.ctx.currentTime - this.debut + this.decalage;
      this.onTemps(t);
      if (l.mots) {
        const i = l.mots.findIndex(([, d, f]) => t >= d && t < f);
        if (i !== -1 && i !== dernierMot) { dernierMot = i; this.onMot(i); }
      }
      if (l.syllabes) {
        const j = l.syllabes.findIndex(([d, f]) => t >= d && t < f);
        if (j !== -1 && j !== derniereSyllabe) { derniereSyllabe = j; if (l.syllabes[j][2] === 1) this.onSyllabeForte(); }
      }
      this.raf = requestAnimationFrame(pas);
    };
    this.raf = requestAnimationFrame(pas);
  }

  /** Arrête la voix en cours (fondu de 30 ms) ; toute attente en cours reçoit « interrompu ». */
  arreter(fondu = 0.03) {
    this.generation++;
    cancelAnimationFrame(this.raf);
    const fin = this.terminer; this.terminer = null;
    if (this.ctx && this.source && this.gain) {
      const t = this.ctx.currentTime;
      this.gain.gain.cancelScheduledValues(t);
      this.gain.gain.setValueAtTime(this.gain.gain.value, t);
      this.gain.gain.linearRampToValueAtTime(0, t + fondu);
      this.source.onended = null;
      this.source.stop(t + fondu + 0.005);
    }
    this.source = null;
    fin?.('interrompu');
  }

  get enLecture(): boolean { return this.source !== null; }

  /** Les quatre voix d'un énoncé, dans l'ordre du lecteur, 600 ms d'intervalle. */
  async quatre(id: string, prefere: Accent,
               donnees: (a: Accent, r: Rythme) => Pick<Lecture, 'mots' | 'syllabes'>,
               surChaque: (a: Accent, r: Rythme) => void): Promise<Issue> {
    const autre: Accent = prefere === 'uk' ? 'us' : 'uk';
    const ordre: [Accent, Rythme][] = [[prefere, 'pose'], [prefere, 'spontane'], [autre, 'pose'], [autre, 'spontane']];
    for (const [a, r] of ordre) {
      surChaque(a, r);
      const issue = await this.jouer({ id, accent: a, rythme: r, ...donnees(a, r) });
      if (issue === 'interrompu') return 'interrompu';
      if (issue === 'absent') continue;
      const gen = this.generation;
      await new Promise((ok) => setTimeout(ok, 600));
      if (gen !== this.generation) return 'interrompu';     // le lecteur a touché ailleurs pendant le silence
    }
    return 'fini';
  }

  /** L'écho (8.16) : passages successifs séparés d'un silence de 1,3 × la durée. */
  async echo(l: Lecture, passages: number, surSilence: (ms: number) => void): Promise<Issue> {
    for (let i = 0; i < passages; i++) {
      const tampon = await this.preparer(l.id, l.accent, l.rythme);
      if (!tampon) return 'absent';
      const issue = await this.jouer(l);
      if (issue !== 'fini') return issue;
      const ms = Math.round(tampon.duration * 1300);
      surSilence(ms);
      const gen = this.generation;
      await new Promise((ok) => setTimeout(ok, ms));
      if (gen !== this.generation) return 'interrompu';
    }
    return 'fini';
  }
}

export const moteur = new MoteurVoix();
