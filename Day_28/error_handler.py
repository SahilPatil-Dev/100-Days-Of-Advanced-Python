from .exceptions import ValidationError, NotFoundError, InfrastructureError


def handle_exception(e: Exception) -> dict:

    if isinstance(e, ValidationError):
        return {
            "success": False,
            "error_type": "validation_error",
            "message": str(e),
            "status_code": 400,
        }

    if isinstance(e, NotFoundError):
        return {
            "success": False,
            "error_type": "not_found",
            "message": str(e),
            "status_code": 404,
        }

    if isinstance(e, InfrastructureError):
        return {
            "success": False,
            "error_type": "infrastructure_error",
            "message": "Internal service failure",
            "status_code": 500,
        }

    # Unknown error (fail-safe fallback)
    return {
        "success": False,
        "error_type": "unknown_error",
        "message": "Unexpected failure",
        "status_code": 500,
    }
