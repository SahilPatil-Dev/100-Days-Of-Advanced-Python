from payment_gateway_interface import PaymentGateway


class StripeGateway(PaymentGateway):

    def process_payment(self, amount: float) -> None:
        print(f"Processing ${amount} via Stripe")
