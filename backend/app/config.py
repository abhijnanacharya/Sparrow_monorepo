from __future__ import annotations
from functools import lru_cache
from pydantic import  AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
  APP_NAME: str = "Word Cloud Visualizer API"
  VERSION: str = "0.1.0"
  ENV: str = "dev"  # production
  LOG_LEVEL: str = "INFO"

  
  CORS_ORIGINS: str = "http://localhost:5173"

  @property
  def cors_origins_list(self) -> List[AnyHttpUrl] | List[str]:
      if self.CORS_ORIGINS.strip() == "*":
          return ["*"]
      return [o.strip() for o in self.CORS_ORIGINS.split(",") if o.strip()]

  class Config:
      env_file = ".env"
      case_sensitive = True


@lru_cache
def get_settings() -> Settings:
    return Settings()
