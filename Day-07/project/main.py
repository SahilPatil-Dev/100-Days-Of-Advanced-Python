from project.validators.user import validate_user
from project.services.payment import process_payment
from project.exceptions.errors import (
    InvalidEmailError,
    InvalidAgeError,
    PaymentError,
)


def main():
    user_data = {
        "email": "test@example.com",
        "age": 20,
        "amount": 100,
    }

    try:
        validate_user(user_data)
        result = process_payment(user_data["amount"])
        print(result)

    except (InvalidEmailError, InvalidAgeError, PaymentError) as e:
        print(f"Operation failed: {e}")


if __name__ == "__main__":
    main()
