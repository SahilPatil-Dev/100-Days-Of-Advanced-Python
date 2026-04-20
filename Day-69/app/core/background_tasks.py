import time
from datetime import datetime, timezone


def log_order_creation(order_id: int, user_id: int):
    """
    Simulate heavy background work (logging + analytics)
    """

    time.sleep(5)  # simulate heavy work

    with open("order_logs.txt", "a") as f:
        f.write(
            f"{datetime.now(timezone.utc)} | Order {order_id} created by User {user_id}\n"
        )