"""Application configuration module."""

from typing import List, Optional

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    # API settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "DataPulse"
    VERSION: str = "0.1.0"
    DESCRIPTION: str = "DataPulse Backend Service API"

    # CORS settings
    BACKEND_CORS_ORIGINS: List[str] = []

    @model_validator(mode="after")
    def validate_cors_origins(self) -> "Settings":
        """Validate CORS origins."""
        if self.BACKEND_CORS_ORIGINS and isinstance(self.BACKEND_CORS_ORIGINS, str):
            self.BACKEND_CORS_ORIGINS = [
                i.strip() for i in self.BACKEND_CORS_ORIGINS.split(",")
            ]
        return self

    # Database settings
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "datapulse"
    SQLALCHEMY_DATABASE_URI: Optional[str] = None
    ASYNC_SQLALCHEMY_DATABASE_URI: Optional[str] = None

    @model_validator(mode="after")
    def validate_db_connections(self) -> "Settings":
        """Validate database connections."""
        if not self.SQLALCHEMY_DATABASE_URI:
            self.SQLALCHEMY_DATABASE_URI = (
                f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
                f"@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
            )

        if not self.ASYNC_SQLALCHEMY_DATABASE_URI:
            self.ASYNC_SQLALCHEMY_DATABASE_URI = (
                f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
                f"@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
            )

        return self

    # Redis settings
    REDIS_SERVER: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_URI: Optional[str] = None

    @model_validator(mode="after")
    def validate_redis_connection(self) -> "Settings":
        """Validate Redis connection."""
        if not self.REDIS_URI:
            self.REDIS_URI = f"redis://{self.REDIS_SERVER}:{self.REDIS_PORT}/0"
        return self

    # Security settings
    SECRET_KEY: str = "development_secret_key"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days

    # Email settings
    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = None
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[str] = (
        "test@example.com"  # Default value for development
    )
    EMAILS_FROM_NAME: Optional[str] = None

    # Pydantic v2 settings config
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()
