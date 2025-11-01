from __future__ import annotations
import logging
from fastapi import HTTPException
from fastapi import FastAPI

from contextlib import asynccontextmanager
from app.models.AnalyzeRequest import AnalyzeRequest
from app.models.AnalyzeResponse import AnalyzeResponse
from utils.analyzer import extract_topics
from utils.fetcher import FetchError, fetch_article_text

from app.config import get_settings
from app.logging_config import configure_logging

settings = get_settings()
configure_logging(settings.LOG_LEVEL)
logger = logging.getLogger("app")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    docs_url="/docs" if settings.ENV != "production" else None,
)



# Health-check
@app.get("/")
def health():
  return {
    "code": 200,
    "status": "ok",
    "service": "Word Cloud Visualizer API : HEALTH ENDPOINT",
    "version": settings.VERSION,
  }


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(req: AnalyzeRequest):
  try:
      text = fetch_article_text(str(req.url))
  except FetchError as e:
      raise HTTPException(status_code=502, detail="page disallowed scraping :(")

  topics = extract_topics(text, method=req.method, top_k=req.top_k)
  if not topics:
      raise HTTPException(status_code=422, detail="No topics could be extracted from the article OR page disallowed scraping :(")

  return {
      "topics": [{"word": w, "weight": float(s)} for w, s in topics],
      "tokens": len(text.split()),
      "method": req.method,
  }