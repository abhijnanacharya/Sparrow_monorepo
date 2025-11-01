from pydantic import BaseModel
from app.models.TopicItem import TopicItem


class AnalyzeResponse(BaseModel):
  topics: list[TopicItem]
  tokens: int
  method: str