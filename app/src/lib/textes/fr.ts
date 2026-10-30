// app/src/lib/textes/fr.ts — TOUS les textes de l'interface (Plan, 3.5 et 10.6).
// Aucune chaîne française n'est écrite ailleurs : le vérificateur de lexique (3.3) et le contrôle
// typographique (3.4) s'exécutent sur ce fichier à chaque compilation.

/** Nombres en toutes lettres (la voix de l'éditeur écrit « six minutes », 3.5). */
const UNITES = ['zéro', 'une', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept', 'huit', 'neuf', 'dix', 'onze', 'douze', 'treize', 'quatorze', 'quinze', 'seize'];
const DIZAINES = ['', '', 'vingt', 'trente', 'quarante', 'cinquante', 'soixante'];

export function enLettres(n: number): string {
  if (n < 0 || n > 69 || !Number.isInteger(n)) return String(n);
  if (n <= 16) return UNITES[n];
  if (n < 20) return `dix-${UNITES[n - 10]}`;
  const d = Math.floor(n / 10), u = n % 10;
  if (u === 0) return DIZAINES[d];
  if (u === 1) return `${DIZAINES[d]} et une`;
  return `${DIZAINES[d]}-${UNITES[u]}`;
}

/** « 12 jours », « 1 jour » : accord du nom. */
export function pluriel(n: number, un: string, plusieurs: string): string {
  return `${n} ${n > 1 ? plusieurs : un}`;
}

/** Heure à la française : « 7 h 30 », « 7 h 10 », « 18 h ». */
export function heure(h: number, m: number): string {
  return m === 0 ? `${h}\u00a0h` : `${h}\u00a0h\u00a0${String(m).padStart(2, '0')}`;
}

/** Durée d'écoute : « 9 h 40 », « 25 minutes ». */
export function duree(minutes: number): string {
  const h = Math.floor(minutes / 60), m = minutes % 60;
  if (h === 0) return pluriel(m, 'minute', 'minutes');
  return m === 0 ? `${h}\u00a0h` : `${h}\u00a0h\u00a0${String(m).padStart(2, '0')}`;
}

const MOIS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'];
const ROMAINS: [number, string][] = [[10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']];

export function romain(n: number): string {
  let s = '', r = n;
  for (const [v, l] of ROMAINS) while (r >= v) { s += l; r -= v; }
  return s;
}

export const t = {
  ouvrage: {
    titre: 'Vivre l’Anglais',
    sousTitre: 'La Maîtrise Pratique et Exhaustive de l’Anglais de A à Z par l’Usage Quotidien',
    edition: (e: string) => `Édition ${e}`
  },

  navigation: {
    principale: 'Carte de l’ouvrage',
    aujourdhui: 'Aujourd’hui',
    livre: 'Le Livre',
    promenade: 'La promenade',
    carnet: 'Mon carnet',
    recherche: 'Comment dit-on… ?',
    preferences: 'Préférences',
    retour: 'Revenir à la page précédente',
    fermer: 'Fermer'
  },

  aujourdhui: {
    salutation: (h: number) => (h >= 4 && h < 12 ? 'Bonjour' : h >= 12 && h < 18 ? 'Bon après-midi' : 'Bonsoir'),
    constance: (n: number) => `${pluriel(n, 'jour', 'jours')} de constance`,
    reprendre: 'Reprendre',
    reprise: (numero: string, titre: string) => `Reprendre là où vous étiez : Scène ${numero}, ${titre}.`,
    retrouvaillesTitre: 'Les retrouvailles',
    retrouvailles: (n: number, minutes: number) =>
      `${n} ${n > 1 ? 'expressions vous attendent' : 'expression vous attend'} aujourd’hui. Environ ${enLettres(minutes)} ${minutes > 1 ? 'minutes' : 'minute'}.`,
    aucuneRetrouvaille: 'Tout est à jour. Pourquoi ne pas découvrir une nouvelle scène ?',
    expressionDuJour: 'Expression du jour',
    rituelDuJour: 'Rituel du jour',
    momentPresentTitre: 'Le moment présent',
    momentPresent: (h: number, m: number, numero: string, titre: string) =>
      `Il est ${heure(h, m)}. C’est l’heure de la Scène ${numero} : ${titre}.`,
    itineraireEnCours: 'Itinéraire en cours',
    expressionsRestantes: (n: number) => `${pluriel(n, 'expression', 'expressions')} avant la fin de l’étape`,
    premierPas: 'Votre lecture commence par le Prélude : six scènes pour accorder l’oreille et la voix.',
    ouvrirPrelude: 'Ouvrir le Prélude',
    ouvrirChapitre1: 'Ouvrir le Chapitre 1'
  },

  accueil: {
    bienvenue: 'Bienvenue. Ce livre se lit avec les oreilles autant qu’avec les yeux.',
    choixAccent: 'Quelle voix souhaitez-vous entendre en premier ? Vous pourrez toujours écouter l’autre d’un geste.',
    niveau: 'Où en êtes-vous en anglais ?',
    niveaux: { fondations: 'Je commence', aisance: 'Je me débrouille', maitrise: 'Je suis à l’aise' },
    rendezVous: 'Un rendez-vous quotidien ?',
    rendezVousHeure: 'Choisir une heure',
    pasMaintenant: 'Pas maintenant',
    commencer: 'Commencer',
    continuer: 'Continuer',
    cestFait: 'C’est fait',
    passer: 'Passer l’accueil',
    ecran: (n: number) => `Accueil, page ${n} sur 4`,
    demonstration: 'Écouter la phrase en quatre voix'
  },

  voix: {
    americain: 'Américain',
    britannique: 'Britannique',
    am: 'Am.',
    brit: 'Brit.',
    pose: 'Posé',
    spontane: 'Spontané',
    accent: 'Accent',
    rythme: 'Rythme',
    quatre: 'Les quatre voix',
    ecouter: 'Écouter',
    ecouterAnnonce: (accent: string, rythme: string) => `Écouter, ${accent}, ${rythme}`,
    arreter: 'Arrêter la voix',
    enEcoute: 'En écoute',
    lectureContinue: 'Lire toute la scène',
    ecouterSceneDabord: 'Écouter la scène d’abord',
    voixDuSens: 'La voix du sens',
    aFaireVenir: 'Voix à faire venir',
    nonInstallees: (taille: number) =>
      `Les voix de ce chapitre ne sont pas encore sur votre téléphone. Les faire venir maintenant ? (${taille} Mo — une connexion Wi-Fi est conseillée.)`,
    arrivent: (pct: number) => `Les voix arrivent… ${pct} %`,
    faireVenir: 'Faire venir les voix',
    faireVenirChapitre: (n: number) => `Faire venir les voix du chapitre ${n}`,
    faireVenirTrois: 'Faire venir les voix des trois prochains chapitres',
    retirer: 'Retirer ces voix',
    verifier: 'Vérifier les voix installées',
    reparees: (n: number) => `Quelques voix du chapitre ${n} étaient abîmées. Elles ont été remises en état.`,
    ecouteDuMot: (mot: string) => `Écoute du mot ${mot}`,
    placeInsuffisante: 'La place manque sur ce téléphone. Retirer les voix des chapitres parcourus depuis le plus longtemps ?',
    confirmationMobile: (taille: number) => `Ces voix pèsent ${taille} Mo et vous êtes sur le réseau mobile. Les faire venir quand même ?`
  },

  messages: {
    horsConnexion: 'Vous êtes hors connexion. Tout ce qui est déjà sur votre téléphone reste à votre disposition.',
    contretempsLecture: 'Cette voix ne répond pas pour l’instant. Touchez pour réessayer.',
    contretemps: 'Un contretemps est survenu. Touchez pour réessayer.',
    volumeBas: 'Le son de votre téléphone est très bas.',
    volumeCoupe: 'Le son de votre téléphone est coupé.',
    microDemande: 'Pour entendre votre voix à côté de celle du livre, le livre a besoin du micro. Vos enregistrements restent sur ce téléphone.',
    microRefuse: 'Sans micro, le miroir reste fermé. Vous pouvez l’ouvrir à tout moment dans les Préférences.',
    expressionDuJourEcran: 'Ajoutez l’expression du jour sur votre écran d’accueil : un toucher, et la voix se fait entendre.',
    quitterRetour: 'Touchez retour une nouvelle fois pour refermer le livre.'
  },

  livre: {
    titre: 'Le Livre',
    prelude: 'Le Prélude',
    chapitre: (n: number) => `Chapitre ${n}`,
    chapitreRomain: (n: number) => `Chapitre ${romain(n)}`,
    scenes: (n: number) => pluriel(n, 'scène', 'scènes'),
    scene: (numero: string) => `Scène ${numero}`,
    etat: { decouvrir: 'à découvrir', enCours: 'en cours', parcourue: 'parcourue' },
    cheminParcouru: (n: number, total: number) => `${n} ${n > 1 ? 'scènes parcourues' : 'scène parcourue'} sur ${total}`,
    filtres: 'Choisir ce que montre le sommaire',
    filtreNiveau: 'Niveau',
    filtreAccent: 'Accent préféré',
    filtreTons: 'Tons',
    tous: 'Tous',
    itineraires: 'Les Itinéraires',
    appendices: 'Les Appendices',
    appendice: {
      cles: 'Les clés du phrasé',
      atlas: 'L’atlas des accents',
      lexique: 'Le lexique',
      fauxPas: 'Tous les faux pas',
      incontournables: 'Tous les incontournables',
      voix: 'Les voix'
    },
    dureeEcoute: (minutes: number) => `${duree(minutes)} d’écoute`
  },

  scene: {
    ouverture: 'L’Ouverture',
    moment: (lettre: string, titre: string) => `Moment ${lettre} — ${titre}`,
    rang: (lettre: string, i: number, n: number) => `Moment ${lettre} · ${i} sur ${n}`,
    essentiel: 'L’Essentiel',
    incontournables: 'Les dix incontournables',
    ecouterIncontournables: 'Écouter les dix d’affilée',
    fauxPas: 'Les faux pas',
    sceneVivante: 'La scène vivante',
    donnezLaReplique: 'Donnez la réplique',
    rituel: 'Le rituel',
    finScene: 'Scène parcourue. Ses expressions reviendront vous voir demain.',
    sceneSuivante: 'La scène suivante',
    autreFacon: 'Autre façon de dire',
    sens: 'Le sens',
    motAMot: 'Mot à mot',
    usage: 'L’usage',
    coulisses: 'En coulisses',
    surLeMemeAir: 'Sur le même air',
    declinaisons: (n: number) => pluriel(n, 'déclinaison', 'déclinaisons'),
    regardExpert: 'Regard expert',
    oreilleEntend: 'Ce que l’oreille entend',
    marquePage: 'Marque-page',
    marquer: 'Garder un marque-page',
    demarquer: 'Retirer le marque-page',
    renvoi: (lettre: string) => `→ Moment ${lettre}`,
    annonceCarte: (sens: string, ton: string) => `Sens : ${sens}. ${ton}.`,
    expressionAnnonce: 'Expression :'
  },

  etiquettes: {
    ton: { courant: 'Ton courant', complice: 'Ton complice', cru: 'Ton cru', soutenu: 'Ton soutenu' },
    niveau: { fondations: 'Fondations', aisance: 'Aisance', maitrise: 'Maîtrise' },
    region: {
      commun: 'Commun aux deux accents', us: 'Américain', uk: 'Britannique', au: 'Australien', ie: 'Irlandais',
      ng: 'Nigérian', gh: 'Ghanéen', za: 'Sud-africain'
    }
  },

  promenade: {
    titre: 'La promenade',
    intro: 'Écoutez les mains libres, écran éteint : dans les transports, en marchant, en cuisinant.',
    programmes: 'Les programmes',
    programme: {
      scene: { titre: 'Une scène', texte: 'Chaque expression en posé, son sens, puis en spontané, avec un temps pour répéter.' },
      itineraire: { titre: 'Un itinéraire', texte: 'Les expressions de l’étape en cours de votre itinéraire.' },
      marquePages: { titre: 'Mes marque-pages', texte: 'Les expressions et répliques gardées, dans l’ordre du carnet.' },
      incontournables: { titre: 'Les incontournables', texte: 'Les dix incontournables de chaque scène parcourue.' },
      retrouvailles: { titre: 'Retrouvailles à l’oreille', texte: 'Les expressions du jour, en écoute seule.' },
      deuxAnglais: { titre: 'Deux Anglais', texte: 'Chaque expression en américain puis en britannique, posé puis spontané.' },
      ombre: { titre: 'L’ombre', texte: 'La voix, puis un silence pour parler avec elle ou juste après elle.' }
    },
    minuteur: 'Minuteur de fin',
    finDeScene: 'Fin de la scène',
    minutes: (n: number) => `${n} min`,
    silences: 'Les silences',
    silence: { court: 'Courts', normal: 'Normaux', long: 'Longs' },
    lecture: 'Lecture',
    pause: 'Pause',
    suivant: 'Expression suivante',
    precedent: 'Expression précédente',
    reprendre: 'Reprendre la promenade',
    rienAEcouter: 'Aucune voix n’est encore installée pour ce programme. Ouvrez une scène du Prélude pour commencer.'
  },

  carnet: {
    titre: 'Mon carnet',
    marquePages: 'Marque-pages',
    maVoix: 'Ma voix',
    familieres: 'Expressions familières',
    constance: 'Constance',
    maVersion: 'Ma version',
    regardArriere: 'Le regard en arrière',
    mettreAlAbri: 'Mettre mon carnet à l’abri',
    restaurer: 'Restaurer mon carnet',
    partagerListe: 'Partager ma liste',
    notes: 'Mes notes',
    classerScene: 'Par scène',
    classerDate: 'Par date',
    videMarquePages: 'Votre carnet attend ses premiers marque-pages. Touchez le marque-page d’une expression pour la garder ici.',
    videMaVoix: 'Le miroir gardera ici les enregistrements que vous choisirez de conserver.',
    videFamilieres: 'Les expressions que vous aurez apprivoisées viendront s’inscrire ici, au fil des retrouvailles.',
    videMaVersion: 'Vos propres phrases, composées sur le même air, prendront place ici.',
    jourDeGrace: 'Un jour de grâce par semaine : la constance ne se perd pas pour un jour manqué.',
    regardArriereMois: (mois: number, n: number, minutes: number) =>
      `En ${MOIS[mois]}, ${n} ${n > 1 ? 'expressions vous sont devenues familières' : 'expression vous est devenue familière'}. Vous avez écouté ${duree(minutes)} de voix.`
  },

  recherche: {
    titre: 'Comment dit-on… ?',
    champ: 'Une expression, en français ou en anglais',
    effacer: 'Effacer la recherche',
    trouveDans: (numero: string, lettre: string) => `Trouvé dans Scène ${numero}, Moment ${lettre}`,
    trouveDansScene: (numero: string) => `Trouvé dans Scène ${numero}`,
    sansResultat: 'Rien de tel dans le livre pour l’instant. Essayez un mot plus simple, en français ou en anglais.',
    recentes: 'Vos recherches récentes',
    situations: 'Situations fréquentes',
    suggestions: [
      'S’excuser d’un retard',
      'Refuser poliment',
      'Demander son chemin',
      'Commander au restaurant',
      'Se présenter',
      'Remercier chaleureusement',
      'Dire que l’on n’a pas compris',
      'Prendre congé',
      'Féliciter quelqu’un',
      'Dire où l’on a mal'
    ],
    parcoursFonction: (f: string) => `Toutes les façons de ${f}`
  },

  preferences: {
    titre: 'Préférences',
    groupes: {
      voix: 'Les voix',
      lecture: 'La lecture',
      parcours: 'Le parcours',
      rendezVous: 'Les rendez-vous',
      miroir: 'Le miroir',
      carnet: 'Mon carnet',
      ecranAccueil: 'L’écran d’accueil',
      lireCeLivre: 'Lire ce livre',
      aPropos: 'À propos'
    },
    accentPrefere: 'Accent préféré',
    rythmeEntree: 'Rythme d’entrée',
    ordreQuatre: 'Ordre des quatre voix',
    ordrePrefereDabord: 'Accent préféré d’abord',
    ordreAlterne: 'En alternance',
    voixDuSens: 'La voix du sens',
    passagesEcho: 'Passages de l’écho',
    voixInstallees: 'Voix des chapitres installées',
    disponibleSansConnexion: 'Disponible sans connexion',
    tailleTexte: 'Taille du texte',
    interligne: 'Interligne',
    interlignes: { serre: 'Serré', normal: 'Normal', aere: 'Aéré' },
    theme: 'Thème',
    themes: { papier: 'Papier', ambre: 'Ambre', nuit: 'Nuit', contraste: 'Contraste', automatique: 'Automatique' },
    aideLecture: 'Police d’aide à la lecture',
    expertParDefaut: 'Afficher le regard expert',
    courbe: 'Afficher la courbe',
    tonCru: 'Afficher le ton cru',
    battement: 'Le battement',
    retourHaptique: 'Retour haptique léger',
    niveauDepart: 'Niveau de départ',
    nouvellesParJour: 'Nouvelles expressions par jour',
    retrouvaillesMax: 'Retrouvailles maximum par jour',
    memorisation: 'Mémorisation visée',
    formesEcartees: 'Formes de retrouvailles écartées',
    retrouvaillesSilencieuses: 'Retrouvailles silencieuses',
    momentPresent: 'Le moment présent',
    dureeQuotidienne: 'Combien de temps souhaitez-vous consacrer à l’anglais chaque jour ? Cinq minutes suffisent pour commencer.',
    heureRendezVous: 'Heure du rendez-vous',
    jours: 'Jours',
    joursSemaine: ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'],
    rendezVousActif: 'Rendez-vous quotidien',
    accesMicro: 'Accès au micro',
    effacerVoix: 'Effacer toutes mes voix',
    toutEffacer: 'Tout effacer',
    confirmerEffacer: 'Effacer définitivement votre carnet ? Cette action ne peut pas être reprise.',
    confirmerEncore: 'Vraiment tout effacer ? Touchez une seconde fois pour confirmer.',
    ecranAccueilAccent: 'Accent de l’expression du jour',
    ecranAccueilRythme: 'Rythme de l’expression du jour',
    ecranAccueilOrigine: 'Tirée de',
    origines: { parcourues: 'Les scènes parcourues', ouvrage: 'Tout l’ouvrage' },
    oui: 'Oui',
    non: 'Non',
    actif: 'Activé',
    inactif: 'Désactivé',
    pourcentage: (n: number) => `${n} %`,
    crans: (n: number, total: number) => `Cran ${n} sur ${total}`,
    apercuSens: 'Mon réveil sonne.',
    formes: {
      oreille: 'L’oreille',
      replique: 'La réplique',
      miroir: 'Le miroir',
      'deux-anglais': 'Deux Anglais',
      'ton-juste': 'Le ton juste',
      'faux-pas': 'Le faux pas',
      'meme-air': 'Sur le même air',
      'oreille-fine': 'L’oreille fine'
    },
    voixEffacees: 'Vos enregistrements ont été effacés.',
    carnetEfface: 'Votre carnet a été effacé.',
    apercu: 'Aperçu'
  },

  lireCeLivre: {
    titre: 'Lire ce livre',
    intro: 'Six pages courtes pour apprivoiser l’ouvrage. Chacune se lit en moins d’une minute.',
    pages: [
      { id: 'gestes', titre: 'Les gestes', texte: 'Touchez une expression pour l’entendre. Touchez-la de nouveau pendant la voix pour la reprendre depuis le début. Maintenez-la pour ouvrir le volet : l’écho, le miroir, le carnet.' },
      { id: 'pupitre', titre: 'Le pupitre', texte: 'En haut de chaque scène, le pupitre choisit l’accent, américain ou britannique, et le rythme, posé ou spontané. « Les quatre voix » les fait entendre à la suite.' },
      { id: 'phrase', titre: 'Le phrasé', texte: 'Sous chaque expression, le phrasé écrit la voix entendue avec des lettres familières. Les syllabes fortes sont en gras ; un arc relie les mots qui se collent.' },
      { id: 'promenade', titre: 'La promenade', texte: 'La promenade enchaîne les voix d’une scène, écran éteint. Les touches de votre casque la mettent en pause ou passent à l’expression suivante.' },
      { id: 'retrouvailles', titre: 'Les retrouvailles', texte: 'Chaque expression d’une scène parcourue revient vous voir au bon moment, ni trop tôt ni trop tard. Vous dites vous-même si elle vous était familière.' },
      { id: 'miroir', titre: 'Le miroir', texte: 'Le miroir enregistre votre voix et la place à côté de celle du livre. Vous comparez, vous seul décidez. Vos enregistrements restent sur ce téléphone.' }
    ],
    page: (i: number, n: number) => `Page ${i} sur ${n}`
  },

  aPropos: {
    titre: 'À propos',
    lesVoix: 'Les voix',
    mentions: 'Mentions légales',
    confidentialite: 'Politique de confidentialité',
    textesConfidentialite: [
      'Vivre l’Anglais ne recueille rien sur vous. Aucun identifiant, aucune mesure d’usage, aucune publicité.',
      'Votre carnet, vos marque-pages, vos notes et vos enregistrements restent dans le stockage privé de ce téléphone.',
      'Le micro ne sert qu’au miroir, à votre demande, et rien n’est jamais transmis.',
      'Les seules connexions servent à faire venir les voix des chapitres, depuis l’éditeur.'
    ],
    textesMentions: [
      'Vivre l’Anglais — La Maîtrise Pratique et Exhaustive de l’Anglais de A à Z par l’Usage Quotidien.',
      'Polices sous licence SIL Open Font License : Literata, Inter, Charis SIL, Atkinson Hyperlegible.'
    ]
  },

  phrase: {
    glotte: 'Coup de glotte',
    battu: 'T battu'
  },

  lettres: {
    attente: 'Un instant',
    vide: 'Rien ici pour l’instant.'
  }
} as const;

export type Textes = typeof t;
