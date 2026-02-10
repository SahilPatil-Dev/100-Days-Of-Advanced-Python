from datetime import datetime, timezone
from pathlib import Path


LOG_FILE = Path(__file__).parent / "app.log"


def write_log(message: str) -> None:
    """
    Appends a timestamped log message to a log file.
    File is created automatically if missing.
    """
    timestamp = datetime.now(timezone.utc).isoformat()
    log_entry = f"{timestamp} | {message}\n"

    with LOG_FILE.open("a", encoding="utf-8") as file:
        file.write(log_entry)


if __name__ == "__main__":
    write_log("Application started")
    write_log("User logged in")
