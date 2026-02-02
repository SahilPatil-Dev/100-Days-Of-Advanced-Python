from project.exceptions.errors import PaymentError


def process_payment(amount: int):
    if amount <= 0:
        raise PaymentError("Payment amount must be greater than zero")

    return "Payment processed successfully"
