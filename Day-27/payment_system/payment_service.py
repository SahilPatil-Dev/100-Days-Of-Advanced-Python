from payment_gateway_interface import PaymentGateway


class PaymentService:

    def __init__(self, gateway: PaymentGateway):
        self._gateway = gateway

    def checkout(self, amount: float) -> None:
        self._gateway.process_payment(amount)


if __name__ == "__main__":
    from stripe_gateway import StripeGateway
    from paypal_gateway import PaypalGateway

    stripe_service = PaymentService(StripeGateway())
    paypal_service = PaymentService(PaypalGateway())

    stripe_service.checkout(100)
    paypal_service.checkout(200)
