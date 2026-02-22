def is_valid_order(order):
    return order["status"] == "completed" and order["amount"] > 0


def calculate_total(orders):
    return sum(order["amount"] for order in orders if is_valid_order(order))


def log_processed_orders(orders):
    for order in orders:
        if is_valid_order(order):
            print("Processed order:", order["id"])


def process_orders(orders):
    total = calculate_total(orders)
    log_processed_orders(orders)
    return total


if __name__ == "__main__":
    orders = [
        {"id": 1, "status": "completed", "amount": 100},
        {"id": 2, "status": "pending", "amount": 200},
        {"id": 3, "status": "completed", "amount": 300},
        {"id": 4, "status": "completed", "amount": -50},
    ]

    total = process_orders(orders)
    print("Total:", total)