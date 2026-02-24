from payment_gateway_interface import PaymentGateway


class PaypalGateway(PaymentGateway):

    def process_payment(self, amount: float) -> None:
        print(f"Processing ${amount} via PayPal")
