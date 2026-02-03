from datetime import datetime, timezone


def generate_event_timestamp():
    return datetime.now(timezone.utc).isoformat()


if __name__ == "__main__":
    timestamp = generate_event_timestamp()
    print(timestamp)
