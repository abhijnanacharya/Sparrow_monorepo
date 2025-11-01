from __future__ import annotations
import re
from typing import List

# Basic stopword set to avoid external downloads
STOPWORDS = set("""
a about above after again against all am an and any are aren't as at be because been
before being below between both but by can't cannot could couldn't did didn't do does
doesn't doing don't down during each few for from further had hadn't has hasn't have
haven't having he he'd he'll he's her here here's hers herself him himself his how
how's i i'd i'll i'm i've if in into is isn't it it's its itself let's me more most
mustn't my myself no nor not of off on once only or other ought our ours ourselves out
over own same shan't she she'd she'll she's should shouldn't so some such than that
that's the their theirs them themselves then there there's these they they'd they'll
they're they've this those through to too under until up very was wasn't we we'd we'll
we're we've were weren't what what's when when's where where's which while who who's
whom why why's with won't would wouldn't you you'd you'll you're you've your yours yourself
yourselves
""".split())

WORD_RE = re.compile(r"[a-zA-Z][a-zA-Z\-']{1,}")


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def tokenize(text: str) -> List[str]:
    return WORD_RE.findall(text)


def normalize_and_tokenize(text: str) -> List[str]:
    """Lowercase, strip punctuation, remove stopwords."""
    text = normalize(text)
    tokens = [t for t in tokenize(text) if t not in STOPWORDS]
    return tokens
