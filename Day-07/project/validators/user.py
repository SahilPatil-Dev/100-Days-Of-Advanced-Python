from project.exceptions.errors import InvalidEmailError, InvalidAgeError


def validate_user(data: dict):
    email = data.get("email")
    age = data.get("age")

    if not email or "@" not in email:
        raise InvalidEmailError("Invalid email format")

    if not isinstance(age, int) or age < 18:
        raise InvalidAgeError("User must be at least 18 years old")

    return True
