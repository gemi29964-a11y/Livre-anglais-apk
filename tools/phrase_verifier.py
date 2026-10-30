"""Vérificateur du phrasé (sections 6.2 à 6.4 et 6.7, étape 4).

Contrôle, pour chaque énoncé, déclinaison et paire d'écoute du corpus :
- les symboles du phrasé appartiennent à la liste fermée (6.2 à 6.4) ;
- chaque phrasé porte au moins une syllabe accentuée (CAPITALES) ;
- la notation experte est une transcription phonémique entre barres obliques, en symboles API admis ;
- les graphies proscrites du 6.3 sont refusées (D pour /ð/, DOWN, SOW, NID, « ou- » pour /w/, gu, ss) ;
- les quatre phrasés d'un énoncé ne sont pas une seule transcription recopiée.
Code de sortie 1 en cas de manquement.
"""
from __future__ import annotations

import re
import sys

import yaml

from commun import CORPUS, RACINE

LETTRES = "abcdefghijklmnopqrstuvwxyzàâäèéêëîïôöûüùç"
SIGNES = "əƏ·‿()ɾʔʳ↗↘ ’-"
ADMIS_PHRASE = set(LETTRES + LETTRES.upper() + SIGNES)
ADMIS_EXPERT = set("/ abdefhijklmnprstuvwzæɑɒɔəɚɛɜɝɪʊʌθðʃʒŋɡɾʔˈˌːˑ.‿()ɹ̩ʧʤoɫxʍɐɵɨʉ")
PROSCRITS = [
    (re.compile(r"\bDOWN"), "« DOWN » pour don’t : écrire DƏOUN (Brit.) ou DÔOUN (Am.)"),
    (re.compile(r"\bSOW\b"), "« SOW » pour so : écrire SƏOU (Brit.) ou SÔOU (Am.)"),
    (re.compile(r"\bNID\b"), "« NID » pour need : écrire NIID"),
    (re.compile(r"gu", re.I), "« gu » : écrire g"),
    (re.compile(r"ss", re.I), "« ss » : écrire s"),
    (re.compile(r"(?:^|[\s·‿])ou-", re.I), "« ou- » pour /w/ : écrire w"),
]


def verifier_phrase(ou: str, p: dict) -> list[str]:
    fautes = []
    ph, ex = p.get("phrase", ""), p.get("expert", "")
    hors = sorted({c for c in ph if c not in ADMIS_PHRASE})
    if hors:
        fautes.append(f"{ou} : symbole hors liste dans le phrasé « {''.join(hors)} »")
    if not re.search(r"[A-ZÀ-ÖØ-ÞƏ]{1,}", ph.replace("(t)", "")):
        fautes.append(f"{ou} : aucune syllabe accentuée (CAPITALES) dans « {ph} »")
    if not (ex.startswith("/") and ex.endswith("/")):
        fautes.append(f"{ou} : notation experte hors barres obliques")
    hors = sorted({c for c in ex if c not in ADMIS_EXPERT})
    if hors:
        fautes.append(f"{ou} : symbole hors liste dans la notation experte « {''.join(hors)} »")
    for motif, raison in PROSCRITS:
        if motif.search(ph):
            fautes.append(f"{ou} : graphie proscrite — {raison}")
    # /ð/ doit être rendu par dh, jamais par d (6.2 et 6.3).
    if ex.count("ð") > len(re.findall(r"dh", ph, re.I)):
        fautes.append(f"{ou} : /ð/ rendu sans « dh » (6.3)")
    if "w" in ex and "w" not in ph.lower():
        fautes.append(f"{ou} : /w/ non rendu par « w » (6.2)")
    return fautes


def verifier_ensemble(ou: str, phrases: dict | None) -> list[str]:
    if not phrases:
        return []
    fautes = []
    vus = []
    for a in ("uk", "us"):
        for rt in ("pose", "spontane"):
            p = (phrases.get(a) or {}).get(rt)
            if p:
                fautes += verifier_phrase(f"{ou} [{a}/{rt}]", p)
                vus.append(p.get("phrase"))
    if len(vus) == 4 and len(set(vus)) == 1 and len(vus[0].split()) > 1:
        fautes.append(f"{ou} : une seule transcription pour deux accents et deux rythmes (6.3)")
    return fautes


def elements(s: dict):
    for m in s.get("moments", []):
        for x in m.get("expressions", []):
            for e in x.get("enonces", []):
                yield e.get("id"), e.get("phrases")
            for d in x.get("declinaisons", []):
                yield d.get("id"), d.get("phrases")


def main() -> int:
    fautes, n = [], 0
    for f in sorted(CORPUS.glob("c[0-9][0-9]/s[0-9][0-9].yaml")):
        s = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
        for ident, phrases in elements(s):
            n += 1
            fautes += verifier_ensemble(ident or str(f.relative_to(RACINE)), phrases)
    if fautes:
        print(f"phrasé : ÉCHEC — {len(fautes)} manquement(s) sur {n} éléments")
        for x in fautes[:300]:
            print("  ✗", x)
        return 1
    print(f"phrasé : conforme — {n} éléments examinés")
    return 0


if __name__ == "__main__":
    sys.exit(main())
