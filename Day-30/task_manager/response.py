from exceptions import ValidationError, NotFoundError, InfrastructureError


def success_response(data, message=""):
    return {
        "success": True,
        "data": data,
        "message": message
    }


def error_response(error_message, status_code):
    return {
        "success": False,
        "error": error_message,
        "status_code": status_code
    }


def handle_exception(e):
    if isinstance(e, ValidationError):
        return error_response(str(e), 400)

    if isinstance(e, NotFoundError):
        return error_response(str(e), 404)

    if isinstance(e, InfrastructureError):
        return error_response("Internal server error", 500)

    return error_response("Unexpected error", 500)
