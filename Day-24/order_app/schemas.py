from dataclasses import dataclass


@dataclass
class Order:
    id: int
    user_id: int
    amount: float
