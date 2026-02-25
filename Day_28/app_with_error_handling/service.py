from ..exceptions import ValidationError, NotFoundError


class UserService:

    def __init__(self, repository):
        self._repository = repository

    def create_user(self, user_id: int, email: str):
        if "@" not in email:
            raise ValidationError("Invalid email format")

        user = {"id": user_id, "email": email}
        self._repository.save(user)
        return user

    def get_user(self, user_id: int):
        user = self._repository.get_by_id(user_id)

        if not user:
            raise NotFoundError("User not found")

        return user
