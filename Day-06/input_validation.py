class InvalidEmailError(Exception):
    pass


class InvalidAgeError(Exception):
    pass


def validate_user(data: dict):
    email = data.get("email")
    age = data.get("age")

    if not email or "@" not in email:
        raise InvalidEmailError("Email format is invalid")

    if not isinstance(age, int) or age < 18:
        raise InvalidAgeError("Age must be 18 or above")

    return True


# Example usage
if __name__ == "__main__":
    print(validate_user({"email": "test@example.com", "age": 20}))
