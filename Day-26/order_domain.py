from dataclasses import dataclass, field
from typing import List
from money import Money


@dataclass
class OrderItem:
    name: str
    price: Money


@dataclass
class Order:
    order_id: int
    _items: List[OrderItem] = field(default_factory=list)

    def add_item(self, item: OrderItem) -> None:
        self._items.append(item)

    @property
    def items(self) -> List[OrderItem]:
        return list(self._items)  # Defensive copy

    def total(self) -> Money:
        if not self._items:
            return Money(0, "USD")

        currency = self._items[0].price.currency
        total = Money(0, currency)

        for item in self._items:
            total = total.add(item.price)

        return total


if __name__ == "__main__":
    order = Order(order_id=101)
    order2 = Order(order_id=102)

    item1 = OrderItem("Laptop", Money(1000, "USD"))
    item2 = OrderItem("Mouse", Money(50, "USD"))
    item3 = OrderItem("Keyboard", Money(500, "USD"))

    order.add_item(item1)
    order.add_item(item2)
    order.add_item(item3)

    order2.add_item(item2)
    order2.add_item(item3)

    print("Order ID:", order.order_id)
    print("Items:", order.items)
    print("Total:", order.total())
    
    print("\nOrder ID:", order2.order_id)
    print("Items:", order2.items)
    print("Total:", order2.total())