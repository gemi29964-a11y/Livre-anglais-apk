<script lang="ts">
  // Aujourd'hui (8.2) : une salutation et des cartes qui n'apparaissent que si elles ont un objet.
  import { onMount } from 'svelte';
  import { t } from '$lib/textes/fr';
  import Entete from '$lib/ui/Entete.svelte';
  import Icone from '$lib/ui/Icone.svelte';
  import { chargerSommaire, sceneDe, type Sommaire } from '$lib/corpus/chargeur';
  import { carnet, constance } from '$lib/carnet/base';
  import { preferences } from '$lib/preferences/magasin.svelte';

  interface Moment { debut: string; fin: string; scene: string }
  interface ExpressionJour { id: string; scene: string; texte: Record<'us' | 'uk', string>; sens: string }

  let sommaire = $state<Sommaire | null>(null);
  let jours = $state(0);
  let reprise = $state<{ scene: string; numero: string; titre: string } | null>(null);
  let moments = $state<Moment[]>([]);
  let expressions = $state<ExpressionJour[]>([]);
  let maintenant = $state(new Date());

  onMount(() => {
    void (async () => {
      sommaire = await chargerSommaire().catch(() => null);
      const pratique = await carnet.pratique.toArray().catch(() => []);
      jours = constance(pratique.map((p) => p.jour));
      const l = await carnet.lecture.get('reprise').catch(() => undefined);
      if (l && sommaire) {
        const trouve = sceneDe(sommaire, l.scene);
        if (trouve?.scene.disponible) reprise = { scene: l.scene, numero: trouve.scene.numero, titre: trouve.scene.titre };
      }
      moments = await fetch('/corpus/moments.json').then((r) => (r.ok ? r.json() : [])).catch(() => []);
      expressions = await fetch('/corpus/expression-du-jour.json').then((r) => (r.ok ? r.json() : [])).catch(() => []);
    })();
    const minuterie = setInterval(() => (maintenant = new Date()), 60_000);
    return () => clearInterval(minuterie);
  });

  const minutesDuJour = $derived(maintenant.getHours() * 60 + maintenant.getMinutes());
  const enMinutes = (h: string) => { const [a, b] = h.split(':').map(Number); return a * 60 + b; };

  const momentPresent = $derived.by(() => {
    if (!preferences.valeur.momentPresent || !sommaire) return null;
    for (const m of Array.isArray(moments) ? moments : []) {
      const d = enMinutes(m.debut), f = enMinutes(m.fin);
      const dedans = d <= f ? minutesDuJour >= d && minutesDuJour < f : minutesDuJour >= d || minutesDuJour < f;
      const trouve = dedans ? sceneDe(sommaire, m.scene) : undefined;
      if (trouve?.scene.disponible) return { ...trouve.scene };
    }
    return null;
  });

  const expressionDuJour = $derived.by(() => {
    if (!expressions.length) return null;
    const jour = Math.floor((maintenant.getTime() - 4 * 3600_000) / 86_400_000);
    return expressions[jour % expressions.length];
  });

  const prelude = $derived(sommaire?.chapitres.find((c) => c.numero === 0)?.scenes.find((s) => s.disponible) ?? null);
  const premiere = $derived(sommaire?.chapitres.find((c) => c.numero === 1)?.scenes.find((s) => s.disponible) ?? null);
</script>

<Entete titre={t.navigation.aujourdhui} />

<main class="page">
  <p class="salutation">{t.aujourdhui.salutation(maintenant.getHours())}</p>

  {#if jours > 0}
    <p class="ui douce constance">{t.aujourdhui.constance(jours)}</p>
  {/if}

  {#if reprise}
    <a class="carte" href="/scene/{reprise.scene}/">
      <p class="surtitre">{t.aujourdhui.reprendre}</p>
      <p>{t.aujourdhui.reprise(reprise.numero, reprise.titre)}</p>
    </a>
  {/if}

  {#if momentPresent}
    <a class="carte" href="/scene/{momentPresent.id}/">
      <p class="surtitre">{t.aujourdhui.momentPresentTitre}</p>
      <p>{t.aujourdhui.momentPresent(maintenant.getHours(), maintenant.getMinutes(), momentPresent.numero, momentPresent.titre)}</p>
    </a>
  {/if}

  {#if expressionDuJour}
    <a class="carte" href="/scene/{expressionDuJour.scene}/#{expressionDuJour.id}">
      <p class="surtitre">{t.aujourdhui.expressionDuJour}</p>
      <p class="enonce" lang="en">{expressionDuJour.texte[preferences.valeur.accent]}</p>
      <p class="douce">{expressionDuJour.sens}</p>
    </a>
  {/if}

  {#if !reprise}
    <section class="carte premier-pas">
      <Icone nom="plume" />
      <p>{t.aujourdhui.premierPas}</p>
      {#if prelude}
        <a class="action" href="/scene/{prelude.id}/">{t.aujourdhui.ouvrirPrelude}</a>
      {:else if premiere}
        <a class="action" href="/scene/{premiere.id}/">{t.aujourdhui.ouvrirChapitre1}</a>
      {:else}
        <a class="action discrete" href="/livre/">{t.livre.titre}</a>
      {/if}
    </section>
  {/if}
</main>

<style>
  .salutation { font-family: var(--police-titre); font-size: 2rem; line-height: 1.2; margin: var(--e6) 0 var(--e2); }
  .constance { margin: 0 0 var(--e6); }
  .premier-pas { display: flex; flex-direction: column; gap: var(--e4); align-items: flex-start; }
  .premier-pas :global(svg) { color: var(--accent); }
</style>
