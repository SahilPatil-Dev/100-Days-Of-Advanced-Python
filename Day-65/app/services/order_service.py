from app.schemas.order import OrderCreate

orders_db = []
order_id_counter = 1


def create_order(order: OrderCreate):

    global order_id_counter

    new_order = {
        "id": order_id_counter,
        "user_id": order.user_id,
        "amount": order.amount
    }

    orders_db.append(new_order)
    order_id_counter += 1

    return new_order