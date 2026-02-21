from repository import OrderRepository
from service import OrderService
from validators import ValidationError


def main():
    repository = OrderRepository()
    service = OrderService(repository)

    try:
        order = service.create_order({
            "user_id": "1",
            "amount": "99.99"
        })

        print({
            "success": True,
            "data": order
        })

    except ValidationError as e:
        print({
            "success": False,
            "error": str(e)
        })


if __name__ == "__main__":
    main()
