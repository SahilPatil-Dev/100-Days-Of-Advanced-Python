from typing import Any, Dict


def success_response(data: Any, message: str = "") -> Dict[str, Any]:
    return {
        "success": True,
        "data": data,
        "message": message,
    }


def error_response(error_message: str, status_code: int) -> Dict[str, Any]:
    return {
        "success": False,
        "error": error_message,
        "status_code": status_code,
    }
