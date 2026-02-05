from Day_09.user_schema import User
from Day_09.serializer import serialize_user


def test_serializer_returns_json_safe_dict():
    # Arrange
    user = User(email="test@example.com", age=30)

    # Act
    result = serialize_user(user)

    # Assert
    assert isinstance(result, dict)
    assert result == {
        "email": "test@example.com",
        "age": 30,
    }


def test_serializer_does_not_expose_internal_state():
    # Arrange
    user = User(email="test@example.com", age=30)

    # Act
    result = serialize_user(user)

    # Assert
    assert "__dict__" not in result
