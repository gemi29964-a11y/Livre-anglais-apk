<script lang="ts" module>
  // Jeu d'icônes dessiné sur mesure (9.6) : trait de 1,75 px à 24 px, coins arrondis,
  // inspiré de l'outillage du livre et du son. SVG en ligne, aucune bibliothèque générique.
  export type NomIcone =
    | 'soleil' | 'livre' | 'casque' | 'carnet' | 'marque-page' | 'marque-page-plein' | 'loupe' | 'plume'
    | 'onde' | 'nuage' | 'ecoute' | 'arret' | 'diapason' | 'retour' | 'fermer' | 'suivant' | 'precedent'
    | 'pause' | 'lecture' | 'micro' | 'boussole' | 'cle';
</script>

<script lang="ts">
  let { nom, taille = 24 }: { nom: NomIcone; taille?: number } = $props();
</script>

<svg
  width={taille}
  height={taille}
  viewBox="0 0 24 24"
  fill="none"
  stroke="currentColor"
  stroke-width="1.75"
  stroke-linecap="round"
  stroke-linejoin="round"
  aria-hidden="true"
  focusable="false"
>
  {#if nom === 'soleil'}
    <path d="M3 18.5h18" />
    <path d="M6.5 18.5a5.5 5.5 0 0 1 11 0" />
    <path d="M12 6.5v2.2M5.2 9.6l1.6 1.4M18.8 9.6l-1.6 1.4M2.8 14.4h2M19.2 14.4h2" />
    <path d="M8 21.2h8" />
  {:else if nom === 'livre'}
    <path d="M12 6.8c-2-1.6-4.9-2.1-8.3-1.5v12.6c3.4-.6 6.3-.1 8.3 1.5 2-1.6 4.9-2.1 8.3-1.5V5.3c-3.4-.6-6.3-.1-8.3 1.5Z" />
    <path d="M12 6.8v12.6" />
    <path d="M6.3 9.2c1.3-.1 2.5.1 3.4.6M14.3 9.8c.9-.5 2.1-.7 3.4-.6" />
  {:else if nom === 'casque'}
    <path d="M4.2 15.5v-3.2a7.8 7.8 0 0 1 15.6 0v3.2" />
    <rect x="3.2" y="14" width="4.2" height="6.2" rx="1.6" />
    <rect x="16.6" y="14" width="4.2" height="6.2" rx="1.6" />
  {:else if nom === 'carnet'}
    <rect x="5" y="3.2" width="13.6" height="17.6" rx="2" />
    <path d="M8.6 3.2v17.6" />
    <path d="M15.6 3.2v17.6" stroke-dasharray="0" />
    <path d="M11.2 8.2h2.4M11.2 11.2h2.4" />
  {:else if nom === 'marque-page'}
    <path d="M7 3.5h10a1 1 0 0 1 1 1v16l-6-4-6 4v-16a1 1 0 0 1 1-1Z" />
  {:else if nom === 'marque-page-plein'}
    <path d="M7 3.5h10a1 1 0 0 1 1 1v16l-6-4-6 4v-16a1 1 0 0 1 1-1Z" fill="currentColor" />
  {:else if nom === 'loupe'}
    <circle cx="10.5" cy="10.5" r="6" />
    <path d="M15 15l5.2 5.2" />
    <path d="M8 9.2a2.8 2.8 0 0 1 2.4-1.6" />
  {:else if nom === 'plume'}
    <path d="M19.5 4.5c-6.2.4-10.6 4.6-12 11.3L5 20" />
    <path d="M19.5 4.5c.3 6.5-4.4 10.9-11 11.4" />
    <path d="M11 13l3.6-3.6" />
  {:else if nom === 'onde'}
    <path d="M3 12h1.6M6.6 9v6M10 6v12M13.4 8.4v7.2M16.8 10.2v3.6M20.2 12H21" />
  {:else if nom === 'nuage'}
    <path d="M7.5 18.5h9.3a3.7 3.7 0 0 0 .4-7.4 5.2 5.2 0 0 0-10-.9 3.9 3.9 0 0 0 .3 8.3Z" />
    <path d="M12 11.6v4.4M10.2 14.4 12 16.2l1.8-1.8" />
  {:else if nom === 'ecoute'}
    <circle cx="12" cy="12" r="8.6" />
    <path d="M10.2 8.6v6.8l5.4-3.4-5.4-3.4Z" />
  {:else if nom === 'arret'}
    <circle cx="12" cy="12" r="8.6" />
    <rect x="9.2" y="9.2" width="5.6" height="5.6" rx="1" />
  {:else if nom === 'diapason'}
    <path d="M9 3.5v6.5a3 3 0 0 0 6 0V3.5" />
    <path d="M12 13v7.5" />
    <path d="M10.2 20.5h3.6" />
  {:else if nom === 'retour'}
    <path d="M14.5 5.5 8 12l6.5 6.5" />
  {:else if nom === 'fermer'}
    <path d="M6.5 6.5l11 11M17.5 6.5l-11 11" />
  {:else if nom === 'suivant'}
    <path d="M6 6.5v11l8-5.5-8-5.5Z" />
    <path d="M18 6.5v11" />
  {:else if nom === 'precedent'}
    <path d="M18 6.5v11l-8-5.5 8-5.5Z" />
    <path d="M6 6.5v11" />
  {:else if nom === 'pause'}
    <path d="M9 6.5v11M15 6.5v11" />
  {:else if nom === 'lecture'}
    <path d="M8 5.5v13l10.5-6.5L8 5.5Z" />
  {:else if nom === 'micro'}
    <rect x="9" y="3.5" width="6" height="10.5" rx="3" />
    <path d="M5.8 11.5a6.2 6.2 0 0 0 12.4 0M12 17.7v2.8" />
  {:else if nom === 'boussole'}
    <circle cx="12" cy="12" r="8.6" />
    <path d="m15.3 8.7-2 4.6-4.6 2 2-4.6 4.6-2Z" />
  {:else if nom === 'cle'}
    <circle cx="8" cy="12" r="3.6" />
    <path d="M11.6 12h8.6M17.4 12v3M20.2 12v2" />
  {/if}
</svg>
