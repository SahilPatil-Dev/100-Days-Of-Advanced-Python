class UserRepository:
    def __init__(self):
        self._users = []
        self._id_counter = 1

    def save(self, email: str, age: int):
        user = {
            "id": self._id_counter,
            "email": email,
            "age": age
        }
        self._users.append(user)
        self._id_counter += 1
        return user

    def get_all(self):
        return self._users