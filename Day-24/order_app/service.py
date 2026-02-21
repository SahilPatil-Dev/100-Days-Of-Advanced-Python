from validators import validate_order_input
from repository import OrderRepository


class OrderService:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def create_order(self, data: dict):
        validate_order_input(data)

        return self.repository.save(
            user_id=int(data["user_id"]),
            amount=float(data["amount"])
        )
