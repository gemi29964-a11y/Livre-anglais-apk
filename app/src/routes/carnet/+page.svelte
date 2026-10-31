<script lang="ts">
  // Mon carnet (8.8) : marque-pages, ma voix, expressions familières, ma version, constance.
  import { onMount } from 'svelte';
  import { t } from '$lib/textes/fr';
  import Entete from '$lib/ui/Entete.svelte';
  import Icone from '$lib/ui/Icone.svelte';
  import { carnet, constance, type Marque } from '$lib/carnet/base';
  import { lister } from '$lib/carnet/maVoix';

  let marquePages = $state<Marque[]>([]);
  let voix = $state(0);
  let versions = $state(0);
  let jours = $state(0);

  onMount(async () => {
    marquePages = await carnet.marques.orderBy('date').reverse().toArray().catch(() => []);
    voix = (await lister()).length;
    versions = await carnet.versions.count().catch(() => 0);
    jours = constance((await carnet.constance.toArray().catch(() => [])).map((p) => p.jour));
  });
</script>

<Entete titre={t.carnet.titre} />

<main class="page">
  <section class="carte">
    <h2>{t.carnet.constance}</h2>
    <p>{t.aujourdhui.constance(jours)}</p>
    <p class="douce">{t.carnet.jourDeGrace}</p>
  </section>

  <section>
    <h2 class="surtitre">{t.carnet.marquePages}</h2>
    {#if marquePages.length}
      {#each marquePages as m (m.id)}
        <a class="carte" href="/scene/{m.scene}/#{m.id}">{m.id}</a>
      {/each}
    {:else}
      <div class="etat-vide"><Icone nom="marque-page" taille={40} /><p>{t.carnet.videMarquePages}</p></div>
    {/if}
  </section>

  <section>
    <h2 class="surtitre">{t.carnet.maVoix}</h2>
    {#if !voix}<div class="etat-vide"><Icone nom="micro" taille={40} /><p>{t.carnet.videMaVoix}</p></div>{/if}
  </section>

  <section>
    <h2 class="surtitre">{t.carnet.familieres}</h2>
    <div class="etat-vide"><Icone nom="cle" taille={40} /><p>{t.carnet.videFamilieres}</p></div>
  </section>

  <section>
    <h2 class="surtitre">{t.carnet.maVersion}</h2>
    {#if !versions}<div class="etat-vide"><Icone nom="plume" taille={40} /><p>{t.carnet.videMaVersion}</p></div>{/if}
  </section>
</main>

<style>
  section { margin-top: var(--e6); }
  h2 { margin: 0 0 var(--e3); }
</style>
