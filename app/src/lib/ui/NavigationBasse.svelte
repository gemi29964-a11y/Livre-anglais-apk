<script lang="ts">
  // Carte de l'ouvrage (8.1) : quatre destinations au pouce ; rail latéral à partir de 600 dp.
  import { page } from '$app/state';
  import { t } from '$lib/textes/fr';
  import Icone, { type NomIcone } from './Icone.svelte';

  const destinations: { href: string; libelle: string; icone: NomIcone }[] = [
    { href: '/', libelle: t.navigation.aujourdhui, icone: 'soleil' },
    { href: '/livre/', libelle: t.navigation.livre, icone: 'livre' },
    { href: '/promenade/', libelle: t.navigation.promenade, icone: 'casque' },
    { href: '/carnet/', libelle: t.navigation.carnet, icone: 'carnet' }
  ];

  const actif = (href: string) =>
    href === '/' ? page.url.pathname === '/' : page.url.pathname.startsWith(href) ||
      (href === '/livre/' && (page.url.pathname.startsWith('/scene/') || page.url.pathname.startsWith('/itineraire/')));
</script>

<nav class="navigation-basse ui" aria-label={t.navigation.principale}>
  <ul>
    {#each destinations as d (d.href)}
      <li>
        <a href={d.href} aria-current={actif(d.href) ? 'page' : undefined} data-sveltekit-noscroll={false}>
          <Icone nom={d.icone} />
          <span>{d.libelle}</span>
        </a>
      </li>
    {/each}
  </ul>
</nav>

<style>
  nav {
    position: fixed;
    inset: auto 0 0 0;
    z-index: 20;
    background: var(--surface);
    border-top: var(--epaisseur-filet) solid var(--filet);
    padding-left: var(--zone-gauche);
    padding-right: var(--zone-droite);
  }
  ul {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: var(--ecart-cibles);
    margin: 0;
    padding: var(--e1) var(--e2) 0;
    list-style: none;
  }
  a {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 2px;
    min-height: var(--hauteur-barre);
    min-width: var(--cible);
    border-radius: var(--rond);
    color: var(--encre-douce);
    text-decoration: none;
    font-size: 12.5px;
    transition: color var(--duree-micro) var(--courbe-entree);
  }
  a[aria-current='page'] {
    color: var(--accent);
    font-weight: 600;
  }
  a[aria-current='page'] :global(svg) {
    stroke-width: 2.1;
  }
  @media (min-width: 600px) {
    nav {
      inset: 0 auto 0 0;
      width: 96px;
      border-top: 0;
      border-right: var(--epaisseur-filet) solid var(--filet);
      padding-top: calc(var(--zone-haut) + var(--e6));
      padding-bottom: var(--zone-bas);
    }
    ul {
      grid-template-columns: 1fr;
      padding: 0 var(--e2);
    }
    a { min-height: 72px; }
  }
</style>
