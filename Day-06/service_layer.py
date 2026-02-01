class PaymentError(Exception):
    pass


def process_payment(amount):
    if amount <= 0:
        raise PaymentError("Payment amount must be greater than zero")

    return "Payment processed"


def checkout(amount):
    try:
        result = process_payment(amount)
        print(result)
    except PaymentError as e:
        print(f"Payment failed: {e}")


# Example runs
checkout(100)
checkout(-50)
