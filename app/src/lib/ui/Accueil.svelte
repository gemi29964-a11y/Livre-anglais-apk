<script lang="ts">
  // L'accueil du premier lancement (8.11) : quatre écrans, moins de 60 secondes, tous passables.
  import { t } from '$lib/textes/fr';
  import { en } from '$lib/textes/en';
  import { preferences } from '$lib/preferences/magasin.svelte';
  import { selonNiveau } from '$lib/preferences/modele';
  import type { Accent, Niveau } from '$lib/corpus/types';
  import { moteur } from '$lib/voix/moteur';
  import Icone from './Icone.svelte';

  let { fini }: { fini: (niveau: Niveau) => void } = $props();
  let ecran = $state(1);
  let accent = $state<Accent>(preferences.valeur.accent);
  let niveau = $state<Niveau>('fondations');
  let heure = $state('07:30');

  const DEMONSTRATION = 'c01.s01.A1.e1';           // My alarm's going off. (Scène 1.1, Moment A)
  const ACCUEIL_ACCENT = 'c01.s01.A2.e1';          // phrase d'accueil jouée dans chaque accent

  async function quatreVoix() {
    await moteur.quatre(DEMONSTRATION, accent, () => ({}), () => undefined);
  }

  async function choisirAccent(a: Accent) {
    accent = a;
    await preferences.changer({ accent: a, ecranAccueil: { ...preferences.valeur.ecranAccueil, accent: a } });
    void moteur.jouer({ id: ACCUEIL_ACCENT, accent: a, rythme: 'pose' });
  }

  async function choisirNiveau(n: Niveau) {
    niveau = n;
    await preferences.changer(selonNiveau($state.snapshot(preferences.valeur), n));
    ecran = 4;
  }

  async function terminer(avecRendezVous: boolean) {
    moteur.arreter();
    if (avecRendezVous) {
      const [h, m] = heure.split(':').map(Number);
      await preferences.changer({ rendezVous: { ...preferences.valeur.rendezVous, actif: true, heure: h, minute: m } });
      try {
        const { LocalNotifications } = await import('@capacitor/local-notifications');
        await LocalNotifications.requestPermissions();
      } catch { /* la permission reste à demander depuis les Préférences */ }
    }
    await preferences.changer({ accueilFait: true });
    fini(niveau);
  }
</script>

<svelte:head><title>{t.ouvrage.titre}</title></svelte:head>

<section class="accueil" aria-label={t.accueil.ecran(ecran)}>
  <div class="haut">
    <span class="ui pagination" aria-hidden="true">{ecran} / 4</span>
    <button type="button" class="lien ui" onclick={() => terminer(false)}>{t.accueil.passer}</button>
  </div>

  {#if ecran === 1}
    <div class="corps">
      <p class="grand-titre">{t.ouvrage.titre}</p>
      <p class="phrase-accueil">{t.accueil.bienvenue}</p>
      <button type="button" class="ecoute" onclick={quatreVoix}>
        <Icone nom="ecoute" taille={32} />
        <span><span class="enonce" lang="en">{en.accueilQuatreVoix}</span><span class="ui sous">{t.accueil.demonstration}</span></span>
      </button>
    </div>
    <button type="button" class="principal ui" onclick={() => (ecran = 2)}>{t.accueil.commencer}</button>
  {:else if ecran === 2}
    <div class="corps">
      <p class="phrase-accueil">{t.accueil.choixAccent}</p>
      <div class="cartes">
        {#each [{ a: 'us' as Accent, nom: t.voix.americain }, { a: 'uk' as Accent, nom: t.voix.britannique }] as c (c.a)}
          <button type="button" class="carte-accent" class:choisie={accent === c.a} aria-pressed={accent === c.a} onclick={() => choisirAccent(c.a)} style:--teinte={c.a === 'us' ? 'var(--voix-am)' : 'var(--voix-brit)'}>
            <span class="nom">{c.nom}</span>
            <span class="enonce" lang="en">{en.accueilAccent}</span>
            <Icone nom="ecoute" taille={28} />
          </button>
        {/each}
      </div>
    </div>
    <button type="button" class="principal ui" onclick={() => (ecran = 3)}>{t.accueil.continuer}</button>
  {:else if ecran === 3}
    <div class="corps">
      <p class="phrase-accueil">{t.accueil.niveau}</p>
      <div class="choix">
        {#each (['fondations', 'aisance', 'maitrise'] as Niveau[]) as n (n)}
          <button type="button" class="choix-niveau ui" onclick={() => choisirNiveau(n)}>{t.accueil.niveaux[n]}</button>
        {/each}
      </div>
    </div>
  {:else}
    <div class="corps">
      <p class="phrase-accueil">{t.accueil.rendezVous}</p>
      <label class="ui heure">
        <span>{t.accueil.rendezVousHeure}</span>
        <input type="time" bind:value={heure} />
      </label>
    </div>
    <div class="pied">
      <button type="button" class="secondaire ui" onclick={() => terminer(false)}>{t.accueil.pasMaintenant}</button>
      <button type="button" class="principal ui" onclick={() => terminer(true)}>{t.accueil.cestFait}</button>
    </div>
  {/if}
</section>

<style>
  .accueil {
    position: fixed;
    inset: 0;
    z-index: 50;
    display: flex;
    flex-direction: column;
    background: var(--fond);
    padding: calc(var(--zone-haut) + var(--e4)) calc(var(--zone-droite) + var(--marge)) calc(var(--zone-bas) + var(--e6)) calc(var(--zone-gauche) + var(--marge));
    animation: entree var(--duree-ecran) var(--courbe-entree);
  }
  .haut { display: flex; justify-content: space-between; align-items: center; min-height: var(--cible); }
  .pagination { color: var(--encre-douce); }
  .corps { flex: 1; display: flex; flex-direction: column; justify-content: center; gap: var(--e6); max-width: var(--colonne); margin: 0 auto; width: 100%; }
  .phrase-accueil { font-size: calc(var(--base) * 1.25); line-height: 1.45; margin: 0; }
  .ecoute, .carte-accent, .choix-niveau {
    display: flex; align-items: center; gap: var(--e4); width: 100%; min-height: 64px;
    padding: var(--e4); border: var(--epaisseur-filet) solid var(--filet); border-radius: var(--rond);
    background: var(--surface); color: var(--encre); text-align: left; font: inherit; cursor: pointer;
  }
  .ecoute { color: var(--accent); }
  .ecoute > span { display: flex; flex-direction: column; color: var(--encre); }
  .sous { color: var(--encre-douce); }
  .cartes { display: grid; gap: var(--e4); }
  .carte-accent { flex-direction: column; align-items: flex-start; border-left: 4px solid var(--teinte); }
  .carte-accent .nom { font-family: var(--police-ui); font-weight: 600; color: var(--teinte); }
  .carte-accent :global(svg) { color: var(--teinte); }
  .carte-accent.choisie { outline: 2px solid var(--teinte); }
  .choix { display: grid; gap: var(--e3); }
  .heure { display: flex; flex-direction: column; gap: var(--e2); }
  .heure input { min-height: var(--cible); font: inherit; font-size: 20px; padding: 0 var(--e3); border: var(--epaisseur-filet) solid var(--filet); border-radius: var(--rond); background: var(--surface); color: var(--encre); }
  .pied { display: flex; gap: var(--e3); }
  .principal, .secondaire { flex: 1; min-height: 52px; border-radius: var(--rond-pilule); font: inherit; font-weight: 600; cursor: pointer; }
  .principal { border: 0; background: var(--accent); color: var(--surface); }
  .secondaire { border: var(--epaisseur-filet) solid var(--filet); background: transparent; color: var(--encre); }
  .lien { min-height: var(--cible); border: 0; background: none; color: var(--accent); font: inherit; cursor: pointer; }
  @keyframes entree { from { opacity: 0; transform: translateY(var(--glissement)); } }
</style>
