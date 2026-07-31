from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Validated settings loaded from environment variables and an optional .env file."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        extra="ignore",
    )

    app_name: str = "AI-Commerce-OS"
    app_env: Literal["local", "development", "staging", "production", "test"] = "local"
    app_debug: bool = False
    app_log_level: str = "INFO"
    app_host: str = "0.0.0.0"
    app_port: int = Field(default=8000, ge=1, le=65535)
    app_cors_origins: list[str] = Field(default_factory=list)
    database_url: str = "postgresql+psycopg://ai_commerce_os:change-me@localhost:5432/ai_commerce_os"
    redis_url: str = "redis://localhost:6379/0"

    @property
    def is_production(self) -> bool:
        return self.app_env == "production"


@lru_cache
def get_settings() -> Settings:
    """Return the process-wide settings instance."""
    return Settings()
