from ..exceptions import InfrastructureError


class UserRepository:

    def __init__(self):
        self._storage = {}

    def save(self, user):
        try:
            self._storage[user["id"]] = user
        except Exception as e:
            raise InfrastructureError("Failed to save user") from e

    def get_by_id(self, user_id):
        try:
            return self._storage.get(user_id)
        except Exception as e:
            raise InfrastructureError("Database access error") from e
