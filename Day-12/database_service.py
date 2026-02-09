from config import settings


class DatabaseService:
    """
    Simulated database service.
    Uses configuration, does not define it.
    """

    def __init__(self, settings):
        self.settings = settings

    def connect(self) -> None:
        print(
            f"Connecting to database at "
            f"{self.settings.db_host}:{self.settings.db_port} "
            f"({self.settings.app_env} environment)"
        )


if __name__ == "__main__":
    db = DatabaseService(settings)
    db.connect()
