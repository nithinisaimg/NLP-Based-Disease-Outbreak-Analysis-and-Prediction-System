"""
Sample NLP module code (college mini-project level).

Features:
- Preprocessing (tokenization, stopword removal)
- Extractive summarization (simple frequency-based)
- Keyword extraction
- Rule-based symptom classification
- Optional spaCy NER (if model installed)
"""

from __future__ import annotations

import re
from collections import Counter
from typing import Dict, List, Tuple


STOPWORDS = {
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


DISEASE_KEYWORDS: Dict[str, List[str]] = {
    "COVID-19": ["covid", "coronavirus", "loss of smell", "loss of taste", "breathlessness"],
    "Influenza / Flu": ["flu", "influenza", "sore throat", "cough", "body ache"],
    "Dengue": ["dengue", "joint pain", "rash", "platelet"],
    "Malaria": ["malaria", "chills", "rigors", "mosquito", "sweating"],
    "Cholera": ["cholera", "watery diarrhea", "dehydration"],
}


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def tokenize(text: str) -> List[str]:
    text = normalize(text.lower())
    return re.findall(r"[a-z]+(?:-[a-z]+)?", text)


def remove_stopwords(tokens: List[str]) -> List[str]:
    return [t for t in tokens if t not in STOPWORDS and len(t) >= 3]


def keywords(text: str, top_k: int = 10) -> List[str]:
    tokens = remove_stopwords(tokenize(text))
    if not tokens:
        return []
    return [w for w, _ in Counter(tokens).most_common(top_k)]


def summarize(text: str, max_sentences: int = 2) -> str:
    text = normalize(text)
    if not text:
        return ""
    sentences = re.split(r"(?<=[.!?])\s+", text)
    sentences = [s.strip() for s in sentences if s.strip()]
    if len(sentences) <= max_sentences:
        return text

    all_tokens = remove_stopwords(tokenize(text))
    freq = Counter(all_tokens)

    scored: List[Tuple[int, float]] = []
    for i, s in enumerate(sentences):
        s_tokens = remove_stopwords(tokenize(s))
        score = sum(freq.get(t, 0) for t in s_tokens) / max(1, len(s_tokens))
        scored.append((i, score))

    scored.sort(key=lambda x: x[1], reverse=True)
    keep = sorted(i for i, _ in scored[:max_sentences])
    return " ".join(sentences[i] for i in keep)


def classify_symptoms(symptom_text: str) -> str:
    t = symptom_text.lower()
    best_label, best_score = "General outbreak", 0
    for label, keys in DISEASE_KEYWORDS.items():
        score = sum(1 for k in keys if k in t)
        if score > best_score:
            best_label, best_score = label, score
    return best_label


def spacy_entities(text: str):
    try:
        import spacy

        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        return [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    except Exception:
        return []


if __name__ == "__main__":
    report = (
        "Public health teams reported a sudden rise in fever and cough cases in multiple districts. "
        "A few patients developed shortness of breath and required hospitalization. "
        "Officials advised mask use in crowded areas and recommended testing for suspected cases."
    )
    symptoms = "I have high fever, headache, body pain and joint pain for 3 days."

    print("SUMMARY:", summarize(report))
    print("KEYWORDS:", keywords(report))
    print("PREDICTED CATEGORY:", classify_symptoms(symptoms))
    print("ENTITIES:", spacy_entities(report))

