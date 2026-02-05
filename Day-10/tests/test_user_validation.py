import pytest
from Day_09.user_schema import User, InvalidEmailError, InvalidAgeError


VALID_EMAIL = "sahil@gmail.com"
VALID_AGE = "25"


def test_valid_user_is_created():
    # Arrange
    data = {"email": "Sahil@gmail.com", "age": VALID_AGE}

    # Act
    user = User.from_dict(data)

    # Assert
    assert user.email == VALID_EMAIL
    assert user.age == 25


@pytest.mark.parametrize(
    "email",
    [
        "Invalid gmail",
        "sahilgmail.com",
        "sahil@",
        "",
        None,
    ],
)
def test_invalid_email_raises_error(email):
    data = {"email": email, "age": VALID_AGE}

    with pytest.raises(InvalidEmailError):
        User.from_dict(data)


@pytest.mark.parametrize(
    "age",
    [
        "12",
        12,
        0,
        -5,
    ],
)
def test_underage_user_raises_error(age):
    data = {"email": VALID_EMAIL, "age": age}

    with pytest.raises(InvalidAgeError):
        User.from_dict(data)
