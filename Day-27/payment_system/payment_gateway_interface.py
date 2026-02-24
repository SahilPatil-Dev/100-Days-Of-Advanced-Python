from abc import ABC, abstractmethod


class PaymentGateway(ABC):

    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass
