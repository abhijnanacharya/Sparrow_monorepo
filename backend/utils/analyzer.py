from __future__ import annotations
from typing import List, Tuple
from collections import Counter
from .cleaner import normalize_and_tokenize

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    _HAS_SK = True
except ImportError:
    _HAS_SK = False


def _score_by_frequency(text: str, top_k: int) -> List[Tuple[str, float]]:
    """Simplest frequency-based scoring (fallback)."""
    tokens = normalize_and_tokenize(text)
    if not tokens:
        return []
    counts = Counter(tokens)
    # Slight length bias — longer words weigh more
    scored = [(w, freq * (1.0 + min(len(w), 12) / 12.0)) for w, freq in counts.items()]
    scored.sort(key=lambda x: x[1], reverse=True)
    top = scored[:top_k]
    if not top:
        return []
    max_s = top[0][1]
    return [(w, round(s / max_s, 4)) for w, s in top]


def _score_by_tfidf(text: str, top_k: int) -> List[Tuple[str, float]]:
    """Use TF-IDF (single-document variant) to identify informative terms."""
    if not _HAS_SK:
        print("NO TF")
        return _score_by_frequency(text, top_k)

    vectorizer = TfidfVectorizer(
        analyzer="word",
        token_pattern=r"[a-zA-Z][a-zA-Z\-']{1,}",
        ngram_range=(1, 2),      # capture bigrams like “climate change”
        lowercase=True,
        stop_words="english",
    )
    X = vectorizer.fit_transform([text])
    weights = X.toarray()[0]
    vocab = vectorizer.get_feature_names_out()

    pairs = [(vocab[i], float(weights[i])) for i in range(len(vocab)) if weights[i] > 0]
    # Bias towards informative length
    pairs = [(w, s * (1 + min(len(w), 18) / 18.0)) for w, s in pairs]
    pairs.sort(key=lambda x: x[1], reverse=True)

    top = pairs[:top_k]
    if not top:
        return []
    max_s = top[0][1]
    return [(w, round(s / max_s, 4)) for w, s in top]


def extract_topics(text: str, method: str = "tfidf", top_k: int = 50) -> List[Tuple[str, float]]:
    """Main dispatcher for keyword extraction."""
    method = (method or "tfidf").lower()
    if method == "freq":
        return _score_by_frequency(text, top_k)
    return _score_by_tfidf(text, top_k)
