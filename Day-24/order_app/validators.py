class ValidationError(Exception):
    pass


def validate_order_input(data: dict) -> None:
    if "user_id" not in data:
        raise ValidationError("User ID required")

    if "amount" not in data:
        raise ValidationError("Amount required")

    try:
        amount = float(data["amount"])
    except ValueError:
        raise ValidationError("Amount must be numeric")

    if amount <= 0:
        raise ValidationError("Amount must be positive")
