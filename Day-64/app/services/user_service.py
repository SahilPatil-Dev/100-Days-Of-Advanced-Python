from app.core.exceptions import NotFoundError, ValidationError


def get_user(user_id: int):

    user = None 

    if not user:
        raise NotFoundError("User not found")

    return user


def create_user(email: str, age: int):

    if age < 18:
        raise ValidationError("User must be at least 18")

    return {"email": email, "age": age}