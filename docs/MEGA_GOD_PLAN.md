# MEGA GOD PLAN — « Vivre l'Anglais »
## La Maîtrise Pratique et Exhaustive de l'Anglais de A à Z par l'Usage Quotidien
### Spécification complète du livre interactif Android : science, méthode, œuvre, voix, design, ingénierie, fabrication industrielle et publication

> Document de référence unique — 30 octobre 2026
> Il fait foi pour l'édition, la production des voix, le design, l'ingénierie et la publication.
> Langues de l'ouvrage : français (accompagnement) et anglais (expressions dites par des voix américaines et britanniques).

---

## Sommaire

- [0. Comment lire ce document](#0-comment-lire-ce-document)
- [1. L'ouvrage en un regard](#1-louvrage-en-un-regard)
- [2. Vision et principes directeurs](#2-vision-et-principes-directeurs)
- [3. La charte du lexique : parler au lecteur comme un éditeur, jamais comme une machine](#3-la-charte-du-lexique)
- [4. L'architecture de l'ouvrage](#4-larchitecture-de-louvrage)
- [5. Anatomie d'une Expression](#5-anatomie-dune-expression)
- [6. Le Phrasé : le système de prononciation](#6-le-phrasé--le-système-de-prononciation)
- [7. Les voix : origine, création, contrôle, intégration](#7-les-voix)
- [8. L'expérience du lecteur : écrans, gestes, déclenchement des voix](#8-lexpérience-du-lecteur)
- [9. Le design system « Encre & Voix »](#9-le-design-system--encre--voix-)
- [10. L'ingénierie : du corpus au fichier APK](#10-lingénierie--du-corpus-au-fichier-apk)
- [11. Assurance qualité et critères d'acceptation](#11-assurance-qualité-et-critères-dacceptation)
- [12. La fabrique éditoriale](#12-la-fabrique-éditoriale)
- [13. Les risques](#13-les-risques)
- [14. Le répertoire des fonctionnalités](#14-le-répertoire-des-fonctionnalités)
- [15. La science qui fonde l'ouvrage](#15-la-science-qui-fonde-louvrage)
- [16. Les secrets de l'anglais parlé](#16-les-secrets-de-langlais-parlé)
- [17. La grammaire parlée](#17-la-grammaire-parlée)
- [18. Le Cap : la méthode pour parler vite et juste](#18-le-cap--la-méthode-pour-parler-vite-et-juste)
- [19. Les modules sonores avancés](#19-les-modules-sonores-avancés)
- [20. L'échelle industrielle](#20-léchelle-industrielle)
- [21. Les volumes de l'œuvre intégrale](#21-les-volumes-de-lœuvre-intégrale)
- [Annexe A — La scène étalon (format final complet)](#annexe-a--la-scène-étalon)
- [Annexe B — Le schéma de validation d'une scène](#annexe-b--le-schéma-de-validation-dune-scène)
- [Annexe C — Fichiers de configuration complets](#annexe-c--fichiers-de-configuration-complets)
- [Annexe D — Glossaire technique](#annexe-d--glossaire-technique)
- [Annexe E — Check-list de mise en production](#annexe-e--check-list-de-mise-en-production)
- [Annexe F — Sources citées](#annexe-f--sources-citées)

---

## 0. Comment lire ce document

### 0.1 Portée

Ce document décrit entièrement **Vivre l'Anglais**, livre interactif pour Android, et tout ce qu'il faut pour le produire. Il se suffit à lui-même : aucune autre source n'est nécessaire pour écrire, enregistrer, dessiner, programmer, compiler et publier l'ouvrage. Il couvre neuf domaines indissociables :

1. **L'œuvre** : architecture, structure, ton, contenu.
2. **La prononciation** : système de transcription, couches de lecture, phénomènes de la langue parlée.
3. **Les voix** : origine, création, choix des prises, finition, contrôle, intégration, déclenchement.
4. **L'expérience** : écrans, gestes, parcours, rythme d'apprentissage.
5. **Le design** : identité, typographie, couleurs, composants, accessibilité.
6. **L'ingénierie** : corpus, application web embarquée, couche Android native, compilation de l'APK et de l'AAB, intégration continue, publication.
7. **La science** : les travaux sur l'apprentissage et l'acquisition des langues qui justifient chaque choix (section 15).
8. **La langue parlée et la méthode** : les secrets de l'anglais oral, la grammaire parlée, le chemin le plus court vers l'aisance et les modules sonores avancés (sections 16 à 19).
9. **L'industrie** : chaîne de production, constance des voix à grande échelle, contrôle statistique, chaîne d'approvisionnement logicielle, conformité et volumes de l'œuvre intégrale (sections 20 et 21).

### 0.2 Conventions normatives

| Mot | Valeur |
|---|---|
| **DOIT** / **NE DOIT PAS** | Exigence absolue. Une livraison qui ne la respecte pas est refusée. |
| **DEVRAIT** | Recommandation forte ; tout écart est justifié par écrit dans le journal des décisions (`docs/decisions/`). |
| **PEUT** | Option laissée au choix de la mise en œuvre. |

Les renvois internes s'écrivent « (8.4) » ou « section 10.9 ». Les chiffres de volume sont des estimations calculées à la densité cible (4.5) ; les valeurs mesurées les remplacent dans le journal des décisions dès qu'elles existent.

### 0.3 Deux vocabulaires, deux publics

- **Ce que voit et entend le lecteur** obéit à la charte du lexique (section 3) : aucun terme mécanique, scolaire ou informatique.
- **Ce que lit la mise en œuvre** (sections 7, 10, 11, 12, 19, 20 et annexes) emploie le vocabulaire technique exact, indispensable à une mise en œuvre sans ambiguïté. Ces termes ne franchissent jamais la frontière de l'interface. Le glossaire interne (annexe D) fait le pont entre les deux.

### 0.4 Décisions figées

Ces décisions ne se rediscutent qu'au moyen d'une révision écrite et datée de ce document.

| Sujet | Décision |
|---|---|
| Nom d'affichage | **Vivre l'Anglais** (sous-titre : La Maîtrise Pratique et Exhaustive de l'Anglais de A à Z par l'Usage Quotidien) |
| Identifiant Android | `com.vivrelanglais.livre` (définitif dès la première publication) |
| Technologie | Application web embarquée (SvelteKit + TypeScript, compilation statique) dans Capacitor 8 ; Android natif en Kotlin pour les voix, la promenade, l'expression du jour sur l'écran d'accueil |
| Android | `minSdk 24` (Android 7.0), `compileSdk 36`, `targetSdk 36` (Android 16) |
| Voix | Indiscernables d'une voix réelle : enregistrements existants sous licence libre ou voix créées par un moteur de très haute fidélité (7.3, 7.5). Aucune imitation d'une personne réelle, aucun étirement temporel ni changement de hauteur après coup |
| Variantes par énoncé | 4 interprétations : Américain posé, Américain spontané, Britannique posé, Britannique spontané |
| Voix du sens | Le sens français des expressions et des répliques est dit par une voix francophone chaleureuse (7.4) |
| Format audio | Opus mono 48 kHz dans conteneur Ogg (`.opus`) |
| Distribution | Deux canaux : **Play** (AAB + Play Asset Delivery) et **Direct** (APK signé + voix complémentaires depuis un serveur de l'éditeur) |
| Données personnelles | Aucune collecte, aucun compte, aucun traceur ; tout reste sur l'appareil |
| Modèle commercial | Hors du périmètre de ce document. L'ouvrage n'embarque aucun code d'achat, de publicité ou d'abonnement ; il fonctionne à l'identique quel que soit le prix fixé sur la fiche Play |

---

## 1. L'ouvrage en un regard

### 1.1 Ce que le lecteur tient entre les mains

Un livre d'anglais pour francophones, organisé non par la grammaire mais par **les situations de la vie** : du réveil au coucher, puis la conversation, les émotions, les opinions, le discours, la maison, l'amour, l'amitié, la table, l'argent, la santé, le travail, le voyage, l'humour, les argots, les idiomes, jusqu'à l'anglais des natifs les plus fins. Chaque expression s'entend, se lit, se comprend dans son usage réel et se retrouve au bon moment.

### 1.2 Les chiffres de l'ouvrage complet (à la densité cible)

| Élément | Quantité |
|---|---|
| Prélude sonore | 6 scènes |
| Chapitres | 26 |
| Scènes | 163 (+ 6 au Prélude) |
| Expressions | ≈ 8 965 (163 × 55) |
| Énoncés principaux (formes de l'expression) | ≈ 13 450 |
| Déclinaisons « Sur le même air » | ≈ 44 800 |
| Répliques de scènes vivantes | ≈ 2 280 |
| Paires d'écoute du Prélude | ≈ 720 |
| **Énoncés anglais à faire vivre en voix** | **≈ 61 250** |
| **Fichiers anglais** (× 4 interprétations) | **≈ 245 000** |
| Fichiers de la voix du sens (français) | ≈ 11 250 |
| Parole nette | ≈ 112 h d'anglais + ≈ 6 h de français |
| Poids encodé total | ≈ 1,5 Go, réparti par chapitre (10.9) |
| Poids installé d'emblée (Prélude, Chapitres 1 et 2) | ≈ 210 Mo |
| Incontournables | 1 630 (10 par scène) |
| Faux pas commentés | ≈ 1 300 (8 par scène) |
| Itinéraires transversaux | 12 (8.17) |
| Secrets de l'anglais parlé | 41 pages sonores (16) |
| Fiches de grammaire parlée | 30 (17) |
| Paliers de la méthode « Le Cap » | 7, du palier 0 au palier 6 (18) |
| Modules sonores avancés | 11 (19) |
| Fichiers des modules, secrets et grammaire | ≈ 56 000 (19.12) |
| **Fichiers sonores de l'œuvre intégrale** (anglais et français) | **≈ 312 000**, ≈ 140 h de parole, ≈ 1,9 Go (21.1) |

### 1.3 Ce qui rend l'ouvrage unique

1. **Quatre voix vivantes par phrase** : américaine et britannique, posée et spontanée, d'un naturel indiscernable d'une vraie conversation.
2. **Un phrasé à la française rigoureux**, écrit à l'écoute de la voix réelle, avec une couche experte en alphabet phonétique international.
3. **L'usage avant la règle** : chaque expression dit quand, avec qui et pourquoi on l'emploie.
4. **Sur le même air** : chaque expression ouvre sur cinq phrases nouvelles, traduites et dites, pour apprendre à créer.
5. **Une série vivante** : une famille et ses proches traversent les 26 chapitres dans des scènes jouées en dialogue continu, comme une vraie conversation.
6. **Retrouver plutôt que réviser** : les expressions reviennent au bon moment, sous huit formes, dont l'écoute, la réplique et le miroir.
7. **Un livre qui s'emporte partout** : la promenade s'écoute écran éteint, avec la voix du sens en français.
8. **Rien ne quitte le téléphone** : aucun compte, aucune collecte, tout fonctionne sans connexion.
9. **Fondé sur la recherche** : chaque fonctionnalité découle d'un résultat établi sur la mémoire, l'écoute et l'aisance orale, et l'ouvrage dit honnêtement ce qu'il ne peut pas promettre (15).
10. **Les secrets de l'oral enfin enseignés** : rythme, formes faibles, liaisons, mélodie, politesse, sous-entendus, tout ce que les manuels taisent et que les natifs font sans y penser (16, 17).
11. **Une méthode pour parler vite** : sept paliers de compétence, des épreuves locales, une journée type de cinq à quatre-vingt-dix minutes (18).
12. **Seize voix pour une oreille neuve** : paires de sons dans seize bouches différentes, conversations à jouer, annonces, bruit réel et voix du monde entier (19).

### 1.4 Ce que l'ouvrage n'est pas

- Ni un cours de grammaire : la grammaire vit en situation (Chapitre 24).
- Ni un jeu : aucun point, aucun classement, aucune récompense artificielle.
- Ni un assistant conversationnel : aucune voix générée, aucune réponse fabriquée par une machine.
- Ni un juge : le miroir montre et fait entendre ; il ne note pas.

---

## 2. Vision et principes directeurs

### 2.1 La promesse

> **Vivre l'Anglais est un livre que l'on écoute autant qu'on le lit.** Chaque phrase de la vie quotidienne y est dite par de vraies voix américaines et britanniques, d'abord posément, puis au rythme réel des natifs. Le lecteur ne « révise » pas : il retrouve ses expressions, les entend, les dit, et finit par penser avec elles.

### 2.2 Les treize principes

1. **La voix d'abord.** Aucune expression anglaise n'apparaît sans sa voix. Une expression muette est un défaut bloquant.
2. **Vivant, de bout en bout.** Des voix que rien ne distingue d'une personne qui parle, des transcriptions écrites à l'écoute, des textes d'un naturel de natif. Une voix qui sonne mécanique est un défaut bloquant.
3. **Deux accents, deux vitesses, toujours.** Américain et britannique ; posé et spontané. Le lecteur choisit, compare, apprend la différence.
4. **La transcription suit la voix.** La voix est produite d'abord ; on transcrit ensuite ce qui a été réellement dit.
5. **Un livre, pas un logiciel.** Le vocabulaire, la typographie, les transitions et le rythme sont ceux de l'édition de qualité.
6. **Comprendre avant de produire.** Écouter, reconnaître, puis répéter, puis créer.
7. **Retrouver plutôt que réviser.** Les expressions reviennent au bon moment, selon un calendrier personnel.
8. **Une main, un pouce, une minute.** Tout geste essentiel est réalisable d'une main, en moins de deux touchers.
9. **Hors connexion par nature.** L'ouvrage, ses voix installées et la progression fonctionnent sans réseau.
10. **Accessible sans compromis.** Lecteur d'écran, grands caractères, contraste élevé, mouvement réduit.
11. **Rien ne quitte le téléphone.** Ni progression, ni enregistrements de la voix du lecteur.
12. **Mesurable.** Chaque exigence de ce document est vérifiable par un test, une check-list ou une écoute.
13. **Prouvé.** Aucune fonctionnalité pédagogique n'entre dans l'ouvrage sans un fondement établi (section 15) ; aucune promesse n'excède ce que la recherche permet d'affirmer.

### 2.3 À qui s'adresse l'ouvrage

| Profil | Besoin principal | Réponse de l'ouvrage |
|---|---|---|
| Francophone débutant (A1–A2) | Oser parler, comprendre l'essentiel | Prélude sonore, filtre « Fondations », voix posée par défaut, toutes les déclinaisons traduites |
| Francophone intermédiaire (B1–B2) | Comprendre les natifs à vitesse réelle | Voix spontanée, écoute comparée, « Ce que l'oreille entend » |
| Francophone avancé (C1–C2) | Nuance, registre, accent | Couche phonétique experte, chapitres Zénith, comparaison d'accents |
| Professionnel en mobilité | Pratiquer dans les transports | Promenade sonore écran éteint, sessions de cinq minutes |
| Enseignant ou formateur | Support fiable | Transcriptions en alphabet phonétique international, index, export de listes de marque-pages |
| Voyageur, expatrié, futur étudiant à l'étranger | Être opérationnel vite sur un terrain précis | Itinéraires transversaux (8.17), voix britanniques ou américaines au choix |
| Francophone vivant au contact de l'anglais (Afrique de l'Ouest, Canada, frontaliers) | Comprendre des accents variés | Atlas des accents, Chapitre 22.5, voix du monde |

---

## 3. La charte du lexique

### 3.1 Le principe

Le lecteur est accompagné par **une voix d'éditeur** : cultivée, chaleureuse, précise, qui vouvoie, ne gronde jamais, ne parle ni de « contenu » ni de « fonctionnalité ». Elle emprunte au monde du livre, du théâtre, de la musique et du voyage — quatre univers liés à la parole vivante — sans jamais mélanger les métaphores au sein d'un même écran.

### 3.2 La table de correspondance (obligatoire)

| Terme proscrit | Terme de l'ouvrage | Où il apparaît |
|---|---|---|
| Module | **Chapitre** | Sommaire, en-têtes |
| Sous-module | **Scène** | Sommaire, en-têtes, parcours |
| Section A, B, C… | **Moment** (« Moment A — Le réveil sonne ») | Corps de la scène |
| Fiche | **Expression** | Partout |
| Phrase principale | **L'expression** (ses formes : « Autre façon de dire ») | Carte d'expression |
| Prononciation | **Le phrasé** | Carte d'expression |
| Code de prononciation | **Les clés du phrasé** | Ressource permanente |
| Connected speech | **La musique de la phrase** | Prélude, notes |
| Vitesse normale | **Posé** | Pupitre des voix |
| Vitesse rapide | **Spontané** | Pupitre des voix |
| US / UK | **Américain / Britannique** (abrégés « Am. » et « Brit. » quand la place manque) | Pupitre des voix |
| Traduction | **Le sens** | Carte d'expression |
| [littéral] | **Mot à mot** | Carte d'expression |
| Pragmatique | **L'usage** | Carte d'expression |
| Note culturelle | **En coulisses** | Carte d'expression |
| Modèle génératif | **Sur le même air** | Carte d'expression |
| Registre neutre | **Ton courant** | Étiquette |
| Registre familier | **Ton complice** | Étiquette |
| Registre argotique | **Ton cru** | Étiquette |
| Registre formel | **Ton soutenu** | Étiquette |
| Niveau A1–A2 / B1–B2 / C1–C2 | **Fondations / Aisance / Maîtrise** | Étiquette, filtres |
| Synthèse active | **L'Essentiel** | Fin de scène |
| Les 10 phrases à automatiser | **Les dix incontournables** | L'Essentiel |
| Les pièges du francophone | **Les faux pas** | L'Essentiel |
| Mini-scène | **La scène vivante** | Fin de scène |
| Exercice d'ancrage | **Le rituel** | Fin de scène |
| Révision, flashcards, répétition espacée | **Les retrouvailles** | Onglet, notifications |
| Quiz, test, évaluation | **L'épreuve d'oreille**, **la réplique**, **le miroir** (voir 8.7) | Retrouvailles |
| Score, points, XP | Aucun. On parle d'**expressions familières** (maîtrisées) et de **jours de pratique** | Carnet |
| Série (streak) | **Constance** (« 12 jours de constance ») | Carnet |
| Progression, pourcentage | **Chemin parcouru** (« 12 scènes parcourues sur 163 ») | Sommaire |
| Favoris | **Marque-pages** | Carnet |
| Mes enregistrements | **Ma voix** | Carnet |
| Lecture audio en continu | **La promenade** | Onglet |
| Mode hors ligne | **Disponible sans connexion** | Préférences |
| Télécharger | **Faire venir** (« Faire venir les voix du chapitre 7 ») | Voix à installer |
| Téléchargement en cours | **Les voix arrivent…** | Indicateur |
| Paramètres | **Préférences** | Onglet secondaire |
| Tutoriel, onboarding | **L'accueil** | Premier lancement |
| Recherche | **Comment dit-on… ?** | Barre de recherche |
| Résultat | **Trouvé dans** (« Trouvé dans Scène 1.1, Moment A ») | Recherche |
| Erreur | **Un contretemps** | Messages |
| Valider, soumettre | **C'est fait**, **Continuer** | Boutons |
| Correct / incorrect | **Juste** / **Pas tout à fait** | Retrouvailles |
| Utilisateur, apprenant, élève | **Vous** (jamais de nom générique) | Partout |
| Leçon, cours | **Scène** | Partout |
| Notification | **Rendez-vous** | Préférences |
| Chargement | Aucun mot : une ligne d'encre qui s'écrit (voir 9.8) | Transitions |
| Cliquer, appuyer sur le bouton | **Touchez**, **effleurez**, **maintenez** | Aides contextuelles |
| Dictée | **L'oreille fine** | Retrouvailles, Prélude |
| Paires minimales | **Le jeu des paires** | Prélude |
| Parcours thématique | **Itinéraire** (« Itinéraire : Premier voyage à Londres ») | Le Livre |
| Statistiques, tableau de bord | **Le regard en arrière** | Mon carnet |
| Widget | **L'expression du jour sur l'écran d'accueil** | Préférences, écran d'accueil Android |
| Aide, FAQ, guide | **Lire ce livre** | Préférences |
| Lecture en boucle | **L'écho** | Volet d'une expression |
| Visualisation de la hauteur | **La courbe** | Carte d'expression, miroir |
| Vibration rythmique | **Le battement** | Préférences |
| Narration française | **La voix du sens** | Promenade, retrouvailles |

### 3.3 Mots bannis de l'interface (contrôle automatique)

Le contrôle de compilation `tools/lexique_verifier.py` (section 10.5) DOIT refuser toute chaîne visible contenant (sans tenir compte de la casse et des accents) :

```
module, sous-module, fiche, exercice, quiz, test, score, points, xp, niveau débloqué,
débloquer, valider, soumettre, erreur, bug, chargement, télécharger, téléchargement,
synchroniser, synchronisation, cliquer, bouton, menu, paramètre, paramètres, utilisateur,
apprenant, élève, leçon, cours, contenu, fichier, données, audio, mode, item, input,
output, tts, synthèse vocale, algorithme, automatiser, génératif, pivot, étape suivante,
prochaine étape, réponse suivante, widget, statistiques, tableau de bord, tutoriel,
onboarding, notification, profil, compte, dictée, playlist, feedback
```

Exceptions autorisées : le mot « mode » dans une citation anglaise (*mode*, *in a mood*), et tout mot banni lorsqu'il fait partie d'une expression anglaise enseignée (ex. *test*, *error*). Le vérificateur ignore le texte balisé `lang="en"`.

### 3.4 La voix de l'éditeur : règles d'écriture

1. **Vouvoiement** constant, chaleureux : « Vous l'entendrez surtout le matin, entre proches. »
2. **Phrases courtes** : 22 mots maximum dans les textes d'interface ; 45 mots maximum par phrase dans « L'usage ».
3. **Jamais d'injonction sèche** : « Écoutez d'abord la voix posée » plutôt que « Écoutez la vitesse normale. »
4. **Jamais de culpabilisation** : pas de « Vous avez oublié ! », mais « Cette expression revient vous saluer. »
5. **Typographie française stricte** : espace insécable avant « ; : ! ? » et à l'intérieur des guillemets « », apostrophe typographique ’, tiret cadratin — pour les incises, points de suspension en un seul caractère « … ».
6. **L'anglais toujours balisé** : tout fragment anglais est encodé `lang="en"` (lecture d'écran correcte, typographie distincte), jamais en italique Markdown dans l'interface finale.
7. **Pas d'émojis** dans le texte d'accompagnement. Les repères visuels sont des composants dessinés (section 9).
8. **Pas de point d'exclamation** dans l'accompagnement, sauf dans les expressions anglaises elles-mêmes.

### 3.5 Microtextes de référence (à reprendre mot pour mot)

| Situation | Texte |
|---|---|
| Premier lancement, écran 1 | « Bienvenue. Ce livre se lit avec les oreilles autant qu'avec les yeux. » |
| Choix de l'accent | « Quelle voix souhaitez-vous entendre en premier ? Vous pourrez toujours écouter l'autre d'un geste. » |
| Durée quotidienne | « Combien de temps souhaitez-vous consacrer à l'anglais chaque jour ? Cinq minutes suffisent pour commencer. » |
| Reprise | « Reprendre là où vous étiez : Scène 1.4, Le petit-déjeuner. » |
| Retrouvailles du jour | « 18 expressions vous attendent aujourd'hui. Environ six minutes. » |
| Aucune retrouvaille due | « Tout est à jour. Pourquoi ne pas découvrir une nouvelle scène ? » |
| Voix non installées | « Les voix de ce chapitre ne sont pas encore sur votre téléphone. Les faire venir maintenant ? (86 Mo — une connexion Wi-Fi est conseillée.) » |
| Voix en cours d'arrivée | « Les voix arrivent… 42 % » |
| Pas de réseau | « Vous êtes hors connexion. Tout ce qui est déjà sur votre téléphone reste à votre disposition. » |
| Contretemps de lecture | « Cette voix ne répond pas pour l'instant. Touchez pour réessayer. » |
| Demande du micro | « Pour entendre votre voix à côté de celle du livre, le livre a besoin du micro. Vos enregistrements restent sur ce téléphone. » |
| Micro refusé | « Sans micro, le miroir reste fermé. Vous pouvez l'ouvrir à tout moment dans les Préférences. » |
| Fin de scène | « Scène parcourue. Ses expressions reviendront vous voir demain. » |
| Constance | « 12 jours de constance. Le rendez-vous de demain vous attend à 7 h 30. » |
| Rendez-vous (notification) | « Vos retrouvailles du matin sont prêtes : 9 expressions, quatre minutes. » |
| Recherche sans résultat | « Rien de tel dans le livre pour l'instant. Essayez un mot plus simple, en français ou en anglais. » |
| L'oreille fine, après la saisie | « Voici ce que la voix a dit. Les mots en couleur vous ont échappé : réécoutez-les seuls. » |
| L'écho | « La voix revient trois fois. Parlez avec elle, puis juste après elle. » |
| Le moment présent (matin) | « Il est 7 h 10. C'est l'heure de la Scène 1.1 : le réveil. » |
| Itinéraire proposé | « Vous partez bientôt ? L'itinéraire Premier voyage réunit 240 expressions en douze étapes. » |
| Le regard en arrière (mensuel) | « En octobre, 214 expressions vous sont devenues familières. Vous avez écouté 9 h 40 de voix. » |
| Voix réparées | « Quelques voix du chapitre 7 étaient abîmées. Elles ont été remises en état. » |
| Volume de l'appareil bas | « Le son de votre téléphone est très bas. » |
| Expression du jour sur l'écran d'accueil | « Ajoutez l'expression du jour sur votre écran d'accueil : un toucher, et la voix se fait entendre. » |

### 3.6 Exemple de rendu : une expression telle que le lecteur la voit

Scène 1.1, Moment A, accent britannique et rythme posé sélectionnés :

```
MOMENT A — LE RÉVEIL SONNE                                 1 sur 7

My alarm's going off.                                  ◉ Écouter
maï ə·LÂMZ gəou·ing OF                   Brit. · Posé   ⇄ Am.  ⇄ Spontané

Mon réveil sonne.
Mot à mot : mon alarme est en train de partir.
Ton courant · Fondations

L'usage
Go off, c'est « se déclencher » : un réveil, une alarme, un détecteur de fumée.
Les natifs ne disent presque jamais My alarm is ringing.

Sur le même air — [quelque chose] is going off
  The fire alarm's going off.        L'alarme incendie sonne.          ◉
  My phone keeps going off.          Mon téléphone n'arrête pas de sonner.  ◉
  The car alarm went off at 3 a.m.   L'alarme de la voiture s'est déclenchée à 3 h.  ◉
  The smoke detector just went off.  Le détecteur de fumée vient de se déclencher.  ◉
  My alarm didn't go off!            Mon réveil n'a pas sonné !  → Moment H
```

---

## 4. L'architecture de l'ouvrage

### 4.1 La hiérarchie

```
L'OUVRAGE  « Vivre l'Anglais »
├── Le Prélude — L'oreille et la voix               (6 scènes, entièrement sonores)
├── 26 CHAPITRES
│   └── 163 SCÈNES
│       ├── L'Ouverture                             (intention + écoute d'immersion)
│       ├── MOMENTS A, B, C…                        (8 à 15 par scène)
│       │   └── EXPRESSIONS                         (40 à 75 par scène)
│       │       ├── Énoncés (1 à 3 formes)          → 4 voix chacun
│       │       ├── Le phrasé (US/UK × posé/spontané) + couche experte
│       │       ├── Le sens · Mot à mot · L'usage · En coulisses
│       │       └── Sur le même air (3 à 6 déclinaisons) → 4 voix chacune
│       ├── L'Essentiel (dix incontournables + faux pas)
│       ├── La scène vivante (pièce sonore à deux accents et deux vitesses)
│       └── Le rituel (pratique dans la vraie vie)
├── Les Itinéraires                                (12 parcours transversaux, 8.17)
├── Les Appendices
│   ├── Les clés du phrasé (ressource permanente, sonore)
│   ├── L'atlas des accents (américain, britannique, voix du monde)
│   ├── Le lexique (index alphabétique anglais et français)
│   ├── Tous les faux pas (compilation)
│   └── Tous les incontournables (1 630 expressions au terme de l'ouvrage)
└── Le Carnet du lecteur (marque-pages, notes, ma voix, constance)
```

### 4.2 Le parcours d'une scène (ordre canonique, identique pour les 163 scènes)

| Temps | Nom | Durée cible | Contenu |
|---|---|---|---|
| 1 | **L'Ouverture** | 1 min | Titre, intention (« À la fin de cette scène, vous saurez… »), écoute d'immersion : la scène vivante jouée **en spontané, sans texte**. Le lecteur découvre ce qu'il ne comprend pas encore. |
| 2 | **Les Moments** | 15 à 40 min (fractionnable) | Les expressions, groupées par moment de vie. Chaque moment est une unité de lecture autonome (signet automatique en fin de moment). |
| 3 | **L'Essentiel** | 3 min | Les dix incontournables (écoutables d'affilée), les faux pas. |
| 4 | **La scène vivante** | 3 min | La même pièce sonore qu'à l'Ouverture, désormais avec texte bilingue aligné, en posé puis en spontané. Puis l'option « Donnez la réplique ». |
| 5 | **Le rituel** | 1 min | Trois à cinq gestes concrets à faire dans la journée, en anglais. |
| 6 | **Les retrouvailles** | automatique | Les expressions de la scène entrent dans le calendrier personnel. |

### 4.3 Le Prélude — L'oreille et la voix

Six scènes courtes, entièrement sonores, qui installent les clés du phrasé avant le Chapitre 1.

| Scène | Titre | Ce que le lecteur entend et pratique |
|---|---|---|
| P.1 | Le souffle et la langue | *h* soufflé ; *th* sourd (*think*) et sonore (*this*) ; *r* anglais |
| P.2 | Voyelles longues, voyelles brèves | *ship / sheep*, *full / fool*, *cot / caught* (et pourquoi l'Américain les confond parfois) |
| P.3 | Le battement de la phrase | Syllabe forte, syllabes effacées, le son ə |
| P.4 | Les petits mots qui s'écrasent | *to, for, and, of, you, can* : formes pleines et formes faibles |
| P.5 | Quand les mots se collent | Enchaînements, *t* battu américain (*get up*), coup de glotte britannique, *did you → didja* |
| P.6 | Deux Anglais, une langue | Le *r* final, *hot*, *go*, *can't*, *tomato* : l'atlas des différences, en écoute comparée |

Chaque scène du Prélude contient 12 à 20 paires d'écoute, un « jeu des paires » (le lecteur entend un mot et désigne lequel des deux il a entendu, *ship* ou *sheep*), une oreille fine de cinq phrases et un miroir (le lecteur s'enregistre et se compare). Le Prélude porte l'identifiant de chapitre `c00` dans tout le système (`c00.s01` à `c00.s06`).

### 4.4 Les 26 chapitres et 163 scènes

Les titres de chapitre sont écrits dans la voix de l'éditeur. L'ordre des chapitres va du plus quotidien au plus fin ; chaque chapitre peut néanmoins s'ouvrir directement.

| Ch. | Titre du chapitre | Scènes |
|---|---|---|
| 1 | **Une journée, du réveil au coucher** | 1.1 Le réveil · 1.2 La salle de bain · 1.3 S'habiller · 1.4 Le petit-déjeuner · 1.5 Partir de la maison · 1.6 Le trajet · 1.7 Le retour · 1.8 Le dîner en famille · 1.9 La soirée · 1.10 Le coucher |
| 2 | **Les gestes de la conversation** | 2.1 Saluer · 2.2 Prendre des nouvelles · 2.3 Se présenter · 2.4 Parler de tout et de rien · 2.5 Prendre congé · 2.6 Remercier · 2.7 S'excuser · 2.8 Faire répéter · 2.9 Interrompre et gagner du temps · 2.10 Féliciter, souhaiter, consoler |
| 3 | **Le cœur et les humeurs** | 3.1 Joie · 3.2 Tristesse · 3.3 Colère · 3.4 Peur et stress · 3.5 Surprise · 3.6 Ennui · 3.7 Gêne · 3.8 Jalousie et fierté · 3.9 Soulagement et gratitude · 3.10 Doute et hésitation |
| 4 | **Penser à voix haute** | 4.1 Donner son avis · 4.2 Être d'accord · 4.3 Être en désaccord · 4.4 Argumenter et nuancer · 4.5 Changer d'avis · 4.6 Esquiver, rester neutre |
| 5 | **Le fil du discours** | 5.1 Ajouter · 5.2 Opposer · 5.3 Cause et conséquence · 5.4 Temps et enchaînement · 5.5 Illustrer et reformuler · 5.6 Conclure et revenir au sujet |
| 6 | **Demander, proposer, refuser** | 6.1 Demander un service · 6.2 Proposer son aide · 6.3 Inviter · 6.4 Suggérer · 6.5 Accepter avec enthousiasme · 6.6 Refuser sans vexer · 6.7 Permettre et interdire |
| 7 | **Chez soi** | 7.1 Les tâches ménagères · 7.2 Cuisiner · 7.3 Pannes et bricolage · 7.4 Colocation et voisins · 7.5 Factures et loyer · 7.6 Déménager |
| 8 | **Les liens intimes** | 8.1 Parents et enfants · 8.2 Frères, sœurs et famille · 8.3 Séduire · 8.4 La vie à deux · 8.5 Se disputer, se réconcilier · 8.6 Se quitter · 8.7 Les grands événements |
| 9 | **Les amis et la vie sociale** | 9.1 Organiser une sortie · 9.2 Les fêtes · 9.3 Taquiner · 9.4 Soutenir un ami · 9.5 Confidences et potins · 9.6 Garder le lien |
| 10 | **À table** | 10.1 Réserver et arriver · 10.2 Commander · 10.3 Pendant le repas · 10.4 L'addition · 10.5 Sur le pouce et à emporter · 10.6 Au bar |
| 11 | **Acheter, payer, compter** | 11.1 En boutique · 11.2 Payer · 11.3 Retours et réclamations · 11.4 Marchander · 11.5 La banque · 11.6 L'argent entre proches |
| 12 | **Le corps et la santé** | 12.1 Dire où l'on a mal · 12.2 Chez le médecin · 12.3 À la pharmacie · 12.4 Les urgences · 12.5 Dentiste et spécialistes · 12.6 Le moral et le bien-être · 12.7 Le sport |
| 13 | **La vie professionnelle** | 13.1 Arriver au bureau · 13.2 Les réunions · 13.3 Écrire des courriels · 13.4 Appels et visioconférences · 13.5 Délais et priorités · 13.6 Donner et recevoir un retour · 13.7 Assumer ses torts · 13.8 La hiérarchie · 13.9 L'entretien d'embauche · 13.10 Partir, changer de voie |
| 14 | **L'art de convaincre** | 14.1 Ouvrir une négociation · 14.2 Proposer, contre-proposer · 14.3 Tenir ses limites · 14.4 Conclure un accord · 14.5 Persuader au quotidien |
| 15 | **La vie connectée** | 15.1 Téléphone et messages · 15.2 Quand l'ordinateur résiste · 15.3 Les réseaux sociaux · 15.4 Le langage des startups et du logiciel · 15.5 Commandes en ligne |
| 16 | **En voyage** | 16.1 Demander son chemin · 16.2 À l'aéroport · 16.3 À l'hôtel · 16.4 Taxi et location · 16.5 Train et transports · 16.6 Visiter · 16.7 Les imprévus du voyage |
| 17 | **Démarches et services** | 17.1 La poste · 17.2 L'administration · 17.3 Le service client · 17.4 La police · 17.5 Artisans et réparateurs |
| 18 | **Loisirs et culture** | 18.1 Films et séries · 18.2 Musique · 18.3 Lecture · 18.4 Le sport en spectateur · 18.5 Jeux vidéo · 18.6 Passions et nature |
| 19 | **Le temps qu'il fait, le temps qui passe** | 19.1 L'heure, la date, les durées · 19.2 La météo · 19.3 Saisons et fêtes |
| 20 | **Quand tout déraille** | 20.1 Retards et annulations · 20.2 Oublis et pertes · 20.3 Petits accidents · 20.4 Malentendus · 20.5 Situations gênantes · 20.6 Urgences graves |
| 21 | **L'humour anglais** | 21.1 Plaisanter · 21.2 Ironie et sarcasme · 21.3 Se moquer de soi · 21.4 L'art de l'euphémisme |
| 22 | **Les registres et les argots** | 22.1 Argot américain · 22.2 Argot britannique · 22.3 La langue des jeunes et d'Internet · 22.4 Jurons : comprendre, doser, éviter · 22.5 Australie, Irlande, Afrique anglophone |
| 23 | **Les idiomes** | 23.1 Le corps · 23.2 Les animaux · 23.3 L'argent et le travail · 23.4 Le temps et la vitesse · 23.5 Les proverbes vivants |
| 24 | **La grammaire vivante** | 24.1 Le présent · 24.2 Raconter le passé · 24.3 Le futur · 24.4 Hypothèses et regrets · 24.5 Les modaux en situation · 24.6 Questions et *question tags* |
| 25 | **Le savoir-vivre** | 25.1 L'art d'adoucir · 25.2 Différences culturelles · 25.3 Sujets délicats · 25.4 Le langage du corps |
| 26 | **Zénith — l'anglais des natifs** | 26.1 Raconter une histoire · 26.2 Parler en public · 26.3 Rhétorique · 26.4 Lire entre les lignes · 26.5 Penser en anglais |

### 4.5 Normes de densité

| Élément | Minimum | Cible | Maximum |
|---|---|---|---|
| Moments par scène | 8 | 12 | 15 |
| Expressions par scène | 40 | 55 | 75 |
| Expressions par moment | 3 | 5 | 8 |
| Énoncés par expression | 1 | 1 à 2 | 3 |
| Déclinaisons par expression | 3 | 5 | 6 |
| Déclinaisons traduites | **100 %** | 100 % | — |
| Répliques de la scène vivante | 10 | 14 | 20 |
| Incontournables | 10 | 10 | 10 |
| Faux pas | 6 | 8 | 10 |

La densité est **égale d'un bout à l'autre de l'ouvrage** : le Chapitre 26 est aussi riche que le Chapitre 1. Le contrôle de compilation bloque toute scène sous le minimum et avertit sous la cible.

### 4.6 Les métadonnées de chaque expression

| Métadonnée | Valeurs | Usage |
|---|---|---|
| Niveau | `fondations` (A1–A2), `aisance` (B1–B2), `maitrise` (C1–C2) | Filtre, parcours, ordre des retrouvailles |
| Fréquence | 1 (rare) à 5 (quotidienne) | Priorité des incontournables, ordre de la promenade |
| Ton | `courant`, `complice`, `cru`, `soutenu` | Étiquette, indication de jeu des voix |
| Région | `commun`, `us`, `uk` (+ `au`, `ie`, `ng`, `gh`, `za` au Chapitre 22) | Règles régionales (7.6), atlas des accents |
| Situation | liste libre normalisée (ex. `matin`, `couple`, `travail`) | Recherche, parcours thématiques |
| Fonction | liste fermée (ex. `saluer`, `refuser`, `se-plaindre`, `adoucir`) | Parcours fonctionnels transversaux |
| Émotion de jeu | ex. `ensommeillé`, `agacé`, `tendre` | Indication de jeu des voix |
| Renvois | identifiants d'autres expressions | Liens navigables |

Le niveau et la fréquence de chaque expression sont attribués à la rédaction, puis contre-vérifiés par deux relectures natives indépendantes (une américaine, une britannique) ; en cas de désaccord, la valeur la plus prudente (niveau le plus élevé, fréquence la plus basse) est retenue.

---

## 5. Anatomie d'une Expression

L'Expression est l'unité fondamentale de l'ouvrage. Sa structure est identique sur les 163 scènes ; elle est décrite ici pour l'éditeur, puis formalisée en schéma de données en section 10.4.

### 5.1 Les douze composants

| # | Composant | Contenu | Règle d'écriture | Obligatoire |
|---|---|---|---|---|
| 1 | **Repère** | Moment + rang (« Moment A · 1 sur 7 ») | Généré | Oui |
| 2 | **L'expression** | 1 à 3 énoncés anglais (forme principale + « Autre façon de dire ») | Ponctuation anglaise, apostrophes typographiques, orthographe de la région de l'énoncé | Oui |
| 3 | **Le pupitre des voix** | Accent (Am./Brit.) et rythme (Posé/Spontané) | Composant | Oui |
| 4 | **Le phrasé** | Transcription « à la française » de la voix sélectionnée (4 versions par énoncé) | Système du phrasé (section 6) ; écrite *après* la mise en voix | Oui |
| 5 | **Ce que l'oreille entend** | Graphie de l'énoncé tel que prononcé en spontané (*Whatcha doin'?*), quand elle diffère de l'écrit | Uniquement si la réduction est audible et usuelle | Si pertinent |
| 6 | **Le regard expert** | Alphabet phonétique international, 4 versions, + courbe d'intonation | Notation large (phonémique) entre barres obliques, accents primaire et secondaire | Oui (masqué par défaut) |
| 7 | **Le sens** | Équivalent français naturel, dans le même ton | Pas de traduction mot à mot ici | Oui |
| 8 | **Mot à mot** | Traduction littérale, si elle éclaire | Entre guillemets, ≤ 12 mots | Si pertinent |
| 9 | **L'usage** | Quand, avec qui, pourquoi ; nuance, piège | 2 à 4 phrases, ≤ 70 mots | Oui |
| 10 | **En coulisses** | Note culturelle ou régionale (UK/US) | ≤ 50 mots | Si pertinent |
| 11 | **Sur le même air** | Gabarit (`[quelque chose] is going off`) + 3 à 6 déclinaisons, **toutes traduites**, toutes en voix | Chaque déclinaison ≤ 12 mots | Oui |
| 12 | **Étiquettes** | Ton, niveau, région | Composant | Oui |

### 5.2 Règles éditoriales fines

1. **Un énoncé = une voix.** Deux formes d'une même expression (« What time is it? » et « What's the time? ») sont deux énoncés distincts, chacun avec ses quatre voix et ses quatre phrasés ; jamais deux formes séparées par une barre oblique.
2. **La forme principale est la plus fréquente**, pas la plus « correcte ».
3. **Le littéral ne se mêle jamais au sens** : il vit dans « Mot à mot », sans crochets ni parenthèses.
4. **Chaque déclinaison a son sens**, dans son champ propre ; aucune déclinaison n'est mise en voix sans sens validé.
5. **Les renvois** sont des liens typés `renvois: [c01.s01.H1]`, rendus par une flèche discrète « → Moment H » ; jamais de renvoi en texte libre (« cf. … »).
6. **Le ton cru** est accompagné d'un avertissement d'usage dans « L'usage » (« À réserver aux amis proches ; choquant au travail. »).
7. **Aucun énoncé n'excède 18 mots** ; au-delà, il est découpé ou déplacé dans la scène vivante.
8. **Orthographe régionale** : l'énoncé britannique s'écrit *colour, Mum, flat, queue* ; l'énoncé américain *color, Mom, apartment, line*. Lorsqu'un énoncé est commun aux deux accents mais que l'orthographe diffère, deux graphies sont stockées et l'écran affiche celle de l'accent sélectionné.

### 5.3 La scène vivante (format enrichi)

- Chaque réplique a un identifiant, un personnage, un texte anglais, un sens français aligné, une émotion de jeu.
- Le texte existe en **deux versions localisées** : britannique (*It's half seven!*, *Mum*) et américaine (*It's seven-thirty!*, *Mom*). La version de référence est rédigée dans un accent, puis adaptée par une relecture native de l'autre accent.
- Elle est produite **en un dialogue continu, les voix se donnant la réplique** (7.8), jamais par montage de répliques produites séparément.
- Quatre interprétations : Brit. posé, Brit. spontané, Am. posé, Am. spontané.
- Option « Donnez la réplique » : le lecteur choisit un personnage ; sa voix est remplacée par un silence calibré (durée de la réplique originale + 1,5 s), avec le texte affiché, puis la réplique originale est rejouée pour comparaison.

### 5.4 La bible des personnages

Les scènes vivantes forment un univers continu, une « série » que le lecteur suit au fil des 26 chapitres. Chaque personnage existe dans une version britannique (Londres et Manchester) et une version américaine (Chicago et Atlanta), interprétée par une voix de l'accent concerné.

| Personnage | Rôle | Version britannique | Version américaine | Chapitres phares |
|---|---|---|---|---|
| **Sarah** | Cheffe de produit, 34 ans, directe et drôle | Londonienne | Originaire de Chicago | Tous |
| **Kofi** | Designer, 36 ans, compagnon de Sarah, d'origine ghanéenne, conciliant | Londonien | Vit à Chicago | Tous |
| **Mia** | Leur fille, 9 ans, curieuse, pose mille questions | Petite Londonienne (*Mum*) | Petite Chicagoane (*Mom*) | 1, 8, 19 |
| **Grace** | Mère de Kofi, chaleureuse, formelle | Accent ghanéen (Chapitre 22.5) | Accent ghanéen | 8, 22 |
| **Tom** | Frère de Sarah, étudiant, argot de sa génération | Mancunien modéré | Atlanta | 9, 22 |
| **Priya** | Collègue de Sarah, ambitieuse | Londonienne | New-yorkaise | 13, 14 |
| **Mr Hughes / Mr Miller** | Voisin âgé, soutenu, ironique | Britannique traditionnel | Américain du Midwest | 7, 21 |
| **Daniel** | Patron de Sarah | Britannique | Américain | 13 |
| **Rôles de passage** | Serveur, médecin, chauffeur, agent… | Voix secondaires | Voix secondaires | Selon scène |

Chaque personnage possède dans `corpus/personnages.yaml` une fiche : âge, métier, tempérament, tics de langage (Tom dit *literally* à tout propos ; Mr Hughes manie l'euphémisme), voix de chaque accent, relations. Les rôles de passage reçoivent un prénom dès qu'ils ont plus de deux répliques. Aucun personnage ne porte plus de 30 % des répliques d'un chapitre, à l'exception de Sarah et Kofi au Chapitre 1.

---

## 6. Le Phrasé : le système de prononciation

### 6.1 Trois couches, une seule vérité : la voix

| Couche | Pour qui | Affichage |
|---|---|---|
| **Le phrasé** | Tous les lecteurs | Toujours visible sous l'expression ; change selon l'accent et le rythme choisis |
| **Ce que l'oreille entend** | Dès le niveau Aisance | Visible en Spontané quand la graphie orale diffère (*gonna*, *whatcha*, *dunno*) |
| **Le regard expert** | Lecteurs avancés, enseignants | Masqué par défaut ; s'ouvre d'un geste ; alphabet phonétique international + intonation |

**Règle cardinale : la transcription suit la voix.** Le phrasé est écrit à l'écoute du fichier retenu, pas avant. Si la voix a dit *gonna*, le phrasé spontané note *gonna* ; s'il ne l'a pas dit, il ne le note pas. Chaque phrasé est ainsi un portrait fidèle de la voix entendue.

### 6.2 Les clés du phrasé — consonnes

| Son | Phrasé | Exemple | Lecture pour un francophone |
|---|---|---|---|
| /p b t d k/ | p b t d k | *pick* PIK | Comme en français, mais *p, t, k* en début de syllabe forte sont **soufflés** |
| /g/ | g | *get* GÈT | **Toujours dur**, même devant *e* et *i* (jamais « gu ») |
| /f v/ | f v | *five* FAÏV | Comme en français |
| /s/ | s | *place* PLÉÏS | **Toujours sifflant**, même entre deux voyelles (jamais « ss ») |
| /z/ | z | *snooze* SNOÛZ | Comme « zèbre » |
| /θ/ | th | *think* THINK | Langue entre les dents, souffle sans voix |
| /ð/ | **dh** | *that* DHAT | Langue entre les dents, avec la voix (jamais « d » : *that* n'est pas *dat*) |
| /ʃ/ | ch | *shine* CHAÏN | Comme « chat » |
| /ʒ/ | j | *usually* YOÛ·jou·ə·li | Comme « jour » |
| /tʃ/ | tch | *watch* WOTCH | Comme « tchèque » |
| /dʒ/ | dj | *jam* DJAM | Comme « djembé » |
| /h/ | h | *hit* HIT | **Toujours soufflé**, comme pour embuer une vitre |
| /r/ | r | *right* RAÏT | Langue recourbée, ne touche rien |
| /w/ | **w** | *way* WÉÏ | « ou » très bref, glissé vers la voyelle suivante (jamais « ou- », qui se confond avec la voyelle) |
| /j/ | y | *you* YOÛ | Comme « yaourt » |
| /ŋ/ | ng | *sing* SING | Comme dans « parking », sans prononcer le *g* final |
| /l/ | l | *feel* FIIL | En fin de mot, l sombre, langue reculée |

### 6.3 Les clés du phrasé — voyelles (les deux accents)

| Mot repère | API Brit. | Phrasé Brit. | API Am. | Phrasé Am. | À retenir |
|---|---|---|---|---|---|
| *sheep* | /iː/ | **ii** (CHIIP) | /i/ | **ii** (CHIIP) | Voyelle longue : fin de la confusion *ship/sheep* |
| *ship* | /ɪ/ | **i** (CHIP) | /ɪ/ | **i** (CHIP) | Brève, relâchée, presque « é » |
| *bed* | /e/ | **è** | /ɛ/ | **è** | |
| *cat* | /æ/ | **a** | /æ/ | **a** | En américain, plus ouvert, tirant vers « è-a » |
| *cup* | /ʌ/ | **eu** (KEUP) | /ʌ/ | **eu** | Bref, au centre de la bouche |
| *car* | /ɑː/ | **â** (KÂ) | /ɑr/ | **âr** (KÂR) | Le *r* final est muet en britannique, prononcé en américain |
| *can't* | /ɑː/ | **â** (KÂNT) | /æ/ | **a** (KANT) | Différence majeure entre les accents |
| *hot* | /ɒ/ | **o** (HOT) | /ɑ/ | **â** (HÂT) | Différence majeure |
| *thought* | /ɔː/ | **ô** (THÔT) | /ɔ/ ou /ɑ/ | **ô** ou **â** | Beaucoup d'Américains confondent *cot* et *caught* |
| *book* | /ʊ/ | **ou** (BOUK) | /ʊ/ | **ou** | Bref |
| *food* | /uː/ | **oû** (FOÛD) | /u/ | **oû** | Long |
| *bird* | /ɜː/ | **eû** (BEÛD) | /ɝ/ | **eur** (BEURD) | Voyelle longue sans *r* en britannique |
| *about* (1re syll.) | /ə/ | **ə** | /ə/ | **ə** | Le son le plus fréquent de l'anglais |
| *water* (finale) | /ə/ | **ə** (WÔ·tə) | /ɚ/ | **ər** (WÂ·ɾər) | |
| *day* | /eɪ/ | **éï** | /eɪ/ | **éï** | |
| *my* | /aɪ/ | **aï** | /aɪ/ | **aï** | |
| *boy* | /ɔɪ/ | **oï** | /ɔɪ/ | **oï** | |
| *now* | /aʊ/ | **aou** | /aʊ/ | **aou** | |
| *go* | /əʊ/ | **əou** (GƏOU) | /oʊ/ | **ôou** (GÔOU) | Jamais « GO » : c'est une diphtongue dans les deux accents |
| *near* | /ɪə/ | **iə** (NIə) | /ɪr/ | **ir** (NIR) | |
| *hair* | /eə/ | **èə** (HÈə) | /ɛr/ | **èr** (HÈR) | |
| *sure* | /ʃɔː/ | **CHÔ** | /ʃʊr/ | **CHOUR** | La voyelle diffère nettement entre les accents |

**Graphies proscrites** (le vérificateur `phrase_verifier.py` les refuse) :

| Proscrit | Pourquoi | Correct |
|---|---|---|
| « D » pour /ð/ (« DAT », « DIS », « DÈR ») | Enseigne à dire *dat* | DHAT, DHIS, DHÈə (Brit.) / DHÈR (Am.) |
| « DOWN(t) » pour *don't* | Se lit comme *down* | DƏOUN(t) (Brit.) / DÔOUN(t) (Am.) |
| « SOW » pour *so* | Évoque *sow* /saʊ/ | SƏOU (Brit.) / SÔOU (Am.) |
| « NID » pour *need* | Efface la voyelle longue | NIID |
| « ou- » pour /w/ | Confusion avec la voyelle | w |
| « gu », « ss » | Orthographe française parasite | g, s |
| Une seule transcription pour deux accents | Les accents divergent | Quatre phrasés distincts |

### 6.4 Les signes de la musique de la phrase

| Signe (source) | Rendu à l'écran | Signification |
|---|---|---|
| CAPITALES | Graisse forte + couleur d'accent, en bas de casse | Syllabe accentuée (on garde les capitales dans le corpus pour la saisie ; l'écran ne « crie » pas) |
| `·` | Point médian discret | Frontière de syllabe |
| `‿` | Petite liaison arquée sous la ligne | Les mots se collent |
| `(t)` | Lettre en gris clair | Son retenu, à peine formé |
| `ʔ` | Apostrophe ’ ; info-bulle « coup de glotte » | Le *t* remplacé par un arrêt du souffle (britannique) |
| `ɾ` | Lettre « d » soulignée de pointillés ; info-bulle « t battu » | Le *t* entre voyelles devient un *d* léger (américain : *water, get up*) |
| `ʳ` | *r* en exposant | *r* de liaison britannique (*far away* → fâ ʳə·WÉÏ) |
| `↗` `↘` `↗↘` | Flèche fine en fin de phrasé | Intonation montante, descendante, montante-descendante |

### 6.5 Posé et spontané : deux phrasés distincts

| Phénomène | Posé (diction claire, naturelle) | Spontané (débit natif réel) |
|---|---|---|
| Petits mots | Formes faibles naturelles conservées (*to* → tə) | Formes faibles poussées, parfois effacées (*going to* → *gonna*) |
| Enchaînements | Présents mais lisibles | Systématiques |
| *t* américain | Battu entre voyelles quand c'est la norme (*water*) | Battu partout où c'est possible (*get it* → gè·ɾit), *t* final retenu |
| *t* britannique | Réalisé ou légèrement retenu | Coup de glotte fréquent (*get up* → gè·ʔEUP selon la voix) |
| Fusions | *did you* → di·djoû | *did you* → DI·djə |
| Élisions | Rares | Fréquentes (*I don't know* → aï·də·NƏOU / *dunno*) |
| Débit indicatif | 120 à 140 mots par minute | 170 à 220 mots par minute |

**Le posé n'est pas un ralenti.** Une voix qui détache artificiellement chaque mot (« I… am… going… to… ») produit une prise refusée. Le posé est la manière dont un natif parle à quelqu'un qu'il veut être sûr de faire comprendre : un collègue étranger, une personne âgée, une salle de réunion.

### 6.6 Exemple complet : une expression, quatre phrasés

**My alarm's going off.**

| | Posé | Spontané |
|---|---|---|
| **Britannique** — phrasé | maï ə·LÂMZ gəou·ing OF ↘ | mə·LÂMZ gəou·in‿OF ↘ |
| Britannique — expert | /maɪ əˈlɑːmz ˌɡəʊɪŋ ˈɒf/ | /məˈlɑːmz ˌɡəʊɪn ˈɒf/ |
| **Américain** — phrasé | maï ə·LÂRMZ gôou·ing ÔF ↘ | mə·LÂRMZ gôou·in‿ÔF ↘ |
| Américain — expert | /maɪ əˈlɑrmz ˌɡoʊɪŋ ˈɔf/ | /məˈlɑrmz ˌɡoʊɪn ˈɔf/ |

**Get up!** (où les accents divergent nettement en spontané)

| | Posé | Spontané |
|---|---|---|
| Britannique | gèt EUP ↘ | gè‿ʔEUP ↘ (ou gè‿TEUP selon la voix) |
| Américain | gèt EUP ↘ | gè‿ɾEUP ↘ (rendu : gè‿dEUP, *d* pointillé) |

Ces valeurs sont des **prévisions** ; la valeur définitive est celle que note le phrasé écrit à l'écoute de la prise retenue (6.1).

### 6.7 Procédure de transcription

1. La prise validée et son alignement mot à mot (section 7.9) sont chargés dans l'outil de transcription.
2. Le phrasé et la notation experte sont écrits pour cette prise précise, à partir des phonèmes alignés et de l'écoute du fichier.
3. Une contre-écoute indépendante, propre à l'accent concerné, approuve ou corrige.
4. Le vérificateur automatique contrôle la conformité des symboles (liste fermée du 6.2 au 6.4) et la présence d'au moins une syllabe accentuée.
5. Toute réécriture de la voix (nouvelle prise) invalide le phrasé correspondant, qui repasse à l'étape 2.

---

## 7. Les voix

### 7.1 Principes non négociables

1. **Aucune voix ne sonne comme une machine.** Toute voix entendue dans l'ouvrage doit être indiscernable, à l'oreille d'un natif, d'une personne qui parle vraiment : souffle, mélodie, micro-pauses, sourire dans la voix. Une voix monotone, métallique, hachée ou à l'accentuation fautive est refusée, quelle que soit son origine.
2. **Deux origines, une seule exigence.** Les voix proviennent soit d'**enregistrements existants** de locuteurs réels, publiés sous une licence qui en permet l'usage dans l'ouvrage (7.3), soit de **voix créées** pour l'ouvrage par un moteur de voix de très haute fidélité (7.5). Les deux passent les mêmes contrôles (7.10).
3. **Deux rythmes = deux interprétations distinctes.** Le spontané n'est jamais le posé accéléré après coup ; le posé n'est jamais le spontané ralenti. Chaque rythme est produit tel quel, à son débit propre. Le réglage de débit intégré au moteur est permis, car la voix naît alors à ce rythme ; tout étirement temporel (*time-stretching*) ou changement de hauteur (*pitch-shifting*) appliqué à un fichier existant est interdit.
4. **Une identité par personnage et par accent.** Le posé et le spontané d'un même énoncé, dans un même accent, sont dits par la même voix : la comparaison porte uniquement sur le rythme. Une voix garde le même timbre d'un bout à l'autre de l'ouvrage (contrôle 7.10).
5. **Chaque énoncé est joué en situation.** *Five more minutes…* se dit les yeux mi-clos, d'une voix traînante ; *Turn that thing off!* avec agacement. L'indication de jeu figure dans le script (7.8) et guide l'interprétation.
6. **Aucune imitation d'une personne réelle.** Aucune voix créée ne reproduit le timbre d'une personne identifiable. Les timbres sont conçus à partir de descriptions (âge, accent, caractère), jamais copiés sur un enregistrement de quelqu'un.
7. **Aucun montage de syllabes** issues de fichiers différents. Un énoncé est une seule coulée de voix.
8. **La transcription suit la voix.** Le phrasé est écrit à partir du fichier retenu, jamais avant (6.1).

### 7.2 Les volumes

#### Par scène (densité cible)

| Élément | Énoncés | × 4 interprétations |
|---|---|---|
| Énoncés principaux (55 expressions × 1,5 forme en moyenne) | ≈ 82 | ≈ 330 |
| Déclinaisons (55 × 5) | 275 | 1 100 |
| Répliques de la scène vivante | 14 | 56 (+ 4 fichiers continus) |
| **Total par scène** | **≈ 371** | **≈ 1 490 fichiers** |
| Voix du sens (français) | 55 sens d'expressions + 14 sens de répliques | 69 fichiers |

#### Pour l'ouvrage complet (Prélude + 163 scènes)

| Élément | Estimation |
|---|---|
| Énoncés anglais | ≈ 61 250 |
| Fichiers anglais | ≈ 245 000 |
| Fichiers de la voix du sens | ≈ 11 250 |
| Parole nette anglaise | ≈ 112 h |
| Parole nette française | ≈ 6 h |
| Poids encodé | ≈ 1,5 Go (réparti en paquets par chapitre, section 10.9) |

Hypothèses de calcul : 4,3 mots par énoncé en moyenne ; débit posé 132 mots/minute, spontané 198 mots/minute ; 0,26 s de silences par fichier (7.9) ; débit moyen d'encodage 26 kbit/s (mélange 32 et 24 kbit/s).

### 7.3 Les enregistrements existants

Des enregistrements de locuteurs réels, publiés sous licence libre, existent déjà pour un grand nombre de mots et de phrases courantes. Ils sont précieux là où l'ouvrage a besoin de **la variété des voix réelles** : paires de sons, voix du monde, voix réservées aux épreuves, chiffres et mots isolés.

| Source | Contenu | Licence | Usage dans l'ouvrage |
|---|---|---|---|
| Mozilla Common Voice (jeu anglais, jeu « Single Word Target Segment », sous-ensembles régionaux) | Phrases lues et mots isolés, avec métadonnées d'accent déclarées | CC0 1.0, domaine public (Mozilla Common Voice — <https://commonvoice.mozilla.org/en/datasets>) | Paires à seize voix (19.6), voix réservées (18.3), Voix du monde non natives (19.9), chiffres (19.4) |
| Lingua Libre et Wikimedia Commons | Mots et expressions prononcés, classés par langue et par locuteur | CC BY-SA 4.0, attribution et partage à l'identique (Lingua Libre — <https://en.wikipedia.org/wiki/Lingua_Libre>) | Mots isolés, variétés régionales, voix réservées |
| Prononciations du Wiktionnaire anglais (hébergées sur Wikimedia Commons) | Mots isolés, souvent en plusieurs accents | Licence propre à chaque fichier, vérifiée une à une | Mots isolés, paires |

**Règles d'emploi.**

1. **Licence vérifiée fichier par fichier** : seules sont admises CC0, domaine public, CC BY et CC BY-SA. Toute autre licence, ou une licence absente, exclut le fichier. La licence, l'auteur et l'adresse d'origine sont inscrits au manifeste (7.11).
2. **Texte exact** : la transcription automatique du fichier doit correspondre exactement au texte attendu (aucune différence de mot après normalisation).
3. **Accent conforme** : l'accent déclaré par le locuteur et l'accent détecté (7.10) concordent.
4. **Qualité sonore** : mêmes seuils que les voix créées (7.10). Une prise de son bruitée, réverbérée ou saturée est exclue ; aucun débruitage de plus de 6 dB n'est appliqué pour la sauver.
5. **Pas de mélange dans une même expression** : les expressions, déclinaisons et scènes vivantes gardent leurs voix attitrées (7.4). Les enregistrements existants servent aux modules où la variété est le but.
6. **Attribution** : chaque auteur d'un fichier sous CC BY ou CC BY-SA est crédité dans la page « Les voix » (7.12) ; les fichiers sous CC BY-SA restent diffusés sous cette licence.

`voix/outils/sources_libres.py` télécharge les jeux de données, filtre par licence, par accent et par texte, puis produit la liste des fichiers candidats et leurs métadonnées.

### 7.4 Les voix de l'ouvrage

#### Les huit voix principales

| Voix | Accent | Profil | Rôle |
|---|---|---|---|
| US-F1 | Américain général (*General American*) | Femme, 28–38 ans, timbre clair et chaud | Expressions et déclinaisons ; Sarah (version américaine) |
| US-F2 | Américain général | Femme, 45–60 ans, timbre posé | Expressions ; rôles soutenus |
| US-M1 | Américain général | Homme, 28–40 ans, timbre souple | Expressions ; Kofi (Am.) |
| US-M2 | Américain général | Homme, 45–65 ans, timbre grave | Expressions ; Mr Miller, Daniel (Am.) |
| UK-F1 | Britannique standard du Sud (*Standard Southern British*, héritier moderne de la *Received Pronunciation*) | Femme, 28–38 ans | Expressions ; Sarah (Brit.) |
| UK-F2 | Britannique standard du Sud | Femme, 45–60 ans | Expressions ; rôles soutenus |
| UK-M1 | Britannique standard du Sud | Homme, 28–40 ans | Expressions ; Kofi (Brit.) |
| UK-M2 | Britannique standard du Sud | Homme, 45–65 ans | Expressions ; Mr Hughes, Daniel (Brit.) |

#### Voix secondaires

| Voix | Usage |
|---|---|
| Deux voix jeunes (une par accent, 18–24 ans) | Tom ; argot des jeunes (22.3) |
| Une voix d'enfant de 8 à 10 ans par accent | Mia |
| Voix du monde : australienne, irlandaise, nigériane, ghanéenne, sud-africaine (une par variété), puis les 24 variétés de 19.9 | Chapitre 22.5, Grace, atlas des accents |
| **La voix du sens** : une voix francophone (français standard, femme, 30–45 ans, timbre chaleureux et posé) | Le sens français des expressions et des répliques, dit dans la promenade, l'écho et les retrouvailles « La réplique » |

#### La fiche vocale

Chaque voix est définie par une fiche, `voix/fiches/{voix}.yaml`, figée une fois choisie :

```yaml
id: UK-F1
accent: en-GB            # variété visée : Standard Southern British
description: >
  Perfect audio quality. Woman in her early thirties from London, standard
  southern British accent, warm and clear, friendly, natural conversational
  delivery, slight smile in the voice, close microphone, quiet room.
moteur: { nom: "<moteur retenu, 7.5>", version: "<version figée>", voix: "<identifiant de voix>" }
reglages: { stabilite: 0.45, similarite: 0.80, style: 0.30, graine: 271828 }
reference: voix/fiches/UK-F1.reference.wav   # 40 lignes, empreinte de timbre (7.10)
personnages: [sarah]
```

#### Le choix des timbres

1. Pour chaque voix, le moteur produit au moins **trois candidats** à partir de la description.
2. Chaque candidat dit le **script d'essai** (identique pour tous) : 40 lignes de l'ouvrage, chacune en posé puis en spontané, couvrant formes faibles, *t* battu ou coup de glotte, intonations de question, quatre tons (courant, complice, cru, soutenu) et une réplique de scène vivante.
3. Les candidats sont classés selon la grille 7.10 (naturel prédit, exactitude du texte, accent détecté, constance du timbre sur 40 lignes, écart entre posé et spontané). Les huit voix principales doivent en outre être **nettement distinctes** les unes des autres (similarité de timbre entre deux voix d'un même accent inférieure à 0,55).
4. Le meilleur candidat devient la voix de l'ouvrage ; ses 40 lignes forment sa **référence de timbre**.

#### Règles propres à la voix du sens

- Un seul fichier retenu par sens, dit d'un ton naturel, jamais didactique, dans le ton de l'expression (le sens d'une expression complice se dit avec un sourire).
- Le sens dit est **exactement** le texte du champ `sens` ; toute modification du texte invalide le fichier.
- La voix du sens ne prononce aucun mot anglais. Si le sens contient un mot anglais (« J'ai appuyé sur *snooze* »), il est reformulé à l'écrit (« J'ai appuyé sur répéter »).
- Mêmes exigences techniques que les voix anglaises (7.9, 7.10) ; nommage `c01s01-A1.fr.sens.opus` (7.11).

### 7.5 Le moteur des voix créées

#### Les exigences

Le moteur retenu DOIT :

1. Produire une parole jugée indiscernable d'une voix réelle (7.10) en anglais américain et britannique, et en français pour la voix du sens.
2. Permettre de **concevoir un timbre à partir d'une description** et de le réutiliser à l'identique sur des centaines de milliers d'énoncés.
3. Accepter des **indications de jeu** (émotion, intention, débit) en langage naturel ou par balises.
4. Permettre les **dialogues à plusieurs voix** en une seule génération, pour les scènes vivantes.
5. Livrer au moins 24 kHz, sans perte, ou mieux.
6. Autoriser, par sa licence ou ses conditions d'utilisation, **l'usage commercial et la redistribution des fichiers produits** dans une application publiée.
7. Être utilisable de façon programmée, avec une version figée.

#### Les candidats

Plusieurs moteurs répondent aujourd'hui à tout ou partie de ces exigences. ElevenLabs propose une conception de voix à partir d'une description, avec réglage de l'âge, de l'accent, du ton et du débit (ElevenLabs Voice Design — <https://elevenlabs.io/voice-design>). Le moteur Gemini de Google se pilote par des indications en langage naturel pour le style, l'accent, le débit et l'émotion, et produit des dialogues à plusieurs voix (Google Cloud, Gemini-TTS — <https://docs.cloud.google.com/text-to-speech/docs/gemini-tts>). Parmi les modèles à poids ouverts, la licence décide : Kokoro (Apache 2.0) et Chatterbox (MIT, sorties marquées) autorisent l'usage commercial, alors que d'autres modèles réputés, comme XTTS v2 ou F5-TTS, l'interdisent pour leurs sorties (comparatif des licences, Cartesia — <https://www.cartesia.ai/learn/open-source-tts>). Les classements à l'aveugle évoluent vite ; ils servent à présélectionner, jamais à décider (Artificial Analysis — <https://artificialanalysis.ai/embed/text-to-speech-leaderboard/leaderboard/provider-voice>).

#### L'épreuve de sélection

Le moteur n'est pas choisi sur réputation mais par une épreuve, rejouable à l'identique :

1. **Corpus d'épreuve** : 300 énoncés de l'ouvrage (dont la scène étalon complète, annexe A), dans les quatre interprétations, plus 60 sens français.
2. **Mesures** pour chaque moteur candidat : naturel prédit, exactitude du texte, accent détecté, constance du timbre, rapport de durée posé/spontané, taux d'artefacts (7.10), et **comparaison à l'aveugle** contre 200 enregistrements réels de référence de même texte ou de texte comparable (7.3).
3. **Décision** : le moteur dont les voix se distinguent le moins des enregistrements réels et qui échoue le moins aux contrôles bloquants. Les résultats sont archivés dans `docs/decisions/moteur-voix.md`.
4. **Un moteur par voix pour toute l'œuvre** : une voix ne change jamais de moteur ni de version en cours d'ouvrage. Changer de moteur impose de recréer tous les fichiers de cette voix.

#### L'interface de production

`voix/outils/creer.py` isole le moteur derrière une interface unique ; chaque moteur est un adaptateur.

```python
class Moteur(Protocol):
    nom: str
    version: str
    def creer(self, texte: str, voix: FicheVocale, jeu: Jeu, rythme: Literal["pose", "spontane"],
              graine: int) -> bytes: ...            # WAV PCM, fréquence native du moteur
    def dialoguer(self, repliques: list[Replique], rythme: str, graine: int) -> bytes: ...
```

Chaque appel est consigné (`voix/registre/creations.jsonl`) : identifiant d'énoncé, voix, moteur, version, réglages, graine, texte envoyé, indication de jeu, empreinte SHA-256 du fichier produit. Un fichier peut ainsi être recréé à l'identique ou expliqué.

### 7.6 Les règles régionales

| Cas | Exemple | Ce que l'on produit |
|---|---|---|
| **Énoncé commun** | *Wake up!* | Le même texte, dit par la voix américaine et par la voix britannique, chacune en posé et en spontané |
| **Énoncé à orthographe divergente** | *Mum / Mom*, *colour / color* | Chaque accent dit sa graphie ; l'écran affiche la graphie de l'accent sélectionné |
| **Énoncé marqué britannique** | *It's half six.* | Voix britannique : l'énoncé tel quel (posé + spontané). Voix américaine : **l'équivalent naturel américain** (*It's six-thirty.*), signalé à l'écran : « En Amérique, on dira plutôt : » |
| **Énoncé marqué américain** | *Shut that thing off!* | Symétrique du cas précédent |
| **Énoncé propre à une variété du monde** | *Arvo* (australien) | Voix de la variété concernée (2 rythmes) + équivalents américain et britannique |
| **Énoncé de ton cru** | Jurons du Chapitre 22.4 | Produits normalement ; l'écran les masque derrière un voile tant que le lecteur n'a pas choisi « Afficher le ton cru » |

**Jamais** une voix américaine n'imite un accent britannique, ni l'inverse.

### 7.7 La définition mesurable des deux rythmes

| Critère | Posé | Spontané |
|---|---|---|
| Intention de jeu | « Je parle à quelqu'un que je veux être sûr de faire comprendre, sans le traiter comme un enfant. » | « Je parle à un ami, dans la vraie vie, sans y penser. » |
| Débit | 120–140 mots/min | 170–220 mots/min |
| Rapport de durée spontané / posé (contrôle automatique) | — | entre 0,55 et 0,90 pour tout énoncé de 4 mots ou plus |
| Formes faibles | Naturelles | Naturelles et poussées |
| Contractions | Celles de l'écrit (*I'm*, *don't*) | Celles de l'oral (*gonna*, *wanna*, *gotta*, *innit* selon accent et ton) |
| Pauses | Légères aux frontières de groupe | Aucune, sauf pause de jeu |
| Fichiers refusés | Diction mot à mot, voix « de manuel », sur-articulation des petits mots | Précipitation artificielle, avalement inintelligible pour un natif |
| Énoncés d'un seul mot (*Morning!*) | Dit clairement | Dit comme dans la vie (souvent plus bref, plus mélodique) ; le rapport de durée n'est pas contrôlé |

**Le texte de jeu.** Pour le spontané, le script peut porter un champ `texte_jeu` qui écrit les réductions attendues (*I'm gonna grab a coffee*) afin que la voix les réalise ; le texte affiché reste celui du corpus (*I'm going to grab a coffee*) et le phrasé suit ce qui a été réellement dit (6.1). Le posé utilise toujours le texte du corpus.

### 7.8 Le script de production

Les scripts sont **générés automatiquement depuis le corpus** (section 10.5), en anglais pour les voix anglaises. Un fichier JSONL par voix et par lot :

| Champ | Exemple |
|---|---|
| `line_id` | `c01.s01.A4.e1` |
| `voice` | `UK-F1` |
| `text` | `Five more minutes.` |
| `play_text` | (spontané seulement, facultatif) `Five more minutes…` |
| `context` | `Said with eyes closed, from under the duvet, to a partner trying to wake you up.` |
| `emotion` | `sleepy, pleading, drawn-out` |
| `register` | `everyday` / `casual` / `slang` / `formal` |
| `pronunciation_note` | `Natural "Mum" (UK). Do not over-articulate "more".` |
| `rhythm` | `careful` ou `natural` (toujours les deux, chacun sur sa ligne) |
| `scene_partner` | (scènes vivantes uniquement) identifiant du partenaire |

Les indications `context`, `emotion` et `pronunciation_note` sont transmises au moteur comme indications de jeu ; elles ne sont jamais prononcées. Les scènes vivantes sont produites **en un seul dialogue continu** par interprétation, puis découpées réplique par réplique d'après l'alignement : les répliques s'enchaînent ainsi avec le naturel d'une vraie conversation.

### 7.9 La production et la finition

Chaîne appliquée à chaque lot (outils : `voix/outils/creer.py`, ffmpeg, `ffmpeg-normalize`, Montreal Forced Aligner, scripts du dossier `voix/outils/`) :

1. **Création de plusieurs prises** : pour chaque énoncé et chaque interprétation, quatre prises sont créées avec quatre graines différentes.
2. **Choix de la prise** : chaque prise passe les contrôles 7.10 ; la prise retenue est celle qui satisfait tous les contrôles bloquants et obtient le meilleur score de naturel. Si aucune ne passe, quatre nouvelles prises sont créées ; après trois échecs, l'énoncé est signalé pour reformulation de l'indication de jeu ou du texte de jeu.
3. **Rééchantillonnage** à 48 kHz (filtre de haute qualité `soxr`), sans aucune autre transformation du signal.
4. **Niveau** : chaque fichier est réglé sur son niveau de parole active (méthode ITU-T P.56), de sorte qu'un lot concaténé atteigne une sonie intégrée de −18 LUFS (± 1 LU) ; crête vraie −1,5 dBTP.
5. **Découpe** : 60 ms de silence en tête, 200 ms en fin ; fondu d'entrée et de sortie de 5 ms.
6. **Filtre passe-haut** à 70 Hz.
7. **Encodage**, avec inscription de l'origine dans les métadonnées :

```bash
# Expressions et scènes vivantes : 32 kbit/s
ffmpeg -hide_banner -i in.wav -af "highpass=f=70" -ac 1 -ar 48000 \
  -c:a libopus -b:a 32k -vbr on -compression_level 10 -application audio \
  -map_metadata -1 -metadata VLA_ORIGINE=creee -metadata VLA_VOIX=UK-F1 out.opus
# Déclinaisons : 24 kbit/s
ffmpeg -hide_banner -i in.wav -af "highpass=f=70" -ac 1 -ar 48000 \
  -c:a libopus -b:a 24k -vbr on -compression_level 10 -application audio \
  -map_metadata -1 -metadata VLA_ORIGINE=creee -metadata VLA_VOIX=UK-F1 out.opus
```

Pour un enregistrement existant, `VLA_ORIGINE=enregistree` et `VLA_SOURCE` porte l'adresse d'origine. Les marques d'origine éventuellement intégrées au signal par le moteur sont conservées.

8. **Alignement mot à mot** : Montreal Forced Aligner (modèles anglais américain et britannique) produit les instants de début et de fin de chaque mot. Ces instants servent au surlignage synchronisé, à l'écoute au mot (8.14) et à la réécoute depuis un mot (8.3). Tout alignement de faible confiance est recalculé avec un découpage plus fin, puis contrôlé (10.22).
9. **Syllabes** : `voix/outils/syllaber.py` regroupe les phonèmes alignés en syllabes (règle du maximum d'attaque) et marque les syllabes accentuées d'après la notation experte (6.7). Ces instants pilotent l'illumination du phrasé et le battement (8.15).
10. **La courbe** : `voix/outils/courbe.py` extrait la mélodie (fréquence fondamentale) avec Praat via `parselmouth` (pas de 10 ms, plage 75–500 Hz), la lisse, la convertit en demi-tons relatifs à la médiane de la voix et la quantifie sur un octet par point. Il s'agit d'une **mesure** de la voix, jamais d'une transformation.
11. **Empreinte** : SHA-256 de chaque fichier encodé.
12. **Inscription au manifeste** (7.11) et au registre des prises.

Les fichiers WAV retenus (48 kHz, 24 bits) sont conservés comme **masters** ; les fichiers Opus en sont toujours dérivés.

### 7.10 Le contrôle des voix

Tous les contrôles portent sur **100 % des fichiers**. Les contrôles bloquants refusent la prise ; les autres la signalent.

| Contrôle | Méthode | Seuil |
|---|---|---|
| Naturel prédit | Prédicteur de note d'écoute UTMOSv2 (VoiceMOS Challenge 2024 — <https://arxiv.org/html/2409.09305>), calibré sur 500 enregistrements réels propres de Common Voice | **Bloquant** sous le 10e centile des enregistrements réels de calibrage |
| Exactitude du texte | Transcription automatique (Whisper large-v3 ou équivalent, exécutée hors de l'application) comparée au texte attendu, avec la liste d'équivalences des réductions (*gonna* = *going to*) | **Bloquant** : aucune différence de mot |
| Accent | Classifieur d'accent anglais (modèle ECAPA « CommonAccent » de SpeechBrain) | **Bloquant** si la probabilité de l'accent visé est inférieure à 0,80 |
| Constance du timbre | Similarité d'empreinte vocale (ECAPA-TDNN) avec la référence de la voix | **Bloquant** sous 0,75 |
| Mélodie vivante | Écart type de la courbe en demi-tons, pour tout énoncé de 4 mots ou plus | **Bloquant** sous 1,5 demi-ton (voix plate) |
| Rythme | Rapport spontané / posé (7.7) ; débit en mots par minute | **Bloquant** hors bornes |
| Artefacts | Détection de clics, de coupures, de répétitions de syllabes, de souffle métallique (énergie spectrale anormale au-dessus de 8 kHz), de silence interne de plus de 700 ms non prévu | **Bloquant** |
| Écrêtage | Crête vraie | **Bloquant** au-delà de −1,0 dBTP |
| Silences | Tête 40–120 ms, fin 150–300 ms | **Bloquant** hors bornes |
| Sonie du lot | Lot concaténé | **Bloquant** au-delà de ±1 LU de −18 LUFS |
| Complétude | Chaque énoncé du corpus possède ses 4 fichiers, chaque fichier son alignement | **Bloquant** |
| Écoute comparative | Échantillon de 5 % de chaque lot comparé à l'aveugle avec des enregistrements réels de même longueur | Signalement si l'échantillon est reconnu comme non réel plus souvent qu'au hasard ; le lot entier est alors réexaminé |

Un second contrôle, du point de vue de l'apprenant, porte sur 10 % des fichiers tirés au hasard : la transcription automatique du **spontané** doit retrouver le texte ; sinon l'énoncé est jugé trop avalé pour un apprenant et recréé.

### 7.11 Le nommage et le manifeste

**Arborescence des fichiers encodés**

```
voix/
└── c01/                                  # chapitre
    └── s01/                              # scène
        ├── manifeste.json
        ├── c01s01-A1-e1.uk.pose.opus
        ├── c01s01-A1-e1.uk.spontane.opus
        ├── c01s01-A1-e1.us.pose.opus
        ├── c01s01-A1-e1.us.spontane.opus
        ├── c01s01-A1-d1.uk.pose.opus
        ├── …
        └── c01s01-sv-l01.uk.pose.opus    # scène vivante, réplique 1
```

Règle : l'identifiant de corpus `c01.s01.A1.e1` devient le nom `c01s01-A1-e1` (points de chapitre et de scène retirés, autres points remplacés par des tirets), suivi de `.{uk|us}.{pose|spontane}.opus`. La voix du sens d'une expression `c01.s01.A1` se nomme `c01s01-A1.fr.sens.opus` ; celle d'une réplique `c01s01-sv-l01.fr.sens.opus`. Pour les syllabes, le troisième nombre vaut 1 si la syllabe est accentuée. Les scènes vivantes sont aussi livrées en un fichier continu par interprétation : `c01s01-sv.uk.spontane.opus`, accompagné des instants de début de chaque réplique.

**Manifeste par scène** (`manifeste.json`)

```json
{
  "scene": "c01.s01",
  "version": 3,
  "genere_le": "AAAA-MM-JJTHH:MM:SSZ",
  "voix": {
    "c01.s01.A1.e1": {
      "uk": {
        "pose":     { "f": "c01s01-A1-e1.uk.pose.opus", "d": 1.62, "sha256": "9f2c…", "voix": "UK-F1", "origine": "creee",
                      "mots": [["My", 0.06, 0.24], ["alarm's", 0.24, 0.81], ["going", 0.81, 1.12], ["off", 1.12, 1.42]],
                      "syllabes": [[0.06, 0.24, 0], [0.24, 0.33, 0], [0.33, 0.81, 1], [0.81, 1.00, 0], [1.00, 1.12, 0], [1.12, 1.42, 1]],
                      "courbe": "base64:AAECBAYIBwUDAQ…" },
        "spontane": { "f": "c01s01-A1-e1.uk.spontane.opus", "d": 1.08, "sha256": "41aa…", "voix": "UK-F1", "origine": "creee",
                      "mots": [["My", 0.06, 0.15], ["alarm's", 0.15, 0.55], ["going", 0.55, 0.76], ["off", 0.76, 0.90]] }
      },
      "us": { "pose": { "…": "…" }, "spontane": { "…": "…" } }
    }
  },
  "sens": {
    "c01.s01.A1": { "f": "c01s01-A1.fr.sens.opus", "d": 1.21, "sha256": "c07e…", "voix": "FR-F1", "origine": "creee" }
  },
  "continus": {
    "uk.spontane": { "f": "c01s01-sv.uk.spontane.opus", "d": 38.4, "repliques": [0.06, 1.92, 3.40] }
  }
}
```

Pour un enregistrement existant, l'entrée porte en plus `"source": { "url": "…", "auteur": "…", "licence": "CC BY-SA 4.0" }`.

### 7.12 Licences, crédits et transparence

1. **Moteur** : la licence ou les conditions d'utilisation du moteur retenu, dans leur version en vigueur au jour de la production, sont archivées dans `docs/decisions/moteur-voix.md`. Elles DOIVENT autoriser l'usage commercial et la redistribution des fichiers dans l'application.
2. **Enregistrements existants** : licence vérifiée fichier par fichier (7.3) ; tout fichier dont la licence ne peut être établie est retiré.
3. **Page « Les voix »** (dans « Lire ce livre ») : elle présente chaque voix par son prénom et son accent, puis indique avec simplicité l'origine des voix : « Les voix de cet ouvrage réunissent des enregistrements de locuteurs anglophones, généreusement partagés sous licence libre, et des voix de haute fidélité créées pour lui. » Suivent la liste des auteurs crédités et les licences.
4. **Marquage** : depuis le 2 août 2026, le règlement européen sur l'intelligence artificielle impose aux fournisseurs de systèmes qui génèrent de l'audio un marquage lisible par machine de ces contenus (Commission européenne — <https://digital-strategy.ec.europa.eu/en/factpages/quick-facts-transparency-rules-ai-systems>). L'ouvrage conserve les marques d'origine du moteur et inscrit l'origine dans les métadonnées de chaque fichier (7.9) et dans le manifeste. Aucune voix ne reproduisant une personne réelle (7.1), aucune ne relève des contenus que ce règlement appelle hypertrucages.

---

## 8. L'expérience du lecteur

### 8.1 La carte de l'ouvrage (navigation)

Barre de navigation inférieure, quatre destinations, toujours accessible au pouce :

| Icône dessinée | Destination | Contenu |
|---|---|---|
| Soleil levant | **Aujourd'hui** | Reprendre la lecture, retrouvailles du jour, expression du jour, constance |
| Livre ouvert | **Le Livre** | Sommaire : Prélude, 26 chapitres, appendices |
| Casque | **La promenade** | Écoute continue, écran éteint possible |
| Carnet à élastique | **Mon carnet** | Marque-pages, notes, ma voix, expressions familières, constance |

En haut de chaque écran principal : la loupe « Comment dit-on… ? » et l'accès aux **Préférences** (icône discrète à droite). Sur tablette et appareil pliable déplié (largeur ≥ 600 dp), la barre inférieure devient un rail latéral ; à partir de 840 dp, la lecture passe en double colonne (sommaire à gauche, scène à droite, 8.26).

### 8.2 Les écrans

#### Aujourd'hui

1. Salutation selon l'heure (« Bonjour », « Bon après-midi », « Bonsoir ») et constance (« 12 jours de constance »).
2. Carte **Reprendre** : scène, moment, chemin parcouru dans la scène ; un toucher rouvre exactement à l'expression quittée.
3. Carte **Retrouvailles** : nombre d'expressions dues, durée estimée.
4. Carte **Expression du jour** : une expression tirée des scènes déjà parcourues (ou de la prochaine scène pour un nouveau lecteur), avec ses voix.
5. Carte **Rituel du jour** : rappel du rituel de la dernière scène parcourue.
6. Carte **Le moment présent** : une scène accordée à l'heure de l'appareil (matin : 1.1 Le réveil ; midi : 10.2 Commander ; soir : 1.9 La soirée), uniquement si elle n'est pas déjà parcourue depuis moins de sept jours (8.20).
7. Carte **Itinéraire en cours**, si le lecteur en suit un : étape actuelle, expressions restantes (8.17).

L'ordre des cartes est fixe ; une carte sans objet disparaît plutôt que d'afficher un état vide.

#### Le Livre (sommaire)

- Prélude en tête, puis chapitres en cartes verticales : numéro en chiffres romains discrets, titre, nombre de scènes, chemin parcouru (fin filet qui se remplit sous le titre, sans pourcentage).
- Toucher un chapitre : liste de ses scènes avec intention en une ligne, durée d'écoute et état (« à découvrir », « en cours », « parcourue »).
- Les chapitres dont les voix ne sont pas installées portent la mention « Voix à faire venir » et la taille.
- Filtres : niveau (Fondations / Aisance / Maîtrise), accent préféré, tons.
- Après les chapitres : **Les Itinéraires** (8.17), puis **Les Appendices** (clés du phrasé, atlas des accents, lexique, tous les faux pas, tous les incontournables, les voix).

#### La scène

Structure verticale continue, une seule colonne de 60 à 70 caractères :

1. **Ouverture** : grand titre, intention, bouton « Écouter la scène d'abord » (scène vivante en spontané, sans texte).
2. **Le pupitre des voix**, épinglé en haut pendant le défilement : bascules Am./Brit. et Posé/Spontané, bouton « Les quatre voix », bouton de lecture continue de la scène.
3. **Les moments** : intertitre « Moment A — Le réveil sonne », puis les cartes d'expression.
4. **L'Essentiel**, **La scène vivante**, **Le rituel**.
5. **Fin de scène** : « Scène parcourue », proposition de la scène suivante, ajout automatique aux retrouvailles.

Index latéral rapide : glisser le pouce le long du bord droit fait défiler les lettres des moments (A … L).

#### La carte d'expression

```
┌────────────────────────────────────────────────────────────┐
│ Moment A · 3 sur 7                         Ton courant  ⌑  │  ⌑ = marque-page
│                                                            │
│ I hit snooze (three times).                      ◉        │  ◉ = écouter
│ aï HIT SNOÛZ (THRII TAÏMZ) ↘                               │
│ Brit. · Posé                    [Am.|Brit.]  [Posé|Spontané]│
│                                                            │
│ J'ai appuyé sur « répéter » (trois fois).                  │
│ Mot à mot : j'ai frappé « snooze ».                         │
│                                                            │
│ L'usage ⌄                                                  │
│ Sur le même air ⌄  — I hit [bouton]        5 déclinaisons  │
│ Regard expert ⌄                                            │
└────────────────────────────────────────────────────────────┘
```

« L'usage » est ouvert par défaut au niveau Fondations, replié aux niveaux supérieurs (préférence modifiable). « Sur le même air » est replié par défaut sur téléphone, ouvert sur tablette.

### 8.3 Le déclenchement des voix (table de référence)

| Geste | Résultat |
|---|---|
| Toucher l'énoncé anglais ou ◉ | Lecture de l'énoncé dans l'accent et le rythme du pupitre |
| Toucher ◉ pendant la lecture | Arrêt (fondu de 30 ms) |
| Toucher l'énoncé pendant la lecture | Reprise immédiate depuis le début (geste naturel de « encore une fois ») |
| Toucher la bascule Am./Brit. de la carte | Bascule l'accent **pour cette carte** et joue aussitôt |
| Toucher la bascule Posé/Spontané de la carte | Bascule le rythme pour cette carte et joue aussitôt |
| Maintenir la bascule de la carte | Applique ce choix à tout le pupitre (toute la scène) |
| « Les quatre voix » | Joue successivement les quatre interprétations, 600 ms d'intervalle, dans l'ordre : accent préféré posé, accent préféré spontané, autre accent posé, autre accent spontané ; chaque interprétation s'affiche avec son phrasé |
| Pendant la lecture | Les mots s'illuminent en synchronie (instants d'alignement) ; le phrasé correspondant s'illumine syllabe par syllabe |
| Toucher un mot après la lecture | **L'écoute au mot** : ce mot seul, extrait du fichier de la phrase (8.14) |
| Maintenir un mot | Réécoute de la phrase depuis ce mot jusqu'à la fin |
| Toucher le phrasé | Ouvre « Les clés du phrasé » au signe touché, avec son exemple sonore du Prélude |
| Toucher « Le sens » | La voix du sens dit le sens en français (7.4) |
| Maintenir l'énoncé | Ouvre le volet : l'écho (8.16), comparer les accents côte à côte, ouvrir le miroir, ma version (8.19), ajouter au carnet, partager (8.23), copier le texte, signaler une coquille |
| Toucher une déclinaison | Lecture dans la configuration du pupitre |
| Bouton de lecture continue de la scène | Enchaîne toutes les expressions et leurs déclinaisons de la scène (voir 8.4) |
| Touche multimédia du casque ou de la montre | Lecture / pause / suivant / précédent pendant la promenade |
| Débranchement du casque ou perte de la connexion Bluetooth | Pause immédiate |
| Appel entrant, autre application audio | Pause ; reprise proposée, jamais automatique |
| Volume du téléphone à zéro | Message discret : « Le son de votre téléphone est coupé. » |
| Volume du téléphone sous 15 % | Message discret, une fois par session : « Le son de votre téléphone est très bas. » |
| Rotation, pliage ou changement de taille de fenêtre pendant la lecture | La lecture continue sans coupure ; la carte reste à l'écran |

**Règles techniques associées** : une seule voix à la fois (la promenade se met en pause dès qu'une voix de page est touchée, et inversement) ; toute nouvelle lecture interrompt la précédente par un fondu de 30 ms ; latence entre le toucher et le premier son ≤ 120 ms pour un énoncé déjà préparé (objectif 60 ms) ; préparation anticipée des voix des cartes visibles et des six suivantes.

### 8.4 La promenade (écoute continue)

Écoute mains libres, écran éteint, pour les transports, la marche, la cuisine.

| Programme | Déroulé |
|---|---|
| **Une scène** | Pour chaque expression : posé (accent préféré) → 1,5 s → voix du sens → 1,5 s → spontané → 3 s (temps pour répéter) → déclinaisons en posé. Puis la scène vivante en spontané. |
| **Un itinéraire** | Les expressions de l'étape en cours d'un itinéraire (8.17), dans le même déroulé |
| **Mes marque-pages** | Les expressions et répliques marquées, dans l'ordre du carnet |
| **Les incontournables** | Les dix incontournables de chaque scène parcourue, enchaînés |
| **Retrouvailles à l'oreille** | Les expressions dues aujourd'hui, en écoute seule |
| **Deux Anglais** | Pour chaque expression : posé américain → posé britannique → spontané américain → spontané britannique |
| **L'ombre** | Pour chaque énoncé : voix → silence égal à la durée de l'énoncé + 1 s, pour répéter en même temps ou juste après (technique de l'ombre, *shadowing*) |

Contrôles sur l'écran verrouillé et dans la zone de notification : lecture/pause, précédent, suivant, titre de l'expression en cours, sens en sous-titre. Minuteur de fin (10, 20, 30, 45 minutes, fin de scène), avec baisse progressive du volume sur les 20 dernières secondes, réalisée par le lecteur natif (le son des voix n'est jamais modifié, seul le volume général décroît). Réglage des silences (court, normal, long). Voix du sens activable ou non (activée par défaut aux niveaux Fondations et Aisance). Reprise exacte : relancer la promenade la reprend à l'expression interrompue.

La promenade fonctionne avec les commandes Bluetooth des casques, des montres et des systèmes audio de voiture (session média Android standard).

### 8.5 Le miroir (s'enregistrer et se comparer)

1. Le lecteur maintient un énoncé → « Le miroir ».
2. La voix du livre est jouée (rythme du pupitre).
3. Le lecteur touche le grand cercle et parle ; l'enregistrement s'arrête au relâchement ou après 1,5 s de silence.
4. L'écran affiche **deux courbes superposées** : l'onde et la mélodie (hauteur de la voix) de la voix du livre, puis celles du lecteur, alignées sur leur début.
5. Boutons : « Écouter la voix », « M'écouter », « Écouter les deux à la suite », « Recommencer », « Garder dans Ma voix ».
6. Le lecteur évalue lui-même : « Très proche », « Presque », « À retravailler ». Cette auto-évaluation alimente les retrouvailles.

Aucune note, aucun jugement automatique de la prononciation : la comparaison est sensorielle, la décision appartient au lecteur. Les enregistrements restent dans le stockage privé de l'application ; ils ne sont jamais transmis.

### 8.6 Les retrouvailles (mémorisation espacée)

- **Moteur** : algorithme FSRS (Free Spaced Repetition Scheduler), bibliothèque libre `ts-fsrs`, rétention cible 90 % (réglable de 80 à 95 %), paramètres par défaut de la bibliothèque. Correspondance des réponses : « Je l'avais » / « Très proche » → *Good* ; « À moitié » / « Presque » → *Hard* ; « Pas encore » / « À retravailler » → *Again* ; « Juste » → *Good* ; « Pas tout à fait » → *Again* ; une réponse juste donnée en moins de 3 s sur L'oreille → *Easy*.
- **Ce qui entre dans les retrouvailles** : chaque expression d'une scène parcourue (la forme principale), plus toute déclinaison marquée par le lecteur.
- **Limite quotidienne** : 20 nouvelles expressions et 120 retrouvailles par jour par défaut (réglables) ; durée estimée affichée.
- **Session** : 5 à 15 minutes, interruptible à tout moment sans perte.
- **Retour après absence** : si plus de 60 retrouvailles sont dues après une absence, l'ouvrage propose de les étaler sur plusieurs jours (« Reprenons doucement : 25 aujourd'hui, le reste dans les jours qui viennent. »), sans rien effacer.
- **Fuseaux et voyages** : la journée de pratique bascule à 4 h du matin heure locale ; un changement de fuseau ne fait ni perdre ni doubler un jour de constance.

### 8.7 Les formes de retrouvailles

| Nom | Ce qui se passe | Ce que le lecteur indique |
|---|---|---|
| **L'oreille** | Une voix (souvent spontanée) dit l'énoncé, sans texte. Le lecteur se demande ce qu'il a compris, puis révèle texte et sens. | « Je l'avais », « À moitié », « Pas encore » |
| **La réplique** | Le sens français s'affiche (« Il est quelle heure ? »). Le lecteur le dit à voix haute en anglais, puis révèle et écoute. | Même échelle |
| **Le miroir** | L'énoncé est joué ; le lecteur le répète et se compare (8.5). | « Très proche », « Presque », « À retravailler » |
| **Deux Anglais** | Une voix est jouée ; le lecteur devine si elle est américaine ou britannique, puis découvre la réponse et l'indice (« Le *r* de *car* est prononcé »). | « Juste » / « Pas tout à fait » |
| **Le ton juste** | Trois énoncés pour une même intention ; le lecteur choisit celui qui convient à une situation (« à votre patron »). | « Juste » / « Pas tout à fait », avec explication |
| **Le faux pas** | Une phrase calquée sur le français (*I made a dream*) ; le lecteur trouve la forme naturelle avant de révéler. | Même échelle |
| **Sur le même air** | Un gabarit et une situation (« [X] is going off » + « votre téléphone sonne pendant la réunion ») ; le lecteur crée sa phrase à voix haute, puis entend une proposition. | Auto-évaluation |
| **L'oreille fine** | Une voix spontanée dit l'énoncé ; le lecteur écrit ce qu'il a entendu (8.18). | Comparaison mot à mot, puis auto-évaluation |

Les formes alternent automatiquement (entrelacement), jamais deux fois la même forme sur la même expression d'affilée ; « Deux Anglais », « Le ton juste » et « L'oreille fine » n'apparaissent qu'à partir du niveau Aisance. Le lecteur peut écarter une forme dans les Préférences (par exemple le miroir dans les transports : « Retrouvailles silencieuses », qui ne propose que les formes sans parole).

### 8.8 Mon carnet

- **Marque-pages** : expressions, déclinaisons, répliques ; classement par scène ou par date ; notes personnelles (texte libre).
- **Ma voix** : les enregistrements gardés via le miroir, réécoutables à côté de la voix du livre.
- **Expressions familières** : celles que les retrouvailles jugent stabilisées (stabilité FSRS > 30 jours).
- **Constance** : calendrier des jours de pratique (une pratique = au moins une scène lue ou une session de retrouvailles) ; aucune pénalité, un « jour de grâce » par semaine.
- **Ma version** : les phrases que le lecteur a composées sur un gabarit, avec sa propre voix (8.19).
- **Le regard en arrière** : le bilan du mois (8.21).
- **Mettre mon carnet à l'abri** : export d'un fichier de sauvegarde (`.vivre`), partage par la feuille de partage d'Android ; import du même fichier.
- **Partager ma liste** : export des marque-pages en tableau (CSV : anglais britannique, anglais américain, sens, scène), pour un enseignant ou un groupe.

### 8.9 Comment dit-on… ? (recherche)

- Recherche instantanée, hors connexion, dans les énoncés anglais, les sens français, les déclinaisons, les usages et les titres.
- Insensible aux accents et à la casse ; tolérance aux fautes de frappe (distance d'édition 1 pour les mots de 5 lettres ou plus) ; recherche par préfixe.
- Les résultats montrent l'énoncé, son sens, « Trouvé dans Scène 1.1, Moment A », et un ◉ pour écouter sans ouvrir la scène.
- Suggestions à vide : les recherches récentes et dix situations fréquentes (« s'excuser d'un retard », « refuser poliment »…).
- Recherche par fonction : taper « refuser », « adoucir », « féliciter » propose aussi le parcours fonctionnel correspondant (4.6).
- Recherche par son : taper un signe du phrasé (« ʔ », « dh ») ou le nom d'un phénomène (« coup de glotte ») renvoie aux clés du phrasé et à des exemples entendus.

### 8.10 Les Préférences

| Groupe | Réglages |
|---|---|
| Les voix | Accent préféré (Américain / Britannique) ; rythme d'entrée (Posé / Spontané) ; « Les quatre voix » : ordre ; voix du sens (oui / non) ; silences de la promenade ; nombre de passages de l'écho (2 à 5) ; voix des chapitres installées (taille par chapitre, faire venir, retirer, vérifier) |
| La lecture | Taille du texte (7 crans, 16 à 26 px de base) ; interligne (3 crans) ; thème (Papier, Ambre, Nuit, Contraste, Automatique) ; police d'aide à la lecture (Atkinson Hyperlegible) ; afficher le regard expert par défaut ; afficher la courbe ; afficher le ton cru ; le battement (oui / non) |
| Le parcours | Niveau de départ ; nouvelles expressions par jour ; retrouvailles maximum par jour ; mémorisation visée (80 à 95 %) ; formes de retrouvailles écartées ; retrouvailles silencieuses ; le moment présent (oui / non) |
| Les rendez-vous | Heure du rendez-vous quotidien ; jours ; activer / désactiver |
| Le miroir | Accès au micro ; effacer toutes mes voix |
| Mon carnet | Mettre à l'abri ; restaurer ; tout effacer (double confirmation) |
| L'écran d'accueil | Expression du jour : accent, rythme, tirée des scènes parcourues ou de tout l'ouvrage |
| Lire ce livre | Les gestes, les clés du phrasé, la promenade, les retrouvailles expliqués en courtes pages sonores (8.24) |
| À propos | Les voix (présentation, origine et crédits, 7.12), mentions légales, politique de confidentialité, édition de l'ouvrage |

### 8.11 L'accueil (premier lancement)

Quatre écrans, moins de 60 secondes, tous passables :

1. « Bienvenue. Ce livre se lit avec les oreilles autant qu'avec les yeux. » — une phrase est jouée en quatre voix pour démontrer la promesse.
2. « Quelle voix souhaitez-vous entendre en premier ? » — deux grandes cartes, chacune joue *Good morning. Did you sleep well?* dans son accent.
3. « Où en êtes-vous en anglais ? » — Je commence / Je me débrouille / Je suis à l'aise (règle le niveau de départ, le rythme d'entrée et l'ouverture de « L'usage »).
4. « Un rendez-vous quotidien ? » — choix d'une heure ou « Pas maintenant ». La permission de notification d'Android n'est demandée qu'à ce moment, et uniquement si le lecteur choisit une heure.

Puis ouverture directe du Prélude (nouveau lecteur) ou du Chapitre 1 (lecteur « à l'aise »).

### 8.12 Hors connexion et voix à faire venir

- Le texte intégral de l'ouvrage, la recherche, le carnet et les retrouvailles sont **toujours** disponibles hors connexion.
- Les voix du Prélude et des Chapitres 1 et 2 sont installées avec l'application.
- Les voix des autres chapitres sont proposées au moment où le lecteur ouvre le chapitre, ou en bloc depuis les Préférences. Sur réseau mobile, au-delà de 50 Mo, une confirmation est toujours demandée.
- Une scène dont les voix ne sont pas installées reste lisible ; les ◉ sont remplacés par un petit nuage « voix à faire venir ».
- **Faire venir en avance** : depuis un itinéraire ou un chapitre, « Faire venir les voix des trois prochains chapitres » prépare un voyage sans réseau.
- **Vérifier** : les voix installées sont vérifiées par empreinte une fois par mois et à la demande ; une voix abîmée est remise en état automatiquement dès que le réseau le permet (« Quelques voix du chapitre 7 étaient abîmées. Elles ont été remises en état. »).
- **Place disponible** : avant de faire venir un chapitre, l'ouvrage vérifie l'espace libre (taille du chapitre + 20 %) et propose, s'il manque, de retirer les voix des chapitres parcourus depuis le plus longtemps.

### 8.13 Les rendez-vous (notifications)

- Un seul rendez-vous par jour au maximum, à l'heure choisie.
- Texte variable et humain, jamais culpabilisant (voir 3.5).
- Aucun rendez-vous les jours où le lecteur a déjà pratiqué.
- Les rendez-vous sont planifiés en mode non exact (tolérance de quelques minutes), ce qui évite toute permission d'alarme exacte ; ils sont reprogrammés au redémarrage du téléphone.
- Toucher le rendez-vous ouvre directement les retrouvailles du jour.

### 8.14 L'écoute au mot

Toucher un mot après la lecture fait entendre **ce mot seul, tel que la voix l'a dit dans la phrase**. Aucun mot n'est produit à part : l'ouvrage lit le même fichier entre les instants du mot donnés par l'alignement (7.9, champ `mots` du manifeste), avec un fondu de 15 ms à l'entrée et à la sortie pour éviter tout claquement.

- Si le mot dure moins de 180 ms (mots grammaticaux : *a*, *to*, *the*), l'ouvrage fait entendre le groupe de souffle qui le contient, signalé par un léger soulignement : un mot faible n'existe pas seul à l'oreille, et c'est précisément ce que le lecteur doit apprendre.
- En spontané, les mots liés (*gonna*, *wanna*) sont alignés comme un seul segment.
- Le mot touché reste surligné pendant son écoute ; TalkBack annonce « Écoute du mot *going* ».

### 8.15 La courbe et le battement

**La courbe** : sous le phrasé, un fin tracé montre la mélodie réelle de la voix (7.9, étape 8) ; il se dessine en même temps que la voix pendant la lecture. Le lecteur voit que *Could you possibly…* monte, que *I'm afraid not* descend. Masquée par défaut au niveau Fondations, affichée à partir du niveau Aisance (réglable).

**Le battement** : pendant la lecture, une vibration très brève (10 ms, amplitude faible) marque chaque syllabe accentuée, à l'instant exact donné par le champ `syllabes` du manifeste. Le rythme de l'anglais se sent dans la main, ce qui aide particulièrement les lecteurs dont l'oreille est fatiguée ou malentendants. Désactivé par défaut, activable dans « La lecture » ; sans effet si le téléphone n'a pas de moteur haptique réglable (repli silencieux).

### 8.16 L'écho

Mode d'imitation guidée, depuis le volet d'une expression : la voix dit l'énoncé, puis un silence égal à 1,3 × la durée de l'énoncé laisse au lecteur le temps de le redire, et ainsi de suite, **2 à 5 passages** (réglable). Enchaînement conseillé : deux passages en posé, puis deux en spontané. Un fin filet indique la plage de silence réservée au lecteur. L'écho n'enregistre rien ; il prépare le miroir.

### 8.17 Les itinéraires

Un itinéraire est un chemin transversal à travers l'ouvrage, pensé pour une échéance réelle du lecteur. Chaque itinéraire comporte 4 à 8 étapes ; chaque étape réunit 12 à 25 expressions issues de scènes différentes, dans un ordre pédagogique.

| Itinéraire | Pour qui, pour quoi | Étapes |
|---|---|---|
| Premier voyage | Aéroport, hôtel, transports, restaurant, imprévus | 6 |
| Premier jour au bureau | Se présenter, comprendre les usages, la réunion, le café | 6 |
| L'entretien d'embauche | Se présenter, parler de son parcours, négocier, remercier | 5 |
| La colocation | Visiter, partager les tâches, régler un différend | 5 |
| Le téléphone | Appeler, être appelé, laisser un message, comprendre au bout du fil | 4 |
| La belle-famille | Être reçu, complimenter, éviter les impairs, remercier | 5 |
| Les études | Inscription, cours, échanges avec les enseignants, vie du campus | 6 |
| Le soin | Pharmacie, médecin, urgences, expliquer une douleur | 5 |
| Les démarches | Banque, administration, logement, réclamations | 6 |
| Recevoir chez soi | Inviter, accueillir, servir, raccompagner | 4 |
| Les mots du cœur | Rencontre, sentiments, désaccords, réconciliations | 6 |
| Le parler juste | Les 1 630 incontournables, répartis en 8 étapes de fréquence décroissante | 8 |

- Source : `corpus/itineraires.yaml` (annexe C.9) ; chaque étape ne référence que des identifiants d'expressions existants, vérifiés à la compilation.
- Un itinéraire peut être suivi en parallèle du parcours principal ; ses expressions rejoignent les mêmes retrouvailles (aucun doublon).
- À l'ouverture d'un itinéraire, l'ouvrage propose de faire venir les voix nécessaires (8.12).

### 8.18 L'oreille fine

La forme de retrouvailles la plus exigeante, réservée aux niveaux Aisance et Maîtrise. Une voix spontanée dit l'énoncé (deux réécoutes permises, sans possibilité de passer en posé) ; le lecteur écrit ce qu'il a entendu. La comparaison est faite mot à mot, sans tenir compte des majuscules ni de la ponctuation, en acceptant les contractions équivalentes (*going to* = *gonna*, *I am* = *I'm*). L'ouvrage affiche alors le texte exact, les mots manqués soulignés en pointillé ; toucher un mot manqué déclenche l'écoute au mot (8.14). Aucune note : le lecteur s'évalue (« Je l'avais », « Presque », « Pas encore »).

### 8.19 Ma version

Depuis un gabarit (« Sur le même air », 5.2), le lecteur peut écrire **sa propre phrase** (« My phone's going off »), puis l'enregistrer avec sa voix et la réécouter à côté de la voix du livre sur l'énoncé d'origine. Ses versions sont rangées dans « Mon carnet → Ma version », avec l'expression d'origine. Elles restent sur l'appareil, sont incluses dans la sauvegarde `.vivre` (texte toujours, voix seulement si le lecteur le choisit) et ne sont jamais corrigées automatiquement : l'ouvrage invite simplement à comparer.

### 8.20 Le moment présent

L'ouvrage connaît le moment de la journée (heure de l'appareil, rien d'autre). Une table `corpus/moments.yaml` associe des scènes à six moments (petit matin, matinée, midi, après-midi, soirée, nuit) et au week-end. La carte « Le moment présent » d'Aujourd'hui propose une scène accordée, jamais deux fois la même dans la semaine. Aucune localisation, aucun agenda n'est consulté. Désactivable.

### 8.21 Le regard en arrière

Le premier jour de chaque mois, Mon carnet propose une page sobre : expressions découvertes, expressions désormais solides (stabilité FSRS ≥ 30 jours), minutes d'écoute, scènes terminées, la réplique la plus écoutée, le faux pas le plus souvent retravaillé. Une phrase de l'éditeur conclut, sans superlatif. Calculé localement ; rien n'est transmis.

### 8.22 L'expression du jour sur l'écran d'accueil

Un widget Android (deux tailles : 4 × 1 et 4 × 2) affiche une expression : énoncé anglais, sens, accent. Toucher l'énoncé ouvre l'ouvrage sur la carte et lance la voix (lien profond `vivrelanglais://expression/c01.s01.A1?ecouter=1`) ; toucher ailleurs ouvre la scène. L'expression change chaque jour à 4 h, tirée des scènes parcourues (par défaut) ou de tout l'ouvrage. Le widget suit le thème du système et le jeu de couleurs dynamique de l'appareil pour son fond, l'encre restant celle du thème (contraste vérifié). Implémentation en section 10.20.

Raccourcis d'application (appui long sur l'icône) : **Reprendre la lecture**, **Les retrouvailles du jour**, **La promenade**, **Comment dit-on… ?**

### 8.23 Partager une expression

Depuis le volet : « Partager » produit une carte image (1080 × 1350 px, typographie de l'ouvrage, énoncé, sens, phrasé, mention « Vivre l'Anglais ») et un lien `https://vivrelanglais.com/e/c01.s01.A1`. Sur un téléphone où l'ouvrage est installé, ce lien l'ouvre directement sur l'expression (liens d'application vérifiés, 10.20) ; sinon, il mène à une page qui présente l'expression et l'ouvrage. Aucun fichier sonore n'est partagé (licences des voix, 7.12).

### 8.24 Lire ce livre

Une courte section, accessible depuis les Préférences et proposée une fois après le Prélude : six pages (les gestes, le pupitre, le phrasé, la promenade, les retrouvailles, le miroir), chacune avec une démonstration sonore réelle et un exemple à toucher. Chaque page se lit en moins d'une minute. Lors de la première rencontre d'un élément (premier regard expert, premier faux pas), une seule bulle discrète explique le geste ; elle ne réapparaît jamais.

### 8.25 Signaler une coquille

Depuis le volet de toute expression ou réplique : « Signaler une coquille » ouvre un court formulaire (nature : texte, sens, phrasé, voix ; commentaire libre). Le signalement est préparé comme un courriel vers l'éditeur via la feuille de partage d'Android, avec l'identifiant de l'énoncé, l'édition de l'ouvrage et, si le lecteur l'accepte explicitement, le **journal des contretemps** local (les 200 dernières erreurs techniques, sans aucune donnée personnelle, 10.18). Rien n'est envoyé sans l'action du lecteur.

### 8.26 Les grands écrans et les appareils pliables

- Tablette et téléphone déplié (largeur ≥ 840 dp) : deux colonnes ; à gauche la carte de l'ouvrage ou la liste des expressions, à droite la scène ; la scène vivante passe en bloc bilingue côte à côte.
- Largeur 600–839 dp : une colonne élargie (marges de 48 dp), pupitre en bas.
- Orientation libre ; la lecture en cours, la position et le volet ouvert survivent à la rotation et au pliage.
- Mode multifenêtre pris en charge ; la promenade continue quand l'ouvrage n'est plus au premier plan.

---

## 9. Le design system « Encre & Voix »

### 9.1 Principes

1. **Le livre avant l'interface** : de grandes marges, une colonne de lecture, une typographie de qualité, peu de chrome.
2. **La voix se voit** : les éléments sonores (◉, pupitre, phrasé) ont une couleur propre à l'accent, constante dans tout l'ouvrage.
3. **Calme** : pas de rouge d'alerte, pas de confettis, pas de badges. La seule animation spectaculaire est l'encre qui s'écrit.
4. **Une main** : toutes les commandes fréquentes dans le tiers inférieur de l'écran.

### 9.2 Couleurs (jetons de design)

| Jeton | Papier (clair) | Ambre (sépia) | Nuit (sombre) | Contraste | Usage |
|---|---|---|---|---|---|
| `--fond` | `#FBF8F3` | `#F3E9D7` | `#121314` | `#FFFFFF` | Fond de page |
| `--surface` | `#FFFFFF` | `#FAF3E6` | `#1B1D1F` | `#FFFFFF` | Cartes |
| `--encre` | `#1C1B1A` | `#2A2118` | `#ECE8E1` | `#000000` | Texte principal |
| `--encre-douce` | `#5E5A55` | `#5A4B3A` | `#A9A49C` | `#262626` | Texte secondaire |
| `--filet` | `#E6E0D6` | `#E2D4BC` | `#2C2F33` | `#000000` | Séparateurs (2 px en Contraste) |
| `--accent` | `#1F3A5F` | `#3B2F6B` | `#A9C1E6` | `#002A66` | Liens, focus |
| `--voix-am` | `#2B5C8A` | `#2A5580` | `#8DB6E0` | `#003B73` | Tout ce qui est américain |
| `--voix-brit` | `#2E5E4E` | `#2D5A49` | `#8CC7AE` | `#004030` | Tout ce qui est britannique |
| `--ton-courant` | `#55705A` | `#4C6651` | `#9CC2A2` | `#1F4D26` | Étiquette |
| `--ton-complice` | `#8A6420` | `#82601F` | `#E0B871` | `#5C3D00` | Étiquette |
| `--ton-cru` | `#8C2F39` | `#86303A` | `#E8939C` | `#6B0F1A` | Étiquette |
| `--ton-soutenu` | `#3F4E6B` | `#3F4E6B` | `#A7B6D6` | `#22304D` | Étiquette |

Contrastes minimaux mesurés (texte le plus faible sur le fond le moins favorable du thème) : Papier 5,05:1 ; Ambre 4,79:1 ; Nuit 6,82:1 ; Contraste 9,78:1. Chaque couleur de texte DOIT atteindre un contraste ≥ 4,5:1 sur `--fond` et `--surface` de son thème, et ≥ 7:1 dans le thème Contraste (vérification automatique en section 11). Le thème Contraste est proposé automatiquement si le réglage système « Texte à contraste élevé » est actif. Le thème Automatique suit le mode clair ou sombre du système (Papier ou Nuit). Aucune information n'est portée par la couleur seule : les tons ont toujours leur mot (« Ton complice »), les accents leur abréviation (« Am. », « Brit. »).

### 9.3 Typographie

| Rôle | Police (licence libre SIL OFL) | Taille de base | Graisse |
|---|---|---|---|
| Texte français d'accompagnement | **Literata** | 18 px (réglable 16–26) | 400 ; 600 pour intertitres |
| Énoncé anglais | **Literata** | 1,22 × base | 600 |
| Phrasé | **Inter** (avec glyphes ə, ʔ, ɾ vérifiés ; repli Charis SIL) | 0,94 × base | 400, syllabe forte 700 |
| Regard expert (alphabet phonétique) | **Charis SIL** | 0,94 × base | 400 |
| Interface (boutons, étiquettes, navigation) | **Inter** | 15 px | 500 |
| Grands titres de scène | **Literata** (police variable, axe optique `opsz` 72) | 32–40 px | 500 |
| Aide à la lecture (option) | **Atkinson Hyperlegible** | remplace Literata et Inter | — |

- Interligne 1,6 pour le texte ; 1,35 pour les énoncés.
- Longueur de ligne 60 à 70 caractères ; marges latérales 20 px sur téléphone, 48 px sur tablette.
- Polices embarquées dans l'application (aucun appel réseau), réduites aux jeux de caractères utilisés (latin étendu, symboles phonétiques) avec `pyftsubset`, format WOFF2.
- Césure française activée pour le texte français (`hyphens: auto` avec `lang="fr"`), désactivée pour l'anglais et le phrasé.

### 9.4 Grille et espacements

- Unité de 4 px ; échelle : 4, 8, 12, 16, 24, 32, 48, 64.
- Cibles tactiles ≥ 48 × 48 dp ; espacement entre cibles ≥ 8 dp.
- Zones sûres : respect intégral des encarts système (barre d'état, barre de navigation gestuelle, encoches) via les variables CSS de zone sûre fournies par Capacitor 8 (section 10.8).

### 9.5 Composants

| Composant | Description | États |
|---|---|---|
| **Carte d'expression** | Section 8.2 | repos, en lecture (bord gauche coloré de l'accent), marquée |
| **Pupitre des voix** | Deux bascules segmentées (Am./Brit., Posé/Spontané) + « Les quatre voix » + lecture continue | repos, épinglé, réduit au défilement rapide |
| **Bouton ◉ Écouter** | Cercle de 40 dp, anneau de progression pendant la lecture | prêt, en préparation (anneau pointillé), en lecture, voix à faire venir (nuage) |
| **Phrasé** | Rendu typographique des signes du 6.4 | statique, synchronisé (syllabe active en couleur) |
| **Étiquette** | Pilule de texte : ton, niveau, région | — |
| **Volet** | Feuille montante (*bottom sheet*) pour les actions longues | ouvert à mi-hauteur, plein écran |
| **Intertitre de moment** | Lettre capitale ornée + titre | — |
| **Bloc bilingue** | Réplique anglaise et sens français alignés côte à côte (tablette) ou l'un sous l'autre (téléphone) | — |
| **Filet de chemin** | Fine ligne sous un titre, qui se remplit | — |
| **Courbe du miroir** | Onde + mélodie, deux couleurs | enregistrement, comparaison |

### 9.6 Iconographie

Jeu d'icônes dessiné sur mesure, au trait (1,75 px à 24 px), coins arrondis, inspiré de l'outillage du livre et du son : soleil levant, livre ouvert, casque, carnet, marque-page, loupe, plume, onde, nuage, cercle d'écoute. Format SVG, intégrées en ligne. Aucune icône issue d'un jeu générique reconnaissable.

### 9.7 Mouvement et haptique

- Durées : 120 ms (micro-interactions), 220 ms (transitions d'écran), 320 ms (volets).
- Courbe : `cubic-bezier(0.2, 0, 0, 1)` pour les entrées, `cubic-bezier(0.3, 0, 1, 1)` pour les sorties.
- Transition entre écrans : glissement court (24 px) + fondu ; jamais de rebond.
- Préférence système « Réduire les animations » : toutes les transitions deviennent des fondus de 120 ms, le surlignage synchronisé devient un simple changement de couleur.
- Retour haptique léger (impact « léger ») au démarrage d'une voix, au marque-page, à la fin d'une scène. Désactivable. Le battement (8.15) est un réglage distinct.

### 9.8 L'encre qui s'écrit (états d'attente)

Aucun indicateur rotatif, aucun mot « chargement ». Quand un temps d'attente dépasse 300 ms, un fin trait d'encre se trace de gauche à droite sous le titre. Les états vides (carnet vide, aucune retrouvaille) affichent une petite illustration au trait et une phrase de la voix de l'éditeur.

### 9.9 Accessibilité (niveau WCAG 2.2 AA, exigence)

- Lecteur d'écran TalkBack : chaque carte annonce « Expression : *My alarm's going off*. Sens : Mon réveil sonne. Ton courant. » ; le bouton ◉ annonce « Écouter, britannique, posé » ; le phrasé est **masqué** pour TalkBack (illisible à la synthèse), remplacé par l'invitation à écouter la voix.
- Attribut `lang="en"` sur tout texte anglais pour que TalkBack bascule de langue.
- Taille du texte du système respectée jusqu'à 200 % sans perte de contenu ni défilement horizontal.
- Navigation complète au clavier externe et au contacteur (ordre de focus logique, focus visible de 3 px couleur `--accent`).
- Contraste vérifié automatiquement (9.2).
- Toutes les voix ont leur texte affiché : aucune information n'est purement sonore.
- Thème Contraste (9.2) et battement haptique (8.15) pour les lecteurs malvoyants ou malentendants.
- Sous-titrage de la promenade : l'écran verrouillé et la notification affichent l'énoncé en cours.
- Respect du réglage système « Supprimer les animations » et de la taille d'affichage.

---

## 10. L'ingénierie : du corpus au fichier APK

### 10.1 Vue d'ensemble

```
 ┌─────────────────────────┐   ┌───────────────────────────┐
 │  CORPUS (source unique) │   │  VOIX (création → masters)│
 │  corpus/*.yaml          │   │  WAV 48 kHz / 24 bits      │
 └───────────┬─────────────┘   └─────────────┬─────────────┘
             │ tools/construire.py            │ voix/outils/*.py
             │ (validation, lexique,          │ (normalisation, découpe,
             │  index, scripts des voix)      │  Opus, alignement, manifestes)
             ▼                                ▼
 ┌──────────────────────────────────────────────────────────┐
 │  APPLICATION WEB EMBARQUÉE  (SvelteKit statique, TS)     │
 │  static/corpus/*.json · static/voix/(socle) · index      │
 └───────────┬──────────────────────────────────────────────┘
             │ npm run build → build/   ·   npx cap sync android
             ▼
 ┌──────────────────────────────────────────────────────────┐
 │  COQUE ANDROID  (Capacitor 8 + Kotlin)                   │
 │  WebView · plugin Voix (paquets) · plugin Promenade      │
 │  (Media3 ExoPlayer, service de lecture) · micro · rappels │
 └───────────┬───────────────────────────────┬──────────────┘
             │ ./gradlew bundlePlayRelease    │ ./gradlew assembleDirectRelease
             ▼                                ▼
   AAB + 24 paquets de voix à la demande   APK signé + voix complémentaires
   (Google Play, Play Asset Delivery)      depuis le serveur de l'éditeur
```

### 10.2 La pile technique et les versions

| Domaine | Choix | Version figée |
|---|---|---|
| Exécution JavaScript (outillage) | Node.js | 22 LTS (minimum exigé par Capacitor 8, selon la politique de support Capacitor — <https://capacitorjs.com/docs/main/reference/support-policy>) |
| Coque native | Capacitor | 8.x (version stable active, publiée le 8 décembre 2025, d'après la même politique de support — <https://capacitorjs.com/docs/main/reference/support-policy>) |
| Java | JDK Temurin | 21 (exigé par Capacitor 8, d'après ce guide de migration — <https://dev.to/batmanofweb/capacitor-8-upgrade-for-lovable-apps-jg6>) |
| IDE | Android Studio | Otter 2025.2.1 ou plus récent (politique de support Capacitor — <https://capacitorjs.com/docs/main/reference/support-policy>) |
| Outils Android | Gradle 8.14.3, Android Gradle Plugin 8.13.x, Kotlin 2.2.20 | Valeurs posées par `npx cap migrate` vers Capacitor 8 (guide de migration — <https://dev.to/batmanofweb/capacitor-8-upgrade-for-lovable-apps-jg6>) |
| SDK Android | `minSdk 24`, `compileSdk 36`, `targetSdk 36` | Android 7.0 minimum pour Capacitor 8 (documentation Android de Capacitor — <https://capacitorjs.com/docs/android>) ; API 36 exigée par Google Play pour toute nouvelle application et mise à jour depuis le 31 août 2026 (Aide Play Console — <https://support.google.com/googleplay/android-developer/answer/11926878?hl=en>) |
| Cadre web | SvelteKit 2 + Svelte 5, `adapter-static`, TypeScript 5 (mode strict) | Dernières versions stables au gel, verrouillées dans `package-lock.json` |
| Construction | Vite (inclus dans SvelteKit) | idem |
| Base locale | Dexie 4 (IndexedDB) | idem |
| Recherche | MiniSearch 7 | idem |
| Mémorisation espacée | ts-fsrs | idem |
| Lecture native continue | AndroidX Media3 (ExoPlayer + MediaSession) | 1.x stable au gel |
| Paquets de voix Play | `com.google.android.play:asset-delivery` (Play Asset Delivery, saveur `play` uniquement) | 2.x stable au gel |
| Enregistrement du lecteur | `@capgo/capacitor-audio-recorder` | Compatible Capacitor 8 (dépôt — <https://github.com/Cap-go/capacitor-audio-recorder>) |
| Plugins officiels | `@capacitor/app`, `filesystem`, `haptics`, `local-notifications`, `preferences`, `share`, `splash-screen` | 8.x |
| Widget d'écran d'accueil, raccourcis, liens d'application | Kotlin natif (`AppWidgetProvider`, `ShortcutManagerCompat`), `androidx.core` | Versions posées par Capacitor |
| Outillage contenu et voix | Python 3.12, ffmpeg 7 (avec libopus), `ffmpeg-normalize`, Montreal Forced Aligner 3, `praat-parselmouth` (courbes), `jsonschema` | — |
| Tests | Vitest, Playwright, axe-core, Maestro, Lighthouse CI | — |

**Règle de gel** : les versions sont figées dans `package-lock.json`, `variables.gradle` et `requirements.txt` ; elles ne changent qu'entre deux éditions, au moyen d'une demande de modification écrite (`docs/decisions/`), validée par le responsable technique et suivie de la totalité des tests de la section 11.

### 10.3 L'arborescence du dépôt

```
vivre-anglais/
├── corpus/                         # SOURCE UNIQUE DU TEXTE (YAML, une scène par fichier)
│   ├── c00/s01.yaml … s06.yaml     # le Prélude (chapitre 00)
│   ├── c01/s01.yaml … s10.yaml
│   ├── …
│   ├── personnages.yaml            # bible des personnages
│   ├── itineraires.yaml            # les 12 itinéraires (8.17)
│   ├── moments.yaml                # scènes associées aux moments de la journée (8.20)
│   └── schema/scene.schema.json    # schéma de validation (annexe B)
├── voix/
│   ├── fiches/                     # fiches vocales et références de timbre (7.4)
│   ├── registre/                   # creations.jsonl, prises retenues (7.5, 7.9)
│   ├── masters/                    # WAV validés (stockage objet, hors Git, voir 10.16)
│   ├── encodes/cXX/sYY/*.opus      # sorties encodées + manifeste.json
│   └── outils/                     # creer.py, sources_libres.py, choisir.py, normaliser.py, decouper.py, encoder.py, aligner.py, syllaber.py, courbe.py, controler.py
├── tools/
│   ├── construire.py               # orchestre toute la chaîne de contenu
│   ├── valider_corpus.py           # schéma, complétude, renvois, densité
│   ├── lexique_verifier.py         # mots bannis (3.3)
│   ├── phrase_verifier.py          # symboles du phrasé (6.2–6.4)
│   ├── scripts_voix.py           # scripts JSONL par voix (7.8)
│   ├── index_recherche.py          # index MiniSearch pré-calculé
│   ├── voix_recuperer.py           # copie du socle dans app/static/voix
│   ├── generer_paquets.py          # modules Gradle des paquets de voix
│   ├── contrastes.py               # contrôle des contrastes des quatre thèmes
│   ├── carte_partage.py            # gabarit des cartes « Partager une expression »
│   ├── profil_lexical.py           # couverture lexicale de chaque scène (15.9)
│   ├── verifier_jouer.py           # graphes des conversations « À vous de jouer » (19.1)
│   ├── fiches_classe.py            # fiches imprimables et codes QR (20.8)
│   ├── sbom.py                     # inventaire CycloneDX de chaque publication (20.4)
│   └── requirements.txt
├── app/                            # APPLICATION WEB (SvelteKit)
│   ├── src/
│   │   ├── app.html
│   │   ├── lib/
│   │   │   ├── corpus/             # types.ts, chargeur.ts
│   │   │   ├── voix/               # moteur.ts, source.ts, promenade.ts, miroir.ts, echo.ts, battement.ts, fluidite.ts, ambiance.ts
│   │   │   ├── modules/            # jouer.ts, paires.ts, relais.ts, ombre.ts, diagnostic.ts, epreuves.ts, cap.ts
│   │   │   ├── retrouvailles/      # fsrs.ts, session.ts, oreille.ts (comparaison mot à mot)
│   │   │   ├── itineraires/        # itineraires.ts
│   │   │   ├── liens/              # liens.ts (liens profonds, raccourcis)
│   │   │   ├── carnet/             # base.ts (Dexie), sauvegarde.ts
│   │   │   ├── recherche/          # recherche.ts
│   │   │   ├── ui/                 # composants Svelte (CarteExpression, Pupitre, Phrase, …)
│   │   │   ├── design/             # jetons.css, typographie.css, themes.css
│   │   │   └── textes/fr.ts        # TOUS les microtextes (aucune chaîne en dur ailleurs)
│   │   └── routes/
│   │       ├── +layout.ts          # export const ssr = false; export const prerender = true;
│   │       ├── +page.svelte        # Aujourd'hui
│   │       ├── livre/+page.svelte
│   │       ├── livre/[chapitre]/+page.svelte
│   │       ├── scene/[id]/+page.svelte
│   │       ├── promenade/+page.svelte
│   │       ├── carnet/+page.svelte
│   │       ├── itineraire/[id]/+page.svelte
│   │       ├── lire-ce-livre/+page.svelte
│   │       ├── recherche/+page.svelte
│   │       └── preferences/+page.svelte
│   ├── static/
│   │   ├── corpus/                 # JSON générés (ne pas éditer)
│   │   ├── voix/                   # socle généré : Prélude (c00), Chapitres 1 et 2
│   │   └── polices/                # WOFF2 réduits
│   ├── svelte.config.js
│   ├── vite.config.ts
│   ├── package.json
│   └── capacitor.config.ts
├── android/                        # généré par `npx cap add android`, puis versionné
│   ├── app/                        # module principal (+ plugins Kotlin locaux, widget, raccourcis)
│   ├── voix_c03/ … voix_c26/       # modules de paquets de voix (générés)
│   ├── variables.gradle
│   └── settings.gradle
├── tests/
│   ├── e2e/                        # Playwright
│   └── maestro/                    # parcours sur émulateur
├── .github/workflows/
│   ├── contenu.yml
│   └── android.yml
└── docs/
    ├── MEGA_GOD_PLAN.md            # ce document
    └── decisions/                  # journal des décisions
```

### 10.4 Le modèle de données

#### Types TypeScript (contrat entre le corpus et l'application)

```ts
// app/src/lib/corpus/types.ts
export type Accent = 'us' | 'uk';
export type Rythme = 'pose' | 'spontane';
export type Ton = 'courant' | 'complice' | 'cru' | 'soutenu';
export type Niveau = 'fondations' | 'aisance' | 'maitrise';
export type Region = 'commun' | 'us' | 'uk' | 'au' | 'ie' | 'ng' | 'gh' | 'za';

export interface Phrase {
  phrase: string;        // système du Phrasé (section 6), ex. "maï ə·LÂMZ gəou·ing OF ↘"
  expert: string;        // alphabet phonétique international, ex. "/maɪ əˈlɑːmz ˌɡəʊɪŋ ˈɒf/"
  entendu?: string;      // ce que l'oreille entend (spontané), ex. "Whatcha doin'?"
}

export type Phrases = Record<Accent, Record<Rythme, Phrase>>;

export interface Enonce {
  id: string;                          // "c01.s01.A1.e1"
  texte: Record<Accent, string>;       // graphies par accent (identiques si commun)
  region: Region;                      // 'uk' → texte.us contient l'équivalent américain
  phrases: Phrases;
  jeu: { contexte: string; emotion: string };   // indication de jeu (en anglais, transmise au moteur des voix)
}

export interface Declinaison {
  id: string;                          // "c01.s01.A1.d1"
  texte: Record<Accent, string>;
  sens: string;
  phrases: Phrases;                    // obligatoires (6.7)
  renvoi?: string;
}

export interface Expression {
  id: string;                          // "c01.s01.A1"
  enonces: Enonce[];                   // 1 à 3
  sens: string;
  motAMot?: string;
  usage: string;
  coulisses?: string;
  gabarit?: string;                    // "[quelque chose] is going off"
  declinaisons: Declinaison[];         // 3 à 6
  ton: Ton;
  niveau: Niveau;
  frequence: 1 | 2 | 3 | 4 | 5;
  situations: string[];
  fonctions: string[];
  renvois: string[];
}

export interface Moment { lettre: string; titre: string; expressions: Expression[] }

export interface Replique {
  id: string;                          // "c01.s01.sv.l01"
  personnage: string;                  // clé de personnages.yaml
  texte: Record<Accent, string>;
  sens: string;
  emotion: string;
}

export interface Itineraire {
  id: string;                          // "premier-voyage"
  titre: string;
  pourQui: string;
  etapes: { titre: string; expressions: string[] }[];   // ids d'expressions
}

export interface FauxPas { fautif: string; naturel: string; pourquoi: string }

export interface Scene {
  id: string;                          // "c01.s01"
  chapitre: number;
  numero: number;
  titre: string;
  intention: string;
  moments: Moment[];
  essentiel: { incontournables: string[]; fauxPas: FauxPas[] };  // ids d'expressions
  sceneVivante: { titre: string; repliques: Replique[] };
  rituel: string[];
  version: number;
}
```

#### Extrait YAML de corpus (format d'édition)

Le format YAML est choisi pour l'édition (lisible, commentable, différences claires dans Git) ; le JSON n'est qu'un produit de compilation.

```yaml
# corpus/c01/s01.yaml (extrait)
id: c01.s01
titre: Le réveil et les premières minutes
intention: >-
  À la fin de cette scène, vous vivez en anglais les quinze premières minutes
  de n'importe quelle journée : vous réveiller, réveiller quelqu'un, parler
  de votre nuit, de vos rêves, d'un réveil manqué, et sortir du lit.
moments:
  - lettre: A
    titre: Le réveil sonne
    expressions:
      - id: c01.s01.A1
        ton: courant
        niveau: fondations
        frequence: 5
        situations: [matin, maison]
        fonctions: [constater]
        enonces:
          - id: c01.s01.A1.e1
            region: commun
            texte: { uk: "My alarm's going off.", us: "My alarm's going off." }
            jeu: { contexte: "Half-asleep, the alarm is ringing on the bedside table.", emotion: "groggy, matter-of-fact" }
            phrases:
              uk:
                pose:     { phrase: "maï ə·LÂMZ gəou·ing OF ↘", expert: "/maɪ əˈlɑːmz ˌɡəʊɪŋ ˈɒf/" }
                spontane: { phrase: "mə·LÂMZ gəou·in‿OF ↘",   expert: "/məˈlɑːmz ˌɡəʊɪn ˈɒf/" }
              us:
                pose:     { phrase: "maï ə·LÂRMZ gôou·ing ÔF ↘", expert: "/maɪ əˈlɑrmz ˌɡoʊɪŋ ˈɔf/" }
                spontane: { phrase: "mə·LÂRMZ gôou·in‿ÔF ↘",   expert: "/məˈlɑrmz ˌɡoʊɪn ˈɔf/" }
        sens: Mon réveil sonne.
        motAMot: mon alarme est en train de partir
        usage: >-
          Go off, c'est « se déclencher » : un réveil, une alarme, un détecteur.
          Les natifs ne disent presque jamais My alarm is ringing.
        gabarit: "[quelque chose] is going off"
        declinaisons:
          - { id: c01.s01.A1.d1, texte: { uk: "The fire alarm's going off.", us: "The fire alarm's going off." }, sens: "L'alarme incendie sonne." }
          - { id: c01.s01.A1.d2, texte: { uk: "My phone keeps going off.", us: "My phone keeps going off." }, sens: "Mon téléphone n'arrête pas de sonner." }
          - { id: c01.s01.A1.d5, texte: { uk: "My alarm didn't go off!", us: "My alarm didn't go off!" }, sens: "Mon réveil n'a pas sonné !", renvoi: c01.s01.H1 }
        renvois: [c01.s01.H1]
```

#### Règles de validation (`tools/valider_corpus.py`) — toute violation bloque la compilation

1. Conformité au schéma `corpus/schema/scene.schema.json` (JSON Schema 2020-12).
2. Identifiants uniques dans tout l'ouvrage, au format `^c\d{2}\.s\d{2}\.[A-Z]\d{1,2}(\.(e|d)\d{1,2})?$` (le Prélude est le chapitre `c00`) ; répliques au format `^c\d{2}\.s\d{2}\.sv\.l\d{2}$`.
3. Tout renvoi pointe vers un identifiant existant.
4. Densité conforme à 4.5 (avertissement en dessous de la cible, blocage en dessous du minimum).
5. Toute déclinaison a un `sens` et ses quatre phrasés.
6. Toute expression a ses quatre phrasés pour chaque énoncé (blocage à partir du gel de la scène).
7. Énoncé ≤ 18 mots ; « L'usage » ≤ 70 mots ; « En coulisses » ≤ 50 mots.
8. Typographie française : espaces insécables avant `; : ! ?` dans les champs français (correction automatique proposée).
9. Lexique : aucun mot banni dans les champs français (3.3).
10. Tout personnage cité dans une scène vivante existe dans `personnages.yaml`.
11. Toute expression citée par `itineraires.yaml` ou `moments.yaml` existe ; chaque étape d'itinéraire compte 12 à 25 expressions.
12. Le champ `sens` ne contient aucun mot anglais non balisé (contrôle de la voix du sens, 7.4).

### 10.5 La chaîne de compilation du contenu

`python3 tools/construire.py` exécute, dans cet ordre :

1. `valider_corpus.py` — règles 10.4.
2. `lexique_verifier.py` — sur le corpus **et** sur `app/src/lib/textes/fr.ts`.
3. `phrase_verifier.py` — symboles autorisés, au moins une syllabe accentuée par phrasé.
4. Conversion YAML → JSON par scène dans `app/static/corpus/` + `sommaire.json` (titres, intentions, tailles de voix par chapitre).
5. `index_recherche.py` — index MiniSearch sérialisé, découpé en deux fichiers (`index-fr.json`, `index-en.json`) chargés au premier usage de la recherche.
6. Contrôle de couverture vocale : pour chaque énoncé, déclinaison et réplique, présence des quatre fichiers dans `voix/encodes/` et dans les manifestes, avec leurs champs `mots`, `syllabes` et `courbe` ; pour chaque sens, présence de la voix du sens. Le rapport `rapport-couverture.md` liste les manques ; **toute scène publiée doit être à 100 %**.
7. `scripts_voix.py` (sur demande `--voix`) — génère les scripts JSONL (7.8) pour les énoncés sans voix validée, puis `voix/outils/creer.py` produit les prises (7.9).
8. Conversion de `itineraires.yaml` et `moments.yaml` en `itineraires.json` et `moments.json`.
9. Production de `expression-du-jour.json` (identifiant, énoncés, sens, accent) lu par le widget natif (10.20).

### 10.6 L'application web embarquée

#### Configuration SvelteKit

```js
// app/svelte.config.js
import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

export default {
  preprocess: vitePreprocess(),
  kit: {
    adapter: adapter({ pages: 'build', assets: 'build', fallback: 'index.html', strict: true }),
    csp: {
      mode: 'hash',
      directives: {
        'default-src': ['self'],
        'script-src': ['self'],
        'style-src': ['self', 'unsafe-inline'],
        'img-src': ['self', 'data:', 'blob:'],
        'media-src': ['self', 'blob:'],
        'connect-src': ['self', 'https://localhost'],
        'font-src': ['self'],
        'object-src': ['none'],
        'base-uri': ['none']
      }
    }
  }
};
```

```ts
// app/src/routes/+layout.ts
export const ssr = false;
export const prerender = true;
export const trailingSlash = 'always';
```

#### Règles d'implémentation

- **Chargement par scène** : `scene/[id]` charge `static/corpus/{id}.json` (≈ 60 à 150 Ko) à l'ouverture ; le sommaire est chargé au démarrage (≈ 40 Ko).
- **Rendu des longues scènes** : chaque moment est un bloc `content-visibility: auto; contain-intrinsic-size: auto 1200px;` — pas de bibliothèque de virtualisation (les 75 cartes maximum restent sous 4 000 nœuds).
- **Composant `Phrase.svelte`** : transforme la chaîne Phrasé en éléments typographiques (capitales → `<b class="fort">` en bas de casse ; `‿` → `<span class="lien">` ; `(t)` → `<span class="retenu">` ; `ʔ` → `’` avec `title` ; `ɾ` → `<span class="battu">d</span>` ; `ʳ` → `<sup>r</sup>` ; flèches → `<span class="intonation">`). Chaque syllabe reçoit un index pour la synchronisation.
- **Textes d'interface** : uniquement dans `textes/fr.ts`, exporté en objet typé ; le vérificateur de lexique s'exécute dessus.
- **Accessibilité** : `aria-hidden="true"` sur le phrasé, `lang="en"` sur les énoncés, rôles ARIA pour les bascules (`role="radiogroup"`).
- **Retour arrière** : un seul écouteur `App.addListener('backButton', …)` : ferme d'abord un volet ouvert, puis revient en arrière dans l'historique, puis, sur l'écran Aujourd'hui, laisse le système fermer l'application (`App.minimizeApp()`).

### 10.7 Le moteur des voix

Deux moteurs complémentaires, derrière une seule interface :

| Moteur | Technologie | Usage |
|---|---|---|
| **Moteur de page** | Web Audio API dans la WebView | Toute écoute déclenchée par un toucher (latence minimale, synchronisation mot à mot) |
| **Moteur de promenade** | Plugin Kotlin `Promenade` (Media3 ExoPlayer dans un `MediaSessionService`) | Écoute continue, écran éteint, contrôles de l'écran verrouillé et du casque |

#### Résolution de l'emplacement d'une voix

```ts
// app/src/lib/voix/source.ts
import { Capacitor, registerPlugin } from '@capacitor/core';
import type { Accent, Rythme } from '$lib/corpus/types';

export interface EtatChapitre { etat: 'socle' | 'installe' | 'absent' | 'en_cours'; base?: string; taille: number }
interface VoixPlugin {
  etat(o: { chapitre: string }): Promise<EtatChapitre>;
  faireVenir(o: { chapitre: string }): Promise<void>;
  retirer(o: { chapitre: string }): Promise<void>;
  addListener(e: 'progression', f: (p: { chapitre: string; octets: number; total: number; etat: string }) => void): Promise<{ remove: () => void }>;
}
export const Voix = registerPlugin<VoixPlugin>('Voix');

const SOCLE = new Set(['c00', 'c01', 'c02']);   // Prélude, Chapitres 1 et 2 : dans le module de base
const bases = new Map<string, string | null>();

export function nomFichier(id: string, accent: Accent, rythme: Rythme): string {
  // "c01.s01.A1.e1" → "c01s01-A1-e1.uk.pose.opus"
  const [c, s, ...reste] = id.split('.');
  return `${c}${s}-${reste.join('-')}.${accent}.${rythme}.opus`;
}

export async function urlVoix(id: string, accent: Accent, rythme: Rythme): Promise<string | null> {
  const [c, s] = id.split('.');
  const chemin = `voix/${c}/${s}/${nomFichier(id, accent, rythme)}`;
  if (SOCLE.has(c)) return `/${chemin}`;
  if (!bases.has(c)) {
    const e = await Voix.etat({ chapitre: c });
    bases.set(c, e.etat === 'installe' && e.base ? e.base : null);
  }
  const base = bases.get(c);
  return base ? Capacitor.convertFileSrc(`${base}/${chemin}`) : null;
}
export async function urlSens(id: string): Promise<string | null> {
  // "c01.s01.A1" → "voix/c01/s01/c01s01-A1.fr.sens.opus" (même emplacement que les voix anglaises)
  const [c, s, ...reste] = id.split('.');
  const chemin = `voix/${c}/${s}/${c}${s}-${reste.join('-')}.fr.sens.opus`;
  if (SOCLE.has(c)) return `/${chemin}`;
  const base = bases.get(c) ?? (await Voix.etat({ chapitre: c })).base ?? null;
  return base ? Capacitor.convertFileSrc(`${base}/${chemin}`) : null;
}
export function oublierBase(chapitre: string) { bases.delete(chapitre); }
```

#### Le moteur de page

```ts
// app/src/lib/voix/moteur.ts
import { urlVoix } from './source';
import type { Accent, Rythme } from '$lib/corpus/types';

type Cle = string;
export type Issue = 'fini' | 'interrompu' | 'absent';
export interface Lecture {
  id: string; accent: Accent; rythme: Rythme;
  mots?: [string, number, number][];
  syllabes?: [number, number, 0 | 1][];
  /** segment à lire, en secondes (écoute au mot) */
  de?: number; a?: number;
}

class MoteurVoix {
  private ctx: AudioContext | null = null;
  private tampons = new Map<Cle, AudioBuffer>();          // cache LRU
  private enCours = new Map<Cle, Promise<AudioBuffer | null>>();
  private source: AudioBufferSourceNode | null = null;
  private gain: GainNode | null = null;
  private terminer: ((i: Issue) => void) | null = null;    // résout la lecture en cours
  private debut = 0;
  private decalage = 0;
  private raf = 0;
  private generation = 0;                                  // invalide les enchaînements interrompus
  private static readonly MAX = 96;
  onMot: (index: number) => void = () => {};
  onSyllabeForte: () => void = () => {};                   // branché sur le battement (8.15)
  onTemps: (t: number) => void = () => {};                 // dessine la courbe (8.15)

  private contexte(): AudioContext {
    if (!this.ctx) this.ctx = new AudioContext({ latencyHint: 'interactive', sampleRate: 48000 });
    if (this.ctx.state === 'suspended') void this.ctx.resume();
    return this.ctx;
  }

  private cle(id: string, a: Accent, r: Rythme): Cle { return `${id}|${a}|${r}`; }

  async preparer(id: string, a: Accent, r: Rythme): Promise<AudioBuffer | null> {
    const k = this.cle(id, a, r);
    const t = this.tampons.get(k);
    if (t) { this.tampons.delete(k); this.tampons.set(k, t); return t; }  // rafraîchit l'ordre LRU
    if (this.enCours.has(k)) return this.enCours.get(k)!;
    const p = (async () => {
      try {
        const url = await urlVoix(id, a, r);
        if (!url) return null;
        const rep = await fetch(url);
        if (!rep.ok) return null;
        const tampon = await this.contexte().decodeAudioData(await rep.arrayBuffer());
        this.tampons.set(k, tampon);
        while (this.tampons.size > MoteurVoix.MAX) this.tampons.delete(this.tampons.keys().next().value!);
        return tampon;
      } catch { return null; }                              // fichier abîmé : signalé par 10.21
    })().finally(() => this.enCours.delete(k));
    this.enCours.set(k, p);
    return p;
  }

  /** Joue une voix ; la promesse se résout quand elle finit, est interrompue, ou est absente. */
  async jouer(l: Lecture): Promise<Issue> {
    const ctx = this.contexte();
    const tampon = await this.preparer(l.id, l.accent, l.rythme);
    if (!tampon) return 'absent';
    this.arreter();
    const g = ctx.createGain();
    const t0 = ctx.currentTime;
    const fondu = l.de !== undefined ? 0.015 : 0.005;
    g.gain.setValueAtTime(0, t0);
    g.gain.linearRampToValueAtTime(1, t0 + fondu);
    const s = ctx.createBufferSource();
    s.buffer = tampon;
    s.connect(g).connect(ctx.destination);
    this.decalage = Math.max(0, l.de ?? 0);
    const duree = l.a !== undefined ? Math.max(0.05, l.a - this.decalage) : undefined;
    if (duree !== undefined) {                                // fondu de sortie du segment
      g.gain.setValueAtTime(1, t0 + duree - fondu);
      g.gain.linearRampToValueAtTime(0, t0 + duree);
    }
    this.debut = t0;
    const issue = new Promise<Issue>((ok) => (this.terminer = ok));
    s.onended = () => {
      if (this.source !== s) return;
      this.source = null; cancelAnimationFrame(this.raf);
      this.terminer?.('fini'); this.terminer = null;
    };
    s.start(0, this.decalage, duree);
    this.source = s; this.gain = g;
    this.suivre(l);
    return issue;
  }

  /** Écoute au mot (8.14) : le mot tel qu'il a été dit dans la phrase. */
  async jouerMot(l: Lecture, index: number): Promise<Issue> {
    const m = l.mots?.[index];
    if (!m) return 'absent';
    let [, de, a] = m;
    if (a - de < 0.18 && l.mots) {                           // mot faible : son groupe de souffle
      const voisins = l.mots.slice(Math.max(0, index - 1), index + 2);
      de = voisins[0][1]; a = voisins[voisins.length - 1][2];
    }
    return this.jouer({ ...l, de, a, mots: undefined, syllabes: undefined });
  }

  private suivre(l: Lecture) {
    let dernierMot = -1, derniereSyllabe = -1;
    const pas = () => {
      if (!this.ctx || !this.source) return;
      const t = this.ctx.currentTime - this.debut + this.decalage;
      this.onTemps(t);
      if (l.mots) {
        const i = l.mots.findIndex(([, d, f]) => t >= d && t < f);
        if (i !== -1 && i !== dernierMot) { dernierMot = i; this.onMot(i); }
      }
      if (l.syllabes) {
        const j = l.syllabes.findIndex(([d, f]) => t >= d && t < f);
        if (j !== -1 && j !== derniereSyllabe) { derniereSyllabe = j; if (l.syllabes[j][2] === 1) this.onSyllabeForte(); }
      }
      this.raf = requestAnimationFrame(pas);
    };
    this.raf = requestAnimationFrame(pas);
  }

  /** Arrête la voix en cours (fondu de 30 ms) ; toute attente en cours reçoit « interrompu ». */
  arreter(fondu = 0.03) {
    this.generation++;
    cancelAnimationFrame(this.raf);
    const fin = this.terminer; this.terminer = null;
    if (this.ctx && this.source && this.gain) {
      const t = this.ctx.currentTime;
      this.gain.gain.cancelScheduledValues(t);
      this.gain.gain.setValueAtTime(this.gain.gain.value, t);
      this.gain.gain.linearRampToValueAtTime(0, t + fondu);
      this.source.onended = null;
      this.source.stop(t + fondu + 0.005);
    }
    this.source = null;
    fin?.('interrompu');
  }

  get enLecture(): boolean { return this.source !== null; }

  /** Les quatre voix d'un énoncé, dans l'ordre du lecteur, 600 ms d'intervalle. */
  async quatre(id: string, prefere: Accent,
               donnees: (a: Accent, r: Rythme) => Pick<Lecture, 'mots' | 'syllabes'>,
               surChaque: (a: Accent, r: Rythme) => void): Promise<Issue> {
    const autre: Accent = prefere === 'uk' ? 'us' : 'uk';
    const ordre: [Accent, Rythme][] = [[prefere, 'pose'], [prefere, 'spontane'], [autre, 'pose'], [autre, 'spontane']];
    for (const [a, r] of ordre) {
      surChaque(a, r);
      const issue = await this.jouer({ id, accent: a, rythme: r, ...donnees(a, r) });
      if (issue === 'interrompu') return 'interrompu';
      if (issue === 'absent') continue;
      const gen = this.generation;
      await new Promise((ok) => setTimeout(ok, 600));
      if (gen !== this.generation) return 'interrompu';     // le lecteur a touché ailleurs pendant le silence
    }
    return 'fini';
  }

  /** L'écho (8.16) : passages successifs séparés d'un silence de 1,3 × la durée. */
  async echo(l: Lecture, passages: number, surSilence: (ms: number) => void): Promise<Issue> {
    for (let i = 0; i < passages; i++) {
      const tampon = await this.preparer(l.id, l.accent, l.rythme);
      if (!tampon) return 'absent';
      const issue = await this.jouer(l);
      if (issue !== 'fini') return issue;
      const ms = Math.round(tampon.duration * 1300);
      surSilence(ms);
      const gen = this.generation;
      await new Promise((ok) => setTimeout(ok, ms));
      if (gen !== this.generation) return 'interrompu';
    }
    return 'fini';
  }
}

export const moteur = new MoteurVoix();
```

**Ce que garantit cette écriture** : chaque lecture renvoie sa propre promesse, résolue une seule fois (`fini`, `interrompu` ou `absent`) ; un nouveau toucher interrompt proprement toute séquence en cours (« Les quatre voix », l'écho), y compris pendant un silence ; aucun rappel global n'est écrasé. L'écoute au mot lit un segment du même fichier, sans aucune transformation de la voix.

**Le battement** (`battement.ts`) : `moteur.onSyllabeForte = () => Haptics.impact({ style: ImpactStyle.Light })` si le réglage est actif ; l'appel est ignoré si la précédente vibration date de moins de 120 ms.

**Préparation anticipée** : un `IntersectionObserver` (marge de 800 px) appelle `moteur.preparer()` pour l'énoncé principal de chaque carte entrant dans la zone, dans la configuration du pupitre, puis pour les six cartes suivantes, avec au plus quatre préparations simultanées.

#### Le plugin Promenade (Kotlin)

```kotlin
// android/app/src/main/java/com/vivrelanglais/livre/promenade/PromenadePlugin.kt
package com.vivrelanglais.livre.promenade

import android.content.ComponentName
import androidx.media3.common.MediaItem
import androidx.media3.common.MediaMetadata
import androidx.media3.session.MediaController
import androidx.media3.session.SessionToken
import com.getcapacitor.*
import com.getcapacitor.annotation.CapacitorPlugin
import com.google.common.util.concurrent.MoreExecutors

@CapacitorPlugin(name = "Promenade")
class PromenadePlugin : Plugin() {
    private var controleur: MediaController? = null

    private fun avecControleur(action: (MediaController) -> Unit) {
        controleur?.let { return action(it) }
        val jeton = SessionToken(context, ComponentName(context, PromenadeService::class.java))
        val futur = MediaController.Builder(context, jeton).buildAsync()
        futur.addListener({ controleur = futur.get(); action(controleur!!) }, MoreExecutors.directExecutor())
    }

    /** elements: [{ url, titre, sousTitre }] ou [{ silenceMs }] */
    @PluginMethod
    fun demarrer(call: PluginCall) {
        val elements = call.getArray("elements") ?: return call.reject("elements manquants")
        val items = (0 until elements.length()).map { i ->
            val e = elements.getJSONObject(i)
            if (e.has("silenceMs")) {
                MediaItem.Builder().setUri("silence://${e.getLong("silenceMs")}").setMediaId("silence-$i").build()
            } else {
                MediaItem.Builder()
                    .setUri(e.getString("url"))
                    .setMediaId(e.optString("id", "item-$i"))
                    .setMediaMetadata(MediaMetadata.Builder()
                        .setTitle(e.optString("titre"))
                        .setArtist(e.optString("sousTitre", "Vivre l'Anglais"))
                        .build())
                    .build()
            }
        }
        avecControleur { c -> c.setMediaItems(items); c.prepare(); c.play(); call.resolve() }
    }

    @PluginMethod fun pause(call: PluginCall) = avecControleur { it.pause(); call.resolve() }
    @PluginMethod fun reprendre(call: PluginCall) = avecControleur { it.play(); call.resolve() }
    @PluginMethod fun arreter(call: PluginCall) = avecControleur { it.stop(); it.clearMediaItems(); call.resolve() }
    @PluginMethod fun suivant(call: PluginCall) = avecControleur { it.seekToNextMediaItem(); call.resolve() }
    @PluginMethod fun precedent(call: PluginCall) = avecControleur { it.seekToPreviousMediaItem(); call.resolve() }
}
```

```kotlin
// android/app/src/main/java/com/vivrelanglais/livre/promenade/PromenadeService.kt
package com.vivrelanglais.livre.promenade

import androidx.annotation.OptIn
import androidx.media3.common.AudioAttributes
import androidx.media3.common.C
import androidx.media3.common.util.UnstableApi
import androidx.media3.exoplayer.ExoPlayer
import androidx.media3.exoplayer.source.DefaultMediaSourceFactory
import androidx.media3.exoplayer.source.MediaSource
import androidx.media3.exoplayer.source.SilenceMediaSource
import androidx.media3.session.MediaSession
import androidx.media3.session.MediaSessionService

@OptIn(UnstableApi::class)
class PromenadeService : MediaSessionService() {
    private var session: MediaSession? = null

    override fun onCreate() {
        super.onCreate()
        val defaut = DefaultMediaSourceFactory(this)
        val fabrique = object : MediaSource.Factory by defaut {
            override fun createMediaSource(item: androidx.media3.common.MediaItem): MediaSource {
                val uri = item.localConfiguration?.uri?.toString().orEmpty()
                return if (uri.startsWith("silence://"))
                    SilenceMediaSource(uri.removePrefix("silence://").toLong() * 1000) // microsecondes
                else defaut.createMediaSource(item)
            }
        }
        val lecteur = ExoPlayer.Builder(this)
            .setMediaSourceFactory(fabrique)
            .setAudioAttributes(AudioAttributes.Builder()
                .setUsage(C.USAGE_MEDIA).setContentType(C.AUDIO_CONTENT_TYPE_SPEECH).build(), true) // gère le focus audio
            .setHandleAudioBecomingNoisy(true)   // pause au débranchement du casque
            .build()
        session = MediaSession.Builder(this, lecteur).build()
    }

    override fun onGetSession(info: MediaSession.ControllerInfo) = session

    override fun onDestroy() {
        session?.run { player.release(); release() }
        session = null
        super.onDestroy()
    }
}
```

Les URL passées à la promenade sont des chemins locaux (`file://` pour les voix installées hors socle ; pour le socle, `asset:///public/voix/...`, schéma lu nativement par ExoPlayer). La page JavaScript construit la liste selon le programme choisi (8.4).

### 10.8 La configuration Capacitor

```ts
// app/capacitor.config.ts
import type { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.vivrelanglais.livre',
  appName: "Vivre l'Anglais",
  webDir: 'build',
  android: {
    path: '../android',
    allowMixedContent: false,
    captureInput: false
  },
  plugins: {
    SplashScreen: { launchAutoHide: false, backgroundColor: '#FBF8F3', showSpinner: false },
    LocalNotifications: { smallIcon: 'ic_stat_plume', iconColor: '#1F3A5F' }
  }
};
export default config;
```

**Affichage bord à bord** : une application qui cible Android 16 ne peut plus s'y soustraire sur les appareils Android 16 (Android Developers — <https://developer.android.com/about/versions/16/behavior-changes-16>). Capacitor 8 n'ajuste plus les marges de la WebView et injecte des variables CSS de zone sûre (`--safe-area-inset-top`, etc.) (guide de migration — <https://dev.to/batmanofweb/capacitor-8-upgrade-for-lovable-apps-jg6>). Règle CSS unique :

```css
/* app/src/lib/design/jetons.css */
:root {
  --zone-haut: var(--safe-area-inset-top, env(safe-area-inset-top, 0px));
  --zone-bas: var(--safe-area-inset-bottom, env(safe-area-inset-bottom, 0px));
  --zone-gauche: var(--safe-area-inset-left, env(safe-area-inset-left, 0px));
  --zone-droite: var(--safe-area-inset-right, env(safe-area-inset-right, 0px));
}
.entete-fixe { padding-top: calc(var(--zone-haut) + 8px); }
.navigation-basse { padding-bottom: calc(var(--zone-bas) + 4px); }
```

L'apparence des icônes de la barre d'état (claires ou sombres) suit le thème via `@capacitor/status-bar` (`StatusBar.setStyle`) à chaque changement de thème.

**Retour prédictif** : sur Android 16, pour une application qui cible Android 16, `onBackPressed` n'est plus appelé et les animations de retour prédictif sont actives par défaut (Android Developers — <https://developer.android.com/about/versions/16/behavior-changes-16>). L'application utilise l'écouteur `backButton` de `@capacitor/app` (10.6). **Critère d'acceptation** : sur un appareil Android 16, le geste retour ferme un volet ouvert, puis remonte l'historique, puis quitte depuis Aujourd'hui. **Plan B prescrit** si ce critère échoue : un `OnBackPressedCallback` enregistré dans `MainActivity` sur `onBackPressedDispatcher`, qui émet l'événement JavaScript `retourDemande` via `bridge.triggerWindowJSEvent("retourDemande")`, l'application web décidant ensuite de l'action.

**Grands écrans** : sur les écrans d'au moins 600 dp de plus petite largeur, Android 16 ignore les verrouillages d'orientation et de proportions pour les applications qui le ciblent (Android Developers — <https://developer.android.com/about/versions/16/behavior-changes-16>). L'ouvrage ne verrouille donc **aucune** orientation et fournit une mise en page adaptative (8.1) testée en portrait, paysage, tablette et appareil pliable.

### 10.9 La couche Android native

#### `android/variables.gradle` (extrait)

```groovy
ext {
    minSdkVersion = 24
    compileSdkVersion = 36
    targetSdkVersion = 36
    media3Version = '1.8.0'          // à confirmer au gel : dernière 1.x stable
    assetDeliveryVersion = '2.3.0'   // à confirmer au gel : dernière 2.x stable
    // les versions AndroidX posées par `npx cap migrate` sont conservées telles quelles
}
```

#### `android/app/build.gradle` (ajouts au fichier généré par Capacitor)

```groovy
android {
    namespace "com.vivrelanglais.livre"
    compileSdk rootProject.ext.compileSdkVersion

    defaultConfig {
        applicationId "com.vivrelanglais.livre"
        minSdkVersion rootProject.ext.minSdkVersion
        targetSdkVersion rootProject.ext.targetSdkVersion
        versionCode((System.getenv("VA_VERSION_CODE") ?: "1").toInteger())
        versionName(System.getenv("VA_VERSION_NAME") ?: "1.0.0")
    }

    buildFeatures { buildConfig true }

    flavorDimensions += "distribution"
    productFlavors {
        play {
            dimension "distribution"
        }
        direct {
            dimension "distribution"
            buildConfigField "String", "CATALOGUE_URL", '"https://voix.vivrelanglais.com/catalogue.json"'
            buildConfigField "String", "CATALOGUE_CLE", '"MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE…"' // clé publique ECDSA P-256 (base64 DER)
        }
    }

    // La liste des paquets de voix n'est jamais écrite ici : tools/generer_paquets.py
    // la produit dans le bloc android { } situé entre les marqueurs // <liste-paquets> (annexe C.6).

    signingConfigs {
        release {
            storeFile file(System.getenv("VA_KEYSTORE") ?: "${rootDir}/../secrets/vivre-anglais-envoi.jks")
            storePassword System.getenv("VA_KEYSTORE_MDP")
            keyAlias System.getenv("VA_CLE_ALIAS") ?: "envoi"
            keyPassword System.getenv("VA_CLE_MDP")
        }
    }

    buildTypes {
        release {
            minifyEnabled true
            shrinkResources true
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
            signingConfig signingConfigs.release
        }
    }

    androidResources {
        noCompress += ['opus', 'json']   // lecture directe sans décompression
    }
}

// <liste-paquets>
android { assetPacks = [":voix_c03", ":voix_c04", "…", ":voix_c26"] }   // produit par generer_paquets.py
// </liste-paquets>

dependencies {
    implementation "androidx.media3:media3-exoplayer:$media3Version"
    implementation "androidx.media3:media3-session:$media3Version"
    playImplementation "com.google.android.play:asset-delivery:$assetDeliveryVersion"
    implementation "androidx.core:core-ktx:$androidxCoreVersion"   // raccourcis (ShortcutManagerCompat)
}
```

`proguard-rules.pro` (ajout) :

```
-keep class com.vivrelanglais.livre.** { *; }
-keep @com.getcapacitor.annotation.CapacitorPlugin class * { *; }
```

#### Les paquets de voix (canal Play)

Google Play impose une limite de 500 Mo pour le module de base, 1,5 Go par paquet d'éléments, 30 Go cumulés pour les paquets « à la demande » et 100 paquets au maximum par bundle (Aide Play Console — <https://support.google.com/googleplay/android-developer/answer/9859372?hl=en>). Répartition retenue :

| Contenu | Emplacement | Taille estimée |
|---|---|---|
| Code, textes, polices, index | Module de base | ≈ 12 Mo |
| Voix du Prélude et des Chapitres 1 et 2 (« socle ») | Module de base, `assets/public/voix/` | ≈ 210 Mo |
| Voix du Chapitre N (3 ≤ N ≤ 26) | Paquet `voix_cNN`, livraison à la demande | 30 à 110 Mo chacun |

Module de paquet généré (`android/voix_c07/build.gradle`) :

```groovy
plugins { id 'com.android.asset-pack' }

assetPack {
    packName = "voix_c07"
    dynamicDelivery { deliveryType = "on-demand" }
}
```

Contenu : `android/voix_c07/src/main/assets/voix/c07/s01/*.opus` (copié depuis `voix/encodes/c07/`). `settings.gradle` reçoit `include ':voix_c07'` pour chaque paquet (généré).

#### Le plugin Voix (Kotlin)

```kotlin
// android/app/src/main/java/com/vivrelanglais/livre/voix/VoixPlugin.kt
package com.vivrelanglais.livre.voix

import com.getcapacitor.*
import com.getcapacitor.annotation.CapacitorPlugin

interface SourceVoix {
    fun etat(chapitre: String): JSObject
    fun faireVenir(chapitre: String, fin: (Throwable?) -> Unit)
    fun retirer(chapitre: String)
}

@CapacitorPlugin(name = "Voix")
class VoixPlugin : Plugin() {
    private lateinit var source: SourceVoix

    override fun load() { source = FabriqueSource.creer(this) }   // définie par saveur (play / direct)

    fun emettre(chapitre: String, octets: Long, total: Long, etat: String) {
        notifyListeners("progression", JSObject()
            .put("chapitre", chapitre).put("octets", octets).put("total", total).put("etat", etat))
    }

    @PluginMethod
    fun etat(call: PluginCall) {
        val ch = call.getString("chapitre") ?: return call.reject("chapitre manquant")
        call.resolve(source.etat(ch))
    }

    @PluginMethod
    fun faireVenir(call: PluginCall) {
        val ch = call.getString("chapitre") ?: return call.reject("chapitre manquant")
        source.faireVenir(ch) { e -> if (e == null) call.resolve() else call.reject(e.message ?: "contretemps") }
    }

    @PluginMethod
    fun retirer(call: PluginCall) {
        val ch = call.getString("chapitre") ?: return call.reject("chapitre manquant")
        source.retirer(ch); call.resolve()
    }
}
```

```kotlin
// android/app/src/play/java/com/vivrelanglais/livre/voix/FabriqueSource.kt
package com.vivrelanglais.livre.voix

import androidx.activity.result.ActivityResultLauncher
import androidx.activity.result.IntentSenderRequest
import com.getcapacitor.JSObject
import com.google.android.play.core.assetpacks.AssetPackManagerFactory
import com.google.android.play.core.assetpacks.AssetPackStateUpdateListener
import com.google.android.play.core.assetpacks.model.AssetPackStatus

object FabriqueSource { fun creer(p: VoixPlugin): SourceVoix = SourcePlay(p) }

class SourcePlay(private val p: VoixPlugin) : SourceVoix {
    private val gestion = AssetPackManagerFactory.getInstance(p.context)
    private val attentes = mutableMapOf<String, (Throwable?) -> Unit>()
    // Le lanceur est enregistré par MainActivity avant son démarrage (exigence d'AndroidX Activity)
    private val confirmation: ActivityResultLauncher<IntentSenderRequest>
        get() = (p.activity as com.vivrelanglais.livre.MainActivity).confirmationPaquets

    private val ecoute = AssetPackStateUpdateListener { s ->
        val ch = s.name().removePrefix("voix_")
        val etat = when (s.status()) {
            AssetPackStatus.COMPLETED -> "installe"
            AssetPackStatus.FAILED, AssetPackStatus.CANCELED -> "absent"
            AssetPackStatus.WAITING_FOR_WIFI, AssetPackStatus.REQUIRES_USER_CONFIRMATION -> "confirmation"
            else -> "en_cours"
        }
        p.emettre(ch, s.bytesDownloaded(), s.totalBytesToDownload(), etat)
        if (etat == "confirmation") gestion.showConfirmationDialog(confirmation)
        if (etat == "installe") attentes.remove(ch)?.invoke(null)
        if (s.status() == AssetPackStatus.FAILED) attentes.remove(ch)?.invoke(IllegalStateException("code ${s.errorCode()}"))
    }
    init { gestion.registerListener(ecoute) }

    override fun etat(chapitre: String): JSObject {
        val lieu = gestion.getPackLocation("voix_$chapitre")
        return if (lieu?.assetsPath() != null) JSObject().put("etat", "installe").put("base", lieu.assetsPath())
        else JSObject().put("etat", "absent")
    }
    override fun faireVenir(chapitre: String, fin: (Throwable?) -> Unit) {
        attentes[chapitre] = fin
        gestion.fetch(listOf("voix_$chapitre"))
    }
    override fun retirer(chapitre: String) { gestion.removePack("voix_$chapitre") }
}
```

```kotlin
// android/app/src/direct/java/com/vivrelanglais/livre/voix/FabriqueSource.kt
package com.vivrelanglais.livre.voix

import android.util.Base64
import com.getcapacitor.JSObject
import com.vivrelanglais.livre.BuildConfig
import org.json.JSONObject
import java.io.File
import java.net.HttpURLConnection
import java.net.URL
import java.security.KeyFactory
import java.security.MessageDigest
import java.security.Signature
import java.security.spec.X509EncodedKeySpec
import java.util.concurrent.Executors
import java.util.zip.ZipInputStream

object FabriqueSource { fun creer(p: VoixPlugin): SourceVoix = SourceDirecte(p) }

class SourceDirecte(private val p: VoixPlugin) : SourceVoix {
    private val racine = File(p.context.filesDir, "voix_paquets")
    private val fil = Executors.newSingleThreadExecutor()

    private fun dossier(ch: String) = File(racine, ch)
    override fun etat(chapitre: String): JSObject {
        val d = dossier(chapitre)
        return if (File(d, ".complet").exists()) JSObject().put("etat", "installe").put("base", d.absolutePath)
        else JSObject().put("etat", "absent")
    }

    private fun lire(url: String): ByteArray =
        (URL(url).openConnection() as HttpURLConnection).run {
            connectTimeout = 15_000; readTimeout = 30_000
            inputStream.use { it.readBytes() }
        }

    private fun verifierSignature(donnees: ByteArray, sig: ByteArray) {
        val cle = KeyFactory.getInstance("EC").generatePublic(
            X509EncodedKeySpec(Base64.decode(BuildConfig.CATALOGUE_CLE, Base64.DEFAULT)))
        val v = Signature.getInstance("SHA256withECDSA").apply { initVerify(cle); update(donnees) }
        require(v.verify(sig)) { "catalogue non authentique" }
    }

    override fun faireVenir(chapitre: String, fin: (Throwable?) -> Unit) = fil.execute {
        try {
            val brut = lire(BuildConfig.CATALOGUE_URL)
            verifierSignature(brut, lire(BuildConfig.CATALOGUE_URL + ".sig"))
            val entree = JSONObject(String(brut)).getJSONObject("chapitres").getJSONObject(chapitre)
            val total = entree.getLong("taille")
            val tmp = File(p.context.cacheDir, "voix_$chapitre.zip")
            val sha = MessageDigest.getInstance("SHA-256")
            racine.mkdirs(); require(racine.usableSpace > total * 12 / 10) { "place insuffisante" }
            (URL(entree.getString("url")).openConnection() as HttpURLConnection).apply {
                connectTimeout = 15_000; readTimeout = 30_000
            }.inputStream.use { ins ->
                tmp.outputStream().use { out ->
                    val tampon = ByteArray(64 * 1024); var lu: Int; var cumul = 0L; var dernier = 0L
                    while (ins.read(tampon).also { lu = it } != -1) {
                        out.write(tampon, 0, lu); sha.update(tampon, 0, lu); cumul += lu
                        val maintenant = System.currentTimeMillis()
                        if (maintenant - dernier >= 250) { dernier = maintenant; p.emettre(chapitre, cumul, total, "en_cours") }
                    }
                }
            }
            val empreinte = sha.digest().joinToString("") { "%02x".format(it) }
            require(empreinte == entree.getString("sha256")) { "archive altérée" }
            val d = dossier(chapitre).apply { deleteRecursively(); mkdirs() }
            ZipInputStream(tmp.inputStream()).use { zip ->
                generateSequence { zip.nextEntry }.forEach { e ->
                    val cible = File(d, e.name)
                    require(cible.canonicalPath.startsWith(d.canonicalPath + File.separator)) { "chemin refusé" }
                    if (e.isDirectory) cible.mkdirs() else { cible.parentFile?.mkdirs(); cible.outputStream().use { zip.copyTo(it) } }
                }
            }
            File(d, ".complet").writeText(entree.getString("version"))
            tmp.delete()
            p.emettre(chapitre, total, total, "installe")
            fin(null)
        } catch (t: Throwable) { p.emettre(chapitre, 0, 0, "absent"); fin(t) }
    }

    override fun retirer(chapitre: String) { dossier(chapitre).deleteRecursively() }
}
```

Enregistrement des plugins locaux dans `MainActivity.kt` :

```kotlin
package com.vivrelanglais.livre

import android.os.Bundle
import androidx.activity.result.ActivityResultLauncher
import androidx.activity.result.IntentSenderRequest
import androidx.activity.result.contract.ActivityResultContracts
import com.getcapacitor.BridgeActivity
import com.vivrelanglais.livre.accueil.RaccourcisPlugin
import com.vivrelanglais.livre.promenade.PromenadePlugin
import com.vivrelanglais.livre.voix.VoixPlugin

class MainActivity : BridgeActivity() {
    /** Confirmation d'un téléchargement de paquet sur réseau mobile (enregistré avant STARTED). */
    val confirmationPaquets: ActivityResultLauncher<IntentSenderRequest> =
        registerForActivityResult(ActivityResultContracts.StartIntentSenderForResult()) { }

    override fun onCreate(savedInstanceState: Bundle?) {
        registerPlugin(VoixPlugin::class.java)
        registerPlugin(PromenadePlugin::class.java)
        registerPlugin(RaccourcisPlugin::class.java)
        super.onCreate(savedInstanceState)
    }
}
```

#### `AndroidManifest.xml` (éléments ajoutés)

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.RECORD_AUDIO" />
    <uses-permission android:name="android.permission.POST_NOTIFICATIONS" />
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE_MEDIA_PLAYBACK" />
    <uses-permission android:name="android.permission.WAKE_LOCK" />

    <application
        android:allowBackup="true"
        android:fullBackupContent="@xml/sauvegarde"
        android:dataExtractionRules="@xml/extraction_donnees"
        android:networkSecurityConfig="@xml/securite_reseau"
        android:enableOnBackInvokedCallback="true"
        android:label="@string/app_name"
        android:icon="@mipmap/ic_launcher"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:theme="@style/AppTheme">

        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:launchMode="singleTask"
            android:configChanges="orientation|keyboardHidden|keyboard|screenSize|locale|smallestScreenSize|screenLayout|uiMode|navigation|density"
            android:theme="@style/AppTheme.NoActionBarLaunch">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

        <service
            android:name=".promenade.PromenadeService"
            android:exported="true"
            android:foregroundServiceType="mediaPlayback">
            <intent-filter>
                <action android:name="androidx.media3.session.MediaSessionService" />
            </intent-filter>
        </service>
    </application>
</manifest>
```

`res/xml/securite_reseau.xml` :

```xml
<network-security-config>
    <base-config cleartextTrafficPermitted="false" />
</network-security-config>
```

`res/xml/extraction_donnees.xml` (Android 12 et plus) et `res/xml/sauvegarde.xml` (Android 7 à 11) :

```xml
<data-extraction-rules>
    <cloud-backup>
        <include domain="file" path="carnet/" />
    </cloud-backup>
    <device-transfer>
        <include domain="file" path="carnet/" />
        <include domain="file" path="ma_voix/" />
    </device-transfer>
</data-extraction-rules>
```

```xml
<full-backup-content>
    <include domain="file" path="carnet/" />
</full-backup-content>
```

Les voix installées ne sont jamais sauvegardées (elles se réinstallent). Les enregistrements du lecteur (« Ma voix ») ne vont jamais dans la sauvegarde en ligne ; ils suivent seulement un transfert direct d'appareil à appareil.

#### Icônes

- Icône adaptative (premier plan, arrière-plan) et **icône monochrome** pour les icônes à thème d'Android 13 et plus (`<monochrome android:drawable="@drawable/ic_launcher_monochrome"/>` dans `mipmap-anydpi-v26/ic_launcher.xml`).
- Génération des tailles : `npx @capacitor/assets generate --android` à partir de `assets/icon-foreground.png`, `icon-background.png`, `splash.png`, `splash-dark.png` (1024 × 1024 minimum pour l'icône, 2732 × 2732 pour l'écran d'ouverture).
- Petite icône de notification `ic_stat_plume` (blanc sur transparent, 24 dp).

### 10.10 Le stockage local

| Donnée | Lieu | Détail |
|---|---|---|
| Progression, retrouvailles (état FSRS et journal), marque-pages, notes | IndexedDB (Dexie), base `vivre` | Tables : `progression`, `cartes`, `journal`, `marques`, `notes`, `constance`, `versions`, `itineraires`, `contretemps` |
| Préférences | `@capacitor/preferences` | Accès synchrone au démarrage (thème, taille, accent) pour éviter tout clignotement |
| Copie de sûreté du carnet | `@capacitor/filesystem`, `Directory.Data`, `carnet/sauvegarde.json` | Écrite 10 s après toute modification (regroupement), incluse dans la sauvegarde Android |
| Ma voix et Ma version | `Directory.Data`, `ma_voix/{id}-{horodatage}.m4a` ; textes de Ma version dans la table `versions` | Effaçable en un geste |
| Itinéraires suivis | IndexedDB, table `itineraires` | Étape en cours, date de début |
| Journal des contretemps | IndexedDB, table `contretemps` (200 entrées, rotation) | Horodatage, code, écran ; aucune donnée personnelle |
| Expressions du widget | `Directory.Data`, `accueil/expressions.json` | Réécrit à chaque fin de session (10.20) |
| Voix installées | Paquets Play ou `files/voix_paquets/` | Gérées par le plugin Voix |

Au démarrage, si la base IndexedDB est vide et qu'une copie de sûreté existe (restauration après réinstallation), le carnet est reconstitué automatiquement : « Votre carnet a été retrouvé. »

Format d'export « Mettre mon carnet à l'abri » : fichier `.vivre` = JSON compressé (gzip) contenant `{ format: 1, edition, date, progression, cartes, journal, marques, notes, constance, itineraires, versions, preferences }` (les enregistrements de « Ma version » sont ajoutés en option, encodés en base64).

### 10.11 La recherche

- Index MiniSearch pré-calculé à la compilation (champs : `en`, `fr`, `usage`, `titre`), sérialisé en JSON, chargé au premier usage (≈ 6 Mo pour l'ouvrage complet, en deux fichiers).
- `processTerm` : minuscules, suppression des diacritiques, apostrophes normalisées (’ → '), formes contractées indexées aussi sous leur forme pleine (*don't* ↔ *do not*).
- Pondération : `en` ×3, `fr` ×3, `titre` ×2, `usage` ×1 ; recherche floue 0,2 pour les termes de 5 lettres et plus ; préfixe activé.
- Temps de réponse ≤ 50 ms sur l'appareil de référence.

### 10.12 Budgets de performance (bloquants)

| Mesure | Budget | Appareil de référence |
|---|---|---|
| Démarrage à froid jusqu'à « Aujourd'hui » affiché | ≤ 1,5 s | Téléphone milieu de gamme Android 14, 4 Go de mémoire (par exemple Samsung Galaxy A15) |
| Ouverture d'une scène | ≤ 300 ms | idem |
| Latence toucher → premier son (voix préparée) | ≤ 120 ms (objectif 60 ms) | idem |
| Latence toucher → premier son (voix non préparée) | ≤ 250 ms | idem |
| Défilement | 95 % des images < 16,7 ms ; aucune > 50 ms | idem |
| JavaScript initial (compressé) | ≤ 150 Ko | — |
| Mémoire en lecture | ≤ 250 Mo | idem |
| APK direct | ≤ 240 Mo | — |
| Module de base Play | ≤ 240 Mo (limite Play : 500 Mo) | — |
| Android 7.0 (API 24) | Fonctionnel, budgets × 1,5 tolérés | Émulateur API 24 + WebView à jour |

### 10.13 Sécurité et confidentialité

- Aucune bibliothèque de mesure d'audience, de publicité ou de suivi.
- Aucune requête réseau, sauf : faire venir les voix (paquets Play ou serveur de l'éditeur, en HTTPS) et, pour le canal direct, la vérification hebdomadaire d'une nouvelle édition (`version.json` signé). Le partage d'une expression et le signalement d'une coquille passent par la feuille de partage d'Android : c'est l'application choisie par le lecteur qui envoie, jamais l'ouvrage.
- Politique de sécurité du contenu stricte (10.6) ; aucun code distant ; débogage de la WebView désactivé en version publiée.
- Catalogue de voix signé (ECDSA P-256) et archives vérifiées par empreinte SHA-256 ; protection contre l'écriture hors dossier lors de la décompression.
- Micro : demandé uniquement à la première ouverture du miroir, avec le microtexte 3.5.
- Notifications : permission demandée uniquement si le lecteur choisit un rendez-vous.
- `lexique_verifier.py` et `valider_corpus.py` sont aussi des garde-fous de qualité : aucune scène incomplète ne peut être publiée.

### 10.14 Compiler l'APK de bout en bout (procédure exacte)

#### Étape 0 — Préparer le poste (Ubuntu 24.04 ; équivalents macOS et Windows dans `docs/poste.md`)

```bash
# Node.js 22
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs
# Java 21
sudo apt-get install -y openjdk-21-jdk
# Python, ffmpeg (avec libopus), outils
sudo apt-get install -y python3.12 python3.12-venv ffmpeg unzip zip git
# SDK Android (outils en ligne de commande)
mkdir -p "$HOME/Android/Sdk/cmdline-tools" && cd "$HOME/Android/Sdk/cmdline-tools"
# Télécharger « Command line tools only » depuis https://developer.android.com/studio, puis :
unzip commandlinetools-linux-*_latest.zip && mv cmdline-tools latest
export ANDROID_HOME="$HOME/Android/Sdk"
export PATH="$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools:$ANDROID_HOME/build-tools/36.0.0:$PATH"
yes | sdkmanager --licenses
sdkmanager "platform-tools" "platforms;android-36" "build-tools;36.0.0"
# Vérifications
node -v      # v22.x
java -version  # 21
```

#### Étape 1 — Initialisation du projet (une seule fois, à la création du dépôt)

```bash
npx sv create app --template minimal --types ts
cd app
npm i -D @sveltejs/adapter-static @capacitor/cli @capacitor/assets vitest @playwright/test @axe-core/playwright
npm i @capacitor/core @capacitor/android @capacitor/app @capacitor/filesystem @capacitor/haptics \
      @capacitor/local-notifications @capacitor/preferences @capacitor/share @capacitor/splash-screen \
      @capacitor/status-bar @capgo/capacitor-audio-recorder dexie minisearch ts-fsrs
npx cap init "Vivre l'Anglais" com.vivrelanglais.livre --web-dir build
npx cap add android          # crée ../android grâce à android.path
```

#### Étape 2 — Contenu et voix

```bash
cd vivre-anglais
python3.12 -m venv .venv && . .venv/bin/activate
pip install -r tools/requirements.txt      # pyyaml, jsonschema, boto3
python3 tools/voix_recuperer.py --tout      # masters encodés depuis le stockage objet → voix/encodes/
python3 tools/construire.py --strict        # validations, JSON, index, couverture vocale
python3 tools/voix_recuperer.py --socle     # copie Prélude + Ch. 1–2 dans app/static/voix/
python3 tools/generer_paquets.py            # android/voix_c03 … voix_c26 + settings.gradle
```

#### Étape 3 — Application web

```bash
cd app
npm ci
npm run check        # svelte-check (types)
npm run test         # vitest
npm run build        # → app/build/
npm run e2e          # playwright sur le build
npx cap sync android # copie build/ dans android/app/src/main/assets/public + plugins
```

#### Étape 4 — Compilation Android

```bash
cd ../android
export VA_KEYSTORE="$HOME/secrets/vivre-anglais-envoi.jks"
export VA_KEYSTORE_MDP='…' VA_CLE_ALIAS='envoi' VA_CLE_MDP='…'
export VA_VERSION_CODE=1001 VA_VERSION_NAME=1.0.0
./gradlew --no-daemon clean assembleDirectRelease bundlePlayRelease
```

Produits :

| Fichier | Usage |
|---|---|
| `android/app/build/outputs/apk/direct/release/app-direct-release.apk` | **APK signé** à distribuer directement |
| `android/app/build/outputs/bundle/playRelease/app-play-release.aab` | Bundle à envoyer sur Google Play |

#### Étape 5 — Vérifications

```bash
apksigner verify --verbose --print-certs app/build/outputs/apk/direct/release/app-direct-release.apk
aapt2 dump badging app/build/outputs/apk/direct/release/app-direct-release.apk | grep -E "package|sdkVersion|targetSdkVersion"
# Doit afficher : package: name='com.vivrelanglais.livre' … sdkVersion:'24' targetSdkVersion:'36'
adb install -r app/build/outputs/apk/direct/release/app-direct-release.apk
# Tester le bundle Play en local avec ses paquets de voix :
java -jar bundletool.jar build-apks --bundle=app/build/outputs/bundle/playRelease/app-play-release.aab \
  --output=play.apks --local-testing --ks="$VA_KEYSTORE" --ks-key-alias=envoi \
  --ks-pass=pass:"$VA_KEYSTORE_MDP" --key-pass=pass:"$VA_CLE_MDP"
java -jar bundletool.jar install-apks --apks=play.apks
```

### 10.15 La signature

```bash
# Clé d'envoi Play (une fois, conservée dans deux coffres distincts)
keytool -genkeypair -v -keystore vivre-anglais-envoi.jks -alias envoi \
  -keyalg RSA -keysize 4096 -validity 10000 \
  -dname "CN=Vivre l'Anglais, O=Editeur, C=CI"
# Clé du canal direct (distincte : Google signe les versions Play avec sa propre clé d'application)
keytool -genkeypair -v -keystore vivre-anglais-direct.jks -alias direct \
  -keyalg RSA -keysize 4096 -validity 10000 \
  -dname "CN=Vivre l'Anglais Direct, O=Editeur, C=CI"
# Clé du catalogue de voix (canal direct)
openssl ecparam -name prime256v1 -genkey -noout -out catalogue-prive.pem
openssl ec -in catalogue-prive.pem -pubout -outform DER | base64 -w0   # → CATALOGUE_CLE
```

- La saveur `direct` est signée avec `vivre-anglais-direct.jks` (variables `VA_KEYSTORE`, `VA_CLE_ALIAS=direct` dans une étape de compilation séparée) ; la saveur `play` avec la clé d'envoi.
- Conséquence assumée et annoncée sur la page de téléchargement : un lecteur ne peut pas passer d'une installation directe à une installation Play sans désinstaller (la copie « Mettre mon carnet à l'abri » permet de conserver sa progression).
- Perte de clé directe = impossibilité définitive de mettre à jour les installations directes : deux copies chiffrées, dans deux lieux, plus une copie papier des mots de passe.

### 10.16 L'intégration continue

Les masters audio ne sont **pas** dans Git ; ils résident dans un stockage objet compatible S3 (versionné), synchronisé par `tools/voix_recuperer.py`.

```yaml
# .github/workflows/android.yml
name: android
on:
  push: { branches: [main] }
  workflow_dispatch: {}
jobs:
  compiler:
    runs-on: ubuntu-24.04
    timeout-minutes: 90
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: npm, cache-dependency-path: app/package-lock.json }
      - uses: actions/setup-java@v4
        with: { distribution: temurin, java-version: 21 }
      - uses: android-actions/setup-android@v3
      - run: sdkmanager "platforms;android-36" "build-tools;36.0.0"
      - uses: actions/setup-python@v5
        with: { python-version: '3.12' }
      - run: sudo apt-get update && sudo apt-get install -y ffmpeg && pip install -r tools/requirements.txt
      - name: Voix
        env:
          VOIX_S3_URL: ${{ secrets.VOIX_S3_URL }}
          VOIX_S3_CLE: ${{ secrets.VOIX_S3_CLE }}
          VOIX_S3_SECRET: ${{ secrets.VOIX_S3_SECRET }}
        run: python3 tools/voix_recuperer.py --tout
      - run: python3 tools/construire.py --strict
      - run: python3 tools/voix_recuperer.py --socle && python3 tools/generer_paquets.py
      - name: Application web
        working-directory: app
        run: |
          npm ci
          npm run check
          npm run test
          npm run build
          npx playwright install --with-deps chromium
          npm run e2e
          npx cap sync android
      - name: Numéro de version
        run: echo "VA_VERSION_CODE=$((1000 + GITHUB_RUN_NUMBER))" >> "$GITHUB_ENV"
      - name: Clés
        run: |
          echo "${{ secrets.VA_ENVOI_JKS_B64 }}" | base64 -d > "$RUNNER_TEMP/envoi.jks"
          echo "${{ secrets.VA_DIRECT_JKS_B64 }}" | base64 -d > "$RUNNER_TEMP/direct.jks"
      - name: Bundle Play
        working-directory: android
        env:
          VA_KEYSTORE: ${{ runner.temp }}/envoi.jks
          VA_KEYSTORE_MDP: ${{ secrets.VA_ENVOI_MDP }}
          VA_CLE_ALIAS: envoi
          VA_CLE_MDP: ${{ secrets.VA_ENVOI_MDP }}
          VA_VERSION_NAME: 1.0.${{ github.run_number }}
        run: ./gradlew --no-daemon bundlePlayRelease
      - name: APK direct
        working-directory: android
        env:
          VA_KEYSTORE: ${{ runner.temp }}/direct.jks
          VA_KEYSTORE_MDP: ${{ secrets.VA_DIRECT_MDP }}
          VA_CLE_ALIAS: direct
          VA_CLE_MDP: ${{ secrets.VA_DIRECT_MDP }}
          VA_VERSION_NAME: 1.0.${{ github.run_number }}
        run: ./gradlew --no-daemon assembleDirectRelease
      - name: Vérifier
        run: |
          apksigner verify --print-certs android/app/build/outputs/apk/direct/release/app-direct-release.apk
          sha256sum android/app/build/outputs/apk/direct/release/app-direct-release.apk > apk.sha256
      - uses: actions/upload-artifact@v4
        with:
          name: vivre-anglais-${{ env.VA_VERSION_CODE }}
          path: |
            android/app/build/outputs/apk/direct/release/app-direct-release.apk
            android/app/build/outputs/bundle/playRelease/app-play-release.aab
            apk.sha256
            rapport-couverture.md
```

Un second flux (`contenu.yml`) s'exécute à chaque modification de `corpus/` : validations, lexique, phrasé, couverture ; il commente la demande de fusion avec le rapport.

### 10.17 Publication sur Google Play

1. **Compte développeur** et création de l'application `com.vivrelanglais.livre`.
2. **Format** : les nouvelles applications doivent être envoyées en AAB avec la signature d'application par Play (référence Capgo — <https://github.com/Cap-go/capgo-skills/blob/main/skills/capacitor-app-store/SKILL.md>).
3. **Niveau d'API cible** : API 36 obligatoire pour toute nouvelle application et mise à jour depuis le 31 août 2026 (Aide Play Console — <https://support.google.com/googleplay/android-developer/answer/11926878?hl=en>).
4. **Test fermé** : les comptes personnels créés après le 13 novembre 2023 doivent mener un test fermé avec au moins 12 testeurs inscrits pendant 14 jours consécutifs avant la production (référence Capgo — <https://github.com/Cap-go/capgo-skills/blob/main/skills/capacitor-app-store/SKILL.md>). Le test fermé est mené avec un panel d'au moins 20 lecteurs francophones de niveaux variés (pour garder 12 inscrits actifs sur 14 jours), recrutés avant la première soumission.
5. **Pages de 16 Ko** : la contrainte vise les bibliothèques natives `.so` des applications ciblant Android 15 et plus (référence Capgo — <https://github.com/Cap-go/capgo-skills/blob/main/skills/capacitor-app-store/SKILL.md>) ; l'ouvrage n'en embarque pas en propre, mais chaque dépendance est contrôlée avant publication (rapport de l'outil d'analyse d'APK d'Android Studio).
6. **Sécurité des données** : « Aucune donnée collectée, aucune donnée partagée » (le traitement du micro reste sur l'appareil ; aucune donnée ne quitte le téléphone).
7. **Classification du contenu** : déclarer honnêtement le langage grossier présent au Chapitre 22.4 (masqué par défaut) ; viser une classification adolescents.
8. **Fiche** : titre « Vivre l'Anglais » ; description courte (≤ 80 caractères) : « L'anglais du quotidien, dit par de vraies voix américaines et britanniques. » ; description longue rédigée selon la charte (section 3) ; captures téléphone et tablette en thèmes Papier et Nuit ; bande-annonce sonore de 30 s.
9. **Déploiement progressif** : 5 % → 20 % → 50 % → 100 %, à 48 heures d'intervalle, si le taux de plantage reste inférieur à 0,2 % des sessions et le taux d'ANR à 0,1 %.

### 10.18 Distribution directe de l'APK

- Page de téléchargement de l'éditeur : APK, empreinte SHA-256, empreinte du certificat de signature, instructions d'installation (autorisation « installer des applications inconnues » pour le navigateur utilisé).
- Voix des Chapitres 3 à 26 : servies par `https://voix.vivrelanglais.com/` :

```json
// catalogue.json (signé : catalogue.json.sig)
{
  "format": 1,
  "edition": "1.0.0",
  "chapitres": {
    "c03": { "version": "3", "url": "https://voix.vivrelanglais.com/voix_c03_v3.zip", "taille": 61234567, "sha256": "…" },
    "c04": { "version": "1", "url": "https://voix.vivrelanglais.com/voix_c04_v1.zip", "taille": 40211876, "sha256": "…" }
  }
}
```

```bash
# Fabrication d'une archive de chapitre (sans recompression : l'Opus est déjà compressé)
cd voix/encodes_pour_archives && zip -0 -r ../../dist/voix_c03_v3.zip voix/c03
sha256sum ../../dist/voix_c03_v3.zip
openssl dgst -sha256 -sign catalogue-prive.pem -out catalogue.json.sig catalogue.json
```

- Nouvelle édition : l'application lit `version.json` (signé de la même manière) au plus une fois par semaine si le réseau est disponible ; si une édition plus récente existe : « Une nouvelle édition de l'ouvrage est disponible. » → ouvre la page de téléchargement dans le navigateur. Aucune installation silencieuse.

### 10.19 Versions de l'ouvrage

| Élément | Règle |
|---|---|
| `versionName` | `MAJEUR.MINEUR.CORRECTIF` — majeur : refonte ; mineur : nouveaux chapitres ; correctif : corrections |
| `versionCode` | `1000 + numéro d'exécution de l'intégration continue` (strictement croissant) |
| Version de scène | Entier dans le YAML, incrémenté à toute modification de texte ; un manifeste de voix porte la version de la scène qu'il couvre |
| Version des paquets de voix | Incrémentée à toute recréation de voix ; Play : livrée avec la mise à jour ; direct : nouvelle entrée du catalogue, proposée au lecteur (« Des voix du chapitre 7 ont été retouchées. Les faire venir ? ») |
| Migration des données locales | Schéma Dexie versionné ; toute montée de version comporte une migration testée |

### 10.20 Le widget, les raccourcis et les liens profonds

#### Les adresses internes

| Adresse | Ouvre |
|---|---|
| `vivrelanglais://expression/{id}` | La scène de l'expression, carte centrée ; `?ecouter=1` lance la voix de l'accent préféré |
| `vivrelanglais://scene/{id}` | La scène |
| `vivrelanglais://retrouvailles` | Les retrouvailles du jour |
| `vivrelanglais://promenade` | La promenade, programme « Reprendre » |
| `vivrelanglais://reprendre` | La dernière scène, à la dernière position |
| `vivrelanglais://recherche` | Comment dit-on… ? |
| `https://vivrelanglais.com/e/{id}` | Identique à `expression/{id}` (lien d'application vérifié) |

Côté web, `app/src/lib/liens/liens.ts` écoute `App.addListener('appUrlOpen', …)` et `App.getLaunchUrl()` au démarrage, valide l'identifiant contre le sommaire (toute adresse inconnue ouvre Aujourd'hui, sans message d'erreur) et navigue. Le lancement de la voix attend la première interaction possible du contexte audio : si le système refuse la lecture automatique, la carte affiche ◉ en surbrillance.

#### `AndroidManifest.xml` (compléments)

```xml
<activity android:name=".MainActivity" ...>
    <!-- adresses internes -->
    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <data android:scheme="vivrelanglais" />
    </intent-filter>
    <!-- liens d'application vérifiés (fichier assetlinks.json publié sur vivrelanglais.com) -->
    <intent-filter android:autoVerify="true">
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <data android:scheme="https" android:host="vivrelanglais.com" android:pathPrefix="/e/" />
    </intent-filter>
    <meta-data android:name="android.app.shortcuts" android:resource="@xml/raccourcis" />
</activity>

<receiver android:name=".accueil.ExpressionDuJour" android:exported="false">
    <intent-filter>
        <action android:name="android.appwidget.action.APPWIDGET_UPDATE" />
    </intent-filter>
    <meta-data android:name="android.appwidget.provider" android:resource="@xml/expression_du_jour" />
</receiver>
```

Le fichier `https://vivrelanglais.com/.well-known/assetlinks.json` déclare l'empreinte SHA-256 des **deux** certificats concernés : la clé de signature de l'application gérée par Google Play (canal Play) et la clé de la distribution directe (10.15).

#### `res/xml/raccourcis.xml`

```xml
<shortcuts xmlns:android="http://schemas.android.com/apk/res/android">
    <shortcut android:shortcutId="reprendre" android:icon="@drawable/rac_livre"
              android:shortcutShortLabel="@string/rac_reprendre">
        <intent android:action="android.intent.action.VIEW" android:data="vivrelanglais://reprendre" />
    </shortcut>
    <shortcut android:shortcutId="retrouvailles" android:icon="@drawable/rac_carnet"
              android:shortcutShortLabel="@string/rac_retrouvailles">
        <intent android:action="android.intent.action.VIEW" android:data="vivrelanglais://retrouvailles" />
    </shortcut>
    <shortcut android:shortcutId="promenade" android:icon="@drawable/rac_casque"
              android:shortcutShortLabel="@string/rac_promenade">
        <intent android:action="android.intent.action.VIEW" android:data="vivrelanglais://promenade" />
    </shortcut>
    <shortcut android:shortcutId="recherche" android:icon="@drawable/rac_loupe"
              android:shortcutShortLabel="@string/rac_recherche">
        <intent android:action="android.intent.action.VIEW" android:data="vivrelanglais://recherche" />
    </shortcut>
</shortcuts>
```

Libellés (`res/values/strings.xml`) : « Reprendre la lecture », « Les retrouvailles », « La promenade », « Comment dit-on… ? ».

#### `res/xml/expression_du_jour.xml`

```xml
<appwidget-provider xmlns:android="http://schemas.android.com/apk/res/android"
    android:minWidth="250dp" android:minHeight="40dp"
    android:targetCellWidth="4" android:targetCellHeight="1"
    android:resizeMode="horizontal|vertical"
    android:updatePeriodMillis="0"
    android:initialLayout="@layout/expression_du_jour"
    android:previewLayout="@layout/expression_du_jour"
    android:description="@string/widget_description"
    android:widgetCategory="home_screen" />
```

#### Le fournisseur du widget (Kotlin)

```kotlin
// android/app/src/main/java/com/vivrelanglais/livre/accueil/ExpressionDuJour.kt
package com.vivrelanglais.livre.accueil

import android.app.PendingIntent
import android.appwidget.AppWidgetManager
import android.appwidget.AppWidgetProvider
import android.content.Context
import android.content.Intent
import android.net.Uri
import android.widget.RemoteViews
import com.vivrelanglais.livre.R
import org.json.JSONObject
import java.io.File

class ExpressionDuJour : AppWidgetProvider() {
    override fun onUpdate(ctx: Context, gestion: AppWidgetManager, ids: IntArray) {
        val e = choisir(ctx) ?: return
        for (id in ids) {
            val vues = RemoteViews(ctx.packageName, R.layout.expression_du_jour).apply {
                setTextViewText(R.id.enonce, e.getString("en"))
                setTextViewText(R.id.sens, e.getString("sens"))
                setTextViewText(R.id.accent, if (e.getString("accent") == "uk") "Brit." else "Am.")
                setOnClickPendingIntent(R.id.enonce, ouvrir(ctx, "vivrelanglais://expression/${e.getString("id")}?ecouter=1", 1))
                setOnClickPendingIntent(R.id.cadre, ouvrir(ctx, "vivrelanglais://expression/${e.getString("id")}", 2))
            }
            gestion.updateAppWidget(id, vues)
        }
    }

    /** Lit la liste écrite par l'application (files/accueil/expressions.json) ; une expression par jour, bascule à 4 h. */
    private fun choisir(ctx: Context): JSONObject? {
        val f = File(ctx.filesDir, "accueil/expressions.json")
        if (!f.exists()) return null
        val liste = JSONObject(f.readText()).getJSONArray("expressions")
        if (liste.length() == 0) return null
        val jour = (System.currentTimeMillis() + java.util.TimeZone.getDefault().getOffset(System.currentTimeMillis()) - 4 * 3_600_000L) / 86_400_000L
        return liste.getJSONObject((jour % liste.length()).toInt())
    }

    private fun ouvrir(ctx: Context, adresse: String, code: Int) = PendingIntent.getActivity(
        ctx, code, Intent(Intent.ACTION_VIEW, Uri.parse(adresse)).setPackage(ctx.packageName),
        PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE)
}
```

L'application écrit `files/accueil/expressions.json` (via `@capacitor/filesystem`, `Directory.Data`) à chaque fin de session : jusqu'à 60 expressions tirées selon le réglage « L'écran d'accueil » (8.10), puis appelle la méthode `rafraichir` du petit plugin `RaccourcisPlugin`, qui envoie `APPWIDGET_UPDATE` au fournisseur. Un `WorkManager` périodique (24 h, contraintes nulles) déclenche aussi la mise à jour, pour que le widget change chaque jour même sans ouverture de l'ouvrage.

```kotlin
// android/app/src/main/java/com/vivrelanglais/livre/accueil/RaccourcisPlugin.kt
package com.vivrelanglais.livre.accueil

import android.appwidget.AppWidgetManager
import android.content.ComponentName
import android.content.Intent
import androidx.work.*
import com.getcapacitor.*
import com.getcapacitor.annotation.CapacitorPlugin
import java.util.concurrent.TimeUnit

@CapacitorPlugin(name = "Accueil")
class RaccourcisPlugin : Plugin() {
    override fun load() {
        WorkManager.getInstance(context).enqueueUniquePeriodicWork(
            "expression_du_jour", ExistingPeriodicWorkPolicy.KEEP,
            PeriodicWorkRequestBuilder<Rafraichir>(24, TimeUnit.HOURS).build())
    }

    @PluginMethod
    fun rafraichir(call: PluginCall) { Rafraichir.envoyer(context); call.resolve() }

    class Rafraichir(ctx: android.content.Context, p: WorkerParameters) : Worker(ctx, p) {
        override fun doWork(): Result { envoyer(applicationContext); return Result.success() }
        companion object {
            fun envoyer(ctx: android.content.Context) {
                val gestion = AppWidgetManager.getInstance(ctx)
                val ids = gestion.getAppWidgetIds(ComponentName(ctx, ExpressionDuJour::class.java))
                if (ids.isEmpty()) return
                ctx.sendBroadcast(Intent(AppWidgetManager.ACTION_APPWIDGET_UPDATE)
                    .setClass(ctx, ExpressionDuJour::class.java)
                    .putExtra(AppWidgetManager.EXTRA_APPWIDGET_IDS, ids))
            }
        }
    }
}
```

Dépendance ajoutée : `implementation "androidx.work:work-runtime-ktx:2.10.+"` (version exacte figée au gel). Le même `WorkManager` porte la vérification mensuelle des voix (10.21).

### 10.21 L'intégrité et la réparation des voix

- Chaque manifeste de scène porte l'empreinte SHA-256 de chaque fichier (7.11).
- **Au démarrage** : aucune vérification complète (budget 10.12) ; seule la présence du manifeste de chaque chapitre installé est contrôlée.
- **Une fois par mois, téléphone en charge et inactif** (`WorkManager`, contraintes `requiresCharging` et `requiresDeviceIdle`) : vérification de toutes les empreintes des chapitres installés hors socle, dans un fil d'arrière-plan.
- **À la lecture** : un échec de décodage (`decodeAudioData` rejeté) marque le fichier comme abîmé dans le journal des contretemps.
- **Réparation** : un chapitre dont au moins un fichier est abîmé est retiré puis refait venir automatiquement à la prochaine connexion Wi-Fi (canal direct) ou par une nouvelle demande `fetch` du paquet (canal Play) ; le lecteur en est informé par la phrase de 8.12. Le socle, inclus dans le module de base, n'est jamais abîmé sans que tout l'APK le soit ; une réinstallation est alors proposée.

### 10.22 Le précalcul des courbes, des syllabes et des segments

Tout ce qui est affiché en même temps que la voix est calculé **à la compilation**, jamais sur le téléphone :

| Donnée | Outil | Format dans le manifeste | Usage |
|---|---|---|---|
| Instants des mots | Montreal Forced Aligner 3 (`aligner.py`) | `mots: [texte, début, fin]` en secondes, 2 décimales | Surlignage synchronisé, écoute au mot (8.14) |
| Syllabes et accents | `syllaber.py` | `syllabes: [début, fin, forte]` | Illumination du phrasé, battement (8.15) |
| Courbe mélodique | `courbe.py` (`parselmouth`) | `courbe` : octets base64, un point toutes les 10 ms, 0 = silence, 1–255 = demi-tons relatifs | La courbe (8.15), référence du miroir (8.5) |

Contrôles automatiques (`controler.py`) : chaque mot aligné dure entre 40 ms et 1,5 s ; la somme des mots couvre au moins 85 % de la durée parlée ; au moins une syllabe forte par énoncé ; courbe non vide sur au moins 50 % de la durée. Tout écart renvoie le fichier en contrôle manuel (porte P4).

---

## 11. Assurance qualité et critères d'acceptation

### 11.1 Les sept portes

Aucune scène, aucune voix, aucune édition ne franchit une porte sans en remplir tous les critères. Chaque porte produit un rapport daté, archivé avec la scène.

| Porte | Objet | Critères bloquants | Preuve archivée |
|---|---|---|---|
| P1 — Texte | Scène rédigée | Validations 10.4 sans erreur ; densité ≥ minimum 4.5 ; 100 % des déclinaisons traduites ; lexique conforme (charte 3) | Éditeur pédagogique |
| P2 — Langue | Scène relue | Double relecture native (Am. et Brit.) ; chaque énoncé marqué « naturel » dans les deux accents ou régionalisé ; versions localisées de la scène vivante validées | Rapport de relecture |
| P3 — Voix | Prises | Prise retenue pour chacune des 4 versions ; tous les contrôles bloquants 7.10 passés ; écoute comparative du lot conforme | Registre des prises |
| P4 — Son | Fichiers finis | Lot normalisé à −18 LUFS intégrés (± 1 LU), crête vraie ≤ −1,5 dBTP (tolérance −1,0), silence de tête 60 ms et de queue 200 ms (± 20 ms), Opus conforme 7.9, nom et manifeste conformes, champs `mots`, `syllabes`, `courbe` valides (10.22) ; contrôle automatique `voix/outils/controler.py` | Rapport `controler.py` |
| P5 — Phrasé | Transcriptions | Quatre phrasés écrits **à l'écoute** de la prise retenue ; `phrase_verifier.py` sans erreur ; contre-écoute indépendante sur 20 % des énoncés tirés au hasard (taux d'écart ≤ 2 %, sinon reprise de toute la scène) | Rapport de phrasé |
| P6 — Ouvrage | Scène intégrée | Couverture vocale 100 % (voix du sens comprise) ; rendu vérifié dans les quatre thèmes et à 200 % de taille de texte ; parcours complet joué sur un appareil réel | Rapport d'intégration |
| P7 — Édition | Version publiée | Tous les tests automatiques verts ; matrice d'appareils 11.3 validée ; budgets 10.12 tenus ; check-list Annexe E cochée | Check-list signée |

### 11.2 Les tests automatiques

| Niveau | Outil | Couverture exigée |
|---|---|---|
| Unitaires (moteur des voix, retrouvailles, recherche, stockage, migrations) | Vitest | ≥ 90 % des lignes de `src/lib/voix`, `src/lib/retrouvailles`, `src/lib/stockage` |
| Composants (pupitre, carte d'expression, lecteur de scène vivante) | Vitest + Testing Library | Tous les états : chargement, lecture, voix absente, contretemps |
| Parcours web | Playwright (Chromium, gabarit 412 × 915) | Premier lancement, lecture d'une scène complète, recherche, retrouvailles, changement d'accent et de rythme, export du carnet |
| Accessibilité | axe-core via Playwright | Zéro violation « serious » ou « critical » sur chaque écran |
| Contrastes | `tools/contrastes.py` sur les jetons des quatre thèmes | Texte ≥ 4,5:1 (≥ 7:1 en thème Contraste) ; grands textes et icônes ≥ 3:1 |
| Lexique | `tools/lexique_verifier.py` | Zéro terme banni dans le corpus et dans `fr.ts` |
| Parcours Android | Maestro sur émulateurs API 24, 30, 34, 36 | Lancement, lecture, mise en arrière-plan de la promenade, faire venir un chapitre, retour prédictif, rotation, pliage (émulateur pliable), widget, raccourcis, liens profonds |
| Moteur des voix | Vitest (AudioContext simulé) | Interruption pendant « Les quatre voix » et pendant l'écho ; écoute au mot (segment et groupe de souffle) ; une seule voix à la fois |
| Oreille fine | Vitest | 200 paires de cas (contractions, ponctuation, majuscules, apostrophes typographiques) |
| Performance | Macrobenchmark Android (démarrage) + traces Chrome à distance (scène) | Budgets 10.12 |

Exemple de parcours Maestro (`android/maestro/premiere_scene.yaml`) :

```yaml
appId: com.vivrelanglais.livre
---
- launchApp:
    clearState: true
- assertVisible: "Vivre l'Anglais"
- tapOn: "Commencer"
- tapOn: "Britannique"
- tapOn: "Continuer"
- tapOn: "Le Livre"
- tapOn: "Le réveil et les premières minutes"
- assertVisible: "My alarm's going off."
- tapOn:
    id: "ecouter-c01.s01.A1.e1"
- assertVisible: "En écoute"
- tapOn: "Spontané"
- assertVisible: "mə·LÂMZ"
- back
- assertVisible: "Le Livre"
```

### 11.3 La matrice d'appareils

| Classe | Appareil réel ou émulateur | Android | Ce qu'on y vérifie |
|---|---|---|---|
| Modeste, Android 7 | Émulateur 2 Go, WebView mise à jour | 7.0 (API 24) | Fonctionnement complet, budgets × 1,5 |
| Milieu de gamme courant | Samsung Galaxy A15 ou équivalent | 14 | **Appareil de référence** des budgets |
| Marché africain d'entrée de gamme | Tecno ou Infinix récent, 3 à 4 Go | 13 ou 14 | Surcouche constructeur, économie d'énergie agressive (lecture en arrière-plan) |
| Haut de gamme | Pixel récent | 16 (API 36) | Bord à bord, retour prédictif, icônes à thème |
| Tablette | Tablette 10 pouces | 14 ou plus | Mise en page deux colonnes, paysage |
| Pliable | Émulateur pliable | 16 | Changement de posture sans perte d'état |
| Accessibilité | Pixel avec TalkBack, taille de police système 200 % | 16 | Lecture complète d'une scène au lecteur d'écran |

### 11.4 Les critères d'acceptation de l'ouvrage

1. Toucher une expression déclenche sa voix en ≤ 120 ms, dans l'accent et le rythme choisis, sur l'appareil de référence.
2. Les quatre versions de chaque énoncé, déclinaison et réplique publiés existent, ont passé tous les contrôles bloquants 7.10 et sont **indiscernables d'une voix réelle** à l'écoute comparative ; le registre des prises (7.9) permet de retrouver, pour chaque fichier, son origine, sa voix et, pour une voix créée, le moteur, la version, les réglages et la graine.
3. Le phrasé affiché correspond toujours à la voix entendue (même accent, même rythme).
4. Aucune chaîne visible par le lecteur ne contient un terme de la liste bannie (3.3) ; une revue complète de tous les écrans est consignée.
5. L'ouvrage fonctionne sans connexion pour toute scène dont les voix sont installées ; les voix du Prélude et des Chapitres 1 et 2 sont présentes dès l'installation.
6. La promenade continue écran éteint pendant 30 minutes, avec les commandes de lecture sur l'écran verrouillé.
7. Après désinstallation puis réinstallation sur le même compte Google, le carnet est retrouvé.
8. Aucune violation d'accessibilité grave ; tout le parcours est possible au lecteur d'écran.
9. Le taux de plantage en test fermé est inférieur à 0,2 % des sessions.
10. Le fichier APK direct est signé, vérifié par `apksigner`, son empreinte SHA-256 est publiée.
11. Toucher un mot fait entendre ce mot tel qu'il a été dit dans la phrase, sans claquement, sur 100 % des énoncés publiés.
12. La voix du sens existe pour chaque expression et chaque réplique publiées, et dit exactement le texte affiché.
13. Le widget « L'expression du jour » change chaque jour et ouvre l'ouvrage sur la bonne expression ; les quatre raccourcis et les liens `https://vivrelanglais.com/e/…` ouvrent l'écran attendu.
14. Les quatre thèmes respectent les contrastes de 9.2.
15. Sur téléphone pliable et tablette, la lecture survit au pliage et à la rotation sans coupure.
16. Chaque itinéraire est parcourable de bout en bout, voix comprises.

### 11.5 Le retour des lecteurs

- Dans chaque carte d'expression, volet → **« Signaler une coquille »** (8.25) : prépare un courriel prérempli (identifiant de l'expression, accent, rythme, édition, journal des contretemps en option) ; aucune collecte automatique.
- Les signalements alimentent un tableau de suivi ; toute coquille confirmée est corrigée dans l'édition correctif suivante (délai cible : 30 jours).

---

## 12. La fabrique éditoriale

### 12.1 Le gabarit de rédaction

Chaque scène est écrite directement en YAML (10.4) à partir du fichier `corpus/_gabarit/scene.yaml`, qui contient la structure complète, des commentaires d'aide et les listes fermées (tons, niveaux, fonctions, régions, personnages). La forme est garantie par construction : un éditeur YAML relié au schéma (annexe B) signale toute erreur pendant la frappe.

### 12.2 Le circuit d'une scène

| Étape | Contenu | Livrable |
|---|---|---|
| 1. Fiche d'intention | Intention, liste des moments, situations couvertes, personnages, renvois avec les autres scènes, itinéraires concernés | `fiche.md` de la scène |
| 2. Rédaction | YAML complet hors phrasés : 55 expressions, déclinaisons traduites, Essentiel, scène vivante dans l'accent de référence, rituel | YAML ; porte P1 |
| 3. Relecture native croisée | Énoncés naturels ou régionalisés dans chaque accent ; scène vivante adaptée dans l'autre accent ; notes « En coulisses » vérifiées | Rapport de relecture |
| 4. Relecture éditoriale | Ton, densité, faux pas, lexique, sens prêts à être dits par la voix du sens | Portes P1 et P2 |
| 5. Scripts des voix | Scripts JSONL générés (`scripts_voix.py --voix`), indications de jeu, textes de jeu du spontané | Scripts par voix |
| 6. Création et choix des prises | Quatre prises par interprétation, contrôles 7.10, prise retenue ; dialogue continu pour la scène vivante ; voix du sens | Prises retenues ; porte P3 |
| 7. Finition | Fichiers finis, alignements, syllabes, courbes, manifestes | Porte P4 |
| 8. Phrasés | Quatre phrasés par énoncé et couche experte | Porte P5 |
| 9. Intégration | Rendu, parcours, couverture vocale | Porte P6 |

Une scène ne passe à l'étape suivante qu'une fois la porte précédente franchie. Le texte est **gelé** à la porte P2 : toute modification ultérieure incrémente la version de scène et renvoie les énoncés touchés à l'étape 5.

### 12.3 La charte de rédaction

- Écrire comme on parle à un ami cultivé : phrases courtes, vocabulaire juste, aucune emphase publicitaire.
- Toujours partir d'une situation vécue (« Le réveil sonne pour la troisième fois »), jamais d'une catégorie grammaticale.
- Une expression mérite sa place si un natif l'a probablement dite **cette semaine**.
- Le ton cru est expliqué, jamais gratuit ; il est absent des Chapitres 1 à 5, sauf mention.
- Chaque faux pas cite l'erreur réelle d'un francophone (*I made a dream*, *I raised*) et sa correction.
- Chaque sens est écrit pour être **dit** : il doit sonner juste à voix haute, dans la voix du sens, sans parenthèse ni barre oblique.
- Aucune déclinaison ne répète une autre déclinaison de la même expression à un mot près : chacune apporte une situation, une personne ou un temps différents.
- Les prénoms, lieux et références des scènes vivantes viennent de `personnages.yaml` ; aucun personnage n'apparaît sans fiche.

### 12.4 Les contrôles de cohérence de l'ouvrage

Au-delà de chaque scène, `valider_corpus.py --ouvrage` vérifie l'ensemble :

- Aucune expression en double dans tout l'ouvrage (même énoncé principal dans deux scènes) ; les reprises volontaires passent par un renvoi.
- Répartition des tons et des niveaux par chapitre (alerte si un chapitre dépasse 15 % de ton cru ou ne compte aucune expression de niveau Fondations).
- Chaque personnage garde son accent, son âge et ses relations d'une scène à l'autre.
- Les 1 630 incontournables sont tous rattachés à l'itinéraire « Le parler juste ».

---

## 13. Les risques

| Risque | Probabilité | Impact | Parade |
|---|---|---|---|
| Voix jugées mécaniques sur certains énoncés (exclamations, rires, chuchotements, ton cru) | Moyenne | Élevé | Quatre prises par interprétation, contrôles 7.10, reformulation de l'indication de jeu ; recours à un enregistrement existant (7.3) ou réécriture de l'énoncé en dernier ressort |
| Retrait ou évolution du moteur retenu | Moyenne | Élevé | Version figée et archivée ; masters conservés (20.11) ; registre des créations (7.5) ; épreuve de sélection rejouable ; une voix ne change de moteur qu'avec recréation complète de ses fichiers |
| Dérive du timbre d'une voix au fil des lots | Moyenne | Moyen | Fiche vocale figée, graine consignée, similarité à la référence de timbre contrôlée sur chaque fichier (7.10, 20.2) |
| Phrasés en désaccord avec la voix | Moyenne | Élevé | Règle « la transcription suit la voix », contre-écoute indépendante sur 20 %, signalement des lecteurs |
| Alignement mot à mot imprécis (écoute au mot) | Moyenne | Moyen | Contrôles automatiques 10.22, recalcul à découpage fin des fichiers signalés, contrôle sur 5 % des mots |
| Taille des voix trop lourde pour les appareils modestes | Moyenne | Moyen | Socle limité, voix par chapitre à la demande, retrait des chapitres terminés en un geste, contrôle de la place disponible (8.12) |
| Changement des règles Google Play (API cible, politiques) | Élevée (annuelle) | Moyen | Veille trimestrielle ; mise à niveau de l'API cible chaque année avant l'échéance de Google |
| Évolution majeure de Capacitor ou de la WebView | Moyenne | Moyen | Versions figées, montée de version dans une branche dédiée avec la matrice 11.3 complète |
| Perte de la clé de signature directe | Faible | Critique | Deux coffres, copie hors ligne (10.15) |
| Licence d'une source ou d'un moteur incompatible avec la publication | Faible | Critique | Licence vérifiée fichier par fichier et conditions du moteur archivées (7.12) ; tout fichier douteux est retiré et recréé |
| Contenu cru mal perçu | Faible | Moyen | Masqué par défaut, avertissement d'usage, classification honnête |
| Écart de niveau ou de couleur entre enregistrements existants et voix créées | Moyenne | Moyen | Mêmes seuils sonores, niveau de parole active, contrôle statistique par lot (20.3) |
| Promesse de progrès excessive | Moyenne | Élevé | Principe « Prouvé » (2.2), heures indicatives citées avec leurs réserves (18.2), page « Ce que l'ouvrage ne promet pas » (15.16) |
| Lien de partage détourné | Faible | Faible | Les pages `vivrelanglais.com/e/{id}` n'affichent que le texte public de l'expression ; identifiants validés contre le sommaire |

---

## 14. Le répertoire des fonctionnalités

Ce répertoire recense chaque fonctionnalité de l'ouvrage, avec la section qui la définit. Il sert de table de contrôle : une fonctionnalité absente de l'édition publiée est une non-conformité.

### 14.1 Le contenu et la pédagogie

| # | Fonctionnalité | Ce qu'elle apporte | Section |
|---|---|---|---|
| 1 | **Le Prélude sonore** | Six scènes pour former l'oreille avant la première expression | 4.3 |
| 2 | **Le parcours en six temps** | Chaque scène suit le même chemin : ouverture, moments, essentiel, scène vivante, rituel, retrouvailles | 4.2 |
| 3 | **L'Ouverture** | Écouter la scène sans texte avant de l'étudier | 4.2 |
| 4 | **Les normes de densité** | Minimum, cible et maximum d'expressions par scène | 4.5 |
| 5 | **Les trois niveaux** | Fondations, Aisance, Maîtrise, sur chaque expression | 4.6 |
| 6 | **La fréquence d'usage** | De 1 à 5 ; elle ordonne incontournables et promenade | 4.6 |
| 7 | **Les fonctions de communication** | Refuser, adoucir, féliciter… et leurs parcours transversaux | 4.6 |
| 8 | **Le sens de chaque déclinaison** | Toutes les déclinaisons sont traduites, sans exception | 5.2 |
| 9 | **Un énoncé, une voix** | Chaque énoncé a ses quatre interprétations et ses quatre phrasés | 5.2 |
| 10 | **Le sens et le mot à mot séparés** | Le lecteur voit ce qu'on dit et comment c'est construit | 5.1 |
| 11 | **L'usage et les coulisses** | Explications courtes, bornées en longueur | 5.1 |
| 12 | **Sur le même air** | Un gabarit et ses déclinaisons sonores pour créer ses propres phrases | 5.1 |
| 13 | **Les renvois** | Liens typés et touchables entre expressions et scènes | 5.2 |
| 14 | **Les graphies régionales** | Orthographe britannique et américaine stockées séparément | 5.2 |
| 15 | **Les personnages récurrents** | Une bible complète : âge, accent, métier, relations | 5.4 |
| 16 | **La scène vivante** | Jouée en dialogue continu, en quatre interprétations | 5.3 |
| 17 | **Les scènes localisées** | Une version britannique et une version américaine de chaque dialogue | 5.3, annexe A |
| 18 | **Donnez la réplique** | Le lecteur joue un rôle, avec un silence calibré | 5.3 |
| 19 | **Le rituel** | Un geste concret à faire dans la journée, rappelé le lendemain | 4.2, 8.2 |
| 20 | **L'Essentiel** | Les incontournables et les faux pas de chaque scène | 4.2 |
| 21 | **Les faux pas** | L'erreur réelle d'un francophone, sa correction et pourquoi | 4.2 |
| 22 | **Les itinéraires** | Douze chemins transversaux pour une échéance réelle | 8.17 |
| 23 | **Le parler juste** | Les 1 630 incontournables en huit étapes | 8.17 |
| 24 | **Le ton** | Courant, complice, cru, soutenu, toujours nommé | 4.6 |
| 25 | **Le ton cru maîtrisé** | Masqué par défaut, expliqué, jamais gratuit | 4.6, 12.3 |
| 26 | **Les appendices** | Clés du phrasé, atlas des accents, lexique, faux pas, incontournables | 4.1 |
| 27 | **La charte de rédaction** | Une voix d'éditeur constante dans tout l'ouvrage | 12.3 |
| 28 | **Les contrôles de cohérence** | Aucun doublon, personnages cohérents, tons équilibrés | 12.4 |

### 14.2 Les voix

| # | Fonctionnalité | Ce qu'elle apporte | Section |
|---|---|---|---|
| 29 | **Huit voix principales** | Quatre voix américaines, quatre britanniques, femmes et hommes | 7.4 |
| 30 | **Deux rythmes** | Posé pour comprendre, spontané pour vivre la langue | 7.1 |
| 31 | **Les quatre voix** | Les quatre interprétations d'un énoncé enchaînées | 8.3 |
| 32 | **La voix du sens** | Une voix francophone dit le sens, dans la promenade et l'écho | 7.4 |
| 33 | **Les voix secondaires** | Enfants, aînés, accents régionaux pour les scènes vivantes | 7.4 |
| 34 | **L'indication de jeu** | Contexte et émotion pour chaque énoncé | 7.8 |
| 35 | **Le moteur des voix créées** | Choisi par une épreuve d'écoute, version figée, création consignée | 7.5 |
| 36 | **La finition** | Niveau de parole active, silences calibrés, origine inscrite | 7.9 |
| 37 | **Les contrôles des voix** | Naturel, texte, accent, timbre, mélodie, rythme, artefacts | 7.10 |
| 38 | **Le registre des prises** | Chaque fichier relié à son origine, sa voix, ses réglages | 7.9, 11.4 |
| 39 | **Le manifeste de scène** | Fichiers, durées, empreintes, mots, syllabes, courbe | 7.11 |
| 40 | **Licences, crédits et transparence** | Sources libres créditées, origine des voix indiquée avec simplicité | 7.12 |
| 41 | **L'écoute au mot** | Le mot seul, tel qu'il a été dit dans la phrase | 8.14 |
| 42 | **La courbe** | La mélodie réelle de la voix, tracée sous le phrasé | 8.15 |
| 43 | **Le battement** | Une vibration sur chaque syllabe accentuée | 8.15 |
| 44 | **L'écho** | Imitation guidée, silences calibrés, 2 à 5 passages | 8.16 |

### 14.3 Le phrasé

| # | Fonctionnalité | Ce qu'elle apporte | Section |
|---|---|---|---|
| 45 | **Le système du phrasé** | Une transcription lisible par un francophone, sans alphabet savant | 6.1–6.4 |
| 46 | **Les syllabes fortes en capitales** | Le rythme se voit d'un coup d'œil | 6.4 |
| 47 | **Les liaisons et réductions** | Signes ‿, ə, ʔ, ɾ expliqués | 6.4 |
| 48 | **La mélodie** | Flèches montante et descendante | 6.4 |
| 49 | **Le regard expert** | L'alphabet phonétique international, sur demande | 5.1, 6.1 |
| 50 | **Ce que l'oreille entend** | La forme réellement entendue en spontané | 6.5 |
| 51 | **La transcription suit la voix** | Phrasés écrits à l'écoute de la prise retenue | 6.7 |
| 52 | **Les graphies proscrites** | Table des transcriptions fautives à ne jamais employer | 6.3 |
| 53 | **Les clés du phrasé** | Chaque signe expliqué avec un exemple sonore du Prélude | 6, 8.3 |
| 54 | **L'illumination synchronisée** | La syllabe dite s'éclaire pendant la voix | 8.3 |

### 14.4 L'expérience du lecteur

| # | Fonctionnalité | Ce qu'elle apporte | Section |
|---|---|---|---|
| 55 | **Aujourd'hui** | Une page d'accueil calme : reprendre, découvrir, retrouver | 8.2 |
| 56 | **Le Livre** | La carte de l'ouvrage, chapitres, scènes, itinéraires, appendices | 8.1, 8.2 |
| 57 | **La promenade** | Écoute continue, écran éteint | 8.4 |
| 58 | **Mon carnet** | Marque-pages, notes, constance, ma version, bilan du mois | 8.8 |
| 59 | **Le pupitre des voix** | Accent et rythme choisis en un geste | 8.2, 9.5 |
| 60 | **La table des gestes** | Chaque toucher a un effet unique et prévisible | 8.3 |
| 61 | **Toucher pour recommencer** | Toucher l'énoncé pendant la voix la reprend au début | 8.3 |
| 62 | **Maintenir un mot** | Réécouter la phrase depuis ce mot | 8.3 |
| 63 | **Le volet d'expression** | Écho, comparaison, miroir, ma version, partage, coquille | 8.3 |
| 64 | **Le miroir** | S'enregistrer et se comparer à la voix du livre | 8.5 |
| 65 | **Les retrouvailles** | Mémorisation espacée par l'algorithme FSRS | 8.6 |
| 66 | **Les huit formes de retrouvailles** | L'oreille, la réplique, le miroir, deux Anglais, le ton juste, le faux pas, sur le même air, l'oreille fine | 8.7 |
| 67 | **L'oreille fine** | Écrire ce qu'on entend, comparaison mot à mot | 8.18 |
| 68 | **Les retrouvailles silencieuses** | Uniquement des formes sans parole, pour les transports | 8.7 |
| 69 | **Le retour en douceur** | Après une absence, les retrouvailles sont étalées | 8.6 |
| 70 | **La journée qui bascule à 4 h** | Aucun jour perdu en veillant tard ou en voyageant | 8.6 |
| 71 | **Ma version** | Sa propre phrase sur un gabarit, avec sa propre voix | 8.19 |
| 72 | **Le moment présent** | Une scène accordée à l'heure de la journée | 8.20 |
| 73 | **Le regard en arrière** | Le bilan sobre du mois, calculé sur le téléphone | 8.21 |
| 74 | **La constance** | Les jours de pratique, sans série à perdre ni culpabilité | 8.8 |
| 75 | **Comment dit-on… ?** | Recherche en français et en anglais, tolérante aux fautes | 8.9, 10.11 |
| 76 | **Recherche par fonction** | Trouver toutes les façons de refuser, d'adoucir… | 8.9 |
| 77 | **Recherche par son** | Trouver les exemples d'un signe du phrasé | 8.9 |
| 78 | **Les préférences** | Voix, lecture, parcours, écran d'accueil, rendez-vous | 8.10 |
| 79 | **L'accueil** | Trois écrans, un niveau de départ, une première voix en moins d'une minute | 8.11 |
| 80 | **Lire ce livre** | Six pages sonores pour tout comprendre | 8.24 |
| 81 | **Les bulles uniques** | Une seule explication à la première rencontre d'un élément | 8.24 |
| 82 | **Les rendez-vous** | Un rappel par jour au plus, jamais culpabilisant | 8.13 |
| 83 | **Mes marque-pages en promenade** | Écouter sa propre sélection | 8.4 |
| 84 | **Le minuteur de la promenade** | Fin douce sur 20 secondes | 8.4 |
| 85 | **Reprise exacte** | La promenade reprend à l'expression interrompue | 8.4 |
| 86 | **Commandes Bluetooth** | Casques, montres et voitures pilotent la promenade | 8.4 |
| 87 | **Partager ma liste** | Exporter ses marque-pages pour un enseignant | 8.8 |
| 88 | **Partager une expression** | Carte image soignée et lien qui ouvre l'ouvrage | 8.23 |
| 89 | **Signaler une coquille** | Un courriel préparé, rien n'est envoyé sans le lecteur | 8.25, 11.5 |
| 90 | **Mettre mon carnet à l'abri** | Sauvegarde et restauration en un fichier | 8.8, 10.10 |
| 91 | **Le carnet retrouvé** | Restauration automatique après réinstallation | 10.10 |
| 92 | **Grands écrans et pliables** | Deux colonnes, lecture continue au pliage | 8.26 |
| 93 | **Le son très bas** | Un message discret si le volume est presque nul | 8.3 |

### 14.5 L'écran d'accueil et Android

| # | Fonctionnalité | Ce qu'elle apporte | Section |
|---|---|---|---|
| 94 | **L'expression du jour** | Widget d'écran d'accueil, deux tailles | 8.22, 10.20 |
| 95 | **Écouter depuis le widget** | Toucher l'énoncé ouvre la carte et lance la voix | 8.22 |
| 96 | **Les raccourcis d'application** | Reprendre, retrouvailles, promenade, recherche | 8.22, 10.20 |
| 97 | **Les liens d'application vérifiés** | Un lien partagé ouvre directement l'expression | 10.20 |
| 98 | **L'icône à thème** | Icône monochrome pour Android 13 et plus | 10.9 |
| 99 | **Le retour prédictif** | Geste retour conforme à Android 16 | 10.6, 10.9 |
| 100 | **Les zones sûres** | Respect des encoches et de la navigation gestuelle | 9.4 |
| 101 | **Les notifications de lecture** | Contrôles sur l'écran verrouillé | 8.4 |
| 102 | **Les rendez-vous non exacts** | Aucune permission d'alarme exacte | 8.13 |

### 14.6 Le design « Encre & Voix »

| # | Fonctionnalité | Ce qu'elle apporte | Section |
|---|---|---|---|
| 103 | **Quatre thèmes** | Papier, Ambre, Nuit, Contraste | 9.2 |
| 104 | **Le thème Contraste** | Contraste ≥ 7:1, proposé automatiquement | 9.2 |
| 105 | **Les couleurs d'accent** | Une couleur américaine, une britannique, constantes | 9.2 |
| 106 | **Les couleurs de ton** | Toujours accompagnées de leur mot | 9.2 |
| 107 | **La typographie de livre** | Literata, Inter, Charis SIL | 9.3 |
| 108 | **Le titre à axe optique** | Literata en taille de titrage | 9.3 |
| 109 | **L'aide à la lecture** | Atkinson Hyperlegible en option | 9.3 |
| 110 | **La colonne de lecture** | 60 à 70 caractères par ligne | 9.3 |
| 111 | **La césure française** | Activée pour le français seulement | 9.3 |
| 112 | **Les cibles de 48 dp** | Tout se touche facilement d'une main | 9.4 |
| 113 | **Les icônes au trait** | Dessinées sur mesure | 9.6 |
| 114 | **Le mouvement calme** | Durées courtes, aucun rebond | 9.7 |
| 115 | **L'encre qui s'écrit** | Un trait d'encre remplace tout indicateur d'attente | 9.8 |
| 116 | **Les états vides** | Une illustration et une phrase de l'éditeur | 9.8 |

### 14.7 L'accessibilité

| # | Fonctionnalité | Ce qu'elle apporte | Section |
|---|---|---|---|
| 117 | **TalkBack complet** | Chaque carte et chaque bouton annoncés clairement | 9.9 |
| 118 | **La langue des énoncés** | TalkBack bascule en anglais sur les énoncés | 9.9 |
| 119 | **Texte à 200 %** | Aucune perte de contenu | 9.9 |
| 120 | **Clavier et contacteur** | Navigation complète, focus visible | 9.9 |
| 121 | **Animations réduites** | Fondus simples si le système le demande | 9.7 |
| 122 | **Aucune information sonore seule** | Tout ce qui est dit est aussi écrit | 9.9 |
| 123 | **Le battement pour l'oreille fatiguée** | Le rythme se sent dans la main | 8.15 |

### 14.8 L'ingénierie et la distribution

| # | Fonctionnalité | Ce qu'elle apporte | Section |
|---|---|---|---|
| 124 | **Un corpus en YAML** | Source unique du texte, lisible et versionnée | 10.3, 10.4 |
| 125 | **Le schéma de validation** | Toute scène est vérifiée avant compilation | 10.4, annexe B |
| 126 | **Le vérificateur de lexique** | Aucun terme proscrit ne passe | 10.5 |
| 127 | **Le vérificateur du phrasé** | Symboles autorisés, syllabe forte obligatoire | 10.5 |
| 128 | **Le contrôle de couverture vocale** | Aucune scène publiée sans toutes ses voix | 10.5 |
| 129 | **SvelteKit statique** | Une application web légère embarquée | 10.6 |
| 130 | **Le moteur de page** | Web Audio, latence ≤ 120 ms | 10.7 |
| 131 | **Des lectures qui ne se marchent pas dessus** | Chaque lecture a sa propre fin ; un toucher interrompt proprement | 10.7 |
| 132 | **Le moteur de promenade** | Media3 dans un service de lecture | 10.7 |
| 133 | **La préparation anticipée** | Les voix des cartes à venir sont prêtes avant le toucher | 10.7 |
| 134 | **Le socle sonore** | Prélude, Chapitres 1 et 2 présents dès l'installation | 10.9 |
| 135 | **Les paquets de voix à la demande** | Un paquet par chapitre sur Google Play | 10.9 |
| 136 | **La liste des paquets générée** | Jamais écrite à la main | 10.9, annexe C.6 |
| 137 | **Le canal direct** | APK signé, catalogue de voix signé | 10.18 |
| 138 | **Le contrôle de la place disponible** | Avant toute arrivée de voix | 8.12, 10.9 |
| 139 | **L'intégrité des voix** | Vérification mensuelle des empreintes | 10.21 |
| 140 | **La réparation automatique** | Une voix abîmée est remise en état | 10.21 |
| 141 | **Le précalcul des courbes** | Rien n'est calculé sur le téléphone | 10.22 |
| 142 | **Le stockage local** | IndexedDB, préférences, copie de sûreté | 10.10 |
| 143 | **La sauvegarde Android** | Le carnet suit le lecteur d'un téléphone à l'autre | 10.9 |
| 144 | **La confidentialité** | Aucun suivi, aucune publicité, rien ne quitte le téléphone | 10.13 |
| 145 | **La politique de sécurité du contenu** | Aucun code distant | 10.6, 10.13 |
| 146 | **Les budgets de performance** | Démarrage, latence, mémoire, taille, bloquants | 10.12 |
| 147 | **La procédure de compilation** | De poste vierge à l'APK signé, étape par étape | 10.14 |
| 148 | **La signature** | Clé d'envoi, clé directe, coffres | 10.15 |
| 149 | **L'intégration continue** | Contenu et Android vérifiés à chaque modification | 10.16 |
| 150 | **La publication Google Play** | Test fermé, fiche, déploiement progressif | 10.17 |
| 151 | **Les éditions** | Règles de version de l'application, des scènes et des voix | 10.19 |
| 152 | **Le journal des contretemps** | Local, joint seulement sur demande du lecteur | 8.25, 10.10 |

### 14.9 La qualité

| # | Fonctionnalité | Ce qu'elle apporte | Section |
|---|---|---|---|
| 153 | **Les sept portes** | Texte, langue, voix, son, phrasé, ouvrage, édition | 11.1 |
| 154 | **Les tests automatiques** | Unitaires, composants, parcours, accessibilité, contrastes | 11.2 |
| 155 | **Les tests du moteur des voix** | Interruptions, écoute au mot, une seule voix | 11.2 |
| 156 | **La matrice d'appareils** | Du petit téléphone à la tablette pliable | 11.3 |
| 157 | **Les critères d'acceptation** | Seize exigences vérifiables | 11.4 |
| 158 | **Le retour des lecteurs** | Toute coquille confirmée corrigée sous 30 jours | 11.5 |
| 159 | **La scène étalon** | La mesure de toute scène | annexe A |
| 160 | **La check-list de mise en production** | Rien n'est oublié | annexe E |

### 14.10 La science, la méthode et l'échelle industrielle

| # | Fonctionnalité | Ce qu'elle apporte | Section |
|---|---|---|---|
| 161 | **Les quatre fils** | Écouter, dire, étudier, gagner en aisance : quatre fils en équilibre | 15.1 |
| 162 | **Le profil lexical** | Chaque scène compréhensible à la bonne étape | 15.9 |
| 163 | **Ce que l'ouvrage ne promet pas** | Des repères honnêtes sur l'effort réel | 15.16 |
| 164 | **Les secrets de l'anglais parlé** | 41 pages sonores sur ce que les manuels taisent | 16 |
| 165 | **La hiérarchie des priorités** | Les dix points qui rendent intelligible, dans l'ordre | 16.1 |
| 166 | **Tapez le rythme** | Sentir les syllabes fortes du doigt | 16.2 |
| 167 | **Une phrase, sept sens** | Le mot fort qui change tout | 16.4 |
| 168 | **Où sont les mots ?** | Retrouver les mots dans la parole enchaînée | 16.17 |
| 169 | **La grammaire parlée** | 30 fiches de la grammaire dont on a besoin pour parler | 17 |
| 170 | **Les trois caps et sept paliers** | Survivre, échanger, vivre : un chemin par compétences | 18.1, 18.2 |
| 171 | **Les épreuves de palier** | Écoute, petits mots, paires, parole, sans note | 18.3 |
| 172 | **La journée type** | De cinq à quatre-vingt-dix minutes, quatre formats | 18.4 |
| 173 | **Avant de dormir** | Une écoute calme des expressions du jour | 18.4 |
| 174 | **Le contrat d'intensité** | Un engagement tenu sans jamais punir | 18.5 |
| 175 | **Les itinéraires à échéance** | Être prêt le jour du départ | 18.6 |
| 176 | **La voix du premier jour** | Mesurer le chemin parcouru à l'oreille | 18.7 |
| 177 | **Les dix habitudes** | L'anglais hors du livre, une habitude à la fois | 18.8 |
| 178 | **Ce qui vous résiste** | Les familles de difficultés du lecteur, avec leurs remèdes | 18.9 |
| 179 | **À vous de jouer** | Tenir son rôle dans une conversation à embranchements | 19.1 |
| 180 | **Sans filet** | Parler librement avant de voir la réplique prévue | 19.1 |
| 181 | **Les annonces** | Gares, aéroports, répondeurs, météo | 19.2 |
| 182 | **L'oreille dans le bruit** | Six ambiances réelles, trois niveaux, la voix intacte | 19.3 |
| 183 | **La voix au téléphone** | Comprendre la bande étroite d'un appel | 19.3 |
| 184 | **Les chiffres et les lettres** | Prix, heures, dates, numéros, épellations | 19.4 |
| 185 | **L'échelle de politesse** | Six degrés pour chaque demande | 19.5 |
| 186 | **Les paires à seize voix** | 18 contrastes, seize voix, quatre gardées pour les épreuves | 19.6 |
| 187 | **La parole en relais** | Le même récit en 4, 3 puis 2 minutes | 19.7 |
| 188 | **L'ombre** | Parler en même temps que la voix, en quatre temps | 19.8 |
| 189 | **Les Voix du monde** | 24 variétés d'anglais, natives et non natives | 19.9 |
| 190 | **Le diagnostic d'oreille** | Dix minutes pour savoir où porter l'effort | 19.10 |
| 191 | **La fluidité mesurée** | Pauses et coulées de parole, calculées sur l'appareil | 19.11 |
| 192 | **La chaîne de production** | Du corpus aux voix, chaque étape rejouable et consignée | 20.1 |
| 193 | **La constance à grande échelle** | Un même timbre et un même son sur des centaines de milliers de fichiers | 20.2 |
| 194 | **Le contrôle statistique** | Échantillonnage par lot, taux de défaut suivis | 20.3 |
| 195 | **La chaîne d'approvisionnement** | Dépendances figées, inventaire, compilations reproductibles | 20.4 |
| 196 | **L'observation sans traceur** | Santé de l'application sans aucun code d'analyse | 20.5 |
| 197 | **Les autres magasins** | Galaxy Store, AppGallery, F-Droid, même ouvrage | 20.7 |
| 198 | **Le Livre en classe** | Listes par code QR, projection, fiches imprimables | 20.8 |
| 199 | **Les autres langues d'accompagnement** | Le même anglais expliqué depuis d'autres langues | 20.9 |
| 200 | **La conservation des masters** | Règle 3-2-1, restauration trimestrielle | 20.11 |
| 201 | **Les enregistrements existants** | Des voix de locuteurs réels, sous licence libre, là où la variété compte | 7.3 |
| 202 | **La fiche vocale** | Un timbre décrit, choisi par épreuve et figé pour toute l'œuvre | 7.4 |
| 203 | **L'épreuve de sélection du moteur** | Le moteur choisi à l'écoute, contre des voix réelles | 7.5 |
| 204 | **Le texte de jeu** | Les réductions du spontané réellement dites, le texte affiché intact | 7.7 |
| 205 | **Les quatre prises** | La meilleure de quatre prises, contrôlée sur onze critères | 7.9, 7.10 |

Total : **205 fonctionnalités**.

---

## 15. La science qui fonde l'ouvrage

Chaque mécanisme de l'ouvrage repose sur un résultat de recherche identifié. Cette section relie chaque principe à sa source, à ce qu'il impose concrètement et à la fonctionnalité qui l'applique. Elle dit aussi honnêtement **les limites** de chaque résultat : un ouvrage sérieux ne promet pas plus que ce que la science établit.

### 15.1 Les quatre fils d'un apprentissage équilibré

Paul Nation montre qu'un parcours de langue équilibré consacre un temps à peu près égal à quatre fils : l'écoute et la lecture centrées sur le sens, l'étude délibérée de la langue, la production orale et écrite centrée sur le sens, et le développement de l'aisance (Nation, Four strands — <https://www.wgtn.ac.nz/lals/resources/paul-nations-resources/paul-nations-publications/publications/documents/1996-Four-strands.pdf>). L'ouvrage répartit explicitement son temps de pratique entre ces quatre fils :

| Fil | Part visée du temps du lecteur | Où il vit dans l'ouvrage |
|---|---|---|
| Écoute centrée sur le sens | 25 % | L'Ouverture, la scène vivante, la promenade, les Voix du monde (19.9), L'oreille dans le bruit (19.3) |
| Étude délibérée de la langue | 25 % | Les expressions, le phrasé, les secrets de l'anglais (16), la grammaire parlée (17), Les paires à seize voix (19.6) |
| Production centrée sur le sens | 25 % | Donnez la réplique, À vous de jouer (19.1), Ma version, Sur le même air, L'échelle de politesse (19.5) |
| Aisance | 25 % | La parole en relais (19.7), l'écho, la promenade à rythme spontané, les retrouvailles rapides |

**Règle d'équilibre** : la page Aujourd'hui calcule localement la répartition des 14 derniers jours et, si un fil tombe sous 15 %, la carte du jour suivant le privilégie (« Cette semaine, vous avez beaucoup écouté. Aujourd'hui, à vous de parler. »).

### 15.2 Les difficultés qui font apprendre

Robert et Elizabeth Bjork appellent « difficultés désirables » les conditions qui ralentissent les progrès apparents mais renforcent la mémoire à long terme et le transfert : espacer, entrelacer, se tester, varier les conditions, produire soi-même la réponse ; elles ne sont utiles que si le lecteur a les bases pour y répondre (Bjork & Bjork, 2011 — <https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2016/04/EBjork_RBjork_2011.pdf>).

| Difficulté désirable | Application dans l'ouvrage | Garde-fou |
|---|---|---|
| Espacer | Retrouvailles FSRS (8.6) | Étalement après une absence |
| Entrelacer | Huit formes de retrouvailles alternées, expressions de scènes différentes dans une même séance (8.7) | Jamais deux scènes nouvelles le même jour au niveau Fondations |
| Se tester | L'oreille, La réplique, L'oreille fine : l'expression est retrouvée avant d'être montrée | Deux réécoutes permises |
| Varier | Huit voix principales, deux accents, deux rythmes, l'ambiance réelle (19.3) | La variation n'arrive qu'après une première rencontre en posé |
| Produire | Sur le même air, Ma version, À vous de jouer | Une proposition modèle est toujours disponible |

### 15.3 Se souvenir en se testant

Se tester renforce davantage la mémoire que relire ; ce résultat, appelé effet de test, a été relancé par les travaux de Roediger et Karpicke en 2006 (Roediger & Karpicke, rétrospective — <https://pubmed.ncbi.nlm.nih.gov/29592647/>). Dans l'ouvrage, **toute retrouvaille commence par un effort de rappel** (entendre puis dire le sens, entendre le sens puis dire l'anglais) avant toute révélation. Aucune forme de retrouvailles ne consiste à relire passivement.

### 15.4 Le bon intervalle

L'intervalle optimal entre deux rencontres dépend du délai visé : environ 20 % du délai pour une échéance de quelques semaines, environ 5 % pour une échéance d'un an (Cepeda et al., 2008 — <https://eric.ed.gov/?id=ED505660>). L'ouvrage s'en sert de deux manières :

- le moteur FSRS (8.6) calcule les intervalles individuels ;
- les **itinéraires à échéance** (18.6) acceptent une date cible (« Je pars le 12 ») : l'ouvrage resserre alors les intervalles des expressions de l'itinéraire pour qu'elles soient au plus haut le jour dit, en plafonnant chaque intervalle à 20 % du temps restant.

### 15.5 Entrelacer plutôt que regrouper

Alterner des types d'exercices (*abcbcacab* plutôt que *aaabbbccc*) améliore en général les résultats ultérieurs, bien que cela paraisse plus difficile sur le moment (Rohrer & Taylor, effets de l'entrelacement — <https://onlinelibrary.wiley.com/doi/pdf/10.1002/acp.1598>). Les retrouvailles mêlent donc toujours au moins trois scènes et trois formes ; les paires de sons (19.6) mélangent les contrastes (*ship/sheep*, *full/fool*, *cat/cut*) au lieu de les travailler un par un, dès que chaque contraste a été rencontré seul une fois.

### 15.6 Produire soi-même

L'effet de génération désigne le fait qu'une information produite par soi-même se retient mieux qu'une information simplement lue (Psychonomic Bulletin & Review — <https://link.springer.com/article/10.3758/s13423-020-01762-3>). C'est le fondement de « Sur le même air », de « Ma version » et des conversations « À vous de jouer » : le lecteur fabrique sa phrase avant d'entendre celle du livre.

### 15.7 Parler pour remarquer ce qui manque

Selon l'hypothèse de la production de Merrill Swain, parler pousse l'apprenant à remarquer les trous de sa connaissance, puis à mieux écouter la forme qui lui manquait ; cette fonction de « remarque » fait encore l'objet de recherches expérimentales récentes (Studies in Second Language Acquisition — <https://www.cambridge.org/core/journals/studies-in-second-language-acquisition/article/decoding-the-noticing-function-of-output-the-roles-of-attention-and-awareness-during-l2-grammar-learning/56BF03840E1F69A197D9381700E709B8>). Dans l'ouvrage, chaque production du lecteur est **immédiatement suivie** de la version du livre, au même endroit, avec les mots différents mis en évidence quand le lecteur a écrit (L'oreille fine) ou la possibilité d'écouter les deux voix côte à côte quand il a parlé (le miroir).

### 15.8 La correction qui fait chercher

En classe, les incitations qui poussent l'apprenant à se corriger lui-même se sont montrées plus efficaces que les reformulations qui donnent directement la bonne forme (Lyster & Saito, 2010, résumé — <https://link.springer.com/content/pdf/10.1007/978-3-030-79143-8_63.pdf>). L'ouvrage ne juge pas automatiquement la parole du lecteur (aucune reconnaissance vocale) ; il applique ce principe à l'écrit et à l'écoute : dans L'oreille fine, la première comparaison **signale l'endroit** de l'écart sans révéler le mot (« Deux mots diffèrent dans la seconde moitié ») ; le lecteur peut réécouter et corriger une fois avant de voir le texte exact.

### 15.9 Combien de mots pour comprendre

- Environ 95 % de mots connus peuvent suffire pour comprendre un message oral, 98 % étant la cible habituelle pour la lecture (Pellicer-Sánchez et al., UCL — <https://discovery.ucl.ac.uk/id/eprint/10216385/3/Pellicer%20Sanchez_Lexical%20coverage%20and%20comprehension%20RFL%20copy%20for%20online%20repository.pdf>).
- Atteindre 98 % à l'oral demande de connaître environ 6 000 à 7 000 familles de mots (Language Teaching, réplication de Nation 2006 — <https://www.cambridge.org/core/journals/language-teaching/article/how-much-vocabulary-is-needed-to-use-english-replication-of-van-zeeland-schmitt-2012-nation-2006-and-cobb-2007/1D217A56A2E0056E67802A6A8360FDDE>).
- Les 2 000 mots les plus fréquents couvrent environ 80 % des occurrences d'un texte courant (Purdue, d'après Milton 2009 — <https://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=1056&context=plcc>).

**Conséquence pour l'ouvrage** : chaque scène est profilée à la compilation (`tools/profil_lexical.py`) contre une liste de fréquence de l'anglais parlé ; le rapport indique la part des mots de la scène situés dans les 1 000, 2 000, 3 000 premiers mots et au-delà. Règle : dans les Chapitres 1 à 6 (Fondations), **au moins 90 % des mots des scènes vivantes** appartiennent aux 2 000 premiers ; dans les Chapitres 7 à 18, au moins 85 % aux 3 000 premiers ; au-delà, aucune contrainte, mais tout mot hors des 5 000 premiers est glosé dans le sens. Le vocabulaire de référence pour l'étiquetage des niveaux est la liste Oxford 3000 et 5000, classée par niveau du Cadre européen (Oxford Learner's Word Lists — <https://www.oxfordlearnersdictionaries.com/about/wordlists/index.html>), recoupée avec l'English Vocabulary Profile (English Profile — <https://englishprofile.org/>) ; les droits d'usage de ces listes sont vérifiés (7.12) avant toute reprise intégrale, l'ouvrage n'en publiant que l'étiquette de niveau.

### 15.10 La langue est faite de blocs

Erman et Warren estiment qu'entre 52 % et 58 % des énoncés qu'ils ont analysés sont préfabriqués, c'est-à-dire composés de séquences toutes faites (ELIA, synthèse — <https://revistas.uned.es/index.php/ELIA/article/download/18098/15247>). C'est la justification de l'unité de base de l'ouvrage : **l'expression**, et non le mot isolé. Le Chapitre 2 et les itinéraires accordent une place centrale aux blocs les plus fréquents de la conversation (*I don't know*, *I don't think so*, *do you want to*, *I was going to*, *it's not that*, *by the way*).

### 15.11 Former l'oreille à la variabilité

L'entraînement phonétique à haute variabilité consiste à faire identifier des contrastes de sons prononcés par de nombreuses voix, avec un retour immédiat. Une méta-analyse de 2025 portant sur 79 études trouve un gain important entre avant et après l'entraînement (g ≈ 0,92), qui se maintient dans le temps, mais un transfert moins net vers des mots nouveaux dits par des voix nouvelles (Uchihara, Karas & Thomson, 2025 — <https://www.cambridge.org/core/journals/studies-in-second-language-acquisition/article/high-variability-phonetic-training-hvpt-a-metaanalysis-of-l2-perceptual-training-studies/6ABB8C1F32D88D53EA8D05A4565E76F6>). L'ouvrage en tire Les paires à seize voix (19.6), avec deux précautions : un **grand nombre de mots différents** par contraste (au moins 40), pour viser le transfert, et une **réserve de voix jamais entendues à l'entraînement** pour mesurer honnêtement le progrès.

### 15.12 Imiter dans la foulée

La technique de l'ombre (répéter un modèle en même temps que lui ou avec un léger retard) semble aider la compréhensibilité, l'intelligibilité et l'accent, selon une revue systématique de 2025, qui qualifie toutefois ces résultats de prudents en raison des limites méthodologiques des études (Whitworth & Rose, 2025 — <https://www.tandfonline.com/doi/full/10.1080/29984475.2025.2546827>). L'ouvrage propose donc l'ombre comme **une** pratique parmi d'autres (19.8), jamais comme la méthode unique.

### 15.13 Être compris avant de sonner natif

Munro et Derwing distinguent trois notions : l'intelligibilité (ce qui est réellement compris), la compréhensibilité (l'effort que demande l'écoute) et l'accent (l'écart perçu par rapport à une norme) ; un accent marqué n'empêche pas d'être parfaitement intelligible (ELT Journal — <https://academic.oup.com/eltj/article/69/2/202/408492>). La prosodie (rythme, accent, mélodie) compte au moins autant que les sons isolés pour être compris (GEPF, Falar — <https://gepf.falar.org/entries/40/>), et même les défenseurs du noyau de l'anglais international tiennent la place de l'accent de phrase pour indispensable (Saito, TUFS — <http://www.tufs.ac.jp/common/fs/ilr/contents/ronshuu/27/jilr27_Article_Saito.pdf>).

**Conséquence** : l'ouvrage hiérarchise ses exigences de prononciation (16.1). Il vise d'abord **être compris sans effort**, puis **comprendre les natifs à leur vitesse**, et seulement ensuite, pour qui le souhaite, **se rapprocher d'un accent**.

### 15.14 Le sommeil travaille pour le lecteur

Le sommeil contribue à consolider les mots nouveaux et à les intégrer au vocabulaire déjà connu (Neuroscience & Biobehavioral Reviews, méta-analyse — <https://eprints.whiterose.ac.uk/id/eprint/113337/1/1-s2.0-S0149763416305784-main.pdf>). D'où la **promenade du soir** (8.4) et la carte « Avant de dormir » (18.4) : une écoute de 5 minutes des expressions découvertes dans la journée, sans exercice, le soir venu.

### 15.15 Comprendre beaucoup, sans s'en contenter

L'idée selon laquelle on acquiert une langue en comprenant ce qu'on entend a beaucoup influencé l'enseignement, mais elle est critiquée pour son manque de preuves directes et parce qu'elle sous-estime le rôle de la production et de l'attention portée à la forme (Frontiers, critique de l'hypothèse de l'input compréhensible — <https://pmc.ncbi.nlm.nih.gov/articles/PMC12577063/>). L'ouvrage prend le meilleur des deux : **beaucoup d'écoute compréhensible** (promenade, scènes vivantes) et **une attention délibérée à la forme** (phrasé, secrets, paires de sons), réunies dans les quatre fils (15.1).

### 15.16 Ce que l'ouvrage ne promet pas

- Aucun délai garanti pour « parler couramment » : la durée dépend du point de départ, du temps quotidien et de la pratique réelle. À titre d'ordre de grandeur, le Foreign Service Institute américain estime à environ 600 à 750 heures de formation intensive le temps nécessaire à un anglophone pour atteindre un bon niveau professionnel en français (estimations FSI — <https://emma-learn.com/learn/blog/how-long-to-learn-each-language/>) ; le chemin inverse est d'un ordre comparable, mais cette donnée concerne des cours intensifs en présentiel, et non une application.
- Aucun « accent natif » promis : l'objectif est d'être compris sans effort et de comprendre les natifs (15.13).
- Aucune méthode miracle : chaque technique est présentée avec sa force et sa limite.

---

## 16. Les secrets de l'anglais parlé

Ce que les manuels taisent, que les natifs ignorent savoir et qui sépare un francophone qui « connaît l'anglais » d'un francophone qui **le comprend et se fait comprendre au premier essai**. Chaque secret est présenté dans le même ordre : ce qu'il faut savoir, un exemple dans les deux accents, le piège propre au francophone, et l'endroit où l'ouvrage le fait vivre.

Ces secrets forment dans l'ouvrage un appendice sonore, **Les secrets de l'anglais**, de 41 pages courtes (une par secret), chacune avec 6 à 12 exemples dits par les voix de l'ouvrage, et reliée aux expressions où le phénomène apparaît. Chaque page se termine par une retrouvaille propre (« Le secret en action ») qui rejoint le moteur FSRS.

### 16.1 La hiérarchie des priorités du francophone

Tous les écarts de prononciation n'ont pas le même poids. La notion de **charge fonctionnelle** mesure combien de distinctions de sens un contraste de sons porte réellement dans la langue ; elle sert à choisir ce qui compte le plus pour être compris (charge fonctionnelle, Université du Texas — <https://repositories.lib.utexas.edu/server/api/core/bitstreams/07405136-cf4d-47ba-912b-c54fd7779f8b/content>). Le noyau proposé par Jennifer Jenkins pour l'anglais international retient par exemple l'aspiration de *p, t, k* en début de mot, l'allongement de la voyelle de *kid* par rapport à *kit*, la différence de longueur entre *heat* et *hit* et l'accent de contraste, tandis que le *th* peut être remplacé sans grand dommage (Lingua Franca Core — <https://en.wikipedia.org/wiki/Lingua_Franca_Core>). L'ouvrage s'en inspire, en y ajoutant la compréhension des natifs, qui exige aussi de connaître les formes faibles et la parole liée.

| Rang | Priorité | Pourquoi | Secrets |
|---|---|---|---|
| 1 | L'accent de mot et l'accent de phrase | Un mot mal accentué devient méconnaissable ; l'accent de phrase porte le sens | 16.3, 16.4, 16.5 |
| 2 | Les voyelles longues et brèves | *ship/sheep*, *full/fool*, *live/leave* : charge fonctionnelle élevée | 16.9, 16.10 |
| 3 | Le *h* prononcé | *eat/heat*, *air/hair*, *art/heart* | 16.12 |
| 4 | L'aspiration de *p, t, k* | Sans elle, *pin* s'entend *bin* | 16.13 |
| 5 | Les finales consonantiques et leur sonorité | *bag/back*, *eyes/ice* | 16.14 |
| 6 | Les formes faibles et le schwa | Indispensables pour **comprendre** les natifs | 16.6, 16.7 |
| 7 | La parole liée | Indispensable pour comprendre à vitesse réelle | 16.17 à 16.22 |
| 8 | La mélodie (intonation) | Elle porte l'attitude et la politesse | 16.23 à 16.27 |
| 9 | Les *th* | Peu de paires minimales ; à apprendre, sans en faire une obsession | 16.15 |
| 10 | Les couleurs d'accent (R, T, L) | Affinent l'accent, n'affectent presque pas la compréhension | 16.16, 16.19, 16.20 |

Le diagnostic d'oreille (19.10) mesure ces dix rangs et le parcours « Le Cap » (18) les travaille **dans cet ordre**.

### 16.2 Le rythme : l'anglais bat, le français coule

**Le secret.** Le français donne à peu près le même poids à chaque syllabe et marque la fin du groupe ; l'anglais oppose fortement syllabes accentuées et inaccentuées, et place l'accent à l'intérieur du mot (Frost, comparaison des accents anglais et français — <https://hal.science/hal-03542760v1/file/FROST_2010_EPIP.pdf>). Des auditeurs qui tapent la cadence d'une phrase ne battent pas de la même façon en anglais et en français (Lidji et al., PMC — <https://pmc.ncbi.nlm.nih.gov/articles/PMC3219863/>).

**L'exemple.** *I WANT to GO to the SHOPS* (UK) / *I WANna GO to the STORE* (US) : quatre temps forts, les petits mots se serrent entre eux.

**Le piège.** Donner la même durée à *to*, *the*, *a*, *of* qu'aux mots pleins : la phrase devient « martelée » et plus difficile à suivre pour un natif.

**Dans l'ouvrage.** Le battement (8.15), la courbe, les capitales du phrasé ; exercice « Tapez le rythme » du Prélude (4.3) : le lecteur tape les temps forts sur l'écran pendant la voix, l'ouvrage compare ses touchers aux syllabes fortes du manifeste (tolérance ± 120 ms), sans note, en montrant les temps manqués.

### 16.3 L'accent de mot n'est pas décoratif

**Le secret.** En anglais, la place de l'accent fait partie du mot. Changer de place peut changer la catégorie : *a REcord / to reCORD*, *a PREsent / to preSENT*, *an OBject / to obJECT*, *a CONtract / to conTRACT*.

**Le piège.** Le francophone accentue la dernière syllabe par habitude (*hotEL* est juste, mais *comforTABLE*, *vegeTABLE*, *developMENT* ne le sont pas : *COMfortable*, *VEGtable*, *deVELopment*).

**Les règles qui marchent le plus souvent** (toujours confirmées par la voix de l'expression) :

| Règle | Exemples |
|---|---|
| Nom ou adjectif de deux syllabes : accent souvent sur la première | *TAble, HAPpy, MOther* |
| Verbe de deux syllabes : accent souvent sur la seconde | *beGIN, deCIDE, forGET* |
| Mots en *-tion, -sion, -ic, -ical, -ity, -ian, -ious* : accent juste avant le suffixe | *inforMAtion, ecoNOMic, uniVERsity, muSIcian* |
| Mots en *-ate* de trois syllabes et plus : accent deux syllabes avant | *COMmunicate* → *comMUnicate* |
| Noms composés : accent sur le premier élément | *GREENhouse, BLACKboard, BEDroom* |
| Adjectif + nom (non composé) : accent sur le nom | *a green HOUSE, a black BOARD* |
| Verbes à particule : accent sur la particule ; nom correspondant : accent sur le verbe | *to set UP* / *a SETup* ; *to break DOWN* / *a BREAKdown* |

**Dans l'ouvrage.** Chaque expression porte ses capitales ; la page « Les faux accents des mots transparents » réunit 300 mots identiques ou presque en français et en anglais dont l'accent trompe (*hotel*, *photograph/photographer/photographic*, *develop*, *comfortable*, *interesting*, *chocolate*, *vegetable*, *restaurant*, *Wednesday*).

### 16.4 La syllabe qui porte le message

**Le secret.** Dans chaque groupe de souffle, une syllabe porte le mouvement mélodique principal : c'est le **noyau**. Par défaut, il tombe sur le dernier mot plein ; on le déplace pour signaler une information nouvelle ou un contraste.

**L'exemple.** *I didn't say she stole the MONEY* (phrase neutre) ; *I didn't say SHE stole the money* (quelqu'un d'autre l'a volé) ; *I didn't SAY she stole the money* (je l'ai seulement laissé entendre). Sept sens différents, une seule phrase.

**Le piège.** Le francophone met la mélodie à la fin du groupe, quel que soit le sens.

**Dans l'ouvrage.** Page sonore « Une phrase, sept sens » (sept versions par accent) ; dans le phrasé, le noyau est souligné ; retrouvaille « Le ton juste » sur le noyau.

### 16.5 Ce qui n'est pas répété ne s'accentue pas

**Le secret.** Une information déjà dite perd son accent : *"Do you like coffee?" — "I LOVE coffee."* Le noyau va sur *love*, pas sur *coffee*. De même, on accentue l'auxiliaire pour insister sur la vérité : *I DID call you*.

**Dans l'ouvrage.** Chaque scène vivante comporte au moins deux répliques qui illustrent ce déplacement ; elles sont signalées par un fin trait sous le mot noyau.

### 16.6 Le schwa, son le plus fréquent de l'anglais

**Le secret.** Le schwa /ə/, voyelle neutre et brève, est le son le plus fréquent de l'anglais ; on l'entend dans la plupart des syllabes inaccentuées et dans les petits mots grammaticaux (BBC Learning English — <https://www.bbc.co.uk/learningenglish/features/the_pronunciation_lounge/episode_1> ; Britannica — <https://www.britannica.com/topic/schwa>).

**L'exemple.** *banana* /bəˈnɑːnə/ (UK), /bəˈnænə/ (US) ; *about* /əˈbaʊt/ ; *the problem* /ðə ˈprɒbləm/.

**Le piège.** Lire les voyelles telles qu'elles s'écrivent : *baNAna* avec trois *a* pleins ; *pho-TO-graph* avec des *o* pleins.

**Dans l'ouvrage.** Le signe ə du phrasé ; page « Le son qui ne s'écrit pas » ; filtre de recherche « ə » (8.9).

### 16.7 Les formes faibles : les natifs avalent les petits mots

**Le secret.** Les mots grammaticaux (articles, prépositions, pronoms, auxiliaires, conjonctions) ont une forme forte, rare, et une forme faible, habituelle, le plus souvent avec un schwa (Weisser, formes fortes et faibles — <https://martinweisser.org/courses/phonetics/connect/weakForms.html>). Qui ne connaît que la forme forte **ne reconnaît pas** ces mots à l'oral.

| Mot | Forme forte (rare) | Forme faible (habituelle) | Exemple |
|---|---|---|---|
| a | /eɪ/ | /ə/ | *a cup of tea* /ə ˈkʌp əv ˈtiː/ |
| an | /æn/ | /ən/ | *an hour* |
| and | /ænd/ | /ənd/, /ən/, /n/ | *fish and chips* /ˌfɪʃ n ˈtʃɪps/ |
| are | /ɑː(r)/ | /ə(r)/ | *Where are you?* |
| as | /æz/ | /əz/ | *as soon as* |
| at | /æt/ | /ət/ | *at home* |
| but | /bʌt/ | /bət/ | *but why?* |
| can | /kæn/ | /kən/, /kn/ | *I can swim* /aɪ kn ˈswɪm/ (mais *I CAN'T* garde sa voyelle pleine) |
| could | /kʊd/ | /kəd/ | *Could you…?* |
| do | /duː/ | /də/, /du/ | *What do you want?* /ˈwɒdʒə ˈwɒnt/ |
| does | /dʌz/ | /dəz/ | *Does he know?* |
| for | /fɔː(r)/ | /fə(r)/ | *for a while* |
| from | /frɒm/ (UK), /frʌm/ (US) | /frəm/ | *from Paris* |
| had | /hæd/ | /həd/, /əd/, /d/ | *I'd gone* |
| has | /hæz/ | /həz/, /əz/, /z/ | *She's left* |
| have | /hæv/ | /həv/, /əv/, /v/ | *should have* /ˈʃʊdəv/ |
| her | /hɜː(r)/ | /hə(r)/, /ə(r)/ | *tell her* /ˈtelə/ |
| him | /hɪm/ | /ɪm/ | *ask him* /ˈɑːskɪm/ |
| his | /hɪz/ | /ɪz/ | *in his car* |
| just | /dʒʌst/ | /dʒəst/ | *just a minute* |
| me | /miː/ | /mi/ | *tell me* |
| must | /mʌst/ | /məst/, /məs/ | *you must be tired* |
| of | /ɒv/ (UK), /ʌv/ (US) | /əv/, /ə/ | *a lot of* /ə ˈlɒtə/ ; US *a lotta* |
| or | /ɔː(r)/ | /ə(r)/ | *tea or coffee* |
| shall | /ʃæl/ | /ʃəl/ | *Shall we?* |
| should | /ʃʊd/ | /ʃəd/ | *You should go* |
| some | /sʌm/ | /səm/ | *some milk* (déterminant) ; forte quand elle signifie « certains » |
| than | /ðæn/ | /ðən/ | *better than ever* |
| that (conjonction) | /ðæt/ | /ðət/ | *I think that…* (le démonstratif reste fort) |
| the | /ðiː/ | /ðə/ devant consonne, /ði/ devant voyelle | *the end* /ði ˈend/ |
| them | /ðem/ | /ðəm/, /əm/ | *tell 'em* |
| there (existentiel) | /ðeə(r)/ | /ðə(r)/ | *There's a problem* |
| to | /tuː/ | /tə/ devant consonne | *going to* → *gonna* |
| us | /ʌs/ | /əs/ | *Let us* → *let's* |
| was | /wɒz/ (UK), /wʌz/ (US) | /wəz/ | *It was fine* |
| were | /wɜː(r)/ | /wə(r)/ | *We were late* |
| will | /wɪl/ | /l/ | *I'll* |
| would | /wʊd/ | /wəd/, /əd/, /d/ | *I'd love to* |
| you | /juː/ | /jə/ | *See you* /ˈsiː jə/ |
| your | /jɔː(r)/ | /jə(r)/ | *your turn* |

**La règle d'or.** Un mot grammatical reprend sa forme forte en fin de phrase (*Where are you FROM?* /frɒm/), quand on le met en contraste (*Not FROM him, TO him*) et quand il est cité.

**Dans l'ouvrage.** Page sonore « Les quarante petits mots » ; retrouvaille L'oreille fine dédiée (« Combien de mots entendez-vous ? »), qui demande de compter les mots d'un énoncé spontané avant de l'écrire.

### 16.8 Les contractions sont la norme orale

**Le secret.** À l'oral, *I am*, *do not*, *it is*, *we will* se disent presque toujours *I'm*, *don't*, *it's*, *we'll*. La forme pleine signale une insistance (*I am NOT going*) ou un registre très formel. Les contractions doubles existent à l'oral : *I'd've* (*I would have*), *wouldn't've*, *shouldn't've*.

**Le piège.** Parler sans contractions sonne raide, voire contrarié.

**Dans l'ouvrage.** Tous les énoncés posés et spontanés sont dits avec les contractions naturelles ; la forme pleine n'apparaît qu'en contraste, signalée par une note « En coulisses ».

### 16.9 Les voyelles longues et brèves

**Le secret.** Le français n'a pas le /ɪ/ bref et relâché de *ship* ; *ship* et *sheep*, *fit* et *feet* risquent de se confondre ; la même opposition existe entre /ʊ/ et /uː/ (*full/fool*, *look/Luke*) (Ipatics, prononciation pour francophones — <https://www.ipatics.com/blog/english-pronunciation-for-french-speakers>).

**Les paires de vie quotidienne** (à fort enjeu) : *ship/sheep*, *live/leave*, *fill/feel*, *sit/seat*, *bitch/beach*, *sheet/shit*, *full/fool*, *pull/pool*, *look/Luke*.

**Le geste.** Pour /ɪ/ : partir du *i* français, relâcher la langue à mi-chemin vers *é*, garder le son court. Pour /ʊ/ : partir du *ou*, relâcher, arrondir à peine.

**Dans l'ouvrage.** Paires à seize voix (19.6), contraste n° 1 et 2.

### 16.10 Trois *a* là où le français n'en a qu'un

**Le secret.** L'anglais distingue *cat* /æ/, *cut* /ʌ/ et *cart* /ɑː/ (UK) ou /ɑr/ (US) ; le français les ramène tous vers son *a*. Ajoutez le /ɒ/ britannique de *hot* (le *hot* américain est /hɑt/), le /ɜː/ de *bird*, *work*, *first* (le seul son du noyau international dont la qualité doit être exacte), et la distinction *walk* /wɔːk/ / *work* /wɜːk/.

**Paires utiles** : *hat/hut/heart*, *cap/cup/carp*, *ban/bun/barn*, *walk/work*, *ward/word*, *four/fur*.

**Dans l'ouvrage.** Contrastes n° 3 à 6 des Paires à seize voix.

### 16.11 Les diphtongues ne s'arrêtent pas en route

**Le secret.** *No*, *go*, *phone* glissent : /nəʊ/ (UK), /noʊ/ (US) ; *day*, *make* glissent aussi : /eɪ/. Le francophone fige souvent ces voyelles (*no* comme *nô*, *day* comme *dé*), ce qui rend *coat/caught*, *wait/wet* ambigus.

**Dans l'ouvrage.** Le phrasé note les glissements (OU, EÏ) ; la courbe montre la voix qui bouge.

### 16.12 Le *h* se prononce

**Le secret.** Le *h* anglais est un vrai souffle : *heat*, *hair*, *heart*, *hungry*. Les francophones ont souvent du mal avec les sons *th* et *h* (Fonds de recherche du Québec — <https://frq.gouv.qc.ca/en/story-and-report/pronouncing-the-th-and-h-sounds-is-no-easy-task/>). Deux pièges symétriques : l'oublier (*I'm ungry*) et l'ajouter par excès de zèle (*h-I h-am*). Le *h* est muet dans *hour*, *honest*, *honour/honor*, *heir* ; il tombe aussi dans les formes faibles (*tell him* → /ˈtelɪm/).

**Le geste.** Souffler sur une vitre pour l'embuer, puis dire la voyelle sur ce souffle.

**Paires utiles** : *eat/heat*, *air/hair*, *art/heart*, *eye/high*, *ear/hear*, *old/hold*, *edge/hedge*, *arm/harm*.

### 16.13 Le petit souffle de *p, t, k*

**Le secret.** En début de syllabe accentuée, *p, t, k* sont suivis d'un léger souffle (aspiration). Sans lui, un anglophone entend *b, d, g* : *pin* devient *bin*, *time* devient *dime*, *coat* devient *goat*. Après *s*, pas de souffle : *spin*, *steam*, *school*.

**Le geste.** Tenir une feuille de papier devant la bouche : elle doit bouger sur *pin*, pas sur *spin*.

### 16.14 Les fins de mots comptent

**Le secret.** La voyelle s'allonge devant une consonne sonore et se raccourcit devant une consonne sourde : *kid* est plus long que *kit*, *bag* que *back*, *eyes* que *ice*. Pour un natif, c'est souvent **la durée de la voyelle** qui fait reconnaître la fin du mot. Les finales *-s* et *-ed* ont trois prononciations :

| Finale | /s/ | /z/ | /ɪz/ ou /ɪd/ |
|---|---|---|---|
| *-s* | *cats, stops, books* | *dogs, plays, calls* | *buses, watches, pages* |
| *-ed* | /t/ : *stopped, watched, laughed* | /d/ : *played, called, cleaned* | /ɪd/ : *wanted, needed, started* |

**Le piège.** Prononcer *-ed* comme une syllabe partout (*stop-ped*) ou laisser tomber les *-s* finals, qui portent le pluriel et la troisième personne.

### 16.15 Les *th* sans obsession

**Le secret.** /θ/ (*think*) et /ð/ (*this*) se font la langue légèrement entre les dents. Le *th* sonore /ð/ est l'un des sons les plus fréquents de l'anglais (*the, this, that, they, there, then, than*), mais il est presque toujours **faible** et rapide ; le *th* sourd /θ/ porte peu de paires minimales. Les remplacer par *s/z* ou *f/v* gêne moins la compréhension que d'oublier un *h* ou un accent de mot (16.1). Dans le langage rapide, *th* s'assimile aux sons voisins : *in the* → /ɪn nə/, *all the* → /ɔːl lə/.

**Paires utiles** : *think/sink*, *thick/sick*, *three/free/tree*, *bath/bass*, *they/day*, *breathe/breeze*.

### 16.16 Le *r* anglais : ni roulé, ni grasseyé

**Le secret.** Le *r* anglais se fait sans toucher le palais, langue retroussée ou ramassée vers l'arrière, lèvres légèrement avancées. L'américain le prononce partout (accent rhotique : *car* /kɑr/, *water* /ˈwɑɾər/) ; le britannique standard ne le prononce que devant une voyelle (*car* /kɑː/, mais *car alarm* /ˈkɑːr əˌlɑːm/).

**Le piège.** Le *r* français, au fond de la gorge, attire l'attention et peut gêner sur *right/light*, *grass/glass* pour l'oreille du natif.

### 16.17 Les mots se tiennent la main

**Le secret.** À l'oral, une consonne finale s'accroche à la voyelle du mot suivant : *turn off* → /tɜː‿nɒf/, *pick it up* → /pɪ‿kɪ‿tʌp/, *an apple* → /ə‿næpl/. Les natifs entendent une suite de syllabes, pas une suite de mots.

**Conséquence pour l'écoute** : *an aim* et *a name* se ressemblent ; *I scream* et *ice cream* aussi. Le lecteur apprend à **découper** autrement.

**Dans l'ouvrage.** Le signe ‿ du phrasé ; exercice « Où sont les mots ? » : une voix spontanée dit un énoncé, le lecteur place les frontières de mots sur une ligne de syllabes.

### 16.18 Les sons qui disparaissent

**Le secret.** Entre deux consonnes, *t* et *d* tombent souvent : *next day* → /neks deɪ/, *last night* → /lɑːs naɪt/, *I don't know* → /aɪ dəʊn nəʊ/, *handbag* → /ˈhæmbæg/. Les syllabes inaccentuées disparaissent aussi : *chocolate* /ˈtʃɒklət/, *interesting* /ˈɪntrəstɪŋ/, *camera* /ˈkæmrə/, *probably* /ˈprɒbli/ dans le langage rapide.

### 16.19 Le *t* qui devient *d* (américain)

**Le secret.** En américain, un *t* (ou *d*) placé entre deux voyelles, devant une syllabe inaccentuée, devient une petite frappe de langue proche d'un *d* rapide : *water*, *better*, *city*, *got it* (BoldVoice — <https://boldvoice.com/sounds/flap-t>). *Writer* et *rider* peuvent alors se ressembler ; *a lot of* devient *a lotta*, *get up* devient *gedup*.

**Dans l'ouvrage.** Signe ɾ du phrasé, uniquement dans les phrasés américains spontanés (6.4).

### 16.20 Le *t* qui s'arrête dans la gorge (britannique)

**Le secret.** Dans de nombreux accents britanniques, *t* est remplacé par un coup de glotte : très courant devant une consonne (*not now*, *football*), devant un *n* syllabique (*button*), en fin de mot, et de plus en plus, chez les jeunes, entre deux voyelles (*getting better*) ; entre deux voyelles à l'intérieur d'un mot comme *water*, il reste mal vu dans l'accent britannique standard (t-glottalisation — <https://en.wikipedia.org/wiki/T-glottalization>). L'américain connaît aussi le coup de glotte dans *button*, *mountain*.

**Dans l'ouvrage.** Signe ʔ dans les phrasés britanniques spontanés ; la voix britannique posée ne l'emploie que devant consonne.

### 16.21 Les sons qui fusionnent

**Le secret.** Deux sons voisins se rapprochent :

| Phénomène | Exemples |
|---|---|
| *t* + *y* → *tch* | *don't you* → /ˈdəʊntʃu/, *what you* → *whatcha*, *got you* → *gotcha* |
| *d* + *y* → *dj* | *did you* → /ˈdɪdʒu/, *would you* → *wouldja* |
| *s* + *y* → *ch* doux | *miss you* → /ˈmɪʃu/, *bless you* |
| *z* + *y* → *j* doux | *as you know* → /əˈʒu nəʊ/ |
| *n* devant *p, b, m* → *m* | *ten boys* → /tem bɔɪz/, *in bed* → /ɪm bed/ |
| *n* devant *k, g* → *ng* | *in case* → /ɪŋ keɪs/ |
| *t* devant *p, b, m* → *p* (non relâché) | *that man* → /ðæp mæn/ |

### 16.22 Les *r* qui apparaissent (britannique)

**Le secret.** En britannique non rhotique, un *r* s'intercale entre deux voyelles même quand il ne s'écrit pas : *law and order* → /ˈlɔːr ən ˈɔːdə/, *the idea of* → /ði aɪˈdɪər əv/, *drawing* → /ˈdrɔːrɪŋ/. Ce *r* de liaison est entendu partout à la BBC ; le lecteur doit le **reconnaître**, sans être tenu de le produire.

### 16.23 La mélodie qui descend affirme, celle qui monte demande

**Le secret.** Une question ouverte (*Where do you live?*) descend en général ; une question fermée (*Do you live here?*) monte souvent. Une phrase affirmative qui monte à la fin sonne hésitante ou interrogative.

### 16.24 Les questions-étiquettes ont deux sens

**Le secret.** *You're coming, aren't you?* Avec une mélodie descendante, on vérifie ce dont on est presque sûr ou on invite l'autre à parler ; avec une mélodie montante, on pose une vraie question (BBC Learning English — <https://www.bbc.co.uk/learningenglish/features/the_pronunciation_lounge/episode_10>).

**La mécanique.** Phrase positive → étiquette négative (*It's cold, isn't it?*) ; phrase négative → étiquette positive (*You don't eat meat, do you?*) ; *I am* → *aren't I?* ; *Let's* → *shall we?* ; impératif → *will you?* / *won't you?* / *can you?*. En britannique familier, l'étiquette sert souvent de simple ponctuation sociale (*Lovely day, isn't it?*) ; en américain, on lui préfère souvent *right?* ou *huh?*.

### 16.25 La descente-montée : le « mais » qu'on ne dit pas

**Le secret.** Une mélodie qui descend puis remonte sur un seul mot signale une réserve : *The food was GOOD…* (sous-entendu : mais le service, non). *I DO like it…* (mais…). C'est l'arme favorite de la politesse britannique.

### 16.26 L'ampleur de la voix

**Le secret.** L'anglais utilise une plage mélodique plus large que le français ; une voix trop plate passe pour froide ou ennuyée, surtout aux oreilles américaines. L'enthousiasme américain (*That's AMAZING!*) se dit avec de grands mouvements ; l'enthousiasme britannique se dit souvent plus bas et plus lentement (*That's rather good, actually*).

**Dans l'ouvrage.** La courbe (8.15) rend cette ampleur visible ; le miroir montre la courbe du lecteur à côté de celle de la voix du livre (calculée localement sur sa propre voix, 19.11).

### 16.27 Les répétitions qui réparent

**Le secret.** Faire répéter est normal et poli : *Sorry?* (UK, mélodie montante), *Sorry, what was that?*, *Come again?* (familier), *Pardon?* (UK, poli), *Excuse me?* (US ; attention, avec une mélodie descendante, il marque l'indignation). Pour clarifier : *What do you mean by…?*, *Do you mean…?*, *So you're saying…?* Pour gagner du temps : *Let me think*, *That's a good question*, *How can I put it?*

**Dans l'ouvrage.** Scène 2.5 « Comprendre et se faire comprendre » ; ces formules sont **les premiers incontournables** du Chapitre 2, parce qu'elles permettent de survivre à toutes les autres.

### 16.28 Les petits mots qui tiennent la conversation

**Le secret.** *Well*, *you know*, *I mean*, *like*, *so*, *right*, *anyway*, *actually* comptent parmi les marqueurs les plus fréquents de la conversation, en américain comme en britannique (Kalbotyra, d'après le corpus LSWE — <https://www.journals.vu.lt/kalbotyra/article/download/23298/22534/43709> ; Cambridge Dictionary — <https://dictionary.cambridge.org/grammar/british-grammar/discourse-markers->).

| Marqueur | Ce qu'il fait | Exemple |
|---|---|---|
| *Well* | Annonce une réponse nuancée, un désaccord doux | *Well, it depends.* |
| *You know* | Cherche la connivence, laisse le temps de penser | *It's, you know, complicated.* |
| *I mean* | Reformule, précise | *It's fine. I mean, it's not perfect.* |
| *Like* | Approxime, cite, hésite (familier) | *She was like, "No way!"* |
| *So* | Ouvre un sujet, tire une conséquence | *So, how was your weekend?* |
| *Right* | Conclut, vérifie, enchaîne | *Right, shall we start?* |
| *Anyway* | Revient au sujet, clôt une digression | *Anyway, where was I?* |
| *Actually* | Corrige ou contredit poliment (jamais « actuellement ») | *Actually, I think it's on Tuesday.* |
| *To be honest* | Annonce une franchise, souvent une critique | *To be honest, I'm not sure.* |
| *Mind you* (UK) | Ajoute une réserve | *It's expensive. Mind you, it's very good.* |

### 16.29 Montrer qu'on écoute

**Le secret.** En anglais, l'auditeur envoie de brefs signaux pendant que l'autre parle : *yeah*, *uh-huh*, *mm-hm*, *right*, *okay*, *really?*, *oh*. Ils sont courants et attendus ; un moment propice est la courte zone de voix basse qui précède une pause de l'interlocuteur (Ward, signaux d'écoute — <https://www.cs.utep.edu/nigel/bc/>). Un francophone silencieux passe pour distrait ; un francophone qui dit *oui, oui* à la française surprend.

**Dans l'ouvrage.** Les scènes vivantes conservent ces signaux (ils sont dits et conservés, jamais retirés) ; « Donnez la réplique » propose des fenêtres de signal d'écoute ; page sonore « Je vous écoute ».

### 16.30 Hésiter comme un natif

**Le secret.** Les natifs hésitent aussi, mais en anglais : *um*, *uh* (US), *er*, *erm* (UK), *sort of*, *kind of*, *I don't know*, *or something*, *and stuff*, *whatever*. Hésiter en français (*euh*, *bah*) trahit l'effort ; hésiter en anglais le masque.

### 16.31 Les verbes à particule, cœur de l'oral

**Le secret.** L'oral préfère *find out* à *discover*, *put off* à *postpone*, *turn down* à *refuse*, *come up with* à *invent*. Dans le British National Corpus, une centaine de verbes à particule représentent plus de la moitié des emplois de ce type de verbe (Nivelo, d'après Gardner & Davies 2007 — <https://getnivelo.com/levels/most-common-phrasal-verbs>) ; leur usage est proche en américain et en britannique (Liu, 2011 — <https://eric.ed.gov/?id=EJ948637>). La liste pédagogique PHaVE donne 150 verbes fréquents avec leurs sens les plus fréquents (UC Davis, d'après Garnier & Schmitt 2015 — <https://globalaffairs.ucdavis.edu/iae/graduate/language-tips/phrasal-verbs>).

**Les trois règles de grammaire qui suffisent** :

1. Avec un nom, la particule se place avant ou après : *pick up the box* / *pick the box up*.
2. Avec un pronom, la particule va **après** : *pick it up* (jamais *pick up it*).
3. Certains ne se séparent jamais : *look after the kids*, *get over it*, *run into someone*.

**Dans l'ouvrage.** Les 150 verbes les plus fréquents sont tous présents comme expressions (dans leurs sens fréquents), tous rattachés à l'itinéraire « Le parler juste » ; page « Les particules et leur idée » (*up* = achèvement, augmentation ; *out* = révéler, finir ; *off* = départ, coupure ; *down* = diminution, mise par écrit ; *over* = examen, transfert ; *on* = continuation ; *back* = retour).

### 16.32 Les faux amis, pièges permanents

**Le secret.** Des mots presque identiques ont un autre sens : *actually* (en fait, pas « actuellement »), *eventually* (finalement, pas « éventuellement »), *realize* (se rendre compte, pas « réaliser un projet ») (The English Workshop — <https://the-english-workshop.com/blog/faux-amis-anglais-liste/>).

| Mot anglais | Ne veut pas dire | Veut dire | Pour dire le mot français |
|---|---|---|---|
| *actually* | actuellement | en fait | *currently* |
| *eventually* | éventuellement | finalement | *possibly* |
| *library* | librairie | bibliothèque | *bookshop* (UK), *bookstore* (US) |
| *sensible* | sensible | raisonnable | *sensitive* |
| *deception* | déception | tromperie | *disappointment* |
| *to attend* | attendre | assister à | *to wait* |
| *to assist* | assister à | aider | *to attend* |
| *achieve* | achever | réussir, atteindre | *to finish* |
| *coin* | coin | pièce de monnaie | *corner* |
| *preservative* | préservatif | conservateur | *condom* |
| *excited* | excité | ravi, impatient | *aroused* (à éviter en public) |
| *journey* | journée | trajet | *day* |
| *lecture* | lecture | conférence, cours magistral | *reading* |
| *location* | location | emplacement | *rental* |
| *resume* | résumer | reprendre | *to sum up* |
| *to pretend* | prétendre | faire semblant | *to claim* |
| *issue* | issue | question, problème | *way out* |
| *chance* | chance | possibilité | *luck* |
| *cave* | cave | grotte | *cellar* |
| *rude* | rude | impoli | *harsh, tough* |

**Dans l'ouvrage.** 180 faux amis dans « Tous les faux pas » ; chacun a son expression juste, dite.

### 16.33 *Quite*, *rather*, *pretty* : le thermomètre trompeur

**Le secret.** *Quite good* signifie souvent « assez bien, sans plus » en britannique, mais « vraiment bien » en américain ; *quite* devant un adjectif absolu signifie « tout à fait » des deux côtés (*quite right*, *quite impossible*). *Pretty good* est franchement positif dans les deux pays. *Rather* est surtout britannique (*rather nice*).

### 16.34 Ce que disent les Britanniques, ce qu'ils veulent dire

**Le secret.** La retenue britannique consiste à dire moins pour signifier plus, ou à habiller la critique (BBC Learning English, 6 Minute English — <https://www.bbc.co.uk/learningenglish/tigrinya/features/6-minute-english_2026/ep-260115>).

| On entend | On comprend souvent |
|---|---|
| *Not bad* | Bien, voire très bien |
| *I'll bear it in mind* | Je ne le ferai probablement pas |
| *With the greatest respect* | Je pense que vous avez tort |
| *That's an interesting idea* | Je n'y crois pas |
| *I'm sure it's my fault* | C'est votre faute |
| *Could we consider other options?* | Votre proposition ne me convient pas |
| *A bit disappointing* | Un échec |
| *I might join you later* | Je ne viendrai pas |
| *You must come for dinner sometime* | Formule de politesse, pas une invitation datée |
| *Sorry* (après qu'on vous a bousculé) | Réflexe social, pas un aveu |

**Dans l'ouvrage.** Page sonore « Ce qu'ils disent, ce qu'ils pensent » (britannique et américain), avec la mélodie qui trahit le sens caché.

### 16.35 La franchise américaine et ses rituels

**Le secret.** *How are you?* (ou *How's it going?*) est un salut, pas une question : la réponse attendue est brève (*Good, thanks! You?*). L'enthousiasme américain est la norme polie (*I'd love to!*, *That's awesome!*, *Great job!*) ; un *It's okay* américain peut signaler une déception. La politesse américaine passe par la chaleur et le prénom, la britannique par la retenue et l'indirect.

### 16.36 L'échelle de la politesse

**Le secret.** Plus on s'éloigne grammaticalement, plus on est poli : le passé, le conditionnel et le progressif créent de la distance.

| Degré | Exemple |
|---|---|
| 1. Direct (proches, urgence) | *Open the window.* |
| 2. Adouci | *Open the window, will you?* |
| 3. Question | *Can you open the window?* |
| 4. Conditionnel | *Could you open the window?* |
| 5. Distance | *Would you mind opening the window?* |
| 6. Grande distance | *I was wondering if you could possibly open the window.* |

**Le piège.** Le francophone traduit *Je voudrais* par *I want* (trop direct) : dire *I'd like* ou *Could I have…?*. *Please* seul ne suffit pas à rendre polie une phrase impérative.

**Dans l'ouvrage.** L'échelle de politesse (19.5).

### 16.37 *Sorry*, *please*, *thank you* : la ponctuation sociale

**Le secret.** En britannique, *sorry* sert à s'excuser, à faire répéter, à attirer l'attention, à exprimer sa compassion, à interrompre. *Cheers* signifie « merci » ou « au revoir » au Royaume-Uni. Les Américains disent plus volontiers *Excuse me* et *Thanks so much*. On remercie le chauffeur de bus, la caissière, la personne qui tient la porte : l'absence de *thank you* se remarque.

### 16.38 Les petits sujets ne sont pas petits

**Le secret.** La conversation de circonstance (*small talk*) sert à créer la confiance avant d'aborder le vrai sujet. Sujets sûrs : le temps qu'il fait, le trajet, le week-end, les projets de vacances, le sport (selon le pays), la nourriture. Sujets risqués avec un inconnu : salaire, religion, politique, âge, poids. La conversation se poursuit par des **questions ouvertes** et des **relances** (*Oh really? What was that like?*).

### 16.39 Les chiffres, les lettres et les dates

**Le secret.** Les francophones confondent les lettres *E* /iː/ et *I* /aɪ/, *G* /dʒiː/ et *J* /dʒeɪ/, et lisent *A* /eɪ/ comme le *a* français. Les dates se disent *the fifth of May* (UK) ou *May fifth* (US) et s'écrivent 05/05 dans des ordres différents (jour/mois au Royaume-Uni, mois/jour aux États-Unis). Les nombres : *thirteen* / *thirty* se distinguent par l'accent (*thirTEEN* / *THIRty*) et le *t* ; *0* se dit *oh*, *zero* ou *nought* (UK) ; les numéros de téléphone se lisent chiffre par chiffre, avec *double* au Royaume-Uni (*double five*). Une adresse électronique : *at*, *dot*, *underscore*, *hyphen* ou *dash*.

**Dans l'ouvrage.** Les chiffres et les lettres (19.4).

### 16.40 Britannique ou américain : les mots qui changent

| Royaume-Uni | États-Unis | Français |
|---|---|---|
| *flat* | *apartment* | appartement |
| *lift* | *elevator* | ascenseur |
| *queue* | *line* | file d'attente |
| *holiday* | *vacation* | vacances |
| *mobile* | *cell phone* | téléphone portable |
| *bill* (restaurant) | *check* | addition |
| *chips* | *fries* | frites |
| *crisps* | *chips* | chips |
| *trousers* | *pants* | pantalon |
| *pants* | *underwear* | sous-vêtement (piège majeur) |
| *ground floor / first floor* | *first floor / second floor* | rez-de-chaussée / premier étage |
| *motorway* | *highway, freeway* | autoroute |
| *petrol* | *gas* | essence |
| *rubbish, bin* | *trash, garbage can* | ordures, poubelle |
| *postcode* | *zip code* | code postal |
| *autumn* | *fall* | automne |
| *Have you got…?* | *Do you have…?* | Avez-vous… ? |
| *I've just eaten.* | *I just ate.* (les deux s'entendent aux États-Unis) | Je viens de manger. |

**Dans l'ouvrage.** Le champ `region` et les deux textes d'énoncé (5.2) ; page « Deux pays, deux mots » ; retrouvaille « Deux Anglais ».

### 16.41 Les deux mille mots du quotidien

**Le secret.** Quelques centaines de mots font l'essentiel de la conversation : pronoms, auxiliaires, *get*, *go*, *know*, *think*, *mean*, *want*, *thing*, *stuff*, *really*, *just*, *actually*. Le verbe *get* à lui seul couvre « obtenir, recevoir, devenir, arriver, comprendre » (*get a job*, *get a message*, *get tired*, *get home*, *I get it*).

**Dans l'ouvrage.** Les 1 630 incontournables couvrent, à la compilation, au moins 95 % des 2 000 mots les plus fréquents de l'anglais parlé (contrôle `profil_lexical.py --couverture`).

### 16.42 Le débit réel

**Le secret.** La conversation se tient autour de 150 mots par minute (médiane d'environ 153 mots par minute selon une compilation de 19 mesures publiées), les émissions et podcasts autour de 200 (Yap, compilation des débits — <https://yapapp.cc/data/speaking-rate>). Le rythme posé de l'ouvrage vise environ 130 mots par minute et le spontané environ 200, soit **plus vite** que la conversation moyenne : qui comprend le spontané comprend la rue.

**Dans l'ouvrage.** Les deux rythmes (7.1) ; La parole en relais (19.7) pour la production.

### 16.43 Les secrets de la grammaire parlée

Développés en section 17.

---

## 17. La grammaire parlée

La grammaire de l'ouvrage n'est pas celle des examens écrits : c'est **la grammaire dont on a besoin pour parler**, présentée par la phrase entendue et jamais par la règle abstraite. Elle prolonge le Chapitre 24, « La grammaire vivante », par un appendice sonore de 30 fiches, **La grammaire parlée**. Chaque fiche suit le même gabarit : **La phrase** (enregistrée), **Ce qu'elle fait**, **Comment elle se construit** (trois lignes au plus), **Le piège du francophone**, **Dix phrases à dire** (enregistrées dans les quatre interprétations), **Où on la rencontre** (liens vers les expressions).

| # | Fiche | La phrase d'entrée | L'essentiel pour parler | Le piège du francophone |
|---|---|---|---|---|
| 1 | Le présent simple des habitudes | *I usually take the bus.* | Habitudes, vérités, horaires ; *-s* à la troisième personne | Oublier le *-s* : *she work* |
| 2 | Le présent en cours | *I'm cooking, can I call you back?* | Ce qui se passe maintenant ou autour de maintenant | Dire *I cook* pour « je suis en train de cuisiner » |
| 3 | Le présent pour le futur prévu | *I'm meeting Sarah tomorrow.* | Rendez-vous déjà fixés | Dire *I will meet* pour un rendez-vous fixé |
| 4 | *Going to* | *It's going to rain.* / *I'm gonna call him.* | Intention, prédiction fondée sur un indice | Ignorer *gonna* à l'oreille |
| 5 | *Will* / *'ll* | *I'll get it!* | Décision prise sur le moment, promesse, offre | Dire *I go to answer* |
| 6 | Le passé simple | *I saw him yesterday.* | Action terminée, moment précis | Dire *I have seen him yesterday* |
| 7 | Le *present perfect* | *Have you ever been to London?* / *I've lost my keys.* | Expérience, résultat présent, période non terminée ; plus courant en britannique, l'américain emploie volontiers le passé simple avec *just*, *already*, *yet* | Traduire « j'ai vu » par *I have seen* dans tous les cas |
| 8 | Depuis : *for* et *since* | *I've lived here for ten years / since 2016.* | *for* + durée, *since* + point de départ, avec le *present perfect* | Dire *I live here since ten years* |
| 9 | Le passé en cours | *I was having a shower when you called.* | Le décor d'une action passée | Tout mettre au passé simple |
| 10 | *Used to* | *I used to smoke.* | Habitude révolue | Confondre avec *I'm used to* (« j'ai l'habitude de ») |
| 11 | Les questions : l'auxiliaire d'abord | *Do you know…? Did she…? Have they…?* | Inverser l'auxiliaire, ajouter *do* si besoin | Dire *You know where…?* sans *do* (accepté à l'oral familier seulement avec mélodie montante) |
| 12 | Les questions indirectes | *Do you know where the station is?* | Dans une question indirecte, plus d'inversion | Dire *where is the station* après *Do you know* |
| 13 | Les réponses courtes | *"Do you like it?" — "Yes, I do."* | Reprendre l'auxiliaire, jamais *Yes, I like* seul | Répondre *Yes* sec (perçu comme abrupt) |
| 14 | *So do I*, *Neither do I* | *"I'm tired." — "So am I."* | Accord en reprenant l'auxiliaire ; familier : *Me too*, *Me neither* | Dire *Me also* |
| 15 | Les questions-étiquettes | *You're French, aren't you?* | 16.24 | Dire *no?* ou *isn't it?* partout |
| 16 | Les modaux de demande | *Can / Could / Would you…?* | Échelle de politesse (16.36) | Dire *I want* |
| 17 | Les modaux de conseil | *You should / ought to / had better…* | *You'd better* = mise en garde | Dire *You must* pour un conseil (trop fort) |
| 18 | Les modaux de probabilité | *She must be tired. He can't be serious. It might rain.* | Déduction présente | Dire *It's possible that it rains* |
| 19 | Les regrets et reproches | *I should have called. You could have told me!* | *modal + have + participe*, dit *shoulda*, *coulda* | Ignorer la forme faible *should've* /ˈʃʊdəv/ |
| 20 | Les conditions réelles | *If it rains, we'll stay in.* | *if* + présent, *will* dans l'autre partie | Mettre *will* après *if* |
| 21 | Les conditions imaginaires | *If I were you, I'd tell her.* | *if* + passé, *would* | Dire *If I would be* |
| 22 | Les regrets imaginaires | *If I'd known, I would've come.* | *if* + *had*, *would have* | Se perdre dans les *'d* : *I'd* = *I had* ou *I would* |
| 23 | *Wish* | *I wish I had more time. I wish you'd stop!* | Regret présent (passé), agacement (*would*) | Dire *I wish I have* |
| 24 | La voix passive utile | *I've been told… / It's been cancelled.* | Quand l'auteur importe peu ; *get* passif à l'oral (*I got fired*) | Dire *One told me* |
| 25 | Faire faire | *I'm getting my hair cut.* / *I had my car fixed.* | *have/get something done* | Dire *I cut my hair* chez le coiffeur |
| 26 | Les verbes suivis de *-ing* ou de *to* | *I enjoy cooking. I want to cook. I stopped smoking / I stopped to smoke.* | Mémoriser par blocs : *enjoy -ing*, *want to*, *mind -ing* | Dire *I enjoy to cook* |
| 27 | Le discours rapporté de la conversation | *She said she was coming. He told me to wait.* | À l'oral, *say* sans complément, *tell* + personne ; *be like* en familier | Dire *She said me* |
| 28 | Les déterminants de quantité | *How much / How many / a lot of / a few / a little / any* | *a lot of* partout à l'oral ; *much/many* surtout en question et négation | Dire *I have much friends* |
| 29 | L'ordre des mots | *I really like it a lot. I often go there.* | Sujet, verbe, complément ; l'adverbe de fréquence avant le verbe | Dire *I like very much it* |
| 30 | Les mots de liaison de l'oral | *so, but, because, cos, then, anyway, though* (en fin de phrase : *It's nice, though.*) | Ce sont les liens de la conversation, plus que *however* ou *moreover* | Dire *moreover* à l'oral |

**Règle éditoriale.** Toute fiche renvoie à au moins vingt expressions de l'ouvrage où la structure apparaît ; aucune fiche n'introduit de terminologie grammaticale sans l'avoir d'abord fait entendre. Les termes « présent », « passé », « conditionnel » sont admis (ils appartiennent à la culture scolaire du lecteur) ; les étiquettes savantes (« aspect », « prétérit modal ») sont réservées à la couche « En coulisses ».

---

## 18. Le Cap : la méthode pour parler vite et juste

« Le Cap » est la méthode de progression de l'ouvrage. Elle organise toutes les fonctionnalités en un chemin unique, mesuré par des **paliers de compétence** et non par des dates. Elle répond à une seule question : quel est le chemin le plus court entre le niveau actuel du lecteur et le moment où il parle sans ambiguïté ?

### 18.1 Les trois caps

| Cap | Ce que le lecteur sait faire | Paliers |
|---|---|---|
| **Survivre** | Se présenter, demander, comprendre une réponse simple, faire répéter, se débrouiller dans les situations les plus fréquentes | 1 et 2 |
| **Échanger** | Tenir une conversation de la vie courante, raconter, donner son avis, comprendre les natifs en rythme posé et souvent en spontané | 3 et 4 |
| **Vivre** | Comprendre les natifs à leur vitesse, dans le bruit, au téléphone, avec humour et sous-entendus ; nuancer, convaincre, plaisanter | 5 et 6 |

### 18.2 Les six paliers

Les heures indiquées sont des ordres de grandeur de pratique réelle (temps passé à écouter, dire et retrouver), inspirés des heures d'apprentissage guidé publiées par Cambridge English pour chaque niveau du Cadre européen : environ 90 à 100 heures cumulées pour A1, 180 à 200 pour A2, 350 à 400 pour B1, 500 à 600 pour B2 et 700 à 800 pour C1 (Cambridge English, Guided learning hours — <https://support.cambridgeenglish.org/hc/en-gb/articles/202838506-Guided-learning-hours>). Cambridge précise que ces chiffres ne sont qu'indicatifs et varient selon le parcours, l'intensité et l'exposition hors des cours ; l'ouvrage les affiche avec la même prudence.

| Palier | Repère européen | Chapitres et contenus | « Je peux… » (exemples) | Pratique cumulée indicative |
|---|---|---|---|---|
| 0. L'oreille | Avant A1 | Prélude, 16.1 à 16.7 en écoute | Reconnaître le rythme, les syllabes fortes et les petits mots | 6 à 10 h |
| 1. Les premiers pas | A1 | Chapitres 1 et 2 ; itinéraire « Le parler juste », étapes 1 et 2 | Me présenter, saluer, faire répéter, demander mon chemin | 90 à 100 h |
| 2. Le quotidien | A2 | Chapitres 3 à 6 ; fiches 1 à 14 | Raconter ma journée, acheter, réserver, parler de ma famille | 180 à 200 h |
| 3. La conversation | B1 | Chapitres 7 à 12 ; fiches 15 à 22 ; À vous de jouer | Donner mon avis, raconter un souvenir, me plaindre poliment | 350 à 400 h |
| 4. L'aisance | B2 | Chapitres 13 à 18 ; Voix du monde ; L'oreille dans le bruit | Suivre une conversation de natifs, débattre, téléphoner | 500 à 600 h |
| 5. La finesse | C1 | Chapitres 19 à 24 ; secrets 16.33 à 16.38 | Saisir l'implicite, plaisanter, adapter mon registre | 700 à 800 h |
| 6. Le zénith | C2 | Chapitres 25 et 26 | Raconter, convaincre, parler en public | au-delà |

### 18.3 Les épreuves de passage

Chaque palier se conclut par **L'épreuve du palier**, entièrement locale, sans note chiffrée, en quatre volets :

1. **L'écoute** : douze extraits spontanés jamais entendus (réserve de voix et de scènes tenue à l'écart de l'entraînement), une question de sens par extrait. Seuil indicatif : 10 sur 12 compris.
2. **Les petits mots** : dix énoncés spontanés ; le lecteur compte les mots (16.7). Seuil : 8 sur 10.
3. **Les paires** : vingt paires de sons dites par des voix jamais entendues (19.6). Seuil : 17 sur 20.
4. **La parole** : le lecteur répond à voix haute à quatre situations (« Votre train est annulé. Demandez au guichet ce que vous pouvez faire. ») ; il s'enregistre puis compare à deux réponses modèles ; il s'évalue sur trois critères écrits (« J'ai été compris », « J'ai trouvé mes mots », « J'ai tenu le rythme »).

Le résultat s'affiche en phrases (« Votre oreille est prête pour le palier suivant. Les petits mots demandent encore un peu d'attention : voici trois pages pour eux. ») et ouvre, le cas échéant, un **chemin de renfort** de 3 à 5 séances ciblées. L'épreuve peut être repassée à volonté ; elle ne bloque jamais l'accès aux chapitres.

### 18.4 La journée type

L'ouvrage propose quatre formats, que le lecteur choisit à l'accueil et peut changer à tout moment :

| Format | Matin | Journée | Soir | Répartition des fils (15.1) |
|---|---|---|---|---|
| **Cinq minutes** | Retrouvailles (5 min) | — | — | Étude, aisance |
| **Vingt minutes** | Retrouvailles (7 min) | Un moment de scène (10 min) | Avant de dormir (3 min) | Les quatre fils |
| **Quarante minutes** | Retrouvailles (10 min) + écho (5 min) | Un moment de scène (15 min) + promenade (5 min) | À vous de jouer (5 min) | Les quatre fils |
| **Le Cap intensif** (60 à 90 min) | Retrouvailles (12 min) + paires (5 min) + écho (5 min) | Deux moments (25 min) + promenade dans les transports (15 min) | À vous de jouer ou parole en relais (10 min) + avant de dormir (5 min) | Les quatre fils |

**Au réveil** et **Avant de dormir** sont deux cartes d'Aujourd'hui : la première propose les retrouvailles et l'expression du jour ; la seconde, une écoute calme (sans exercice) des expressions découvertes dans la journée, en posé puis en spontané, avec la voix du sens (15.14).

### 18.5 Le contrat d'intensité

Le lecteur peut s'engager sur un format (« Je choisis Le Cap intensif »). L'ouvrage s'y tient : les rendez-vous (8.13) sont accordés à ce format, les cartes d'Aujourd'hui le respectent et la constance (8.8) compte les jours où le format a été tenu, **sans jamais punir** un jour manqué. Après sept jours de format non tenu, l'ouvrage propose de passer au format inférieur (« Vingt minutes, c'est déjà beaucoup. Voulez-vous essayer ce rythme ? »).

### 18.6 Les itinéraires à échéance

Un itinéraire (8.17) peut recevoir une date cible. L'ouvrage calcule alors le nombre d'expressions nouvelles par jour nécessaire, avertit honnêtement si l'échéance est trop courte (« Pour ce départ, nous vous conseillons de vous concentrer sur les étapes 1 à 3. »), et ajuste les retrouvailles pour que les expressions de l'itinéraire soient au plus haut le jour dit (15.4). La veille, une carte « Demain, c'est le jour » propose une promenade de 15 minutes des 40 expressions les plus utiles de l'itinéraire.

### 18.7 La voix du premier jour

À l'accueil, le lecteur peut enregistrer deux minutes de parole libre sur un sujet proposé (« Présentez-vous et parlez de votre journée d'hier. »). À chaque palier franchi, l'ouvrage propose de refaire l'exercice sur le même sujet, puis de réécouter les enregistrements côte à côte. Ces enregistrements restent sur l'appareil, comme toutes les voix du lecteur (10.13). C'est la mesure la plus parlante du chemin parcouru.

### 18.8 Les dix habitudes hors du livre

Le rituel de chaque scène est complété, au fil des paliers, par dix habitudes simples, présentées une à une (une par semaine de pratique) :

1. Passer la langue du téléphone en anglais (palier 2).
2. Se décrire à voix basse ce que l'on fait, en anglais, cinq minutes par jour (« I'm making coffee. I'm running late. »).
3. Écouter un podcast lent pour apprenants, puis un podcast natif sur un sujet connu (palier 3).
4. Regarder un épisode déjà vu en français, en anglais avec sous-titres anglais (palier 3).
5. Écrire trois lignes par jour dans « Ma version ».
6. Penser une phrase en anglais avant chaque appel ou chaque réunion importante.
7. Lire à voix haute une page par jour (palier 4).
8. Converser une fois par semaine avec un anglophone (échange linguistique, collègue, association).
9. Rejouer mentalement une conversation de la journée en anglais, le soir.
10. Choisir un domaine de passion et n'en consommer le contenu qu'en anglais (palier 5).

L'ouvrage ne recommande aucun service tiers nommément et n'ouvre aucun lien externe sans confirmation du lecteur.

### 18.9 Le profil du lecteur

Au fil des retrouvailles, l'ouvrage repère localement les **familles de difficultés** du lecteur (par exemple : formes faibles, *h*, paires *ɪ/iː*, verbes à particule, accent de mots transparents). Ces familles sont déduites des expressions marquées « Pas encore » à plusieurs reprises et des erreurs de L'oreille fine (mots manqués par catégorie grammaticale). La page « Ce qui vous résiste » de Mon carnet les présente sans jugement, avec, pour chacune, la page de secret correspondante (16) et un chemin de renfort. Aucune donnée ne quitte le téléphone.

---

## 19. Les modules sonores avancés

Onze modules complètent les scènes. Tous reposent sur des voix produites et contrôlées selon la section 7 : enregistrements existants là où la variété des voix réelles est le but, voix créées ailleurs. Aucune voix n'est produite, transformée ou accélérée par l'appareil. Chaque module décrit ci-dessous son principe, son contenu, son interface, ses volumes et sa mise en œuvre.

### 19.1 À vous de jouer

**Principe.** Le lecteur tient un rôle dans une conversation. Le partenaire (une voix de l'ouvrage) parle ; le lecteur choisit parmi deux ou trois répliques possibles, **les dit à voix haute**, puis touche « J'ai dit ». Le partenaire répond selon la réplique choisie. C'est une conversation à embranchements, entièrement préenregistrée.

**Contenu.** Une conversation par scène (163, plus une au Prélude pour s'initier), de 6 à 10 échanges, avec 2 à 3 branches par échange qui se rejoignent toutes au bout de deux répliques (graphe borné, pas d'arbre explosif). Environ 30 énoncés enregistrés par conversation pour chaque interprétation retenue.

**Déroulé d'un échange.**
1. Le partenaire parle (rythme choisi par le lecteur).
2. Les répliques possibles apparaissent, en anglais, avec leur sens en petit (masquable).
3. Le lecteur dit sa réplique. Le bouton « J'ai dit » s'active après 1 seconde.
4. Option « Entendre la mienne » : la réplique choisie, dite par une voix du même accent.
5. Le partenaire enchaîne.

**Mode « Sans filet »** (paliers 4 à 6) : les répliques ne s'affichent pas ; le lecteur parle librement puis voit la réplique la plus proche parmi celles prévues, qu'il choisit lui-même pour poursuivre.

**Modèle de données.**
```json
{
  "id": "c07-s03-jouer",
  "partenaire": "UK-F2",
  "noeuds": [
    { "id": "n1", "dit": "c07-s03-j-n1", "texte": "Hiya, what can I get you?",
      "repliques": [
        { "texte": "Could I have a flat white, please?", "sens": "Je pourrais avoir un flat white, s'il vous plaît ?", "audio": "c07-s03-j-r1a", "suite": "n2a" },
        { "texte": "What would you recommend?", "sens": "Que me conseillez-vous ?", "audio": "c07-s03-j-r1b", "suite": "n2b" }
      ] }
  ]
}
```
La vérification `tools/verifier_jouer.py` contrôle que chaque nœud est atteignable, que toute branche rejoint le tronc en au plus deux échanges, que chaque fin est atteinte, et que chaque `audio` existe dans le manifeste.

### 19.2 Les annonces

**Principe.** Comprendre les voix que l'on ne choisit pas : annonces de gare, d'aéroport, de métro, messages de répondeur, consignes de sécurité, boîtes vocales d'entreprise, météo, radio de circulation.

**Contenu.** 240 annonces écrites d'après les formulations réelles en usage (« Mind the gap », « This is a final call for passengers… », « Please hold, your call is important to us »), réparties US et UK, chacune dite par deux voix. Les ambiances (hall de gare, cabine d'avion, quai) sont des **prises de son réelles** sous licence libre, mêlées à la lecture sur une piste distincte (19.3).

**Exercice.** Une question pratique par annonce (« Quel quai ? », « À quelle heure ? », « Que devez-vous faire ? »), réponse par choix ou par saisie de chiffres.

### 19.3 L'oreille dans le bruit

**Principe.** Entraîner la compréhension en conditions réelles : café, rue, voiture, fête, téléphone.

**Mise en œuvre.** Chaque scène peut être écoutée avec une **ambiance réelle** jouée simultanément sur un second lecteur. La voix n'est jamais modifiée ; seule l'ambiance est ajoutée. Six ambiances de 3 minutes en boucle sans couture (café, rue, gare, voiture, fête, open space), issues de prises de son réelles publiées sous licence libre (CC0 ou CC BY, vérifiée fichier par fichier), en stéréo 48 kHz, livrées en Opus 96 kb/s stéréo. Trois niveaux : « Léger » (ambiance à −24 LUFS sous une voix à −18), « Animé » (−20), « Comme en vrai » (−17). L'effet **téléphone** est la seule transformation permise : il est réalisé à la production, une fois pour toutes, par un filtrage passe-bande 300–3 400 Hz appliqué à une copie des fichiers de 40 scènes, et livré comme fichier distinct marqué `tel` ; la voix originale reste intacte.

### 19.4 Les chiffres et les lettres

**Principe.** Les chiffres sont l'un des premiers points de rupture de la compréhension : prix, numéros de téléphone, dates, heures, adresses, codes, épellations.

**Contenu.** Environ 1 500 énoncés : nombres de 0 à 1 000 000, paires piégeuses (*thirteen/thirty*, *fifteen/fifty*), prix (*four ninety-nine*, *a fiver*, *a quid*, *a buck*), heures UK et US (*half past*, *quarter to*, *ten after*), dates (*the third of May* / *May third*), années (*nineteen eighty-four*, *twenty twenty-six*), téléphones (*double five*, *oh* et *zero*), alphabet complet, épellation d'adresses e-mail (*at*, *dot*, *underscore*, *hyphen/dash*), alphabet radio.

**Exercice.** Dictée rapide : un énoncé, une saisie, une correction immédiate avec réécoute du segment manqué.

### 19.5 L'échelle de politesse

**Principe.** Rendre audible la différence entre une demande brusque et une demande parfaite (16.36).

**Contenu.** 60 demandes de la vie courante, chacune en six degrés, du plus direct (*Window.*) au plus délicat (*I don't suppose you could possibly open the window, could you?*), dites par une voix US et une voix UK. Total 720 énoncés.

**Exercice.** « Dans quelle situation ? » : un degré est joué, le lecteur choisit à qui il conviendrait (ami, collègue, inconnu, supérieur). Puis « Remontez l'échelle » : on lui donne un degré, il dit le degré supérieur, puis l'entend.

### 19.6 Les paires à seize voix

**Principe.** L'entraînement phonétique à haute variabilité : entendre un même contraste dans la bouche de nombreuses voix différentes. Une méta-analyse de 79 études conclut à un effet important sur la perception, avec une généralisation plus limitée vers des contextes nouveaux (Uchihara et al., Studies in Second Language Acquisition — <https://www.cambridge.org/core/journals/studies-in-second-language-acquisition/article/high-variability-phonetic-training-hvpt-a-metaanalysis-of-l2-perceptual-training-studies/6ABB8C1F32D88D53EA8D05A4565E76F6>). L'ouvrage en tire deux règles : beaucoup de voix, et des mots variés.

**Les 18 contrastes.**

| # | Contraste | Exemple | # | Contraste | Exemple |
|---|---|---|---|---|---|
| 1 | /ɪ/ – /iː/ | *ship / sheep* | 10 | /θ/ – /s/ | *think / sink* |
| 2 | /ʊ/ – /uː/ | *full / fool* | 11 | /θ/ – /t/ | *thank / tank* |
| 3 | /æ/ – /ʌ/ | *cat / cut* | 12 | /ð/ – /z/ | *then / Zen* |
| 4 | /ʌ/ – /ɑː/ | *cut / cart* | 13 | /ð/ – /d/ | *they / day* |
| 5 | /e/ – /æ/ | *bed / bad* | 14 | /h/ – rien | *hat / at* |
| 6 | /ɜː/ – /ɔː/ | *work / walk* | 15 | /v/ – /w/ | *vine / wine* |
| 7 | /ɔː/ – /əʊ/ | *law / low* | 16 | /tʃ/ – /ʃ/ | *chair / share* |
| 8 | /ɒ/ – /əʊ/ | *not / note* | 17 | /s/ – /z/ en finale | *price / prize* |
| 9 | /eɪ/ – /e/ | *late / let* | 18 | /n/ – /ŋ/ | *thin / thing* |

**Contenu.** 18 contrastes, 40 paires de mots par contraste, 2 mots par paire, **16 voix** (les huit voix principales et huit voix complémentaires : deux australiennes, deux irlandaises, deux écossaises, deux canadiennes). Total : 18 × 40 × 2 × 16 = **23 040 fichiers** de mots isolés. Les enregistrements existants de locuteurs réels (7.3) sont employés en priorité pour chaque mot disponible dans l'accent voulu ; les autres mots sont créés dans une phrase porteuse (« Now say … again. ») puis découpés d'après l'alignement, pour conserver un débit naturel.

**Réserve.** Quatre voix sur seize ne sont jamais utilisées à l'entraînement : elles servent aux épreuves (18.3), pour mesurer une vraie généralisation. Ce sont, autant que possible, des enregistrements existants de locuteurs réels.

**Exercice.** Deux images ou deux mots ; une voix au hasard prononce l'un d'eux ; le lecteur touche celui qu'il a entendu ; réponse immédiate, réécoute de la paire dans la même voix. Séances de 40 essais, environ 5 minutes. Le choix des voix et des paires est tiré sans répétition immédiate.

### 19.7 La parole en relais

**Principe.** La technique dite « 4/3/2 » : raconter la même histoire trois fois de suite, en 4, puis 3, puis 2 minutes. Le contenu étant connu, la contrainte de temps oblige l'aisance ; des travaux rapportent des gains de débit et de fluidité (étude disponible sur ERIC — <https://files.eric.ed.gov/fulltext/EJ1171669.pdf>).

**Interface.** Un sujet (lié à la scène), un compte à rebours visible et sonore discret, trois manches. L'enregistrement est facultatif ; s'il est activé, chaque manche est conservée et la courbe de fluidité (19.11) est affichée après la troisième. Durées réglables 3/2/1 pour les paliers 1 et 2.

### 19.8 L'ombre

**Principe.** Répéter en même temps que la voix, avec un léger décalage, comme une ombre. Une synthèse récente des études sur cette pratique conclut à des effets positifs sur la compréhension orale et la prononciation, avec une grande variété de protocoles (Whitworth et Rose, 2025 — <https://www.tandfonline.com/doi/full/10.1080/29984475.2025.2546827>).

**Déroulé en quatre temps.** 1. Écoute seule, texte visible. 2. Ombre à voix basse, texte visible, rythme posé. 3. Ombre à voix haute, texte masqué, rythme posé. 4. Ombre à voix haute, rythme spontané. Le texte suit la voix au mot près (8.14). Un mode « Phrase par phrase » insère une pause égale à 1,3 fois la durée de la phrase entre chaque phrase.

### 19.9 Les Voix du monde

**Principe.** L'anglais se parle partout ; le lecteur doit comprendre aussi ceux qui ne sont ni Américains ni Britanniques.

**Contenu.** 24 scènes courtes (2 à 3 minutes), chacune avec une voix d'une autre variété : australienne, néo-zélandaise, irlandaise, écossaise, galloise, canadienne, sud-africaine, nigériane, ghanéenne, kényane, indienne, singapourienne, jamaïcaine, et des voix d'anglophones non natifs (français, espagnol, allemand, chinois, arabe, brésilien), car la majorité des conversations en anglais se déroule entre non-natifs. Les voix non natives proviennent en priorité d'enregistrements existants de locuteurs réels, dont l'accent est déclaré (7.3). Chaque scène offre une page « Ce qui change » : trois à cinq traits audibles, illustrés par des extraits.

### 19.10 Le diagnostic d'oreille

**Principe.** Savoir en dix minutes où porter l'effort.

**Contenu.** 60 items : 20 paires de sons (voix réservées), 15 énoncés où compter les mots, 10 phrases où repérer le mot fort, 10 chiffres, 5 extraits spontanés. Proposé à l'accueil (facultatif), puis à volonté.

**Résultat.** Une page en phrases, classant les dix priorités de 16.1 du plus urgent au moins urgent pour ce lecteur, chacune avec son lien direct. Le diagnostic alimente le profil (18.9).

### 19.11 La fluidité mesurée

**Principe.** Montrer au lecteur sa propre aisance, sans reconnaissance vocale ni envoi de données.

**Mise en œuvre.** Lorsque le lecteur s'enregistre (écho, relais, voix du premier jour), l'ouvrage calcule **localement** sur le signal : la durée totale, le temps de parole (détection d'énergie par fenêtres de 20 ms, seuil adaptatif sur le bruit de fond mesuré pendant les 300 premières millisecondes), le nombre et la durée des pauses de plus de 250 ms, la longueur moyenne des « coulées » de parole entre deux pauses. Aucun mot n'est reconnu. L'affichage : une courbe de l'énergie (même dessin que 8.15) et trois indications en phrases (« Vos coulées durent en moyenne 2,4 secondes, contre 1,6 la semaine dernière. »). Le calcul tient dans `app/src/lib/voix/fluidite.ts`, en Web Audio (`OfflineAudioContext`, `AnalyserNode` non requis), moins de 200 ms pour un enregistrement de 2 minutes sur un appareil d'entrée de gamme.

```ts
export interface Fluidite { dureeS: number; paroleS: number; pauses: number; couleeMoyS: number; }
export function mesurer(pcm: Float32Array, hz = 48000): Fluidite {
  const fen = Math.round(hz * 0.02); const n = Math.floor(pcm.length / fen);
  const e = new Float32Array(n);
  for (let i = 0; i < n; i++) { let s = 0; for (let j = 0; j < fen; j++) { const v = pcm[i * fen + j]; s += v * v; } e[i] = Math.sqrt(s / fen); }
  const bruit = e.slice(0, Math.min(15, n)).reduce((a, b) => a + b, 0) / Math.max(1, Math.min(15, n));
  const seuil = Math.max(bruit * 3, 0.01);
  let parole = 0, pauses = 0, silence = 0, coulees: number[] = [], cour = 0;
  for (let i = 0; i < n; i++) {
    if (e[i] > seuil) { parole++; cour++; if (silence >= 13 && cour === 1) pauses++; silence = 0; }
    else { silence++; if (silence === 13 && cour > 0) { coulees.push(cour); cour = 0; } }
  }
  if (cour > 0) coulees.push(cour);
  const moy = coulees.length ? coulees.reduce((a, b) => a + b, 0) / coulees.length : 0;
  return { dureeS: n * 0.02, paroleS: parole * 0.02, pauses, couleeMoyS: moy * 0.02 };
}
```

### 19.12 Volumes des modules

| Module | Fichiers | Durée de parole estimée |
|---|---|---|
| À vous de jouer (164 × 30 × 2 interprétations) | ≈ 9 840 | ≈ 6 h |
| Les annonces (240 × 2) | 480 | ≈ 1 h |
| Les chiffres et les lettres (1 500 × 4 voix) | ≈ 6 000 | ≈ 2 h |
| L'échelle de politesse | 720 | ≈ 0,5 h |
| Les paires à seize voix | 23 040 | ≈ 3 h |
| Les Voix du monde (24 scènes) | ≈ 1 200 | ≈ 1 h |
| Le diagnostic et les épreuves (réserve) | ≈ 1 600 | ≈ 0,7 h |
| Les secrets (16) et la grammaire parlée (17) | ≈ 13 000 | ≈ 8 h |
| Ambiances réelles | 6 | 0,3 h |
| **Total des modules** | **≈ 56 000** | **≈ 22,5 h** |

---

## 20. L'échelle industrielle

Cette section décrit comment l'ouvrage se fabrique, se vérifie et se maintient à l'échelle de plusieurs centaines de milliers de fichiers sonores et d'une distribution sur plusieurs magasins, sans jamais sacrifier la promesse : des voix vivantes, rien qui quitte le téléphone.

### 20.1 La chaîne de production

Le corpus (fichiers YAML de `corpus/`) reste la source unique. Toute la production, du texte au fichier Opus, est une **chaîne de commandes rejouables**, orchestrée par `tools/construire.py` et `voix/outils/creer.py` :

| Étape | Commande | Entrée | Sortie | Reprise |
|---|---|---|---|---|
| Validation | `construire.py --valider` | YAML | Rapport P1 | Immédiate |
| Scripts | `scripts_voix.py --voix` | Corpus validé | JSONL par voix | Idempotente |
| Sources libres | `sources_libres.py` | Jeux de données | Candidats sous licence | Idempotente |
| Création | `creer.py --lot {voix}:{chapitre}` | JSONL | Quatre prises WAV par interprétation | Reprend au dernier énoncé non créé |
| Choix | `choisir.py --lot …` | Prises | Prise retenue, registre | Idempotente |
| Finition | `normaliser.py`, `decouper.py`, `encoder.py` | Prises retenues | Masters, Opus | Idempotente |
| Mesures | `aligner.py`, `syllaber.py`, `courbe.py` | Masters | Mots, syllabes, courbes | Idempotente |
| Contrôle | `controler.py` | Opus, manifestes | Rapports P3, P4 | Immédiate |

Chaque étape lit et écrit des fichiers datés, avec empreinte ; une étape interrompue reprend où elle s'est arrêtée ; aucune étape ne modifie l'entrée d'une autre. Les lots sont traités en parallèle par voix et par chapitre, dans la limite de débit du moteur.

### 20.2 La constance à grande échelle

Sur plusieurs centaines de milliers de fichiers, la constance se garantit par la méthode, jamais par l'espoir :

- **Fiches vocales figées** (7.4) : description, moteur, version, réglages ; toute modification crée une nouvelle voix, jamais une retouche de l'ancienne.
- **Référence de timbre** : chaque fichier est comparé à la référence de sa voix (7.10) ; la similarité moyenne de chaque lot est suivie, et une baisse de plus de 0,03 par rapport au premier lot suspend la voix jusqu'à examen.
- **Lot témoin** : les 40 lignes du script d'essai sont recréées au début de chaque lot et comparées à la référence ; un écart bloque le lot.
- **Couleur sonore commune** : les enregistrements existants et les voix créées partagent les mêmes seuils de niveau, de silence et de bande passante ; leur équilibre spectral moyen est mesuré par module, et un écart de plus de 3 dB dans une bande d'octave entre deux sources d'un même exercice est signalé.

### 20.3 Le contrôle statistique des voix

Au-delà des contrôles sur 100 % des fichiers (7.10), une **écoute comparative par échantillonnage** s'applique à chaque lot (un lot = une voix × un chapitre) : 8 % des fichiers (au moins 80) sont tirés au hasard et comparés à l'aveugle à des enregistrements réels, avec une grille de défauts majeurs. Plus de 1 % de défauts majeurs (mot erroné, bruit, coupe, rythme hors norme) entraîne l'écoute intégrale du lot. Les taux de défaut par voix, par moteur et par module sont suivis dans le registre et déclenchent un recalage dès qu'ils dépassent 0,5 % sur trois lots consécutifs.

### 20.4 La chaîne d'approvisionnement logicielle

- **Dépendances figées** : `package-lock.json`, verrouillage Gradle (`gradle --write-locks`), vérification des signatures des dépendances (`gradle/verification-metadata.xml`).
- **Inventaire des composants** : un inventaire au format CycloneDX est produit à chaque compilation de publication et archivé avec l'AAB et l'APK.
- **Compilations reproductibles** : horodatages figés (`SOURCE_DATE_EPOCH`), ordre des fichiers déterministe ; deux compilations du même commit produisent des archives identiques octet pour octet, vérifiées une fois par publication sur deux machines différentes.
- **Analyse des vulnérabilités** : `npm audit` et OWASP Dependency-Check à chaque demande de fusion ; toute vulnérabilité haute bloque la publication.
- **Attestation** : chaque binaire publié est accompagné de sa somme SHA-256 et d'une attestation de provenance signée, publiées sur la page de distribution directe (10.18).

### 20.5 L'observation sans traceur

L'ouvrage n'embarque aucun outil d'analyse. La santé de l'application s'observe uniquement par les **statistiques agrégées de la Play Console** (plantages, ANR, temps de démarrage, consommation), qui ne demandent aucun code dans l'application, et par les journaux de contretemps que les lecteurs choisissent d'envoyer (8.25). Seuils d'alerte : taux de plantage perçu par l'utilisateur > 0,5 %, ANR > 0,2 %. Un dépassement suspend le déploiement progressif.

### 20.6 Les obligations de Google Play

Google Play exige que les nouvelles applications et les mises à jour ciblent un niveau d'API récent ; à compter du 31 août 2026, le niveau exigé est Android 16 (API 36) (Aide Play Console — <https://support.google.com/googleplay/android-developer/answer/11926878?hl=en>). L'ouvrage cible déjà l'API 36 (0.4). Chaque année, la montée de l'API cible est préparée dès la publication de la nouvelle version d'Android, testée sur la matrice 11.3 et publiée avant l'échéance.

### 20.7 Les autres magasins

L'application PEUT être publiée sur d'autres magasins Android (par exemple Samsung Galaxy Store, Huawei AppGallery, F-Droid pour une édition sans composant Google). Chacun est une **saveur Gradle** distincte (`play`, `direct`, `galaxy`, `appgallery`), qui ne change que le mode de livraison des voix complémentaires : Play Asset Delivery pour `play`, téléchargement depuis le serveur de l'éditeur pour les autres (10.18). Le contenu, les voix et l'expérience sont strictement identiques.

### 20.8 L'édition pour la classe

**Le Livre en classe** est un mode de l'ouvrage, sans compte ni serveur :
- l'enseignant compose une **liste de lecture** (scènes, itinéraires, expressions) et la partage sous forme de code QR ; ce code ne contient que des identifiants d'expressions (format `vla:l:c07-s03,c10-s02,...`) ;
- l'élève scanne le code avec l'appareil photo ; l'ouvrage ouvre la liste, sans aucun échange réseau ;
- le **mode projection** affiche une expression en très grand, avec les quatre voix et le phrasé, pour un écran de classe ou un téléviseur relié ;
- des **fiches imprimables** (PDF générés à la compilation, une par scène) reprennent le texte, le sens et un code QR qui ouvre la scène dans l'ouvrage.

### 20.9 Les autres langues d'accompagnement

L'architecture permet d'accompagner l'anglais depuis d'autres langues que le français. Le sens, les notes d'usage, les faux pas et le phrasé sont propres à chaque langue du lecteur ; les voix anglaises sont communes. Dans le corpus, les champs de langue d'accompagnement sont suffixés (`sens.fr`, `sens.es`, `sens.pt`, `sens.ar`) ; les phrasés à la française sont remplacés par un phrasé propre à chaque langue, établi selon les règles phonologiques de cette langue. Chaque langue d'accompagnement est une édition distincte, avec sa propre voix du sens, son identifiant d'application et sa fiche Play ; elle n'est publiée que lorsque l'ensemble de ses textes a passé les sept portes.

### 20.10 Le droit et la conformité

- **Données personnelles** : l'ouvrage ne collecte rien (10.13). La fiche « Sécurité des données » de Google Play le déclare. L'éditeur respecte le règlement général sur la protection des données pour ses lecteurs européens et, en Côte d'Ivoire, la loi n° 2013-450 du 19 juin 2013 relative à la protection des données à caractère personnel ; aucune déclaration de traitement n'est nécessaire pour l'application elle-même, puisqu'elle ne traite aucune donnée hors de l'appareil. 
- **Voix** : licences des enregistrements existants vérifiées fichier par fichier, conditions du moteur archivées, crédits et transparence selon 7.12.
- **Accessibilité** : conformité visée au niveau AA des règles d'accessibilité WCAG 2.2 pour l'interface (section 9) et à la norme européenne EN 301 549 pour les ventes institutionnelles.

### 20.11 La conservation des masters

Les masters (WAV 48 kHz/24 bits), le registre des créations et les fiches vocales sont le patrimoine de l'ouvrage. Ils sont conservés selon la règle **3-2-1** : trois copies, sur deux supports différents, dont une hors site ; une restauration de contrôle est effectuée chaque trimestre sur un échantillon de 1 000 fichiers tirés au hasard, comparés à leur somme de contrôle. Les masters ne sont jamais réencodés à partir des fichiers Opus.

---

## 21. Les volumes de l'œuvre intégrale

### 21.1 Les volumes consolidés

| Ensemble | Fichiers | Parole nette | Poids encodé |
|---|---|---|---|
| Scènes, Prélude, déclinaisons et répliques (7.2) | ≈ 245 000 | ≈ 112 h | ≈ 1,5 Go |
| Voix du sens (français) | ≈ 11 250 | ≈ 6 h | ≈ 80 Mo |
| Modules sonores avancés (19.12), secrets (16) et grammaire parlée (17) | ≈ 56 000 | ≈ 22,5 h | ≈ 300 Mo |
| **Œuvre intégrale** | **≈ 312 000** | **≈ 140 h** | **≈ 1,9 Go** |

Les modules sont livrés comme les chapitres (10.9) : un paquet de voix par module, installé à la demande. Le socle installé d'emblée reçoit uniquement le diagnostic d'oreille (19.10), les 41 pages de secrets en version courte (un exemple par secret) et l'échelle de politesse, soit ≈ 25 Mo supplémentaires.

### 21.2 Le volume de création

| Grandeur | Estimation | Base |
|---|---|---|
| Fichiers retenus | ≈ 312 000 | 21.1 |
| Part issue d'enregistrements existants | ≈ 10 000 à 20 000 | Mots isolés, paires, voix réservées, voix du monde non natives (7.3) |
| Prises créées | ≈ 1,2 million | Quatre prises par interprétation (7.9), moins les fichiers issus d'enregistrements existants |
| Texte dit | ≈ 30 millions de caractères | ≈ 23 caractères par énoncé en moyenne, quatre prises |
| Masters retenus | ≈ 75 Go | 140 h en WAV 48 kHz/24 bits mono (≈ 518 Mo par heure) |
| Prises non retenues, archivées | ≈ 220 Go | Conservées jusqu'à la publication de l'édition qui les concerne, puis supprimées |

Ces grandeurs dimensionnent le stockage objet, la parallélisation des lots (20.1) et les limites de débit à négocier avec le moteur retenu.

---

## Annexe A — La scène étalon

La scène 1.1 « Le réveil et les premières minutes » sert d'étalon : elle est rédigée, mise en voix, finie et transcrite la première, ses mesures (durées, débits, taux de prises refusées, scores des contrôles 7.10) recalibrent toute la production, et chaque scène de l'ouvrage se mesure à elle. Ci-dessous, trois expressions complètes au format d'édition (l'expression A1 figure en 10.4), puis la scène vivante bilingue et localisée, puis le rendu attendu à l'écran.

### A.1 Expressions complètes (YAML)

```yaml
      - id: c01.s01.A3
        ton: courant
        niveau: fondations
        frequence: 5
        situations: [matin, maison, retard]
        fonctions: [s-excuser, expliquer]
        enonces:
          - id: c01.s01.A3.e1
            region: commun
            texte: { uk: "I hit snooze.", us: "I hit snooze." }
            jeu: { contexte: "Admitting to a partner why you're late getting up.", emotion: "sheepish, a little amused" }
            phrases:
              uk:
                pose:     { phrase: "aï HIT SNOÛZ ↘",  expert: "/aɪ ˈhɪt ˈsnuːz/" }
                spontane: { phrase: "aï HIʔ SNOÛZ ↘",  expert: "/aɪ ˈhɪʔ ˈsnuːz/" }
              us:
                pose:     { phrase: "aï HIT SNOÛZ ↘",  expert: "/aɪ ˈhɪt ˈsnuz/" }
                spontane: { phrase: "aï HI(t) SNOÛZ ↘", expert: "/aɪ ˈhɪt̚ ˈsnuz/" }
          - id: c01.s01.A3.e2
            region: commun
            texte: { uk: "I hit snooze three times.", us: "I hit snooze three times." }
            jeu: { contexte: "Same confession, exaggerated for effect.", emotion: "guilty grin" }
            phrases:
              uk:
                pose:     { phrase: "aï HIT SNOÛZ THRII TAÏMZ ↘", expert: "/aɪ ˈhɪt ˈsnuːz ˈθriː ˈtaɪmz/" }
                spontane: { phrase: "aï HIʔ SNOÛZ thrii TAÏMZ ↘", expert: "/aɪ ˈhɪʔ ˈsnuːz θriː ˈtaɪmz/" }
              us:
                pose:     { phrase: "aï HIT SNOÛZ THRII TAÏMZ ↘", expert: "/aɪ ˈhɪt ˈsnuz ˈθri ˈtaɪmz/" }
                spontane: { phrase: "aï HI(t) SNOÛZ thrii TAÏMZ ↘", expert: "/aɪ ˈhɪt̚ ˈsnuz θri ˈtaɪmz/" }
        sens: J'ai appuyé sur « répéter » (trois fois).
        motAMot: j'ai frappé « somnoler »
        usage: >-
          Snooze, c'est la touche qui fait sonner le réveil de nouveau quelques
          minutes plus tard. La phrase sert d'aveu léger pour expliquer un petit
          retard. Le verbe hit est le seul naturel ici : on ne dit pas I pressed snooze
          dans la conversation.
        gabarit: "I hit [une touche]"
        declinaisons:
          - { id: c01.s01.A3.d1, texte: { uk: "I hit snooze again.", us: "I hit snooze again." }, sens: "J'ai encore appuyé sur « répéter »." }
          - { id: c01.s01.A3.d2, texte: { uk: "I kept hitting snooze.", us: "I kept hitting snooze." }, sens: "Je n'arrêtais pas d'appuyer sur « répéter »." }
          - { id: c01.s01.A3.d3, texte: { uk: "Don't hit snooze!", us: "Don't hit snooze!" }, sens: "N'appuie pas sur « répéter » !" }
          - { id: c01.s01.A3.d4, texte: { uk: "I must've hit snooze in my sleep.", us: "I must've hit snooze in my sleep." }, sens: "J'ai dû appuyer sur « répéter » en dormant." }
          - { id: c01.s01.A3.d5, texte: { uk: "I hit the off button by mistake.", us: "I hit the off button by mistake." }, sens: "J'ai appuyé sur « arrêt » par erreur." }
        renvois: [c01.s01.H1]

  - lettre: B
    titre: Réveiller quelqu'un
    expressions:
      - id: c01.s01.B1
        ton: courant
        niveau: fondations
        frequence: 5
        situations: [matin, maison, famille]
        fonctions: [inciter]
        enonces:
          - id: c01.s01.B1.e1
            region: commun
            texte: { uk: "Wake up!", us: "Wake up!" }
            jeu: { contexte: "Gently shaking a sleeping partner's shoulder.", emotion: "warm, slightly insistent" }
            phrases:
              uk:
                pose:     { phrase: "wéïk EUP ↘",  expert: "/weɪk ˈʌp/" }
                spontane: { phrase: "wéï‿KEUP ↘",  expert: "/weɪˈkʌp/" }
              us:
                pose:     { phrase: "wéïk EUP ↘",  expert: "/weɪk ˈʌp/" }
                spontane: { phrase: "wéï‿KEUP ↘",  expert: "/weɪˈkʌp/" }
          - id: c01.s01.B1.e2
            region: commun
            texte: { uk: "Come on, wake up!", us: "Come on, wake up!" }
            jeu: { contexte: "Third attempt, the clock is ticking.", emotion: "playful pressure" }
            phrases:
              uk:
                pose:     { phrase: "keum ON · wéïk EUP ↘",   expert: "/kʌm ˈɒn | weɪk ˈʌp/" }
                spontane: { phrase: "kə·MON wéï‿KEUP ↘",      expert: "/kəˈmɒn weɪˈkʌp/" }
              us:
                pose:     { phrase: "keum ÂN · wéïk EUP ↘",   expert: "/kʌm ˈɑn | weɪk ˈʌp/" }
                spontane: { phrase: "kə·MÂN wéï‿KEUP ↘",      expert: "/kəˈmɑn weɪˈkʌp/" }
        sens: Réveille-toi ! / Allez, réveille-toi !
        usage: >-
          Direct et neutre. Avec come on, on ajoute une pression amicale.
          Attention : wake up, c'est sortir du sommeil ; get up, c'est sortir du lit.
        gabarit: "Wake [quelqu'un] up"
        declinaisons:
          - { id: c01.s01.B1.d1, texte: { uk: "Wake me up at seven.", us: "Wake me up at seven." }, sens: "Réveille-moi à sept heures." }
          - { id: c01.s01.B1.d2, texte: { uk: "Don't wake the baby up.", us: "Don't wake the baby up." }, sens: "Ne réveille pas le bébé." }
          - { id: c01.s01.B1.d3, texte: { uk: "Can you wake me up when we get there?", us: "Can you wake me up when we get there?" }, sens: "Tu peux me réveiller quand on arrive ?" }
          - { id: c01.s01.B1.d4, texte: { uk: "What woke you up?", us: "What woke you up?" }, sens: "Qu'est-ce qui t'a réveillé ?" }
          - { id: c01.s01.B1.d5, texte: { uk: "Sorry, did I wake you?", us: "Sorry, did I wake you?" }, sens: "Pardon, je t'ai réveillé ?" }
        renvois: [c01.s01.I1]
```

Points à observer : chaque énoncé porte quatre phrasés distincts ; le coup de glotte britannique (ʔ) et le *t* retenu américain ((t)) ne sont notés qu'en spontané ; chaque déclinaison a son sens ; le renvoi vers I1 est un lien typé.

### A.2 La scène vivante, localisée

Personnages : **Kofi** et **Sarah** (bible 5.4), **Mia** leur fille. Chaque scène vivante est produite en un dialogue continu dans chaque accent, en posé puis en spontané.

| # | Personnage | Version britannique | Version américaine | Le sens |
|---|---|---|---|---|
| 1 | Kofi | Rise and shine! | Rise and shine! | Debout là-dedans ! |
| 2 | Sarah | Ugh… five more minutes. | Ugh… five more minutes. | Pff… encore cinq minutes. |
| 3 | Kofi | You said that twenty minutes ago. It's half seven! | You said that twenty minutes ago. It's seven-thirty! | Tu as dit ça il y a vingt minutes. Il est sept heures et demie ! |
| 4 | Sarah | What? Why didn't you wake me up? | What? Why didn't you wake me up? | Quoi ? Pourquoi tu ne m'as pas réveillée ? |
| 5 | Kofi | I tried! You told me to go away. | I tried! You told me to go away. | J'ai essayé ! Tu m'as dit de te laisser tranquille. |
| 6 | Sarah | My alarm didn't go off… I must've turned it off in my sleep. | My alarm didn't go off… I must've turned it off in my sleep. | Mon réveil n'a pas sonné… J'ai dû l'éteindre en dormant. |
| 7 | Kofi | Rough night? | Rough night? | Mauvaise nuit ? |
| 8 | Sarah | I didn't sleep a wink. You were snoring like a chainsaw. | I didn't sleep a wink. You were snoring like a chainsaw. | Je n'ai pas fermé l'œil. Tu ronflais comme une tronçonneuse. |
| 9 | Kofi | I don't snore! | I don't snore! | Je ne ronfle pas ! |
| 10 | Sarah | Whatever. I need a coffee. Don't talk to me yet. | Whatever. I need coffee. Don't talk to me yet. | C'est ça. Il me faut un café. Ne me parle pas encore. |
| 11 | Mia (depuis le couloir) | Mum! Have you seen my school shoes? | Mom! Have you seen my sneakers? | Maman ! Tu as vu mes chaussures (d'école / de sport) ? |
| 12 | Sarah | Kofi, can you deal with that? I'm not awake yet. | Kofi, can you handle that? I'm not awake yet. | Kofi, tu peux t'en occuper ? Je ne suis pas encore réveillée. |
| 13 | Kofi | On it. Someone got out of bed on the wrong side… | On it. Someone woke up on the wrong side of the bed… | J'y vais. Quelqu'un s'est levé du pied gauche… |
| 14 | Sarah | I heard that! | I heard that! | Je t'ai entendu ! |

Différences régionales mises en valeur par la scène (et reprises dans « Deux Anglais ») : *half seven* / *seven-thirty* ; *a coffee* (britannique plus fréquent) / *coffee* ; *Mum* / *Mom* ; *school shoes* / *sneakers* ; *deal with* / *handle* ; *got out of bed on the wrong side* / *woke up on the wrong side of the bed*.

### A.3 Le rendu attendu de la carte A3 (thème Papier, accent britannique, rythme spontané)

```
┌──────────────────────────────────────────────────────┐
│ Moment A · Le réveil sonne                  3 sur 7  │
│                                                      │
│  I hit snooze.                                 ◉     │   ← toucher : voix Brit. spontanée
│  aï HI’ SNOÛZ ↘                                      │   ← phrasé (’ = coup de glotte)
│                                                      │
│  [ Am. | Brit. ]   [ Posé | Spontané ]   Les quatre voix │
│                                                      │
│  Le sens   J'ai appuyé sur « répéter ».              │
│  Mot à mot   j'ai frappé « somnoler »                │
│                                                      │
│  L'usage   Snooze, c'est la touche qui fait sonner   │
│  le réveil de nouveau quelques minutes plus tard…    │
│                                                      │
│  Autre façon de dire   I hit snooze three times.  ◉  │
│                                                      │
│  Sur le même air — I hit [une touche]                │
│   ◉ I hit snooze again.     J'ai encore appuyé…      │
│   ◉ I kept hitting snooze.  Je n'arrêtais pas…       │
│   ◉ Don't hit snooze!       N'appuie pas…            │
│   …                                                  │
│                                                      │
│  Ton courant · Fondations         → Moment H    ☆   │
└──────────────────────────────────────────────────────┘
```

---

## Annexe B — Le schéma de validation d'une scène

Fichier `corpus/schema/scene.schema.json` (JSON Schema 2020-12), appliqué par `tools/valider_corpus.py` à chaque fichier YAML de `corpus/`, après chargement par `yaml.safe_load`. Il est aussi déclaré dans l'éditeur de texte (extension YAML reliée au schéma), ce qui signale les erreurs pendant la rédaction. Les champs `chapitre` et `numero` du type `Scene` (10.4) ne figurent pas dans le YAML : ils sont déduits de l'identifiant à la compilation. Les règles qui portent sur plusieurs fichiers (renvois, unicité, personnages, itinéraires) sont vérifiées par `valider_corpus.py` en plus du schéma (10.4, règles 2, 3, 10 et 11).

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://vivrelanglais.com/schema/scene.schema.json",
  "title": "Scène de Vivre l'Anglais",
  "type": "object",
  "additionalProperties": false,
  "required": ["id", "titre", "intention", "moments", "essentiel", "sceneVivante", "rituel", "version"],
  "properties": {
    "id": { "type": "string", "pattern": "^c\\d{2}\\.s\\d{2}$" },
    "titre": { "type": "string", "minLength": 3, "maxLength": 60 },
    "intention": { "type": "string", "minLength": 40, "maxLength": 400 },
    "version": { "type": "integer", "minimum": 1 },
    "moments": {
      "type": "array", "minItems": 3, "maxItems": 12,
      "items": { "$ref": "#/$defs/moment" }
    },
    "essentiel": {
      "type": "object", "additionalProperties": false,
      "required": ["incontournables", "fauxPas"],
      "properties": {
        "incontournables": {
          "type": "array", "minItems": 5, "maxItems": 15, "uniqueItems": true,
          "items": { "$ref": "#/$defs/idExpression" }
        },
        "fauxPas": {
          "type": "array", "minItems": 3, "maxItems": 12,
          "items": {
            "type": "object", "additionalProperties": false,
            "required": ["fautif", "naturel", "pourquoi"],
            "properties": {
              "fautif": { "type": "string", "minLength": 2 },
              "naturel": { "type": "string", "minLength": 2 },
              "pourquoi": { "type": "string", "minLength": 10, "maxLength": 300 }
            }
          }
        }
      }
    },
    "sceneVivante": {
      "type": "object", "additionalProperties": false,
      "required": ["titre", "repliques"],
      "properties": {
        "titre": { "type": "string", "minLength": 3 },
        "repliques": {
          "type": "array", "minItems": 8, "maxItems": 24,
          "items": { "$ref": "#/$defs/replique" }
        }
      }
    },
    "rituel": {
      "type": "array", "minItems": 1, "maxItems": 3,
      "items": { "type": "string", "minLength": 10, "maxLength": 240 }
    }
  },
  "$defs": {
    "idExpression": { "type": "string", "pattern": "^c\\d{2}\\.s\\d{2}\\.[A-Z]\\d{1,2}$" },
    "texteAccents": {
      "type": "object", "additionalProperties": false,
      "required": ["uk", "us"],
      "properties": {
        "uk": { "type": "string", "minLength": 1, "maxLength": 140 },
        "us": { "type": "string", "minLength": 1, "maxLength": 140 }
      }
    },
    "phrase": {
      "type": "object", "additionalProperties": false,
      "required": ["phrase", "expert"],
      "properties": {
        "phrase": { "type": "string", "minLength": 1 },
        "expert": { "type": "string", "pattern": "^/.+/$" },
        "entendu": { "type": "string" }
      }
    },
    "rythmes": {
      "type": "object", "additionalProperties": false,
      "required": ["pose", "spontane"],
      "properties": {
        "pose": { "$ref": "#/$defs/phrase" },
        "spontane": { "$ref": "#/$defs/phrase" }
      }
    },
    "phrases": {
      "type": "object", "additionalProperties": false,
      "required": ["uk", "us"],
      "properties": {
        "uk": { "$ref": "#/$defs/rythmes" },
        "us": { "$ref": "#/$defs/rythmes" }
      }
    },
    "enonce": {
      "type": "object", "additionalProperties": false,
      "required": ["id", "region", "texte", "phrases", "jeu"],
      "properties": {
        "id": { "type": "string", "pattern": "^c\\d{2}\\.s\\d{2}\\.[A-Z]\\d{1,2}\\.e\\d{1,2}$" },
        "region": { "enum": ["commun", "us", "uk", "au", "ie", "ng", "gh", "za"] },
        "texte": { "$ref": "#/$defs/texteAccents" },
        "phrases": { "$ref": "#/$defs/phrases" },
        "jeu": {
          "type": "object", "additionalProperties": false,
          "required": ["contexte", "emotion"],
          "properties": {
            "contexte": { "type": "string", "minLength": 10 },
            "emotion": { "type": "string", "minLength": 3 }
          }
        }
      }
    },
    "declinaison": {
      "type": "object", "additionalProperties": false,
      "required": ["id", "texte", "sens", "phrases"],
      "properties": {
        "id": { "type": "string", "pattern": "^c\\d{2}\\.s\\d{2}\\.[A-Z]\\d{1,2}\\.d\\d{1,2}$" },
        "texte": { "$ref": "#/$defs/texteAccents" },
        "sens": { "type": "string", "minLength": 2, "maxLength": 200 },
        "phrases": { "$ref": "#/$defs/phrases" },
        "renvoi": { "$ref": "#/$defs/idExpression" }
      }
    },
    "expression": {
      "type": "object", "additionalProperties": false,
      "required": ["id", "enonces", "sens", "usage", "declinaisons", "ton", "niveau", "frequence", "situations", "fonctions", "renvois"],
      "properties": {
        "id": { "$ref": "#/$defs/idExpression" },
        "enonces": { "type": "array", "minItems": 1, "maxItems": 3, "items": { "$ref": "#/$defs/enonce" } },
        "sens": { "type": "string", "minLength": 2, "maxLength": 200 },
        "motAMot": { "type": "string", "maxLength": 200 },
        "usage": { "type": "string", "minLength": 20, "maxLength": 600 },
        "coulisses": { "type": "string", "maxLength": 450 },
        "gabarit": { "type": "string", "pattern": "\\[.+\\]" },
        "declinaisons": { "type": "array", "minItems": 3, "maxItems": 6, "items": { "$ref": "#/$defs/declinaison" } },
        "ton": { "enum": ["courant", "complice", "cru", "soutenu"] },
        "niveau": { "enum": ["fondations", "aisance", "maitrise"] },
        "frequence": { "type": "integer", "minimum": 1, "maximum": 5 },
        "situations": { "type": "array", "minItems": 1, "items": { "type": "string", "pattern": "^[a-z-]+$" } },
        "fonctions": { "type": "array", "minItems": 1, "items": { "type": "string", "pattern": "^[a-z-]+$" } },
        "renvois": { "type": "array", "uniqueItems": true, "items": { "$ref": "#/$defs/idExpression" } }
      }
    },
    "moment": {
      "type": "object", "additionalProperties": false,
      "required": ["lettre", "titre", "expressions"],
      "properties": {
        "lettre": { "type": "string", "pattern": "^[A-Z]$" },
        "titre": { "type": "string", "minLength": 3, "maxLength": 60 },
        "expressions": { "type": "array", "minItems": 3, "maxItems": 12, "items": { "$ref": "#/$defs/expression" } }
      }
    },
    "replique": {
      "type": "object", "additionalProperties": false,
      "required": ["id", "personnage", "texte", "sens", "emotion"],
      "properties": {
        "id": { "type": "string", "pattern": "^c\\d{2}\\.s\\d{2}\\.sv\\.l\\d{2}$" },
        "personnage": { "type": "string", "pattern": "^[a-z][a-z0-9_]*$" },
        "texte": { "$ref": "#/$defs/texteAccents" },
        "sens": { "type": "string", "minLength": 1, "maxLength": 300 },
        "emotion": { "type": "string", "minLength": 3 }
      }
    }
  }
}
```

Règles de lecture du schéma :

- Les longueurs maximales en caractères (`usage` 600, `coulisses` 450) sont des garde-fous ; la règle éditoriale exacte (70 et 50 mots, 10.4 règle 7) est comptée en mots par `valider_corpus.py`.
- Les phrasés des déclinaisons sont exigés par le schéma ; pendant la rédaction (avant la porte P5), `valider_corpus.py --brouillon` applique une variante du schéma qui rend `phrases` facultatif, pour permettre de valider le texte avant la mise en voix.
- Le Prélude (`c00`) utilise le même schéma ; ses moments contiennent des paires d'écoute exprimées comme des expressions à un énoncé (`frequence` 5, `fonctions: [ecouter]`).

Validation, extrait de `tools/valider_corpus.py` :

```python
import json, pathlib, sys, yaml
from jsonschema import Draft202012Validator

RACINE = pathlib.Path(__file__).resolve().parents[1]
schema = json.loads((RACINE / "corpus/schema/scene.schema.json").read_text(encoding="utf-8"))
if "--brouillon" in sys.argv:
    schema["$defs"]["declinaison"]["required"].remove("phrases")
    schema["$defs"]["enonce"]["required"].remove("phrases")
valideur = Draft202012Validator(schema)

erreurs = 0
for f in sorted((RACINE / "corpus").glob("c[0-9][0-9]/s[0-9][0-9].yaml")):
    scene = yaml.safe_load(f.read_text(encoding="utf-8"))
    for e in sorted(valideur.iter_errors(scene), key=lambda e: list(e.path)):
        erreurs += 1
        print(f"{f.relative_to(RACINE)} : {'/'.join(map(str, e.path)) or '(racine)'} : {e.message}")
sys.exit(1 if erreurs else 0)
```

---

## Annexe C — Fichiers de configuration complets

Les fichiers déjà donnés intégralement dans le corps du plan ne sont pas répétés : `svelte.config.js` (10.6), `capacitor.config.ts` (10.8), `variables.gradle`, ajouts à `app/build.gradle`, `AndroidManifest.xml`, fichiers XML de sauvegarde et de réseau (10.9), flux d'intégration continue (10.16). Les numéros de version marqués « ^ » sont figés (`package-lock.json`) au gel de chaque édition.

### C.1 `app/package.json`

```json
{
  "name": "vivre-anglais",
  "version": "1.0.0",
  "private": true,
  "type": "module",
  "engines": { "node": ">=22" },
  "scripts": {
    "dev": "vite dev",
    "build": "vite build",
    "preview": "vite preview",
    "check": "svelte-kit sync && svelte-check --tsconfig ./tsconfig.json --fail-on-warnings",
    "test": "vitest run --coverage",
    "e2e": "playwright test",
    "android": "npm run build && npx cap sync android && npx cap open android"
  },
  "dependencies": {
    "@capacitor/android": "^8.0.0",
    "@capacitor/app": "^8.0.0",
    "@capacitor/core": "^8.0.0",
    "@capacitor/filesystem": "^8.0.0",
    "@capacitor/haptics": "^8.0.0",
    "@capacitor/local-notifications": "^8.0.0",
    "@capacitor/preferences": "^8.0.0",
    "@capacitor/share": "^8.0.0",
    "@capacitor/splash-screen": "^8.0.0",
    "@capacitor/status-bar": "^8.0.0",
    "@capgo/capacitor-audio-recorder": "^8.0.0",
    "dexie": "^4.0.0",
    "minisearch": "^7.0.0",
    "ts-fsrs": "^5.0.0"
  },
  "devDependencies": {
    "@axe-core/playwright": "^4.10.0",
    "@capacitor/assets": "^3.0.0",
    "@capacitor/cli": "^8.0.0",
    "@playwright/test": "^1.50.0",
    "@sveltejs/adapter-static": "^3.0.0",
    "@sveltejs/kit": "^2.20.0",
    "@sveltejs/vite-plugin-svelte": "^6.0.0",
    "@testing-library/svelte": "^5.2.0",
    "@vitest/coverage-v8": "^3.0.0",
    "svelte": "^5.30.0",
    "svelte-check": "^4.0.0",
    "typescript": "^5.8.0",
    "vite": "^7.0.0",
    "vitest": "^3.0.0"
  }
}
```

Règle : toute dépendance dont la version majeure ne correspond pas à Capacitor 8 est refusée par la revue ; la commande `npx cap doctor` doit être propre avant chaque édition.

### C.2 `app/src/routes/+layout.ts`

```ts
export const prerender = true;
export const ssr = false;      // application entièrement locale, rendue dans la WebView
export const trailingSlash = 'always';
```

### C.3 `app/playwright.config.ts`

```ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: 'tests/parcours',
  webServer: { command: 'npm run preview -- --port 4173', port: 4173, reuseExistingServer: false },
  use: { baseURL: 'http://localhost:4173', ...devices['Pixel 7'], locale: 'fr-FR' },
  reporter: [['list'], ['html', { open: 'never' }]]
});
```

### C.4 `tools/requirements.txt`

```
pyyaml==6.0.2
jsonschema==4.23.0
boto3==1.35.0
praat-parselmouth==0.4.5
numpy==2.1.3
Pillow==11.0.0
```

### C.5 `tools/voix_recuperer.py`

```python
#!/usr/bin/env python3
"""Synchronise les voix encodées depuis le stockage objet et prépare le socle de l'application."""
import argparse, os, pathlib, shutil, boto3

RACINE = pathlib.Path(__file__).resolve().parent.parent
ENCODES = RACINE / "voix" / "encodes"
SOCLE = ("c00", "c01", "c02")   # Prélude, Chapitres 1 et 2
CIBLE_SOCLE = RACINE / "app" / "static" / "voix"

def client():
    return boto3.client("s3", endpoint_url=os.environ["VOIX_S3_URL"],
                        aws_access_key_id=os.environ["VOIX_S3_CLE"],
                        aws_secret_access_key=os.environ["VOIX_S3_SECRET"])

def tout():
    s3, seau = client(), os.environ.get("VOIX_S3_SEAU", "vivre-anglais-voix")
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=seau, Prefix="encodes/"):
        for o in page.get("Contents", []):
            local = ENCODES / o["Key"].removeprefix("encodes/")
            if local.exists() and local.stat().st_size == o["Size"]:
                continue
            local.parent.mkdir(parents=True, exist_ok=True)
            s3.download_file(seau, o["Key"], str(local))

def socle():
    if CIBLE_SOCLE.exists():
        shutil.rmtree(CIBLE_SOCLE)
    for ch in SOCLE:
        src = ENCODES / ch
        if src.exists():
            shutil.copytree(src, CIBLE_SOCLE / ch)

if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--tout", action="store_true")
    a.add_argument("--socle", action="store_true")
    o = a.parse_args()
    if o.tout: tout()
    if o.socle: socle()
```

### C.6 `tools/generer_paquets.py`

```python
#!/usr/bin/env python3
"""Crée un module de paquet de voix Android par chapitre hors socle, et met à jour Gradle."""
import pathlib, re, shutil

RACINE = pathlib.Path(__file__).resolve().parent.parent
ENCODES = RACINE / "voix" / "encodes"
ANDROID = RACINE / "android"
SOCLE = {"c00", "c01", "c02"}

GABARIT = """plugins {{ id 'com.android.asset-pack' }}

assetPack {{
    packName = "voix_{ch}"
    dynamicDelivery {{ deliveryType = "on-demand" }}
}}
"""

def remplacer_bloc(fichier, debut, fin, contenu):
    texte = fichier.read_text(encoding="utf-8")
    motif = re.compile(re.escape(debut) + r".*?" + re.escape(fin), re.S)
    nouveau = f"{debut}\n{contenu}\n{fin}"
    texte = motif.sub(lambda _: nouveau, texte) if motif.search(texte) else texte + "\n" + nouveau + "\n"
    fichier.write_text(texte, encoding="utf-8")

def main():
    chapitres = sorted(p.name for p in ENCODES.glob("c[0-9][0-9]") if p.name not in SOCLE)
    for ch in chapitres:
        module = ANDROID / f"voix_{ch}"
        if module.exists():
            shutil.rmtree(module)
        (module / "src/main/assets/voix").mkdir(parents=True)
        shutil.copytree(ENCODES / ch, module / "src/main/assets/voix" / ch)
        (module / "build.gradle").write_text(GABARIT.format(ch=ch), encoding="utf-8")
    remplacer_bloc(ANDROID / "settings.gradle", "// <paquets-voix>", "// </paquets-voix>",
                   "\n".join(f"include ':voix_{ch}'" for ch in chapitres))
    remplacer_bloc(ANDROID / "app/build.gradle", "// <liste-paquets>", "// </liste-paquets>",
                   "android { assetPacks = [" + ", ".join(f'":voix_{ch}"' for ch in chapitres) + "] }")
    print(f"{len(chapitres)} paquets de voix générés")

if __name__ == "__main__":
    main()
```

Note : la liste `assetPacks` présentée en 10.9 est donc **produite** par ce script entre les marqueurs `// <liste-paquets>` et `// </liste-paquets>` (bloc `android { }` additionnel, que Gradle fusionne avec le principal) ; elle ne s'édite jamais à la main.

### C.7 `android/app/src/main/res/mipmap-anydpi-v26/ic_launcher.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@mipmap/ic_launcher_background" />
    <foreground android:drawable="@mipmap/ic_launcher_foreground" />
    <monochrome android:drawable="@drawable/ic_launcher_monochrome" />
</adaptive-icon>
```

### C.8 `.gitignore` (extrait)

```
node_modules/
app/build/
app/.svelte-kit/
app/static/voix/
app/static/corpus/
android/app/build/
android/voix_c*/
voix/masters/
voix/encodes/
secrets/
*.jks
*.pem
.venv/
```

### C.9 `corpus/itineraires.yaml` (extrait)

```yaml
# Chaque étape : 12 à 25 identifiants d'expressions existants (vérifiés par valider_corpus.py)
- id: premier-voyage
  titre: Premier voyage
  pourQui: >-
    Vous partez bientôt dans un pays anglophone : aéroport, hôtel,
    transports, restaurant et petits imprévus.
  etapes:
    - titre: À l'aéroport
      expressions: [c13.s01.A1, c13.s01.A3, c13.s01.B2, c13.s02.A1, c13.s02.C4, c20.s01.A2, c20.s01.B1, c13.s03.A1, c13.s03.A2, c13.s03.D1, c13.s04.A1, c13.s04.B3]
    - titre: L'arrivée à l'hôtel
      expressions: [c14.s01.A1, c14.s01.A2, c14.s01.B1, c14.s01.B4, c14.s02.A1, c14.s02.C2, c14.s02.C3, c14.s03.A1, c14.s03.B2, c20.s04.A1, c20.s04.A3, c14.s03.D1]
    # … quatre étapes encore : se déplacer, au restaurant, demander son chemin, quand tout déraille
- id: entretien-embauche
  titre: L'entretien d'embauche
  pourQui: Vous préparez un entretien en anglais.
  etapes:
    - titre: Se présenter
      expressions: [c02.s03.A1, c02.s03.A2, c02.s03.B1, c02.s03.B3, c08.s01.A1, c08.s01.A4, c08.s01.B2, c08.s02.A1, c08.s02.B1, c08.s02.C2, c08.s02.C3, c08.s03.A1]
    # …
```

Les identifiants ci-dessus illustrent la forme ; la liste définitive de chaque itinéraire est établie par l'éditeur pédagogique une fois les chapitres concernés franchis par la porte P2.

### C.10 `corpus/moments.yaml` (extrait)

```yaml
petit-matin: [c01.s01, c01.s02]
matinee:     [c01.s03, c08.s01, c08.s02]
midi:        [c10.s02, c10.s03]
apres-midi:  [c08.s04, c11.s01]
soiree:      [c01.s09, c10.s04, c16.s01]
nuit:        [c01.s10]
week-end:    [c16.s02, c17.s01, c18.s03]
```

---

## Annexe D — Glossaire technique

Ces termes techniques sont **réservés à la mise en œuvre** (code, rapports, registres). Ils n'apparaissent jamais dans l'ouvrage ; la charte du lexique (section 3) s'applique à tout ce que voit ou entend le lecteur.

| Terme interne | Définition | Ce que voit le lecteur |
|---|---|---|
| Corpus | Ensemble des fichiers YAML de contenu | — |
| Énoncé | Une phrase anglaise enregistrée (forme principale ou « autre façon de dire ») | L'expression |
| Déclinaison | Phrase du gabarit « Sur le même air » | Sur le même air |
| Réplique | Ligne de dialogue de la scène vivante | La scène vivante |
| Version (de voix) | Une des quatre combinaisons accent × rythme | Le pupitre des voix |
| Manifeste | Fichier JSON qui décrit les voix d'une scène | — |
| Socle | Voix présentes dès l'installation (Prélude, Chapitres 1–2) | — |
| Paquet de voix | Module Android ou archive contenant les voix d'un chapitre | « Les voix du chapitre 7 » |
| Saveur | Variante de compilation `play` ou `direct` | — |
| Porte (P1–P7) | Étape de validation qualité | — |
| Gel | Moment où une scène ou une édition ne change plus avant publication | — |
| Master | Fichier sonore source 48 kHz / 24 bits, archivé | — |
| Prise | Une réalisation sonore d'un énoncé (créée ou issue d'un enregistrement existant) | — |
| FSRS | Algorithme de mémorisation espacée | Les retrouvailles |
| Moteur des voix | Code de préparation et de lecture des voix | — |
| Contretemps | Toute situation d'échec visible | « Un contretemps » |
| Alignement | Instants de début et de fin de chaque mot dans un fichier sonore | Le surlignage synchronisé, l'écoute au mot |
| Segment | Portion d'un fichier sonore lue seule | L'écoute au mot |
| Courbe (F0) | Mélodie mesurée de la voix | La courbe |
| FR-F1 | Voix francophone qui dit les sens | La voix du sens |
| Fiche vocale | Description, moteur, version et réglages figés d'une voix | — |
| Graine | Valeur qui rend une création reproductible | — |
| Référence de timbre | 40 lignes qui définissent l'empreinte d'une voix | — |
| Enregistrement existant | Fichier de locuteur réel publié sous licence libre | — |
| Widget | Élément de l'écran d'accueil Android | L'expression du jour sur l'écran d'accueil |
| Lien profond | Adresse qui ouvre un écran précis de l'ouvrage | — |
| Gabarit | Modèle de phrase à compléter | Sur le même air |
| HVPT | Entraînement phonétique à haute variabilité (nombreuses voix) | Les paires à seize voix |
| Graphe de dialogue | Nœuds et branches d'une conversation préenregistrée | À vous de jouer |
| Détection d'activité vocale | Repérage local des instants de parole par l'énergie du signal | La fluidité mesurée |
| 4/3/2 | Répétition d'un récit en temps décroissant | La parole en relais |
| Voix réservées | Voix jamais utilisées à l'entraînement, gardées pour les épreuves | — |
| SBOM | Inventaire des composants logiciels (format CycloneDX) | — |
| Plan d'échantillonnage | Tirage aléatoire des fichiers écoutés par lot | — |
| Profil lexical | Couverture d'une scène par les listes de fréquence | — |

---

## Annexe E — Check-list de mise en production

À cocher intégralement, dans l'ordre, pour chaque édition. Une seule case vide bloque la publication.

### E.1 Contenu

- [ ] `python3 tools/construire.py --strict` sans erreur ni avertissement.
- [ ] Portes P1 à P6 consignées pour chaque scène publiée.
- [ ] `rapport-couverture.md` : 100 % de couverture vocale pour chaque scène publiée.
- [ ] Revue complète de tous les écrans et de tous les microtextes (lexique, ton, typographie).
- [ ] Le registre des prises permet de remonter de chaque fichier à son origine, sa voix et ses réglages.
- [ ] Page « Les voix » à jour : crédits de chaque auteur d'enregistrement existant, licences, mention d'origine (7.12).
- [ ] Conditions d'utilisation du moteur retenu archivées dans leur version du jour de production.
- [ ] Voix du sens présente et conforme au texte pour chaque expression et chaque réplique publiées.
- [ ] `itineraires.yaml` et `moments.yaml` valides ; chaque itinéraire publié a toutes ses voix.

### E.2 Application

- [ ] `npm run check`, `npm run test`, `npm run e2e` verts ; zéro violation d'accessibilité grave.
- [ ] Budgets 10.12 mesurés et consignés sur l'appareil de référence.
- [ ] Matrice d'appareils 11.3 parcourue ; parcours Maestro verts sur API 24, 30, 34, 36.
- [ ] Bord à bord, retour prédictif, rotation, tablette et pliable vérifiés sur Android 16.
- [ ] Promenade de 30 minutes écran éteint réussie sur l'appareil de référence et sur un appareil d'entrée de gamme à surcouche.
- [ ] Réinstallation : carnet retrouvé.
- [ ] Widget, quatre raccourcis et liens `https://vivrelanglais.com/e/…` vérifiés ; `assetlinks.json` en ligne avec les deux empreintes de certificat.
- [ ] Quatre thèmes vérifiés par `tools/contrastes.py` et à l'œil.
- [ ] Débogage de la WebView désactivé dans la version publiée ; aucune requête réseau hors liste 10.13.

### E.3 Compilation et signature

- [ ] `versionCode` supérieur à la version publiée ; `versionName` conforme à 10.19.
- [ ] `aapt2 dump badging` : `targetSdkVersion:'36'`, `sdkVersion:'24'`.
- [ ] `apksigner verify --print-certs` : certificat attendu pour l'APK direct.
- [ ] Bundle Play testé localement avec `bundletool --local-testing` (paquets de voix à la demande).
- [ ] Empreinte SHA-256 de l'APK direct calculée et prête à publier.

### E.4 Google Play

- [ ] Test fermé conduit (au moins 12 testeurs pendant 14 jours consécutifs pour un premier lancement en production).
- [ ] Fiche à jour (textes, captures téléphone et tablette, icône 512 × 512, bannière 1024 × 500).
- [ ] Sécurité des données : « Aucune donnée collectée ».
- [ ] Classification du contenu à jour (ton cru du Chapitre 22).
- [ ] `tools/profil_lexical.py` et `tools/verifier_jouer.py` sans erreur.
- [ ] Plan d'échantillonnage (20.3) consigné pour chaque lot publié ; aucun lot au-delà du seuil.
- [ ] Inventaire CycloneDX archivé, compilation reproductible vérifiée sur deux machines (20.4).
- [ ] Voix réservées des épreuves absentes de tout module d'entraînement (19.6).
- [ ] Niveau d'API cible conforme à l'exigence Google Play en vigueur (20.6).
- [ ] Notes de version rédigées dans la voix de l'éditeur (« Nouveau : le chapitre 7, Chez soi, avec ses voix. »).
- [ ] Déploiement progressif configuré (5 % → 20 % → 50 % → 100 %).

### E.5 Canal direct

- [ ] APK, empreinte SHA-256 et empreinte du certificat publiés sur la page de téléchargement.
- [ ] `catalogue.json` et `version.json` signés et mis en ligne ; signatures vérifiées par l'APK publié.
- [ ] Archives de voix accessibles en HTTPS, empreintes conformes au catalogue.

### E.6 Après publication

- [ ] Suivi quotidien pendant 7 jours : plantages (< 0,2 %), ANR (< 0,1 %), avis des lecteurs.
- [ ] Signalements de coquilles triés chaque semaine.
- [ ] Sauvegarde des masters, des clés et du corpus vérifiée (restauration test une fois par trimestre).

---

Fin du MEGA GOD PLAN. Ce document fait foi : toute décision qui s'en écarte est consignée par écrit, datée et motivée dans `docs/decisions/`, puis reportée ici.

---

## Annexe F — Sources citées

Chaque source citée dans l'ouvrage, dans l'ordre de sa première apparition, avec son adresse complète.

1. Mozilla Common Voice — <https://commonvoice.mozilla.org/en/datasets>
2. Lingua Libre — <https://en.wikipedia.org/wiki/Lingua_Libre>
3. ElevenLabs Voice Design — <https://elevenlabs.io/voice-design>
4. Google Cloud, Gemini-TTS — <https://docs.cloud.google.com/text-to-speech/docs/gemini-tts>
5. Comparatif des licences, Cartesia — <https://www.cartesia.ai/learn/open-source-tts>
6. Artificial Analysis — <https://artificialanalysis.ai/embed/text-to-speech-leaderboard/leaderboard/provider-voice>
7. VoiceMOS Challenge 2024 — <https://arxiv.org/html/2409.09305>
8. Commission européenne — <https://digital-strategy.ec.europa.eu/en/factpages/quick-facts-transparency-rules-ai-systems>
9. Politique de support Capacitor — <https://capacitorjs.com/docs/main/reference/support-policy>
10. Ce guide de migration — <https://dev.to/batmanofweb/capacitor-8-upgrade-for-lovable-apps-jg6>
11. Documentation Android de Capacitor — <https://capacitorjs.com/docs/android>
12. Aide Play Console — <https://support.google.com/googleplay/android-developer/answer/11926878?hl=en>
13. Dépôt — <https://github.com/Cap-go/capacitor-audio-recorder>
14. Android Developers — <https://developer.android.com/about/versions/16/behavior-changes-16>
15. Aide Play Console — <https://support.google.com/googleplay/android-developer/answer/9859372?hl=en>
16. Référence Capgo — <https://github.com/Cap-go/capgo-skills/blob/main/skills/capacitor-app-store/SKILL.md>
17. Nation, Four strands — <https://www.wgtn.ac.nz/lals/resources/paul-nations-resources/paul-nations-publications/publications/documents/1996-Four-strands.pdf>
18. Bjork & Bjork, 2011 — <https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2016/04/EBjork_RBjork_2011.pdf>
19. Roediger & Karpicke, rétrospective — <https://pubmed.ncbi.nlm.nih.gov/29592647/>
20. Cepeda et al., 2008 — <https://eric.ed.gov/?id=ED505660>
21. Rohrer & Taylor, effets de l'entrelacement — <https://onlinelibrary.wiley.com/doi/pdf/10.1002/acp.1598>
22. Psychonomic Bulletin & Review — <https://link.springer.com/article/10.3758/s13423-020-01762-3>
23. Studies in Second Language Acquisition — <https://www.cambridge.org/core/journals/studies-in-second-language-acquisition/article/decoding-the-noticing-function-of-output-the-roles-of-attention-and-awareness-during-l2-grammar-learning/56BF03840E1F69A197D9381700E709B8>
24. Lyster & Saito, 2010, résumé — <https://link.springer.com/content/pdf/10.1007/978-3-030-79143-8_63.pdf>
25. Pellicer-Sánchez et al., UCL — <https://discovery.ucl.ac.uk/id/eprint/10216385/3/Pellicer%20Sanchez_Lexical%20coverage%20and%20comprehension%20RFL%20copy%20for%20online%20repository.pdf>
26. Language Teaching, réplication de Nation 2006 — <https://www.cambridge.org/core/journals/language-teaching/article/how-much-vocabulary-is-needed-to-use-english-replication-of-van-zeeland-schmitt-2012-nation-2006-and-cobb-2007/1D217A56A2E0056E67802A6A8360FDDE>
27. Purdue, d'après Milton 2009 — <https://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=1056&context=plcc>
28. Oxford Learner's Word Lists — <https://www.oxfordlearnersdictionaries.com/about/wordlists/index.html>
29. English Profile — <https://englishprofile.org/>
30. ELIA, synthèse — <https://revistas.uned.es/index.php/ELIA/article/download/18098/15247>
31. Uchihara, Karas & Thomson, 2025 — <https://www.cambridge.org/core/journals/studies-in-second-language-acquisition/article/high-variability-phonetic-training-hvpt-a-metaanalysis-of-l2-perceptual-training-studies/6ABB8C1F32D88D53EA8D05A4565E76F6>
32. Whitworth & Rose, 2025 — <https://www.tandfonline.com/doi/full/10.1080/29984475.2025.2546827>
33. ELT Journal — <https://academic.oup.com/eltj/article/69/2/202/408492>
34. GEPF, Falar — <https://gepf.falar.org/entries/40/>
35. Saito, TUFS — <http://www.tufs.ac.jp/common/fs/ilr/contents/ronshuu/27/jilr27_Article_Saito.pdf>
36. Neuroscience & Biobehavioral Reviews, méta-analyse — <https://eprints.whiterose.ac.uk/id/eprint/113337/1/1-s2.0-S0149763416305784-main.pdf>
37. Frontiers, critique de l'hypothèse de l'input compréhensible — <https://pmc.ncbi.nlm.nih.gov/articles/PMC12577063/>
38. Estimations FSI — <https://emma-learn.com/learn/blog/how-long-to-learn-each-language/>
39. Charge fonctionnelle, Université du Texas — <https://repositories.lib.utexas.edu/server/api/core/bitstreams/07405136-cf4d-47ba-912b-c54fd7779f8b/content>
40. Lingua Franca Core — <https://en.wikipedia.org/wiki/Lingua_Franca_Core>
41. Frost, comparaison des accents anglais et français — <https://hal.science/hal-03542760v1/file/FROST_2010_EPIP.pdf>
42. Lidji et al., PMC — <https://pmc.ncbi.nlm.nih.gov/articles/PMC3219863/>
43. BBC Learning English — <https://www.bbc.co.uk/learningenglish/features/the_pronunciation_lounge/episode_1>
44. Britannica — <https://www.britannica.com/topic/schwa>
45. Weisser, formes fortes et faibles — <https://martinweisser.org/courses/phonetics/connect/weakForms.html>
46. Ipatics, prononciation pour francophones — <https://www.ipatics.com/blog/english-pronunciation-for-french-speakers>
47. Fonds de recherche du Québec — <https://frq.gouv.qc.ca/en/story-and-report/pronouncing-the-th-and-h-sounds-is-no-easy-task/>
48. BoldVoice — <https://boldvoice.com/sounds/flap-t>
49. T-glottalisation — <https://en.wikipedia.org/wiki/T-glottalization>
50. BBC Learning English — <https://www.bbc.co.uk/learningenglish/features/the_pronunciation_lounge/episode_10>
51. Kalbotyra, d'après le corpus LSWE — <https://www.journals.vu.lt/kalbotyra/article/download/23298/22534/43709>
52. Cambridge Dictionary — <https://dictionary.cambridge.org/grammar/british-grammar/discourse-markers->
53. Ward, signaux d'écoute — <https://www.cs.utep.edu/nigel/bc/>
54. Nivelo, d'après Gardner & Davies 2007 — <https://getnivelo.com/levels/most-common-phrasal-verbs>
55. Liu, 2011 — <https://eric.ed.gov/?id=EJ948637>
56. UC Davis, d'après Garnier & Schmitt 2015 — <https://globalaffairs.ucdavis.edu/iae/graduate/language-tips/phrasal-verbs>
57. The English Workshop — <https://the-english-workshop.com/blog/faux-amis-anglais-liste/>
58. BBC Learning English, 6 Minute English — <https://www.bbc.co.uk/learningenglish/tigrinya/features/6-minute-english_2026/ep-260115>
59. Yap, compilation des débits — <https://yapapp.cc/data/speaking-rate>
60. Cambridge English, Guided learning hours — <https://support.cambridgeenglish.org/hc/en-gb/articles/202838506-Guided-learning-hours>
61. Étude disponible sur ERIC — <https://files.eric.ed.gov/fulltext/EJ1171669.pdf>
