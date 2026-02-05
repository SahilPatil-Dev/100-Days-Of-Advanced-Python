from user_schema import User, ValidationError
from serializer import serialize_user


def handle_create_user(request_data: dict):
    """
    Simulates an API endpoint handler.
    Acts as an error boundary.
    """
    try:
        # 1. Validate & normalize input
        user = User.from_dict(request_data)

        # 2. (Business logic would go here)
        # e.g. save to DB, apply rules, etc.

        # 3. Serialize response
        return {
            "success": True,
            "data": serialize_user(user),
        }

    except ValidationError as e:
        return {
            "success": False,
            "error": str(e),
        }


if __name__ == "__main__":
    # Valid request
    print(handle_create_user({"email": "Test@Example.com", "age": "25"}))

    # Invalid request
    print(handle_create_user({"email": "invalid", "age": 12}))
