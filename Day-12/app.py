import sys
from config import ConfigError, settings
from database_service import DatabaseService


def main() -> None:
    try:
        print("Starting application...")
        print(f"Running in {settings.app_env} environment")

        db_service = DatabaseService(settings)
        db_service.connect()

        print("Application started successfully")

    except ConfigError as e:
        print(f"Startup failed due to configuration error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
