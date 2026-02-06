# from typing import Union
class DiscountError(Exception):
    pass


def calculate_discount(price: int | float, percentage: int | float) -> float: # def calculate_discount(price: Union[int, float], percentage: Union[int, float]) -> float: (old way)
    """
    Calculates discounted price.
    Explicitly defensive: rejects invalid types and values.
    """

    if not isinstance(price, (int, float)):
        raise DiscountError("Price must be a number")

    if not isinstance(percentage, (int, float)):
        raise DiscountError("Percentage must be a number")

    if price < 0:
        raise DiscountError("Price cannot be negative")

    if not 0 <= percentage <= 100:
        raise DiscountError("Percentage must be between 0 and 100")

    discount: float = price * (percentage / 100)
    return round(price - discount, 2)

if __name__ == "__main__":
    final_price = calculate_discount(100, 15)
    print(final_price)
