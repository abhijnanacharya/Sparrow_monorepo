from pydantic import BaseModel, Field, HttpUrl


class AnalyzeRequest(BaseModel):
  url: HttpUrl
  method: str = Field(default="tfidf", description="Keyword method: 'tfidf' or 'freq'")
  top_k: int = Field(default=50, ge=5, le=200)