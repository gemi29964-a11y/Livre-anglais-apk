# Porte — intégration continue (10.16)

Date : 31 octobre 2026 · état de base : commit c8d188c plus les modifications de ce commit.

## Flux versionnés

- `.github/workflows/contenu.yml` : tests des outils, validation du corpus (`--strict`), lexique, phrasé, couverture, commentaire de la demande de fusion.
- `.github/workflows/android.yml` : voix, construction `--strict`, application web (ci, check, test, build, e2e), synchronisation Capacitor, AAB Play et APK direct signés, vérification des signatures, artefacts.

## Exécution sur GitHub : bloquée par le compte

Les exécutions 41148847203 (android) et 41148847263 (contenu) n'ont pas démarré : « The job was not started because your account is locked due to a billing issue ». Ce blocage tient au compte GitHub, pas au code. Le lever demande une action de votre part sur la page de facturation de GitHub ; je n'engage aucune dépense (D-031).

## Équivalent exécuté : tools/ci_locale.sh

Le script enchaîne les étapes des deux flux, dans le même ordre, sur la machine de construction. Sortie intégrale : `ci-locale.txt`.

| Étape | Résultat |
|---|---|
| Tests des outils (pytest) | 25 réussis |
| Validation du corpus --strict, lexique, phrasé | conformes |
| Voix, construire --strict, socle et paquets | réussis (0 paquet hors socle à ce stade) |
| npm ci, svelte-check, vitest + couverture | 0 erreur ; 48 tests réussis ; couverture 98,58 % des instructions |
| vite build (lexique avant et après construction) | conforme |
| Playwright | 8 parcours réussis |
| bundlePlayRelease (versionCode 1001) | réussi, AAB vérifié (« jar verified ») |
| assembleDirectRelease | réussi, APK vérifié par apksigner (CN=Vivre l'Anglais Direct, SHA-256 ebe0c7bb…d9d8f) |
| Code de sortie | 0 |

## Défaut trouvé par cette exécution et corrigé

Lors de la première exécution, `generer_paquets.py` effaçait le bloc de signature de `build.gradle` (D-035). L'outil est corrigé et couvert par un test ; la seconde exécution est entièrement verte.
