# État d'avancement — Vivre l'Anglais

- Tranche : 2/10 en cours (Phase 2, les voix ; Phase 3, Prélude, scène étalon et chapitre 1). La tranche 1 est approuvée.
- Phase 2 : épreuve 7.5 en cours sur les 39 candidats. Le rendu en une passe est fait pour 216 lots sur 337, et le contrôle 7.10 est en cours pour ces lots.
- Phase 3 : la rédaction avance. Le Prélude est complet (P.1 à P.6). Sont écrites aussi la scène étalon c01.s01 et la scène c01.s02. Il reste huit scènes du chapitre 1 à écrire : c01.s03 à c01.s10.
- Prochaine action exacte :
  1. Terminer le contrôle de l'essai : `bash /tmp/boucle_int.sh 5` (journal dans /tmp/int3.log). La commande reprend là où elle s'est arrêtée.
  2. Classer les candidats avec `python3 voix/outils/bilan_essai.py`.
  3. Pour chaque voix, retenir le meilleur candidat, puis vérifier l'écart entre les voix (similarité inférieure à 0,55).
  4. Écrire les fiches `voix/fiches/{voix}.yaml`.
  5. Rédiger c01.s03 (S'habiller) avec `~/workspace/gen/chap.py`.

## Fait en tranche 2

- Calibrage 7.10 sur 500 enregistrements réels (`voix/calibrage/seuils.json`, D-037 à D-039).
- Outils de création et de contrôle (`voix/outils/`) :
  - `creer.py` : appels groupés, format G1 (D-045) et échelle d'allure (D-044) ;
  - `controler.py`, avec une transcription de confirmation par fichier ;
  - `decouper.py`, `bilan_essai.py`, `pipeline.mjs` et `sources_libres.py`.
- Inventaire des enregistrements libres (7.3) dans `voix/sources/inventaire.csv`. Il couvre 2 783 fichiers pour les 417 mots de c01.s01 :
  - 510 sont admis au regard de la licence (Wiktionary : us 371, uk 89, au 40, ca 7, nz 3) ;
  - 2 273 viennent de Lingua Libre et sont exclus, faute d'accent déclaré.
- 39 candidats (`voix/fiches/candidats/`), avec un script d'essai de 40 lignes (D-042). Kokoro a été mesuré et écarté comme moteur (D-043).
- Registre `voix/registre/creations.jsonl` : 834 entrées, dont 82 prises acceptées, 385 refusées et 367 lignes omises par le moteur.
- Corpus : huit scènes validées sans violation bloquante (`tools/valider_corpus.py --brouillon`). Il exige 7 270 fichiers de voix à ce stade.
  - Le Prélude est complet : 164 expressions et 88 paires d'écoute réciproques. Ses ateliers (jeu des paires, oreille fine, miroir) sont décrits en D-046.
  - Scène étalon c01.s01 : 55 expressions.
  - Scène c01.s02 : 50 expressions.

## Mesures de débit de la voix (constatées)

- Le moteur intégré met de 30 à 60 s par appel. Dans environ la moitié des lots, il s'arrête après la première ligne.
- Le premier essai passe dans 0 à 40 % des cas selon le candidat (`bilan_essai.py`). Les causes dominantes sont l'énoncé omis, le débit hors de la fenêtre 120–140 mots/min et l'accent sous 0,80.
- Le contrôle 7.10 complet prend de 60 à 110 s de calcul par lot de 10 lignes sur la machine de construction (2 processeurs, aucune carte graphique).
- Au rythme constaté, il faudrait plusieurs semaines de calcul continu pour le seul chapitre 1, soit environ 18 500 fichiers. Le livre entier en demande environ 245 000. Le périmètre n'est pas réduit : la production est découpée en lots repris d'une session à l'autre.

## Non vérifié à ce stade (consigné)

- Comparaison à l'aveugle avec des voix réelles (7.5, étape 2) : pas encore faite.
- Conditions d'usage commercial et de redistribution des voix du moteur intégré : à vérifier et archiver dans `docs/decisions/moteur-voix.md`.
- Common Voice exige désormais un compte Mozilla Data Collective. Le calibrage a donc été fait sur OpenSLR 83 et LibriSpeech (D-037).
- Les points déjà ouverts en tranche 1 restent ouverts : rendu sur émulateur sans KVM (D-032, D-034) et CI GitHub bloquée par la facturation (D-031).

## Reports suivis

Voir `pilotage/statuts.csv` et `pilotage/journal_des_decisions.md` (D-001 à D-046). Les décisions de la tranche sont copiées dans `docs/decisions/journal-tranche-02.md`.
