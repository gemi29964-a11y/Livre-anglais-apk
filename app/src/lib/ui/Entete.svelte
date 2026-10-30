<script lang="ts">
  // En-tête des écrans principaux (8.1) : titre, loupe « Comment dit-on… ? », accès discret aux Préférences.
  import { t } from '$lib/textes/fr';
  import Icone from './Icone.svelte';
  import LigneEncre from './LigneEncre.svelte';

  let { titre, retour = false, attente = false }: { titre: string; retour?: boolean; attente?: boolean } = $props();
</script>

<svelte:head><title>{`${titre} · ${t.ouvrage.titre}`}</title></svelte:head>

<header class="entete-fixe">
  <div class="barre">
    {#if retour}
      <button class="icone" type="button" aria-label={t.navigation.retour} onclick={() => history.back()}>
        <Icone nom="retour" />
      </button>
    {/if}
    <h1 class="titre">{titre}</h1>
    <a class="icone" href="/recherche/" aria-label={t.navigation.recherche}><Icone nom="loupe" /></a>
    <a class="icone" href="/preferences/" aria-label={t.navigation.preferences}><Icone nom="diapason" /></a>
  </div>
  <LigneEncre active={attente} />
</header>

<style>
  header {
    position: sticky;
    top: 0;
    z-index: 10;
    background: var(--fond);
    padding-left: calc(var(--zone-gauche) + var(--marge));
    padding-right: calc(var(--zone-droite) + var(--marge) - var(--e3));
  }
  .barre {
    display: flex;
    align-items: center;
    gap: var(--e1);
    min-height: 56px;
  }
  .titre {
    flex: 1;
    margin: 0;
    font-family: var(--police-texte);
    font-size: 22px;
    font-weight: 600;
    line-height: 1.2;
    overflow-wrap: anywhere;
  }
  .icone {
    display: inline-grid;
    place-items: center;
    width: var(--cible);
    height: var(--cible);
    border: 0;
    border-radius: 50%;
    background: transparent;
    color: var(--encre);
    cursor: pointer;
  }
  .icone:active { background: var(--filet); }
</style>
