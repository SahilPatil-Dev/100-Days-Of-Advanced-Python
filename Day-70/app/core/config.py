from pydantic_settings import BaseSettings
from functools import lru_cache
import os


class Settings(BaseSettings):

    ENV: str = os.getenv("ENV", "dev")
    DATABASE_URL: str

    class Config:
        env_file = f".env.{os.getenv('ENV', 'dev')}"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
