#!/usr/bin/env python3
"""Écrit pilotage/statuts.csv (id;statut;preuve) pour la tranche 1.

Trois statuts, sans complaisance :
  * « fait (T1) » : l'exigence est satisfaite et la preuve citée existe dans pilotage/portes/ ;
  * « socle en place (T1) — preuve finale Tn » : le mécanisme existe et est testé, mais la preuve
    exigée par le Plan ne peut être apportée qu'avec le contenu, les voix ou la matrice d'appareils ;
  * « reporté (Tn) » : rien de livré encore ; la tranche qui le livre est indiquée.
Les exigences des tranches suivantes gardent le statut « à faire (Tn) » du générateur.
"""
import csv, pathlib, re

R = pathlib.Path(__file__).resolve().parent
P = "pilotage/portes/"
LEX = P + "lexique.txt"
TESTS = P + "tests-unitaires.txt, " + P + "tests-outils.txt"
E2E = P + "parcours-web.txt"
AND = P + "rapport-android.md"
CTR = P + "contrastes.md"
J = "pilotage/journal_des_decisions.md"

FAIT, SOCLE, REP = "fait (T1)", "socle en place (T1) — preuve finale {}", "reporté ({})"

def f(preuve): return (FAIT, preuve)
def s(t, preuve): return (SOCLE.format(t), preuve)
def r(t, raison): return (REP.format(t), raison)

regles = {}
def poser(ids, v):
    for i in ids.split(): regles[i] = v

# Fonctionnalités de la section 14 portées par la tranche 1
poser("F098", f(AND + " (ic_launcher_monochrome, mipmap-anydpi-v26)"))
poser("F099", s("T10", "android:enableOnBackInvokedCallback, liens/retour.ts + tests ; geste à confirmer sur la matrice 11.3"))
poser("F100", s("T10", "env(safe-area-inset-*) dans app.css ; contrôle sur appareils à encoche en T10"))
poser("F103 F104 F105 F106", f(CTR + " ; ui/apparence.test.ts"))
poser("F107 F108 F109 F110 F111", f("app/static/polices + design/typographie.css ; " + E2E))
poser("F112", s("T10", "jeton --cible 48px dans app.css ; mesure axe target-size sur chaque écran en T10"))
poser("F113", f("android/app/src/main/res/drawable/rac_*_trait.xml, ui/Icone.svelte"))
poser("F114 F121", f("jetons de mouvement 9.7 + prefers-reduced-motion dans app.css ; " + E2E))
poser("F115", f("ui/LigneEncre.svelte ; contrôle lexique « chargement » banni"))
poser("F116", r("T2", "les états vides des écrans dépendent du contenu du carnet et des scènes"))
poser("F117 F118 F119 F120 F122", s("T10", E2E + " (axe-core : 0 violation sur accueil, Aujourd'hui, Livre, Recherche, Préférences) ; TalkBack sur appareil en T10"))
poser("F124 F125 F126 F127 F128", f(TESTS + " ; " + LEX))
poser("F129", f(P + "build-web.txt"))
poser("F130 F133", s("T2", "voix/moteur.ts + moteur.test.ts ; latence mesurée avec les premières voix"))
poser("F131", f(P + "tests-unitaires.txt (voix/moteur.test.ts)"))
poser("F132", s("T9", "PromenadePlugin.kt et PromenadeService.kt compilés (" + AND + ")"))
poser("F134", r("T2", "les voix du socle sont produites en Phase 2"))
poser("F135", r("T3", "les paquets voix_c03… naissent avec les chapitres 3 et suivants"))
poser("F136", f("tools/generer_paquets.py + marqueurs settings.gradle et app/build.gradle"))
poser("F137", s("T10", "APK direct signé (" + AND + ") ; catalogue signé avec la clé ECDSA P-256 en T10"))
poser("F139 F140", r("T10", "vérification mensuelle et réparation : WorkManager branché à l'assemblage final"))
poser("F141", r("T2", "courbes, syllabes et segments précalculés à partir des voix"))
poser("F142", s("T2", "carnet/base.ts (Dexie 10.10), preferences/magasin.ts, tests ; copie de sûreté sauvegarde.json en T2"))
poser("F143", s("T10", "res/xml/sauvegarde.xml et extraction_donnees.xml ; restauration à prouver sur appareil"))
poser("F144 F145", f("aucune dépendance de mesure (package.json) ; CSP kit.csp ; res/xml/securite_reseau.xml"))
poser("F146", s("T10", P + "budgets-t1.md (tailles mesurées) ; démarrage et latences sur l'appareil de référence en T10"))
poser("F147 F148", f(AND))
poser("F149", s("T10", ".github/workflows/android.yml et contenu.yml ; équivalent exécuté : " + P + "ci.md, " + P + "ci-locale.txt ; exécution sur GitHub bloquée par le compte (D-031)"))
poser("F150", r("T10", "aucune publication (consigne) : paquet prêt à déposer et fiche rédigée en T10"))
poser("F151", s("T10", "versionCode 1000 + n° d'exécution (android.yml), Dexie versionné"))
poser("F153", s("T2", "outils des portes P1 et P5 en place ; rapports par scène dès la tranche étalon"))
poser("F154", f(TESTS + " ; " + E2E))
poser("F155", s("T2", "moteur.test.ts (une seule voix à la fois) ; interruption de « Les quatre voix » et écoute au mot avec les voix"))
poser("F156", r("T10", "matrice d'appareils : émulateurs API 24, 30, 34, 36 et appareils réels"))
poser("F157", r("T10", "critères d'acceptation vérifiés à l'assemblage final"))
poser("F158", r("T9", "signalement de coquille dans le volet de la carte d'expression"))
poser("F091", r("T2", "restauration automatique du carnet : copie de sûreté et sauvegarde Android"))
poser("F097", s("T10", "intent-filter autoVerify (AndroidManifest.xml) ; assetlinks.json exige le domaine de l'éditeur, non publié (consigne)"))

# Section 0
poser("R-0.1-001 R-0.1-002 R-0.1-003 R-0.1-004 R-0.1-005 R-0.1-006 R-0.1-007 R-0.1-008 R-0.1-009 R-0.1-010",
      s("T10", "pilotage/exigences.csv couvre chaque section du Plan"))
poser("R-0.2-001 R-0.2-002 R-0.2-003", f("pilotage/exigences.csv (colonne type) ; " + J))
poser("R-0.3-001 R-0.3-002", f(LEX))
poser("R-0.4-001 R-0.4-002 R-0.4-003 R-0.4-004", f(AND + " (aapt2 dump badging)"))
poser("R-0.4-005 R-0.4-006 R-0.4-007", r("T2", "Phase 2 : essai des voix 7.5 et seuils 7.10"))
poser("R-0.4-008", s("T2", "encodage Opus mono 48 kHz dans tools ; premiers fichiers en Phase 2"))
poser("R-0.4-009", f(AND + " (AAB play + APK direct signés)"))
poser("R-0.4-010", f("aucune dépendance de mesure ; securite_reseau.xml ; allowBackup limité au carnet"))
poser("R-0.4-011", f("aucun achat, aucune publicité dans l'application"))

# Section 3
for i in range(1, 60): regles[f"R-3.2-{i:03d}"] = f(LEX + " (table 3.2 appliquée à fr.ts)")
for i in range(1, 25): regles[f"R-3.5-{i:03d}"] = f(P + "tests-outils.txt (test_microtextes.py)")
poser("R-3.1-001 R-3.3-001 R-3.3-002", f(LEX))
for i in range(1, 9): regles[f"R-3.4-{i:03d}"] = f(LEX + " (typographie, exclamations, émojis, longueur)")

# Section 9
for i in range(1, 14): regles[f"R-9.2-{i:03d}"] = f(CTR)
for i in range(1, 12): regles[f"R-9.3-{i:03d}"] = f("design/typographie.css, app/static/polices, tools/polices.py")
poser("R-9.1-001 R-9.1-002 R-9.1-003 R-9.1-004", f("app.css, NavigationBasse.svelte ; " + E2E))
poser("R-9.4-001", f("jetons --e1…--e8 dans app.css"))
poser("R-9.4-002 R-9.4-003", s("T10", "jetons et safe-area ; vérification sur la matrice d'appareils"))
poser("R-9.5-004 R-9.5-005", f("ui/Phrase.svelte, ui/phrase.test.ts"))
poser("R-9.5-001 R-9.5-002 R-9.5-003 R-9.5-006 R-9.5-007 R-9.5-008 R-9.5-009 R-9.5-010",
      r("T2", "composants de la scène : carte, pupitre, volet, bloc bilingue, courbe, livrés avec la tranche étalon"))
poser("R-9.6-001", f("tools/icones.mjs, drawables rac_*_trait.xml, ui/Icone.svelte"))
poser("R-9.7-001 R-9.7-002 R-9.7-003 R-9.7-004", f("jetons de mouvement dans app.css"))
poser("R-9.7-005", s("T2", "@capacitor/haptics installé ; déclenché par le moteur des voix"))
poser("R-9.8-001", f(LEX + " ; ui/LigneEncre.svelte"))
poser("R-9.9-002 R-9.9-005", f(CTR + " ; ui/phrase.test.ts (lang=\"en\")"))
poser("R-9.9-001 R-9.9-003 R-9.9-004 R-9.9-006 R-9.9-007 R-9.9-008 R-9.9-009",
      s("T10", E2E + " (axe-core) ; TalkBack, texte à 200 %, clavier, contacteur sur appareil en T10"))

# Section 10
for i in range(1, 19): regles[f"R-10.2-{i:03d}"] = f(J + " (D-001, versions vérifiées le 30/10/2026)")
for i in range(1, 13): regles[f"R-10.4-{i:03d}"] = f(P + "tests-outils.txt (test_valider_corpus.py)")
poser("R-10.5-001 R-10.5-002 R-10.5-003 R-10.5-004 R-10.5-005 R-10.5-006", f(TESTS + " ; " + LEX + " ; " + P + "rapport-couverture.md"))
poser("R-10.5-007 R-10.5-008 R-10.5-009", r("T2", "scripts_voix.py et sorties itinéraires et expression du jour avec le premier contenu"))
poser("R-10.6-001 R-10.6-003 R-10.6-004 R-10.6-005 R-10.6-006", f(TESTS + " ; " + E2E))
poser("R-10.6-002", r("T2", "rendu des longues scènes par moment"))
poser("R-10.7-001 R-10.7-002 R-10.7-004", f(P + "tests-unitaires.txt (voix/moteur.test.ts, voix/source.test.ts)"))
poser("R-10.7-003", s("T9", "PromenadePlugin.kt compilé (" + AND + ")"))
poser("R-10.7-005 R-10.7-006", r("T2", "battement et préparation anticipée avec les premières voix"))
poser("R-10.8-001 R-10.8-002", s("T10", "app/capacitor.config.ts et styles.xml ; vérification sur tablette et pliable"))
poser("R-10.9-001 R-10.9-002 R-10.9-006 R-10.9-007 R-10.9-008 R-10.9-009", f(AND))
poser("R-10.9-003", r("T2", "voix du socle produites en Phase 2"))
poser("R-10.9-004 R-10.9-005", r("T3", "paquets voix_c03 et suivants"))
poser("R-10.10-001 R-10.10-002 R-10.10-004 R-10.10-005 R-10.10-006", f(P + "tests-unitaires.txt (carnet/base.test.ts, carnet/maVoix.test.ts, preferences)"))
poser("R-10.10-003", r("T2", "copie de sûreté carnet/sauvegarde.json"))
poser("R-10.10-007", r("T2", "expressions du widget écrites à partir du corpus"))
poser("R-10.10-008", r("T3", "voix installées par paquets"))
poser("R-10.11-001 R-10.11-002 R-10.11-003", f("tools/index_recherche.mjs ; " + E2E + " (recherche.spec.ts)"))
poser("R-10.11-004", s("T10", "mesure sur l'appareil de référence"))
for i in range(1, 11): regles[f"R-10.12-{i:03d}"] = s("T10", P + "budgets-t1.md ; mesures sur l'appareil de référence")
poser("R-10.13-001 R-10.13-002 R-10.13-003 R-10.13-007", f("package.json, securite_reseau.xml, kit.csp ; " + LEX))
poser("R-10.13-004", s("T10", "clé ECDSA P-256 générée, clé publique dans android/catalogue_cle_publique.txt"))
poser("R-10.13-005 R-10.13-006", r("T2", "micro et notifications demandés au premier usage du miroir et du rendez-vous"))
poser("R-10.14-001 R-10.14-002", f(AND))
poser("R-10.15-001 R-10.15-003", f(AND + " (apksigner verify) ; " + J))
poser("R-10.15-002", r("T10", "page de téléchargement de l'éditeur rédigée à l'assemblage final"))
poser("R-10.16-001", s("T10", ".github/workflows/contenu.yml ; équivalent exécuté : " + P + "ci.md, " + P + "ci-locale.txt ; exécution sur GitHub bloquée par le compte (D-031)"))
poser("R-10.17-002 R-10.17-003 R-10.17-005", f(AND + " (AAB, targetSdk 36, aucune bibliothèque native propre)"))
poser("R-10.17-001 R-10.17-004 R-10.17-006 R-10.17-007 R-10.17-008 R-10.17-009",
      r("T10", "aucune publication (consigne) : déclarations et fiche prêtes à déposer en T10"))
poser("R-10.18-001 R-10.18-002 R-10.18-003", r("T10", "distribution directe : page, catalogue signé, version.json"))
poser("R-10.19-001 R-10.19-002 R-10.19-005", f(".github/workflows/android.yml ; carnet/base.ts (versions Dexie)"))
poser("R-10.19-003 R-10.19-004", s("T2", "champ version du schéma de scène ; version des paquets avec les voix"))
poser("R-10.20-001 R-10.20-002 R-10.20-003 R-10.20-004 R-10.20-005 R-10.20-006 R-10.20-008",
      f(P + "tests-unitaires.txt (liens/liens.test.ts, liens.natif.test.ts) ; AndroidManifest.xml"))
poser("R-10.20-007", s("T10", "intent-filter autoVerify ; assetlinks.json sur le domaine de l'éditeur"))
poser("R-10.20-009", r("T2", "files/accueil/expressions.json écrit à partir du corpus"))
for i in range(1, 6): regles[f"R-10.21-{i:03d}"] = r("T10", "intégrité et réparation des voix")
for i in range(1, 6): regles[f"R-10.22-{i:03d}"] = r("T2", "précalcul à partir des voix")

# Section 11
for i in range(1, 9): regles[f"R-11.1-{i:03d}"] = s("T2", "pilotage/portes/ ; outils P1 et P5 ; rapports par scène dès la tranche étalon")
poser("R-11.2-001 R-11.2-003 R-11.2-004 R-11.2-005 R-11.2-006", f(TESTS + " ; " + E2E + " ; " + CTR + " ; " + LEX))
poser("R-11.2-002 R-11.2-008", s("T2", "tests du moteur et des composants livrés ; carte, pupitre et scène vivante avec la tranche étalon"))
poser("R-11.2-007", s("T10", "tests/maestro/*.yaml ; " + AND + " (émulateur API 30 : installation et ouverture ; rendu bloqué par l'émulation logicielle, D-034)"))
poser("R-11.2-009", r("T2", "200 paires de L'oreille fine"))
poser("R-11.2-010", r("T10", "Macrobenchmark et traces"))
for i in range(1, 8): regles[f"R-11.3-{i:03d}"] = r("T10", "matrice d'appareils")
for i in range(1, 17): regles[f"R-11.4-{i:03d}"] = r("T10", "critères d'acceptation de l'ouvrage complet")
poser("R-11.4-004", s("T10", LEX))
poser("R-11.4-010", s("T10", AND + " (apksigner verify sur l'APK direct)"))
poser("R-11.5-001 R-11.5-002", r("T9", "retour des lecteurs"))

# Annexes
poser("R-B-001 R-B-002 R-B-003", f("corpus/schema/scene.schema.json ; " + P + "tests-outils.txt"))
poser("R-B-004", r("T2", "le Prélude est rédigé en tranche 2"))
poser("R-C-001 R-C.1-001 R-C.6-001", f("fichiers de l'annexe C présents (FICH-*) ; " + J))
poser("R-C.9-001", r("T2", "corpus/itineraires.yaml versé avec les premières expressions"))

poser("FICH-002", r("T2", "scène étalon 1.1 rédigée en Phase 3"))
poser("FICH-024 FICH-025", r("T2", "leurs renvois doivent viser des expressions existantes (10.4) : versés avec le chapitre 1"))

# Fichiers imposés : présence vérifiée maintenant
racine = R.parent
with (R / "exigences.csv").open(encoding="utf-8") as fh:
    lignes = list(csv.DictReader(fh))
for l in lignes:
    if l["id"].startswith("FICH-"):
        m = re.search(r"Le fichier (\S+) existe", l["exigence"])
        if m and (racine / m.group(1)).exists():
            regles[l["id"]] = f("fichier présent : " + m.group(1))

connus = {l["id"] for l in lignes}
inconnus = sorted(set(regles) - connus)
if inconnus:
    raise SystemExit(f"identifiants inconnus : {inconnus}")
with (R / "statuts.csv").open("w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter=";")
    w.writerow(["# id", "statut", "preuve"])
    for i in sorted(regles):
        w.writerow([i, *regles[i]])
t1 = [l["id"] for l in lignes if l["statut"].startswith("à faire (T1)")]
oublies = [i for i in t1 if i not in regles]
print(f"statuts.csv : {len(regles)} statuts ; exigences T1 sans statut : {len(oublies)}")
for i in oublies: print("  ", i)
