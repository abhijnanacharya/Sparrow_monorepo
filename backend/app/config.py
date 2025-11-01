from __future__ import annotations
from functools import lru_cache
from typing import List, Union

from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    APP_NAME: str = "Word Cloud Visualizer API"
    VERSION: str = "0.1.0"
    ENV: str = "dev"          
    LOG_LEVEL: str = "INFO"

    CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
    ]
    ALLOW_CREDENTIALS: bool = False

    @field_validator("CORS_ORIGINS", mode="before")
    @classmethod
    def _coerce_origins(cls, v: Union[str, List[str]]) -> List[str]:
        """
        Allow:
          - CORS_ORIGINS="*"'
        """
        if isinstance(v, str):
            v = v.strip()
            if v == "*":
                return ["*"]
            return [o.strip() for o in v.split(",") if o.strip()]
        if isinstance(v, list):
            return [str(o).strip() for o in v if str(o).strip()]
        return []

    @property
    def allow_all_origins(self) -> bool:
        return "*" in self.CORS_ORIGINS

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache
def get_settings() -> Settings:
    return Settings()
