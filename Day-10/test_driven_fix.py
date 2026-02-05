import pytest
from Day_09.user_schema import User, InvalidAgeError


def test_age_float_is_rejected():
    with pytest.raises(InvalidAgeError):
        User.from_dict({"email": "test@example.com", "age": 25.5})
