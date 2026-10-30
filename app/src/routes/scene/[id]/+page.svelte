<script lang="ts">
  // La scène (8.4) : Ouverture, Moments, Essentiel, Scène vivante, Rituel.
  import { t } from '$lib/textes/fr';
  import Entete from '$lib/ui/Entete.svelte';
  import Phrase from '$lib/ui/Phrase.svelte';
  import Icone from '$lib/ui/Icone.svelte';
  import { chargerScene, chargerSommaire, sceneDe, fragments } from '$lib/corpus/chargeur';
  import type { Scene, Enonce } from '$lib/corpus/types';
  import { preferences } from '$lib/preferences/magasin.svelte';
  import { moteur } from '$lib/voix/moteur';
  import { carnet } from '$lib/carnet/base';

  let { data } = $props();
  let scene = $state<Scene | null>(null);
  let numero = $state('');
  let charge = $state(false);
  let enCours = $state<string | null>(null);

  $effect(() => {
    const id = data.id;
    charge = false;
    void Promise.all([chargerScene(id), chargerSommaire().catch(() => null)]).then(([s, som]) => {
      scene = s;
      numero = som ? (sceneDe(som, id)?.scene.numero ?? '') : '';
      charge = true;
      if (s) void carnet.lecture.put({ cle: 'reprise', scene: id, moment: s.moments[0]?.lettre ?? 'A', expression: s.moments[0]?.expressions[0]?.id ?? '', date: Date.now() }).catch(() => undefined);
    });
  });

  const accent = $derived(preferences.valeur.accent);
  const rythme = $derived(preferences.valeur.rythme);

  async function ecouter(e: Enonce) {
    if (enCours === e.id) { moteur.arreter(); enCours = null; return; }
    enCours = e.id;
    await moteur.jouer({ id: e.id, accent, rythme });
    if (enCours === e.id) enCours = null;
  }
</script>

<Entete titre={numero ? t.livre.scene(numero) : t.livre.titre} retour />

<main class="page">
  {#if scene}
    <article>
      <h2 class="titre-scene">{scene.titre}</h2>
      <section aria-labelledby="ouverture">
        <h3 id="ouverture" class="surtitre">{t.scene.ouverture}</h3>
        <p>{#each fragments(scene.intention) as f, i (i)}{#if f.en}<span lang="en">{f.texte}</span>{:else}{f.texte}{/if}{/each}</p>
      </section>

      {#each scene.moments as m (m.lettre)}
        <section aria-labelledby="moment-{m.lettre}">
          <h3 id="moment-{m.lettre}" class="moment">{t.scene.moment(m.lettre, m.titre)}</h3>
          {#each m.expressions as x (x.id)}
            <div class="carte expression" id={x.id}>
              {#each x.enonces as e (e.id)}
                <button type="button" id="ecouter-{e.id}" class="enonce-bouton" aria-label={t.voix.ecouterAnnonce(accent === 'us' ? t.voix.americain : t.voix.britannique, rythme === 'pose' ? t.voix.pose : t.voix.spontane)} aria-pressed={enCours === e.id} onclick={() => ecouter(e)}>
                  <span class="enonce" lang="en">{e.texte[accent]}</span>
                  <Icone nom={enCours === e.id ? 'arret' : 'ecoute'} />
                </button>
                {#if enCours === e.id}<span class="ui en-ecoute" aria-live="polite">{t.voix.enEcoute}</span>{/if}
                <Phrase phrase={e.phrases[accent][rythme].phrase} />
              {/each}
              <p class="sens"><span class="visuellement-masque">{t.scene.sens}</span>{x.sens}</p>
              <p class="douce">{x.usage}</p>
            </div>
          {/each}
        </section>
      {/each}

      {#if scene.rituel.length}
        <section aria-labelledby="rituel">
          <h3 id="rituel" class="moment">{t.scene.rituel}</h3>
          <ol>{#each scene.rituel as r, i (i)}<li>{r}</li>{/each}</ol>
        </section>
      {/if}
      <p class="ui douce fin">{t.scene.finScene}</p>
    </article>
  {:else if charge}
    <p class="etat-vide">{t.lettres.vide}</p>
  {:else}
    <p class="etat-vide">{t.lettres.attente}</p>
  {/if}
</main>

<style>
  .titre-scene { font-family: var(--police-titre); font-size: 1.6rem; margin: var(--e6) 0; }
  .moment { font-family: var(--police-titre); font-size: 1.2rem; margin: var(--e8) 0 var(--e4); }
  .expression { display: flex; flex-direction: column; gap: var(--e2); }
  .enonce-bouton { display: flex; align-items: center; justify-content: space-between; gap: var(--e3); width: 100%; min-height: var(--cible); padding: 0; border: 0; background: none; color: var(--encre); text-align: left; cursor: pointer; font: inherit; }
  .enonce-bouton :global(svg) { color: var(--accent); flex: none; }
  .en-ecoute { color: var(--accent); font-size: 13px; }
  .sens { margin: var(--e2) 0 0; }
  .fin { margin-top: var(--e8); }
</style>
