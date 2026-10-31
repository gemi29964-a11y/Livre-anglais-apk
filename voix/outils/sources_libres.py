#!/usr/bin/env python3
"""Inventaire des enregistrements existants sous licence libre (Plan 7.3).

Pour chaque mot du corpus (ou d'une liste fournie), interroge Wikimedia Commons :
  - prononciations du Wiktionnaire « En-<région>-<mot>.ogg » (accent déclaré par le nom de fichier) ;
  - enregistrements Lingua Libre « LL-Q1860 (eng)-<locuteur>-<mot>.wav ».
Consigne pour chaque fichier : licence, auteur, accent déclaré, adresse source et page, puis le statut
d'admission par la règle 1 de 7.3 (CC0, domaine public, CC BY, CC BY-SA seulement).
Les règles 2 à 4 (texte exact, accent détecté, qualité 7.10) sont appliquées par `--controler`,
qui télécharge les fichiers admis et les mesure avec controler.py.

Reprenable : les réponses de l'API sont gardées en cache (voix/sources/cache/), un mot déjà
inventorié n'est pas réinterrogé.

Usage :
  python3 voix/outils/sources_libres.py inventaire --corpus corpus/c01/s01.yaml [--mots fichier.txt]
  python3 voix/outils/sources_libres.py controler [--limite N]
"""
import argparse, csv, hashlib, html, json, re, sys, time, urllib.parse, urllib.request
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
SORTIE = RACINE / "voix/sources"
CACHE = SORTIE / "cache"
API = "https://commons.wikimedia.org/w/api.php"
UA = {"User-Agent": "VivreAnglais/1.0 (inventaire 7.3; https://github.com/gemi29964-a11y/Livre-anglais-apk)"}
# préfixes de région du Wiktionnaire → accent de l'ouvrage (7.4)
REGIONS = {"us": "us", "uk": "uk", "au": "au", "ca": "ca", "nz": "nz", "ie": "ie", "za": "za",
           "in": "in", "ng": "ng", "gh": "gh", "sc": "uk-ecosse", "scotland": "uk-ecosse"}
ADMISES = re.compile(r"^(cc0|cc-zero|public domain|pd|cc by(-sa)? [0-9.]+( [a-z]+)?|cc by(-sa)?)$", re.I)
CHAMPS = ["fichier", "texte", "source", "accent_declare", "locuteur", "licence", "auteur", "url", "page",
          "statut", "raison", "sha256"]


def appel(params):
    params = {**params, "format": "json", "formatversion": "2"}
    cle = hashlib.sha1(json.dumps(params, sort_keys=True).encode()).hexdigest()
    f = CACHE / f"{cle}.json"
    if f.exists():
        return json.loads(f.read_text())
    url = API + "?" + urllib.parse.urlencode(params)
    for essai in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                d = json.loads(r.read())
            break
        except Exception:
            time.sleep(2 * (essai + 1))
    else:
        raise RuntimeError(f"API Commons injoignable : {url}")
    CACHE.mkdir(parents=True, exist_ok=True); f.write_text(json.dumps(d))
    time.sleep(0.2)
    return d


def mots_du_corpus(fichiers):
    import yaml
    mots = set()
    def textes(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "texte" and isinstance(v, dict):
                    yield from (t for t in v.values() if isinstance(t, str))
                else:
                    yield from textes(v)
        elif isinstance(o, list):
            for v in o:
                yield from textes(v)
    for f in fichiers:
        for t in textes(yaml.safe_load(open(f, encoding="utf-8"))):
            for m in re.findall(r"[A-Za-z][A-Za-z'’-]*", t):
                m = m.replace("’", "'").strip("'-")
                if len(m) > 1 or m in ("I", "a"):
                    mots.add(m.lower() if m != "I" else m)
    return sorted(mots)


def nettoyer(h):
    return html.unescape(re.sub(r"<[^>]+>", "", h or "")).strip()


def metadonnees(titres):
    out = {}
    for i in range(0, len(titres), 40):
        d = appel({"action": "query", "prop": "imageinfo|revisions", "iiprop": "url|extmetadata|sha1",
                   "rvprop": "content", "rvslots": "main", "titles": "|".join(titres[i:i + 40])})
        for p in d.get("query", {}).get("pages", []):
            if p.get("missing") or "imageinfo" not in p:
                continue
            ii = p["imageinfo"][0]; m = ii.get("extmetadata", {})
            wt = ""
            if p.get("revisions"):
                wt = p["revisions"][0]["slots"]["main"].get("content", "")
            out[p["title"]] = {"url": ii.get("url", "").split("?")[0], "page": ii.get("descriptionurl", ""),
                               "licence": nettoyer(m.get("LicenseShortName", {}).get("value")),
                               "auteur": nettoyer(m.get("Artist", {}).get("value")), "wikitexte": wt}
    return out


def inventaire(a):
    SORTIE.mkdir(parents=True, exist_ok=True)
    mots = mots_du_corpus(a.corpus) if a.corpus else []
    if a.mots:
        mots += [l.strip() for l in open(a.mots, encoding="utf-8") if l.strip()]
    mots = sorted(set(mots))
    inv = SORTIE / "inventaire.csv"
    deja = {}
    if inv.exists():
        for r in csv.DictReader(open(inv, encoding="utf-8")):
            deja[r["fichier"]] = r
    vus = {r["texte"].lower() for r in deja.values()}
    fait = json.loads((SORTIE / "mots_inventories.json").read_text()) if (SORTIE / "mots_inventories.json").exists() else []
    lignes = dict(deja)
    for k, mot in enumerate(mots):
        if mot in fait:
            continue
        # 1. Wiktionnaire : En-<région>-<mot>.ogg (casse du mot telle quelle et en minuscules)
        titres = []
        for reg in REGIONS:
            for forme in {mot, mot.lower(), mot.capitalize()}:
                titres.append(f"File:En-{reg}-{forme}.ogg")
        trouves = metadonnees(titres)
        for t, m in trouves.items():
            reg = re.match(r"File:En-([a-z]+)-", t).group(1)
            lignes[t] = ligne(t, mot, "wiktionnaire", REGIONS[reg], "", m)
        # 2. Lingua Libre : recherche plein texte puis filtre exact sur la transcription
        d = appel({"action": "query", "list": "search", "srnamespace": 6, "srlimit": 50,
                   "srsearch": f'"LL-Q1860 (eng)" intitle:"{mot}"'})
        ll = [r["title"] for r in d.get("query", {}).get("search", [])
              if re.fullmatch(r"File:LL-Q1860 \(eng\)-[^-]+-" + re.escape(mot) + r"\.(wav|ogg|flac)", r["title"], re.I)]
        for t, m in metadonnees(ll).items():
            loc = re.search(r"\|\s*locutor\s*=\s*([^\n|]*)", m["wikitexte"])
            lignes[t] = ligne(t, mot, "lingualibre", "", loc.group(1).strip() if loc else "", m)
        fait.append(mot)
        if k % 20 == 0:
            ecrire(inv, lignes); (SORTIE / "mots_inventories.json").write_text(json.dumps(fait))
            print(f"{k + 1}/{len(mots)} mots, {len(lignes)} fichiers", flush=True)
    ecrire(inv, lignes); (SORTIE / "mots_inventories.json").write_text(json.dumps(fait))
    s = {}
    for r in lignes.values():
        s[r["statut"]] = s.get(r["statut"], 0) + 1
    print(json.dumps({"mots": len(mots), "fichiers": len(lignes), "statuts": s}, ensure_ascii=False))


def ligne(titre, mot, source, accent, locuteur, m):
    lic = m["licence"]
    statut, raison = "admis_licence", ""
    if not lic:
        statut, raison = "exclu", "licence absente"
    elif not ADMISES.match(lic.strip()):
        statut, raison = "exclu", f"licence non admise ({lic})"
    elif not accent:
        statut, raison = "exclu_accent", "accent non déclaré (fiche locuteur Lingua Libre injoignable) : inutilisable là où l'accent compte (7.3 règle 3)"
    return {"fichier": titre, "texte": mot, "source": source, "accent_declare": accent, "locuteur": locuteur,
            "licence": lic, "auteur": m["auteur"], "url": m["url"], "page": m["page"],
            "statut": statut, "raison": raison, "sha256": ""}


def ecrire(inv, lignes):
    with open(inv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CHAMPS); w.writeheader()
        for k in sorted(lignes):
            w.writerow({c: lignes[k].get(c, "") for c in CHAMPS})


def controler(a):
    """Règles 2 à 4 : télécharge chaque fichier admis à la licence, mesure (controler.py) et met à jour le statut."""
    sys.path.insert(0, str(Path(__file__).parent))
    import controler as C, soundfile as sf, numpy as np, subprocess, tempfile
    inv = SORTIE / "inventaire.csv"
    L = list(csv.DictReader(open(inv, encoding="utf-8")))
    seuils = json.loads((RACINE / "voix/calibrage/seuils.json").read_text())
    M = C.Modeles()
    dl = Path.home() / "reel/libres"; dl.mkdir(parents=True, exist_ok=True)
    n = 0
    for r in L:
        if r["statut"] != "admis_licence" or r["accent_declare"] not in ("us", "uk"):
            continue
        if a.limite and n >= a.limite:
            break
        n += 1
        brut = dl / Path(urllib.parse.unquote(r["url"])).name
        if not brut.exists():
            with urllib.request.urlopen(urllib.request.Request(r["url"], headers=UA), timeout=60) as x:
                brut.write_bytes(x.read())
        r["sha256"] = hashlib.sha256(brut.read_bytes()).hexdigest()
        wav = brut.with_suffix(".24k.wav")
        if not wav.exists():
            subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(brut), "-ac", "1", "-ar", "24000", str(wav)], check=True)
        e = {"id": r["fichier"], "f": str(wav), "texte": r["texte"], "accent": r["accent_declare"], "rythme": "mot"}
        mes = C.mesurer(M, e, seuils, True)
        b = [x for x in mes.get("bloquants", []) if not x.startswith("débit")]  # un mot isolé n'a pas de débit (D-044)
        r["statut"] = "admis" if not b else "exclu_controle"
        r["raison"] = "; ".join(b)
        print(r["fichier"], r["statut"], r["raison"][:120], flush=True)
        if n % 10 == 0:
            ecrire(inv, {x["fichier"]: x for x in L})
    ecrire(inv, {x["fichier"]: x for x in L})


if __name__ == "__main__":
    p = argparse.ArgumentParser(); sp = p.add_subparsers(dest="cmd", required=True)
    q = sp.add_parser("inventaire"); q.add_argument("--corpus", nargs="*"); q.add_argument("--mots")
    q = sp.add_parser("controler"); q.add_argument("--limite", type=int, default=0)
    a = p.parse_args()
    {"inventaire": inventaire, "controler": controler}[a.cmd](a)
