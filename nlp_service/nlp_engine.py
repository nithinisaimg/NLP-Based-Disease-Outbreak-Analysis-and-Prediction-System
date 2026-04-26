from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple


DISEASE_KEYWORDS = {
    "COVID-19": ["covid", "coronavirus", "sars-cov-2", "loss of smell", "loss of taste"],
    "Influenza / Flu": ["flu", "influenza", "cough", "sore throat", "body ache"],
    "Dengue": ["dengue", "joint pain", "retro-orbital", "rash", "platelet"],
    "Malaria": ["malaria", "chills", "rigors", "mosquito", "sweating"],
    "Cholera": ["cholera", "watery diarrhea", "dehydration", "rice-water stool"],
    "Ebola / Viral Hemorrhagic Fever": ["ebola", "bleeding", "hemorrhagic", "body fluids"],
    "Measles": ["measles", "rash", "koplik", "conjunctivitis"],
}

TRANSMISSION_KEYWORDS = {
    "airborne/droplet": ["airborne", "droplet", "aerosol", "mask", "respiratory"],
    "water/food-borne": ["water", "food", "contaminated", "diarrhea", "sanitation"],
    "vector-borne": ["mosquito", "vector", "bite", "stagnant water"],
    "close-contact/bodily-fluid": ["close contact", "lesion", "bodily fluid", "blood", "vomit"],
}

COUNTRY_HINTS = [
    "India",
    "USA",
    "United States",
    "China",
    "Brazil",
    "Nigeria",
    "South Africa",
    "UK",
    "United Kingdom",
    "France",
    "Germany",
]


@dataclass
class SimpleEntity:
    text: str
    label: str


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def preprocess(text: str) -> List[str]:
    raw = _normalize(text.lower())
    tokens = re.findall(r"[a-z]+(?:-[a-z]+)?", raw)
    stop = {
        "a",
        "an",
        "the",
        "and",
        "or",
        "of",
        "in",
        "on",
        "to",
        "for",
        "with",
        "is",
        "are",
        "was",
        "were",
        "has",
        "have",
        "had",
        "this",
        "that",
        "as",
        "at",
        "by",
        "from",
        "it",
        "be",
        "been",
        "into",
        "their",
        "they",
        "we",
        "you",
        "i",
    }
    return [t for t in tokens if t not in stop and len(t) >= 3]


def extract_keywords(text: str, top_k: int = 10) -> List[str]:
    toks = preprocess(text)
    if not toks:
        return []
    counts = Counter(toks)
    return [w for w, _ in counts.most_common(top_k)]


def summarize(text: str, max_sentences: int = 2) -> str:
    text = _normalize(text)
    if not text:
        return ""
    sentences = re.split(r"(?<=[.!?])\s+", text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 0]
    if len(sentences) <= max_sentences:
        return text

    toks = preprocess(text)
    freq = Counter(toks)
    scored: List[Tuple[int, float]] = []
    for i, s in enumerate(sentences):
        s_tokens = preprocess(s)
        score = sum(freq.get(t, 0) for t in s_tokens) / max(len(s_tokens), 1)
        scored.append((i, score))
    scored.sort(key=lambda x: x[1], reverse=True)
    top_idx = sorted(i for i, _ in scored[:max_sentences])
    return " ".join(sentences[i] for i in top_idx)


def predict_category(symptom_text: str, report_text: str = "") -> str:
    combined = f"{symptom_text} {report_text}".lower()
    best = ("General outbreak", 0)
    for label, keys in DISEASE_KEYWORDS.items():
        score = 0
        for k in keys:
            if k in combined:
                score += 1
        if score > best[1]:
            best = (label, score)
    return best[0]


def extract_entities(text: str) -> List[SimpleEntity]:
    text = _normalize(text)
    if not text:
        return []

    entities: List[SimpleEntity] = []

    for disease, keys in DISEASE_KEYWORDS.items():
        for k in keys:
            if re.search(rf"\b{re.escape(k)}\b", text, flags=re.IGNORECASE):
                entities.append(SimpleEntity(text=disease, label="DISEASE"))
                break

    for tlabel, keys in TRANSMISSION_KEYWORDS.items():
        for k in keys:
            if re.search(rf"\b{re.escape(k)}\b", text, flags=re.IGNORECASE):
                entities.append(SimpleEntity(text=tlabel, label="TRANSMISSION"))
                break

    for c in COUNTRY_HINTS:
        if re.search(rf"\b{re.escape(c)}\b", text, flags=re.IGNORECASE):
            entities.append(SimpleEntity(text=c, label="COUNTRY"))

    symptom_terms = [
        "fever",
        "cough",
        "headache",
        "rash",
        "diarrhea",
        "vomiting",
        "breathlessness",
        "shortness of breath",
        "fatigue",
        "joint pain",
        "body pain",
        "chills",
    ]
    for s in symptom_terms:
        if re.search(rf"\b{re.escape(s)}\b", text, flags=re.IGNORECASE):
            entities.append(SimpleEntity(text=s, label="SYMPTOM"))

    severity_terms = [
        "mild",
        "moderate",
        "severe",
        "critical",
        "hospitalized",
        "icu",
        "death",
        "fatal",
    ]
    for s in severity_terms:
        if re.search(rf"\b{re.escape(s)}\b", text, flags=re.IGNORECASE):
            entities.append(SimpleEntity(text=s, label="SEVERITY"))

    dedup: Dict[Tuple[str, str], SimpleEntity] = {}
    for e in entities:
        dedup[(e.text.lower(), e.label)] = e
    return list(dedup.values())


def _try_spacy_entities(text: str) -> Tuple[Optional[List[SimpleEntity]], Dict[str, Any]]:
    try:
        import spacy
    except Exception as e:  # noqa: BLE001
        return None, {"spacy": f"not_available: {e.__class__.__name__}"}

    try:
        try:
            nlp = spacy.load("en_core_web_sm")
        except Exception:
            nlp = spacy.blank("en")
        doc = nlp(text)
        ents = [SimpleEntity(text=ent.text, label=ent.label_) for ent in doc.ents]
        return ents, {"spacy": "ok"}
    except Exception as e:  # noqa: BLE001
        return None, {"spacy": f"failed: {e.__class__.__name__}"}


def _try_transformer_summary(text: str) -> Tuple[Optional[str], Dict[str, Any]]:
    try:
        from transformers import pipeline
    except Exception as e:  # noqa: BLE001
        return None, {"transformers": f"not_available: {e.__class__.__name__}"}

    try:
        summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
        out = summarizer(text, max_length=80, min_length=25, do_sample=False)
        return str(out[0]["summary_text"]).strip(), {"transformers": "ok"}
    except Exception as e:  # noqa: BLE001
        return None, {"transformers": f"failed: {e.__class__.__name__}"}


def analyze_text(report_text: str, symptom_text: str) -> Dict[str, Any]:
    combined = _normalize(f"{report_text} {symptom_text}")

    debug: Dict[str, Any] = {}

    transformer_summary, dbg_sum = _try_transformer_summary(report_text) if report_text else (None, {})
    debug.update(dbg_sum)
    summary = transformer_summary if transformer_summary else summarize(report_text or symptom_text, max_sentences=2)

    spacy_ents, dbg_spacy = _try_spacy_entities(combined)
    debug.update(dbg_spacy)
    ents = spacy_ents if spacy_ents else extract_entities(combined)

    keywords = extract_keywords(combined, top_k=10)
    predicted = predict_category(symptom_text=symptom_text, report_text=report_text)

    return {
        "summary": summary,
        "predicted_category": predicted,
        "entities": [{"text": e.text, "label": e.label} for e in ents],
        "keywords": keywords,
        "debug": debug,
    }

