from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
import os

class Settings(BaseSettings):
    APP_NAME: str = "Backend System"
    ENV: str = os.getenv("ENV", "dev")

    DATABASE_URL: str
    SECRET_KEY: str

    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=f".env.{os.getenv('ENV', 'dev')}",
        extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()