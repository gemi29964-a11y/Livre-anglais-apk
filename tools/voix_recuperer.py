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

REGISTRE = RACINE / "voix" / "registre" / "creations.jsonl"

def tout():
    if not os.environ.get("VOIX_S3_URL"):
        # Aucun stockage configuré : acceptable seulement tant que le registre ne déclare aucune voix créée.
        nb = sum(1 for l in REGISTRE.read_text(encoding="utf-8").splitlines() if l.strip()) if REGISTRE.exists() else 0
        if nb:
            raise SystemExit(f"voix_recuperer : {nb} voix au registre mais VOIX_S3_URL absent — récupération impossible")
        print("voix_recuperer : registre vide, aucune voix à récupérer")
        return
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
