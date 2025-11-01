from pydantic import BaseModel


class TopicItem(BaseModel):
  word: str
  weight: float