import json
from typing import Any, Dict


class JSONError(Exception):
    """Raised when JSON serialization or parsing fails."""
    pass


def serialize(data: Dict[str, Any]) -> str:
    try:
        return json.dumps(data)
    except (TypeError, ValueError) as e:
        raise JSONError(f"Serialization failed: {e}")


def deserialize(json_string: str) -> Dict[str, Any]:
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        raise JSONError(f"Invalid JSON: {e}")


if __name__ == "__main__":
    sample = {"name": "Sahil", "age": 25}

    json_str = serialize(sample)
    print("Serialized:", json_str)

    parsed = deserialize(json_str)
    print("Deserialized:", parsed)
