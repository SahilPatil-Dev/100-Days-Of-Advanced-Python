import os


class ConfigError(Exception):
    """Raised when required configuration is missing or invalid."""
    pass


class Settings:
    """
    Centralized, validated configuration.
    Loaded once at application startup.
    """

    def __init__(self) -> None:
        self.app_env: str = self._get_env("APP_ENV")
        self.db_host: str = self._get_env("DB_HOST")
        self.db_port: int = self._get_int_env("DB_PORT")

        self._validate_env()

    def _get_env(self, key: str) -> str:
        value = os.getenv(key)
        if not value:
            raise ConfigError(f"Missing required environment variable: {key}")
        return value

    def _get_int_env(self, key: str) -> int:
        value = self._get_env(key)
        try:
            return int(value)
        except ValueError:
            raise ConfigError(f"Environment variable {key} must be an integer")

    def _validate_env(self) -> None:
        if self.app_env not in ("dev", "prod"):
            raise ConfigError("APP_ENV must be either 'dev' or 'prod'")


# Single source of truth
settings = Settings()
