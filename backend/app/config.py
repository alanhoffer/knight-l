"""Application configuration from environment variables."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from .env."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # App
    app_name: str = "IronClash Backend"
    app_version: str = "1.0.0"
    debug: bool = False
    environment: str = "development"

    # Database (SQLite local por defecto; PostgreSQL para producción)
    database_url: str = "sqlite:///./ironclash.db"

    # Redis
    redis_url: str = "redis://localhost:6379/0"

    # Security
    secret_key: str = "change-me-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # CORS
    cors_origins: str = "http://localhost:3000,http://localhost:8080"

    # Game
    max_lives: int = 5
    life_regeneration_minutes: int = 25
    max_chest_slots: int = 5

    @property
    def cors_origins_list(self) -> list[str]:
        """Return CORS origins as list."""
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]


settings = Settings()
