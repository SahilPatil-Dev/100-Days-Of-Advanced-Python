from typing import List
from schemas import Order


class OrderRepository:
    def __init__(self):
        self._orders: List[Order] = []
        self._id_counter = 1

    def save(self, user_id: int, amount: float) -> Order:
        order = Order(
            id=self._id_counter,
            user_id=user_id,
            amount=amount
        )
        self._orders.append(order)
        self._id_counter += 1
        return order
