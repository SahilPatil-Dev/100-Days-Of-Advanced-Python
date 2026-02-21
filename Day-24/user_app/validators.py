class ValidationError(Exception):
    pass


def validate_user_input(data: dict) -> None:
    if "email" not in data or "@" not in data["email"]:
        raise ValidationError("Invalid email")

    if "age" not in data:
        raise ValidationError("Age is required")

    try:
        age = int(data["age"])
    except ValueError:
        raise ValidationError("Age must be a number")

    if age < 18:
        raise ValidationError("User must be 18+")
