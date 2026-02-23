from dataclasses import dataclass
from typing import ClassVar
import re


@dataclass
class User:
    id: int
    email: str
    age: int

    _EMAIL_PATTERN: ClassVar[re.Pattern] = re.compile(r"^[^@]+@[^@]+\.[^@]+$")

    def __post_init__(self):
        if not self._is_valid_email(self.email):
            raise ValueError("Invalid email format")

        if self.age < 0:
            raise ValueError("Age cannot be negative")

    def is_adult(self) -> bool:
        return self.age >= 18

    def change_email(self, new_email: str) -> None:
        if not self._is_valid_email(new_email):
            raise ValueError("Invalid email format")

        self.email = new_email

    @classmethod
    def _is_valid_email(cls, email: str) -> bool:
        return bool(cls._EMAIL_PATTERN.match(email))


if __name__ == "__main__":
    user1 = User(id=1, email="test1@gmail.com", age=20)
    user2 = User(id=2, email="test2@gmail.com", age=25)

    print("User created:", user1)
    print("User created:", user2)
    
    print("Is adult?", user1.is_adult())
    print("Is adult?", user2.is_adult())

    user1.change_email("newemail1@gmail.com")
    user2.change_email("newemail2@gmail.com")
    
    print("Updated email:", user1.email)
    print("Updated email:", user2.email)
    
    print("User updated:", user1)
    print("User updated:", user2)
