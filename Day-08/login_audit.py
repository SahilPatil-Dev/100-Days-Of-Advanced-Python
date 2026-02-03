import logging
import uuid
from datetime import datetime, timezone
import json
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

userpath = Path(__file__).parent / "users.json"


def log_login(username):
    # Load existing users
    if userpath.exists():
        with userpath.open("r", encoding="utf-8") as file:
            try:
                users = json.load(file)
            except json.JSONDecodeError:
                users = []
    else:
        users = []

    # Create login record
    request_id = str(uuid.uuid4())
    timestamp = datetime.now(timezone.utc).isoformat()

    login_record = {
        "request_id": request_id,
        "action": "login",
        "username": username,
        "timestamp": timestamp
    }

    # Save to file
    users.append(login_record)
    with userpath.open("w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)

    # Log to console
    logging.info(
        f"action=login username={username} request_id={request_id} timestamp={timestamp}"
    )

    return users


if __name__ == "__main__":
    log_login("Sahil Patil")
