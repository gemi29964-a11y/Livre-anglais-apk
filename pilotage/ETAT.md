# État d'avancement — Vivre l'Anglais

- Tranche : 1/10 terminée (Phase 0, lecture intégrale et cahier d'exécution ; Phase 1, socle technique). En attente de l'approbation du lecteur.
- Fait : voir la section « Fait » ci-dessous.
- Reste : tranches 2 à 10. Sont aussi dus, hors de portée de la machine de construction : la vérification du rendu sur appareil réel ou émulateur accéléré (matrice 11.3, tranche 10) et une première exécution de la CI sur GitHub une fois le compte débloqué (D-031).
- Prochaine action exacte (après approbation) : tranche 2, Phase 2 (voix). Il faut d'abord rechercher les enregistrements sous licence libre, ensuite faire l'essai 7.5 de la génération intégrée, puis celui des modèles locaux ouverts, en mesurant contre les seuils 7.10. Résultats à consigner dans `voix/registre/creations.jsonl` et `pilotage/portes/voix-essai.md`.

## Fait

- Phase 0 : lecture intégrale du Plan.
  - `pilotage/exigences.csv` : 1 532 exigences, dont les 205 fonctionnalités F001–F205. Le fichier est généré par `pilotage/generer_exigences.py`.
  - Les statuts sont tenus dans `pilotage/statuts.csv`, écrit par `pilotage/statuts_t1.py` : 284 « fait (T1) », 73 « socle en place (T1) », 87 « reporté (Tn) ». Les autres exigences sont « à faire (Tn) ».
  - Versions 10.2 vérifiées (D-001, `docs/decisions/pile-technique.md`).
- Phase 1, socle technique :
  - arborescence 10.3, schéma de l'annexe B, configurations de l'annexe C ;
  - outils de contrôle : lexique, phrasé, validation du corpus, typographie, contrastes, couverture vocale, paquets ;
  - application SvelteKit « Encre & Voix », avec le complément de compatibilité pour les WebView anciennes (D-033) ;
  - couche Android : Capacitor 8.6, plugins Kotlin du Plan, widget, raccourcis, liens profonds, icônes ;
  - signature : clé d'envoi et clé directe ;
  - CI : `android.yml` et `contenu.yml`, avec l'équivalent local `tools/ci_locale.sh`, entièrement vert.
- Livrables de la tranche :
  - APK direct signé, versionCode 1001, version 1.0.0, 3 474 699 octets, SHA-256 148eb4d91be4851e04163ecba7ce8d42c9f50bda9bcb302bd032c813b0b4911c ;
  - AAB Play signé, 5 531 480 octets, SHA-256 c6bddf1f91d0eeec932fac79af04e9da9dd0f3bb79df38dc13d4da45904820a9.
- Preuves dans `pilotage/portes/` : `lexique.txt`, `contrastes.md`, `tests-outils.txt` (25), `tests-unitaires.txt` (48, couverture 98,58 %), `parcours-web.txt` (8), `build-web.txt`, `gradle-*.txt`, `rapport-android.md`, `ci.md` et `ci-locale.txt`, `budgets-t1.md`, `emulateur-api30-*` et `emulateur-api36-evenements.txt`.

## Non vérifié à ce stade (consigné)

- Rendu de l'interface sur émulateur. Sous API 30, l'APK s'installe et s'ouvre (activité au premier plan, aucun plantage). En revanche, l'émulation logicielle du processeur, sans KVM, calcule faux en JavaScript, ce qui bloque le rendu (D-034). Sous API 36, la WebView de l'image plante en code natif (D-032).
- Exécution de la CI sur GitHub : le compte est bloqué pour une question de facturation (D-031).
- Budgets de temps et de mémoire de 10.12 : ils se mesurent sur l'appareil de référence, en tranche 10.

## Reports suivis

Voir `pilotage/statuts.csv` (statuts « socle en place » et « reporté (Tn) ») et `pilotage/journal_des_decisions.md` (D-001 à D-035).
