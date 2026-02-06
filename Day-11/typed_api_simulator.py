from typing import Dict, Any

from user_service import (
    create_user,
    ValidationError,
    User,
)
from discount_calculator import calculate_discount, DiscountError


ApiResponse = Dict[str, Any]


def handle_create_user(request_data: Dict[str, Any]) -> ApiResponse:
    """
    Simulates an API endpoint with typed contracts.
    Acts as a strict boundary.
    """
    try:
        user: User = create_user(request_data)

        discounted_price: float = calculate_discount(
            price=1000,
            percentage=10,
        )

        return {
            "success": True,
            "data": {
                "email": user.email,
                "age": user.age,
                "discounted_price": discounted_price,
            },
        }

    except (ValidationError, DiscountError) as e:
        return {
            "success": False,
            "error": str(e),
        }


if __name__ == "__main__":
    print(handle_create_user({"email": "Test@Example.com", "age": "25"}))
    print(handle_create_user({"email": "invalid", "age": 15}))
