from datetime import datetime


class ValidationError(Exception):
    pass


def validate_record(record: dict) -> dict:

    try:
        timestamp = datetime.fromisoformat(record["timestamp"])
    except Exception:
        raise ValidationError("Invalid timestamp format")

    endpoint = record.get("endpoint")
    if not isinstance(endpoint, str) or not endpoint:
        raise ValidationError("Invalid endpoint")

    try:
        response_time = float(record["response_time"])
        if response_time < 0:
            raise ValidationError("response_time must be >= 0")
    except Exception:
        raise ValidationError("Invalid response_time")

    try:
        status_code = int(record["status_code"])
        if status_code < 100 or status_code > 599:
            raise ValidationError("Invalid HTTP status_code")
    except Exception:
        raise ValidationError("Invalid status_code")

    return {
        "timestamp": timestamp,
        "endpoint": endpoint,
        "response_time": response_time,
        "status_code": status_code
    }