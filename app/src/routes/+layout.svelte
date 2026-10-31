<script lang="ts">
  import '../app.css';
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';
  import { page } from '$app/state';
  import { Capacitor } from '@capacitor/core';
  import NavigationBasse from '$lib/ui/NavigationBasse.svelte';
  import Accueil from '$lib/ui/Accueil.svelte';
  import { preferences } from '$lib/preferences/magasin.svelte';
  import { appliquer } from '$lib/ui/apparence';
  import { installerRetour } from '$lib/liens/retour';
  import { chargerSommaire } from '$lib/corpus/chargeur';
  import { ecouterLiens } from '$lib/liens/liens';

  let { children } = $props();

  onMount(() => {
    void preferences.ouvrir().then(async () => {
      if (Capacitor.isNativePlatform()) {
        const { SplashScreen } = await import('@capacitor/splash-screen');
        await SplashScreen.hide({ fadeOutDuration: 220 });
      }
    });
    installerRetour(() => page.url.pathname, () => void goto('/'));
    void ecouterLiens(() => chargerSommaire().catch(() => null), (c) => void goto(c));
    const systeme = window.matchMedia('(prefers-color-scheme: dark)');
    const suivre = () => appliquer(preferences.valeur);
    systeme.addEventListener('change', suivre);
    return () => systeme.removeEventListener('change', suivre);
  });

  $effect(() => {
    appliquer(preferences.valeur);
  });

  // Puis ouverture directe du Prélude (nouveau lecteur) ou du Chapitre 1 (lecteur « à l'aise ») : 8.11.
  async function accueilFini(niveau: string) {
    const chapitre = niveau === 'maitrise' ? 'c01' : 'c00';
    const s = await chargerSommaire().catch(() => null);
    const premiere = s?.chapitres.find((c) => c.id === chapitre)?.scenes.find((x) => x.disponible);
    void goto(premiere ? `/scene/${premiere.id}/` : `/livre/${chapitre}/`);
  }
</script>

{#if preferences.pret && !preferences.valeur.accueilFait}
  <Accueil fini={accueilFini} />
{:else}
  {@render children()}
  <NavigationBasse />
{/if}
