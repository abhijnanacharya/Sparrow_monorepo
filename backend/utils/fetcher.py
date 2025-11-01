from __future__ import annotations
import re
import requests
from bs4 import BeautifulSoup


USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0 Safari/537.36"
)


class FetchError(Exception):
    """Custom exception for failed article fetches."""
    pass


def fetch_article_text(url: str, timeout: int = 12) -> str:
    """
    Fetch an article and extract the visible paragraph text.
    - Removes scripts, navs, styles, etc.
    - Joins all <p> tags into a single string.
    """
    try:
        resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=timeout)
        resp.raise_for_status()
    except requests.RequestException as e:
        raise FetchError(f"Failed to fetch article: {e}")

    soup = BeautifulSoup(resp.text, "html.parser")

    # remove junky tags
    for tag in soup(["script", "style", "noscript", "header", "footer", "nav", "aside", "form"]):
        tag.decompose()

    paragraphs = [p.get_text(" ", strip=True) for p in soup.find_all("p")]
    text = " ".join(paragraphs)
    text = re.sub(r"\s+", " ", text).strip()

    if not text:
        raise FetchError("No text could be extracted from the given URL.")

    return text
