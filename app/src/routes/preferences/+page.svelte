<script lang="ts">
  // Les Préférences (8.10) : neuf groupes, chaque réglage enregistré aussitôt dans le stockage privé.
  import { t } from '$lib/textes/fr';
  import { en } from '$lib/textes/en';
  import Entete from '$lib/ui/Entete.svelte';
  import Bascule from '$lib/ui/Bascule.svelte';
  import { preferences } from '$lib/preferences/magasin.svelte';
  import { TAILLES, type Forme, type Preferences } from '$lib/preferences/modele';
  import { carnet } from '$lib/carnet/base';
  import type { Accent, Niveau, Rythme } from '$lib/corpus/types';

  const p = $derived(preferences.valeur);
  const changer = (m: Partial<Preferences>) => void preferences.changer(m);

  const ouiNon = [{ valeur: 'oui' as const, libelle: t.preferences.oui }, { valeur: 'non' as const, libelle: t.preferences.non }];
  const yn = (b: boolean) => (b ? 'oui' : 'non') as 'oui' | 'non';
  const accents = [{ valeur: 'us' as Accent, libelle: t.voix.americain }, { valeur: 'uk' as Accent, libelle: t.voix.britannique }];
  const rythmes = [{ valeur: 'pose' as Rythme, libelle: t.voix.pose }, { valeur: 'spontane' as Rythme, libelle: t.voix.spontane }];
  const formes = Object.entries(t.preferences.formes) as [Forme, string][];

  let confirmation = $state(0);
  let annonce = $state('');

  async function toutEffacer() {
    if (confirmation < 2) { confirmation += 1; return; }
    await Promise.all(carnet.tables.map((tb) => tb.clear()));
    confirmation = 0;
    annonce = t.preferences.carnetEfface;
  }

  async function effacerVoix() {
    await carnet.maVoix.clear();
    annonce = t.preferences.voixEffacees;
  }

  function basculerForme(f: Forme) {
    const s = new Set(p.formesEcartees);
    if (s.has(f)) s.delete(f); else s.add(f);
    changer({ formesEcartees: [...s] });
  }

  function basculerJour(j: number) {
    const s = new Set(p.rendezVous.jours);
    if (s.has(j)) s.delete(j); else s.add(j);
    changer({ rendezVous: { ...p.rendezVous, jours: [...s].sort() } });
  }

  const heureTexte = $derived(`${String(p.rendezVous.heure).padStart(2, '0')}:${String(p.rendezVous.minute).padStart(2, '0')}`);
</script>

<Entete titre={t.preferences.titre} retour />

<main class="page">
  <p class="visuellement-masque" aria-live="polite">{annonce}</p>

  <section class="carte">
    <h2>{t.preferences.groupes.voix}</h2>
    <Bascule libelle={t.preferences.accentPrefere} options={accents} valeur={p.accent} onchange={(v) => changer({ accent: v })} />
    <Bascule libelle={t.preferences.rythmeEntree} options={rythmes} valeur={p.rythme} onchange={(v) => changer({ rythme: v })} />
    <Bascule libelle={t.preferences.ordreQuatre} options={[{ valeur: 'prefere', libelle: t.preferences.ordrePrefereDabord }, { valeur: 'alterne', libelle: t.preferences.ordreAlterne }]} valeur={p.ordreQuatre} onchange={(v) => changer({ ordreQuatre: v })} />
    <Bascule libelle={t.preferences.voixDuSens} options={ouiNon} valeur={yn(p.voixDuSens)} onchange={(v) => changer({ voixDuSens: v === 'oui' })} />
    <Bascule libelle={t.promenade.silences} options={[{ valeur: 'court', libelle: t.promenade.silence.court }, { valeur: 'normal', libelle: t.promenade.silence.normal }, { valeur: 'long', libelle: t.promenade.silence.long }]} valeur={p.silences} onchange={(v) => changer({ silences: v })} />
    <label class="reglage">
      <span>{t.preferences.passagesEcho}</span>
      <input type="range" min="2" max="5" step="1" value={p.passagesEcho} aria-valuetext={String(p.passagesEcho)} oninput={(e) => changer({ passagesEcho: +e.currentTarget.value })} />
      <output>{p.passagesEcho}</output>
    </label>
  </section>

  <section class="carte">
    <h2>{t.preferences.groupes.lecture}</h2>
    <label class="reglage">
      <span>{t.preferences.tailleTexte}</span>
      <input type="range" min="0" max={TAILLES.length - 1} step="1" value={p.tailleCran} aria-valuetext={t.preferences.crans(p.tailleCran + 1, TAILLES.length)} oninput={(e) => changer({ tailleCran: +e.currentTarget.value })} />
      <output>{TAILLES[p.tailleCran]}</output>
    </label>
    <p class="apercu"><span class="enonce" lang="en">{en.apercu}</span><span class="douce">{t.preferences.apercuSens}</span></p>
    <Bascule libelle={t.preferences.interligne} options={[{ valeur: '0', libelle: t.preferences.interlignes.serre }, { valeur: '1', libelle: t.preferences.interlignes.normal }, { valeur: '2', libelle: t.preferences.interlignes.aere }]} valeur={String(p.interligneCran) as '0' | '1' | '2'} onchange={(v) => changer({ interligneCran: +v })} />
    <Bascule libelle={t.preferences.theme} options={(['papier', 'ambre', 'nuit', 'contraste', 'automatique'] as const).map((v) => ({ valeur: v, libelle: t.preferences.themes[v] }))} valeur={p.theme} onchange={(v) => changer({ theme: v })} />
    <Bascule libelle={t.preferences.aideLecture} options={ouiNon} valeur={yn(p.aideLecture)} onchange={(v) => changer({ aideLecture: v === 'oui' })} />
    <Bascule libelle={t.preferences.expertParDefaut} options={ouiNon} valeur={yn(p.expertParDefaut)} onchange={(v) => changer({ expertParDefaut: v === 'oui' })} />
    <Bascule libelle={t.preferences.courbe} options={ouiNon} valeur={yn(p.courbe)} onchange={(v) => changer({ courbe: v === 'oui' })} />
    <Bascule libelle={t.preferences.tonCru} options={ouiNon} valeur={yn(p.tonCru)} onchange={(v) => changer({ tonCru: v === 'oui' })} />
    <Bascule libelle={t.preferences.battement} options={ouiNon} valeur={yn(p.battement)} onchange={(v) => changer({ battement: v === 'oui' })} />
    <Bascule libelle={t.preferences.retourHaptique} options={ouiNon} valeur={yn(p.haptique)} onchange={(v) => changer({ haptique: v === 'oui' })} />
  </section>

  <section class="carte">
    <h2>{t.preferences.groupes.parcours}</h2>
    <Bascule libelle={t.preferences.niveauDepart} options={(['fondations', 'aisance', 'maitrise'] as Niveau[]).map((v) => ({ valeur: v, libelle: t.etiquettes.niveau[v] }))} valeur={p.niveau} onchange={(v) => changer({ niveau: v })} />
    <label class="reglage">
      <span>{t.preferences.nouvellesParJour}</span>
      <input type="range" min="5" max="50" step="5" value={p.nouvellesParJour} oninput={(e) => changer({ nouvellesParJour: +e.currentTarget.value })} />
      <output>{p.nouvellesParJour}</output>
    </label>
    <label class="reglage">
      <span>{t.preferences.retrouvaillesMax}</span>
      <input type="range" min="20" max="400" step="10" value={p.retrouvaillesMax} oninput={(e) => changer({ retrouvaillesMax: +e.currentTarget.value })} />
      <output>{p.retrouvaillesMax}</output>
    </label>
    <label class="reglage">
      <span>{t.preferences.memorisation}</span>
      <input type="range" min="80" max="95" step="1" value={p.retention} aria-valuetext={t.preferences.pourcentage(p.retention)} oninput={(e) => changer({ retention: +e.currentTarget.value })} />
      <output>{t.preferences.pourcentage(p.retention)}</output>
    </label>
    <fieldset>
      <legend>{t.preferences.formesEcartees}</legend>
      {#each formes as [f, nom] (f)}
        <label class="case"><input type="checkbox" checked={p.formesEcartees.includes(f)} onchange={() => basculerForme(f)} /><span>{nom}</span></label>
      {/each}
    </fieldset>
    <Bascule libelle={t.preferences.retrouvaillesSilencieuses} options={ouiNon} valeur={yn(p.silencieuses)} onchange={(v) => changer({ silencieuses: v === 'oui' })} />
    <Bascule libelle={t.preferences.momentPresent} options={ouiNon} valeur={yn(p.momentPresent)} onchange={(v) => changer({ momentPresent: v === 'oui' })} />
  </section>

  <section class="carte">
    <h2>{t.preferences.groupes.rendezVous}</h2>
    <Bascule libelle={t.preferences.rendezVousActif} options={[{ valeur: 'oui', libelle: t.preferences.actif }, { valeur: 'non', libelle: t.preferences.inactif }]} valeur={yn(p.rendezVous.actif)} onchange={(v) => changer({ rendezVous: { ...p.rendezVous, actif: v === 'oui' } })} />
    <label class="reglage">
      <span>{t.preferences.heureRendezVous}</span>
      <input type="time" value={heureTexte} onchange={(e) => { const [h, m] = e.currentTarget.value.split(':').map(Number); changer({ rendezVous: { ...p.rendezVous, heure: h, minute: m } }); }} />
    </label>
    <fieldset>
      <legend>{t.preferences.jours}</legend>
      {#each t.preferences.joursSemaine as j, i (j)}
        <label class="case"><input type="checkbox" checked={p.rendezVous.jours.includes(i)} onchange={() => basculerJour(i)} /><span>{j}</span></label>
      {/each}
    </fieldset>
  </section>

  <section class="carte">
    <h2>{t.preferences.groupes.miroir}</h2>
    <button type="button" class="action discrete" onclick={effacerVoix}>{t.preferences.effacerVoix}</button>
  </section>

  <section class="carte">
    <h2>{t.preferences.groupes.carnet}</h2>
    {#if confirmation === 1}<p>{t.preferences.confirmerEffacer}</p>{:else if confirmation === 2}<p>{t.preferences.confirmerEncore}</p>{/if}
    <button type="button" class="action discrete" onclick={toutEffacer}>{t.preferences.toutEffacer}</button>
  </section>

  <section class="carte">
    <h2>{t.preferences.groupes.ecranAccueil}</h2>
    <Bascule libelle={t.preferences.ecranAccueilAccent} options={accents} valeur={p.ecranAccueil.accent} onchange={(v) => changer({ ecranAccueil: { ...p.ecranAccueil, accent: v } })} />
    <Bascule libelle={t.preferences.ecranAccueilRythme} options={rythmes} valeur={p.ecranAccueil.rythme} onchange={(v) => changer({ ecranAccueil: { ...p.ecranAccueil, rythme: v } })} />
    <Bascule libelle={t.preferences.ecranAccueilOrigine} options={[{ valeur: 'parcourues', libelle: t.preferences.origines.parcourues }, { valeur: 'ouvrage', libelle: t.preferences.origines.ouvrage }]} valeur={p.ecranAccueil.origine} onchange={(v) => changer({ ecranAccueil: { ...p.ecranAccueil, origine: v } })} />
  </section>

  <a class="carte lien" href="/lire-ce-livre/"><h2>{t.preferences.groupes.lireCeLivre}</h2><p class="douce">{t.lireCeLivre.intro}</p></a>

  <section class="carte">
    <h2>{t.preferences.groupes.aPropos}</h2>
    <p>{t.ouvrage.titre} — {t.ouvrage.sousTitre}</p>
    <p class="douce">{t.ouvrage.edition(__EDITION__)}</p>
    <h3>{t.aPropos.confidentialite}</h3>
    {#each t.aPropos.textesConfidentialite as x (x)}<p>{x}</p>{/each}
    <h3>{t.aPropos.mentions}</h3>
    {#each t.aPropos.textesMentions as x (x)}<p>{x}</p>{/each}
  </section>
</main>

<style>
  .carte { display: flex; flex-direction: column; gap: var(--e4); }
  .carte h2 { font-family: var(--police-titre); font-size: 1.2rem; }
  .carte h3 { font-family: var(--police-ui); font-size: 15px; margin: var(--e2) 0 0; }
  .reglage { display: grid; grid-template-columns: 1fr auto; gap: var(--e2) var(--e3); align-items: center; font-family: var(--police-ui); }
  .reglage > span { grid-column: 1 / -1; }
  .reglage input[type='range'] { width: 100%; min-height: var(--cible); accent-color: var(--accent); }
  .reglage input[type='time'] { grid-column: 1 / -1; min-height: var(--cible); font: inherit; padding: 0 var(--e3); border: var(--epaisseur-filet) solid var(--filet); border-radius: var(--rond); background: var(--surface); color: var(--encre); }
  output { min-width: 3ch; text-align: right; font-variant-numeric: tabular-nums; }
  fieldset { border: 0; padding: 0; margin: 0; display: grid; gap: var(--e1); font-family: var(--police-ui); }
  legend { margin-bottom: var(--e2); }
  .case { display: flex; align-items: center; gap: var(--e3); min-height: var(--cible); }
  .case input { width: 22px; height: 22px; accent-color: var(--accent); }
  .apercu { display: flex; flex-direction: column; gap: var(--e1); margin: 0; }
  .lien { color: var(--encre); }
</style>
