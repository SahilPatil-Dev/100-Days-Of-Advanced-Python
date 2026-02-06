from typing import Optional, TypedDict


# ---- Type aliases / contracts ----

class RawUserData(TypedDict, total=False):
    email: str
    age: int | str


class User:
    """
    Internal domain model.
    Business logic trusts this object completely.
    """

    def __init__(self, email: str, age: int) -> None:
        self.email: str = email
        self.age: int = age

    def __repr__(self) -> str:
        return f"User(email={self.email!r}, age={self.age})"


# ---- Custom errors ----

class ValidationError(Exception):
    pass


class InvalidEmailError(ValidationError):
    pass


class InvalidAgeError(ValidationError):
    pass


# ---- Service-layer function ----

def create_user(data: RawUserData) -> User:
    """
    Validation + normalization boundary.
    Converts untrusted input into a trusted User object.
    """

    email: Optional[str] = data.get("email")
    age_raw: Optional[int | str] = data.get("age")

    # ---- Email validation ----
    if email is None or not isinstance(email, str) or "@" not in email:
        raise InvalidEmailError("Invalid email")

    # ---- Age presence ----
    if age_raw is None:
        raise InvalidAgeError("Age is required")

    # ---- Prevent bool from passing as int ----
    if isinstance(age_raw, bool):
        raise InvalidAgeError("Age must be a number")

    # ---- Convert age to int ----
    try:
        age: int = int(age_raw)
    except (TypeError, ValueError):
        raise InvalidAgeError("Age must be numeric")

    # ---- Business rule ----
    if age < 18:
        raise InvalidAgeError("User must be at least 18")

    # ---- Create trusted domain object ----
    return User(email=email.lower(), age=age)

if __name__ == "__main__":
    raw_data = {
        "email": "TEST@Example.com",
        "age": "25",
    }

    user = create_user(raw_data)
    print(user)
