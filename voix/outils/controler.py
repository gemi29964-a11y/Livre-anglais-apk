#!/usr/bin/env python3
"""Contrôle des voix (Plan 7.10) — appliqué à 100 % des fichiers.

Entrée : un fichier JSONL, une ligne par fichier audio :
  {"id": "...", "f": "chemin.wav", "texte": "Five more minutes.", "accent": "uk"|"us"|"fr"|"au"|...,
   "rythme": "pose"|"spontane"|"sens", "voix": "UK-F1", "reference": "voix/fiches/UK-F1.reference.wav" (facultatif),
   "pair": "id de l'interprétation posée correspondante" (spontané seulement, facultatif),
   "fini": true|false   # fichier passé par la finition 7.9 (contrôle des silences et de la crête)}
Sortie : JSONL des mesures et verdicts, un objet par fichier, plus un résumé.

Équivalents retenus (journal D-037 à D-040) :
  - naturel prédit : UTMOS22 (strong learner, VoiceMOS 2022), car UTMOSv2 n'est pas installable ici ;
    le seuil reste relatif : 10e centile des enregistrements réels de calibrage (voix/calibrage/seuils.json) ;
  - transcription : Whisper large-v3-turbo (faster-whisper, int8) ;
  - accent : ECAPA CommonAccent (SpeechBrain) ; probabilité = softmax(échelle × cosinus), échelle calibrée ;
  - timbre : ECAPA-TDNN VoxCeleb (SpeechBrain) ;
  - mélodie : Praat via parselmouth, pas 10 ms, 75–500 Hz.
"""
from __future__ import annotations
import argparse, json, math, os, pathlib, re, sys, time, warnings
warnings.filterwarnings("ignore")
import numpy as np, librosa, soundfile as sf

RACINE = pathlib.Path(__file__).resolve().parents[2]
SEUILS = RACINE / "voix" / "calibrage" / "seuils.json"

# ---------------------------------------------------------------- normalisation du texte
NOMBRES = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven",
           "8": "eight", "9": "nine", "10": "ten", "11": "eleven", "12": "twelve", "15": "fifteen", "20": "twenty",
           "30": "thirty", "45": "forty-five"}
# Liste d'équivalences des réductions (7.10) : chaque forme est ramenée à une forme canonique.
EQUIV = [
    (r"\bgonna\b", "going to"), (r"\bwanna\b", "want to"), (r"\bgotta\b", "got to"), (r"\bhafta\b", "have to"),
    (r"\bkinda\b", "kind of"), (r"\bsorta\b", "sort of"), (r"\boutta\b", "out of"), (r"\blotta\b", "lot of"),
    (r"\bdunno\b", "do not know"), (r"\blemme\b", "let me"), (r"\bgimme\b", "give me"), (r"\bya\b", "you"),
    (r"\by'all\b", "you all"), (r"\bcos\b", "because"), (r"\b'cause\b", "because"), (r"\bcause\b", "because"),
    (r"\bc'mon\b", "come on"), (r"\bcmon\b", "come on"), (r"\bdidn't\b", "did not"), (r"\bdon't\b", "do not"),
    (r"\bdoesn't\b", "does not"), (r"\bcan't\b", "can not"), (r"\bcannot\b", "can not"), (r"\bwon't\b", "will not"),
    (r"\bisn't\b", "is not"), (r"\baren't\b", "are not"), (r"\bwasn't\b", "was not"), (r"\bweren't\b", "were not"),
    (r"\bhaven't\b", "have not"), (r"\bhasn't\b", "has not"), (r"\bshouldn't\b", "should not"),
    (r"\bwouldn't\b", "would not"), (r"\bcouldn't\b", "could not"), (r"\bmustn't\b", "must not"),
    (r"\bi'm\b", "i am"), (r"\byou're\b", "you are"), (r"\bwe're\b", "we are"), (r"\bthey're\b", "they are"),
    (r"\bi've\b", "i have"), (r"\byou've\b", "you have"), (r"\bwe've\b", "we have"), (r"\bthey've\b", "they have"),
    (r"\bi'll\b", "i will"), (r"\byou'll\b", "you will"), (r"\bwe'll\b", "we will"), (r"\bthey'll\b", "they will"),
    (r"\bit'll\b", "it will"), (r"\bthat'll\b", "that will"), (r"\blet's\b", "let us"),
    (r"\bit's\b", "it is"), (r"\bthat's\b", "that is"), (r"\bwhat's\b", "what is"), (r"\bthere's\b", "there is"),
    (r"\bhere's\b", "here is"), (r"\bhe's\b", "he is"), (r"\bshe's\b", "she is"), (r"\bwho's\b", "who is"),
    (r"\bwhere's\b", "where is"), (r"\bhow's\b", "how is"), (r"\binnit\b", "is not it"), (r"\bain't\b", "is not"),
    (r"\bokay\b", "ok"), (r"\bo\.k\.\b", "ok"), (r"\bmum\b", "mom"), (r"\bmummy\b", "mommy"),
    (r"\b(\w+)in'(?=\s|$)", r"\1ing"), (r"\byeah\b", "yes"), (r"\byep\b", "yes"), (r"\byup\b", "yes"),
    (r"\bmr\b", "mister"), (r"\bmrs\b", "missus"), (r"\bms\b", "miz"), (r"\bdr\b", "doctor"),
    (r"\b(\w+)'ve\b", r"\1 have"), (r"\b(\w+)'ll\b", r"\1 will"), (r"\b(\w+)'re\b", r"\1 are"),
    (r"\b(\w+)'d\b", r"\1 _d"),
    (r"\b'em\b", "them"), (r"\bt'\b", "to"), (r"\btryna\b", "trying to"), (r"\bwhatcha\b", "what are you"),
]
# Graphies britanniques et américaines ramenées à une seule forme (la différence d'orthographe n'est pas une différence de mot).
GRAPHIES = {"colour": "color", "favourite": "favorite", "realise": "realize", "realised": "realized", "organise": "organize",
            "apologise": "apologize", "centre": "center", "theatre": "theater", "travelling": "traveling", "cancelled": "canceled",
            "neighbour": "neighbor", "honour": "honor", "flavour": "flavor", "grey": "gray", "programme": "program",
            "pyjamas": "pajamas", "jewellery": "jewelry", "cheque": "check", "tyre": "tire", "defence": "defense",
            "licence": "license", "practise": "practice", "behaviour": "behavior", "labour": "labor", "humour": "humor",
            "alright": "all right", "whisky": "whiskey", "doughnut": "donut", "ageing": "aging", "storey": "story"}

def normaliser(t: str, langue: str = "en") -> list[str]:
    t = t.lower().replace("’", "'").replace("‘", "'").replace("—", " ").replace("–", " ").replace("…", " ")
    if langue == "fr":
        t = re.sub(r"[^\w\s'-]", " ", t)
        t = t.replace("'", "' ").replace("-", " ")
        return t.split()
    t = re.sub(r"(\d+):(\d+)", lambda m: f"{m.group(1)} {m.group(2)}", t)
    t = re.sub(r"\b\d+\b", lambda m: NOMBRES.get(m.group(0), m.group(0)), t)
    t = re.sub(r"[^\w\s'-]", " ", t)
    t = t.replace("-", " ")
    for a, b in EQUIV:
        t = re.sub(a, b, t)
    t = re.sub(r"\b(\w+)'s\b", r"\1 s", t)          # possessifs et « 's » contractés : même jeton des deux côtés
    t = t.replace("'", "")
    mots = [GRAPHIES.get(m, m) for m in t.split()]
    out = []
    for m in mots:
        out.extend(GRAPHIES.get(m, m).split())
    # interjections d'hésitation que Whisper ajoute ou retire sans changer le texte
    return [m for m in out if m not in {"uh", "um", "erm", "er", "hmm", "mm"}]

def egal(x: str, y: str) -> bool:
    """« 'd » contracté vaut would ou had (la transcription développe l'un ou l'autre)."""
    if x == y:
        return True
    return {x, y} in ({"_d", "would"}, {"_d", "had"})

def ecart_mots(a: list[str], b: list[str]) -> int:
    """Distance d'édition en mots."""
    d = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        p, d[0] = d[0], i
        for j, y in enumerate(b, 1):
            p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (not egal(x, y)))
    return d[-1]

# ---------------------------------------------------------------- mesures de signal
def crete_vraie(x: np.ndarray, sr: int) -> float:
    y = librosa.resample(x, orig_sr=sr, target_sr=sr * 4, res_type="soxr_hq")
    pk = float(np.max(np.abs(y))) + 1e-12
    return 20 * math.log10(pk)

def activite(x: np.ndarray, sr: int, seuil_db: float = -45.0):
    """Masque de parole par trames de 10 ms : énergie au-dessus de (crête de trame − 45 dB) et d'un plancher."""
    h = int(sr * 0.010); n = len(x) // h
    if n == 0:
        return np.zeros(0, bool), h
    e = np.array([np.sqrt(np.mean(x[i * h:(i + 1) * h] ** 2) + 1e-12) for i in range(n)])
    db = 20 * np.log10(e)
    ref = np.percentile(db, 95)
    return db > max(ref + seuil_db, -60.0), h

def silences(x, sr):
    m, h = activite(x, sr)
    if not m.any():
        return None, None, 0.0
    idx = np.flatnonzero(m)
    tete, fin = idx[0] * h / sr, (len(m) - 1 - idx[-1]) * h / sr
    # plus long silence interne
    interne, cur = 0, 0
    for v in m[idx[0]:idx[-1] + 1]:
        cur = 0 if v else cur + 1
        interne = max(interne, cur)
    return tete, fin, interne * h / sr

def clics(x, sr):
    """Discontinuités : dérivée seconde hors norme par rapport au voisinage (rapport > 12 à la médiane locale de 5 ms × 40)."""
    d = np.abs(np.diff(x, n=2))
    if len(d) < sr // 10:
        return 0, 0.0
    w = int(sr * 0.2)
    c = np.concatenate([[0.0], np.cumsum(d, dtype=np.float64)])
    i0 = np.clip(np.arange(len(d)) - w // 2, 0, len(d)); i1 = np.clip(np.arange(len(d)) + w // 2, 0, len(d))
    loc = (c[i1] - c[i0]) / np.maximum(i1 - i0, 1) + 1e-6
    r = d / loc
    pics = np.flatnonzero(r > 25)
    # regroupe les pics distants de moins de 5 ms
    n, last = 0, -10 ** 9
    for p in pics:
        if p - last > sr * 0.005:
            n += 1
        last = p
    return n, float(r.max())

def energie_hf(x, sr) -> float | None:
    """Part d'énergie au-dessus de 8 kHz dans les trames de parole (dB relatifs à l'énergie totale)."""
    if sr <= 16000:
        return None
    S = np.abs(librosa.stft(x, n_fft=1024, hop_length=256)) ** 2
    f = librosa.fft_frequencies(sr=sr, n_fft=1024)
    tot = S.sum(axis=0) + 1e-12
    act = tot > np.percentile(tot, 50)
    hf = S[f > 8000].sum(axis=0)
    return float(10 * np.log10(hf[act].sum() / tot[act].sum() + 1e-12))

def f0_ecart_demitons(x, sr) -> float | None:
    import parselmouth
    snd = parselmouth.Sound(x.astype(np.float64), sampling_frequency=sr)
    p = snd.to_pitch(time_step=0.01, pitch_floor=75, pitch_ceiling=500)
    f = p.selected_array["frequency"]; f = f[f > 0]
    if len(f) < 10:
        return None
    st = 12 * np.log2(f / np.median(f))
    return float(np.std(st))

# ---------------------------------------------------------------- modèles
class Modeles:
    def __init__(s, avec=("utmos", "whisper", "accent", "timbre")):
        import torch
        torch.set_num_threads(2)
        s.torch = torch
        s.avec = set(avec)
        if "utmos" in s.avec:
            s.utmos = torch.jit.load(os.path.expanduser("~/.cache/utmos/utmos_cpu.jit"), map_location="cpu").eval()
        if "whisper" in s.avec:
            from faster_whisper import WhisperModel
            s.whisper = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8", cpu_threads=2)
        if "accent" in s.avec:
            from speechbrain.inference.classifiers import EncoderClassifier
            s.acc = EncoderClassifier.from_hparams(source="Jzuluaga/accent-id-commonaccent_ecapa",
                                                  savedir=os.path.expanduser("~/.cache/sb/accent"))
            s.labels = [s.acc.hparams.label_encoder.ind2lab[i] for i in range(len(s.acc.hparams.label_encoder.ind2lab))]
        if "timbre" in s.avec:
            from speechbrain.inference.speaker import EncoderClassifier as Spk
            s.spk = Spk.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir=os.path.expanduser("~/.cache/sb/spk"))
        s._ref = {}

    def note_utmos(s, x16):
        t = s.torch.tensor((np.clip(x16, -1, 1) * 32767).astype(np.int16)).unsqueeze(0)
        with s.torch.no_grad():
            return float(s.utmos(t).reshape(-1)[0])

    def transcrire(s, x16, langue):
        segs, info = s.whisper.transcribe(x16, beam_size=5, language=langue, word_timestamps=True,
                                          condition_on_previous_text=False, vad_filter=False)
        segs = list(segs)
        mots = [(w.word.strip(), round(w.start, 3), round(w.end, 3), round(w.probability, 3)) for sg in segs for w in (sg.words or [])]
        return " ".join(sg.text.strip() for sg in segs).strip(), mots

    def cosinus_accent(s, x16):
        with s.torch.no_grad():
            out = s.acc.classify_batch(s.torch.tensor(x16).unsqueeze(0))
        return out[0][0].numpy()

    def empreinte(s, x16):
        with s.torch.no_grad():
            e = s.spk.encode_batch(s.torch.tensor(x16).unsqueeze(0)).reshape(-1).numpy()
        return e / (np.linalg.norm(e) + 1e-12)

    def empreinte_reference(s, chemin):
        if chemin not in s._ref:
            x = librosa.load(chemin, sr=16000, mono=True)[0]
            s._ref[chemin] = s.empreinte(x)
        return s._ref[chemin]

# ---------------------------------------------------------------- correspondance accents
ACCENT_LABEL = {"uk": "england", "us": "us", "au": "australia", "ie": "ireland", "za": "southatlandtic", "ng": "african",
                "gh": "african", "ca": "canada", "nz": "newzealand", "sc": "scotland", "in": "indian", "wa": "wales"}

def seuil_utmos(seuils: dict, d: float):
    """10e centile du réel pour la classe de durée du fichier (D-039) ; à défaut, 10e centile global."""
    for b in seuils.get("utmos_p10_par_duree", []):
        if b["min"] <= d < b["max"]:
            return b["p10"]
    return seuils.get("utmos_p10")

def charger_seuils():
    if SEUILS.exists():
        return json.loads(SEUILS.read_text(encoding="utf-8"))
    return {}

def mesurer(M: Modeles, e: dict, seuils: dict, avec_asr=True) -> dict:
    f = e["f"]
    x, sr = sf.read(f, dtype="float32", always_2d=True); x = x.mean(axis=1)
    x16 = librosa.resample(x, orig_sr=sr, target_sr=16000, res_type="soxr_hq") if sr != 16000 else x
    r = {"id": e.get("id"), "f": f, "voix": e.get("voix"), "rythme": e.get("rythme"), "sr": sr, "d": round(len(x) / sr, 3)}
    langue = "fr" if e.get("accent") == "fr" else "en"
    texte = e.get("texte", "")
    # mots écrits (une contraction ou un mot composé à trait d'union = un mot), pour le débit et les seuils « 4 mots »
    nb_mots = len(re.findall(r"[\w’']+(?:-[\w’']+)*", texte)) if texte else 0
    r["nb_mots"] = nb_mots
    bloq, signal = [], []
    if r["d"] < 0.25:
        # segment vide ou quasi vide (découpe sur un énoncé absent) : rien à mesurer, refus direct
        r["bloquants"] = ["énoncé absent ou trop court (moins de 0,25 s)"]; r["signalements"] = []; r["ok"] = False
        return r
    # naturel
    if "utmos" in M.avec:
        r["utmos"] = round(M.note_utmos(x16), 3)
        s10 = seuil_utmos(seuils, r["d"])
        if s10 is not None and r["utmos"] < s10:
            bloq.append(f"naturel {r['utmos']} < p10 {s10}")
    # texte
    if texte and (e.get("asr_lot") is not None or (avec_asr and "whisper" in M.avec)):
        if e.get("asr_lot") is not None:
            # transcription de la génération groupée par le même modèle, mots situés dans ce segment (D-041)
            hyp, mots = e["asr_lot"], e.get("mots_lot", [])
            r["asr_source"] = "lot"
        else:
            hyp, mots = M.transcrire(x16, langue)
            r["asr_source"] = "segment"
        r["transcription"] = hyp; r["mots_asr"] = mots
        a, b = normaliser(texte, langue), normaliser(hyp, langue)
        r["ecart_mots"] = ecart_mots(a, b)
        if r["ecart_mots"]:
            bloq.append(f"texte : attendu « {' '.join(a)} », entendu « {' '.join(b)} »")
        elif r["asr_source"] == "lot" and avec_asr and "whisper" in M.avec:
            # confirmation sur le fichier seul : un segment rogné par la découpe ne peut pas passer
            hyp2, _ = M.transcrire(x16, langue)
            r["transcription_fichier"] = hyp2
            b2 = normaliser(hyp2, langue)
            if ecart_mots(a, b2):
                bloq.append(f"texte (fichier seul) : attendu « {' '.join(a)} », entendu « {' '.join(b2)} »")
    # accent
    if "accent" in M.avec and langue == "en" and e.get("accent"):
        cos = M.cosinus_accent(x16)
        k = seuils.get("accent_echelle", 30.0)
        p = np.exp(k * (cos - cos.max())); p = p / p.sum()
        lab = ACCENT_LABEL.get(e["accent"], e["accent"])
        i = M.labels.index(lab) if lab in M.labels else None
        top = int(np.argmax(p))
        r["accent_top"] = M.labels[top]; r["accent_p"] = round(float(p[i]), 4) if i is not None else None
        r["accent_cos"] = round(float(cos[i]), 4) if i is not None else None
        if i is None or r["accent_p"] < 0.80:
            bloq.append(f"accent {lab} p={r['accent_p']} (détecté {M.labels[top]})")
    # timbre
    if "timbre" in M.avec:
        emb = M.empreinte(x16)
        r["_emb"] = emb
        if e.get("reference") and os.path.exists(e["reference"]):
            r["timbre"] = round(float(np.dot(emb, M.empreinte_reference(e["reference"]))), 4)
            if r["timbre"] < 0.75:
                bloq.append(f"timbre {r['timbre']} < 0,75")
    # mélodie
    st = f0_ecart_demitons(x, sr)
    r["f0_st"] = round(st, 3) if st is not None else None
    if nb_mots >= 4 and e.get("rythme") != "sens" and (st is None or st < 1.5):
        bloq.append(f"mélodie plate {r['f0_st']} demi-ton")
    # artefacts
    tete, fin, interne = silences(x, sr)
    r["tete"], r["fin"], r["silence_interne"] = (round(v, 3) if v is not None else None for v in (tete, fin, interne))
    if interne and interne > 0.70 and not e.get("pause_prevue"):
        bloq.append(f"silence interne {interne:.2f} s")
    # débit : mots écrits / durée de parole (du premier au dernier son, silences de tête et de fin exclus)
    if tete is not None and fin is not None:
        r["parole"] = round(max(1e-3, r["d"] - tete - fin), 3)
        if nb_mots:
            r["mpm"] = round(nb_mots / r["parole"] * 60, 1)
    # débit
    if r.get("mpm") and nb_mots >= 4 and e.get("rythme") in ("pose", "spontane"):
        lo, hi = (120, 140) if e["rythme"] == "pose" else (170, 220)
        tol = seuils.get("mpm_tolerance", 0)
        if not (lo - tol <= r["mpm"] <= hi + tol):
            bloq.append(f"débit {r['mpm']} mots/min hors {lo}–{hi}")
    r["clics"], r["clic_ratio"] = clics(x, sr)
    r["clic_ratio"] = round(r["clic_ratio"], 1)
    if seuils.get("clic_ratio_max") is not None and r["clic_ratio"] > seuils["clic_ratio_max"]:
        bloq.append(f"clic (discontinuité {r['clic_ratio']} > {seuils['clic_ratio_max']})")
    hf = energie_hf(x, sr)
    r["hf_db"] = round(hf, 2) if hf is not None else None
    if hf is not None and seuils.get("hf_db_max") is not None and hf > seuils["hf_db_max"]:
        bloq.append(f"souffle haute fréquence {hf:.1f} dB > {seuils['hf_db_max']}")
    # écrêtage et silences (fichiers finis)
    r["crete_dbtp"] = round(crete_vraie(x, sr), 2)
    if e.get("fini"):
        if r["crete_dbtp"] > -1.0:
            bloq.append(f"crête vraie {r['crete_dbtp']} dBTP")
        if tete is None or not (0.040 <= tete <= 0.120):
            bloq.append(f"tête {tete}")
        if fin is None or not (0.150 <= fin <= 0.300):
            bloq.append(f"fin {fin}")
    r["bloquants"] = bloq; r["signalements"] = signal
    r["ok"] = not bloq
    return r

def rapport_pairs(res: list[dict], entrees: dict) -> None:
    """Rapport de durée spontané / posé (énoncés de 4 mots ou plus) : borne 0,55–0,90, durée de parole."""
    par_id = {r["id"]: r for r in res}
    for r in res:
        e = entrees.get(r["id"], {})
        pid = e.get("pair")
        if r.get("rythme") == "spontane" and pid and pid in par_id and r["nb_mots"] >= 4:
            p = par_id[pid]
            dp = p.get("parole") or p["d"]
            ds = r.get("parole") or r["d"]
            r["rapport_duree"] = round(ds / max(dp, 1e-3), 3)
            if not (0.55 <= r["rapport_duree"] <= 0.90):
                r["bloquants"].append(f"rapport spontané/posé {r['rapport_duree']}")
                r["ok"] = False

def sonie_lot(fichiers: list[str]) -> float:
    import pyloudnorm as pyln
    xs, sr0 = [], None
    for f in fichiers:
        x, sr = sf.read(f, dtype="float32", always_2d=True)
        if sr0 is None: sr0 = sr
        if sr != sr0:
            x = librosa.resample(x.mean(axis=1), orig_sr=sr, target_sr=sr0)[:, None]
        xs.append(x.mean(axis=1))
    y = np.concatenate(xs)
    return float(pyln.Meter(sr0).integrated_loudness(y))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("entree"); ap.add_argument("sortie")
    ap.add_argument("--sans", default="", help="modèles à ne pas charger : utmos,whisper,accent,timbre")
    ap.add_argument("--lot", action="store_true", help="contrôler aussi la sonie du lot (fichiers finis)")
    a = ap.parse_args()
    avec = [m for m in ("utmos", "whisper", "accent", "timbre") if m not in a.sans.split(",")]
    entrees = [json.loads(l) for l in open(a.entree, encoding="utf-8") if l.strip()]
    base = os.path.dirname(os.path.abspath(a.entree))
    for e in entrees:  # chemins relatifs au fichier d'entrées
        if not os.path.isabs(e["f"]) and not os.path.exists(e["f"]):
            e["f"] = os.path.join(base, e["f"])
    deja = {}
    if os.path.exists(a.sortie):   # reprise sans doublon
        for l in open(a.sortie, encoding="utf-8"):
            if l.strip():
                o = json.loads(l); deja[o["id"]] = o
    M = Modeles(avec); seuils = charger_seuils()
    with open(a.sortie, "a", encoding="utf-8") as out:
        for i, e in enumerate(entrees):
            if e["id"] in deja:
                continue
            t = time.time()
            r = mesurer(M, e, seuils)
            r.pop("_emb", None)
            r["duree_mesure"] = round(time.time() - t, 1)
            out.write(json.dumps(r, ensure_ascii=False) + "\n"); out.flush()
            deja[r["id"]] = r
            print(f"[{i+1}/{len(entrees)}] {e['id']} ok={r['ok']} {'; '.join(r['bloquants'])}", flush=True)
    res = list(deja.values())
    rapport_pairs(res, {e["id"]: e for e in entrees})
    with open(a.sortie, "w", encoding="utf-8") as out:
        for r in res:
            out.write(json.dumps(r, ensure_ascii=False) + "\n")
    if a.lot:
        L = sonie_lot([e["f"] for e in entrees])
        print(f"sonie du lot : {L:.2f} LUFS ({'ok' if abs(L + 18) <= 1 else 'BLOQUANT'})")
    n = sum(r["ok"] for r in res)
    print(f"{n}/{len(res)} fichiers sans contrôle bloquant en échec")

if __name__ == "__main__":
    main()
