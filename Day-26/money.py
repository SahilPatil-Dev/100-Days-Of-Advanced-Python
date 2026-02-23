from dataclasses import dataclass


@dataclass(frozen=True)
class Money:
    amount: float
    currency: str

    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Amount cannot be negative")

        if not self.currency:
            raise ValueError("Currency must be provided")

    def add(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError("Cannot add money with different currencies")

        return Money(
            amount=self.amount + other.amount,
            currency=self.currency
        )


if __name__ == "__main__":
    m1 = Money(100, "USD")
    m2 = Money(50, "USD")

    total = m1.add(m2)

    print("Money 1:", m1)
    print("Money 2:", m2)
    print("Total:", total)