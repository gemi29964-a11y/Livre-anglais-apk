# État d'avancement — Vivre l'Anglais

- Tranche en cours : 1/10 (Phase 0 — lecture intégrale et cahier d'exécution ; Phase 1 — socle technique).
- Fait : voir la section « Fait » ci-dessous.
- Reste (tranche 1) : contrôle d'ouverture sur émulateur Android (en cours) ; vérification du premier passage de la CI ; rapport de fin de tranche.
- Prochaine action exacte : démarrer l'émulateur API 30 (image x86_64 google_apis), installer `android/app/build/outputs/apk/direct/release/app-direct-release.apk`, lancer `com.vivrelanglais.livre/.MainActivity`, capturer l'écran dans `pilotage/portes/emulateur-api30.png` et compléter `pilotage/portes/rapport-android.md`.

## Fait

- Phase 0 : lecture intégrale du Plan ; `pilotage/exigences.csv` (1 532 exigences, dont les 205 fonctionnalités F001–F205), généré par `pilotage/generer_exigences.py`, statuts tenus dans `pilotage/statuts.csv` (écrit par `pilotage/statuts_t1.py`) ; versions 10.2 vérifiées (D-001, `docs/decisions/pile-technique.md`).
- Phase 1 : arborescence 10.3, schéma annexe B, configurations annexe C ; outils de contrôle (lexique, phrasé, validation du corpus, typographie, contrastes, couverture vocale, paquets) ; application SvelteKit « Encre & Voix » ; couche Android (Capacitor 8.6, plugins Kotlin du Plan, widget, raccourcis, liens profonds, icônes) ; signature (clés d'envoi et directe) ; CI `android.yml` et `contenu.yml`.
- Preuves : `pilotage/portes/` (lexique, contrastes, tests des outils, tests unitaires, parcours web, build web, compilation Android et vérification des signatures).

## Reports suivis

Voir `pilotage/statuts.csv` (statuts « socle en place » et « reporté (Tn) ») et `pilotage/journal_des_decisions.md`.
