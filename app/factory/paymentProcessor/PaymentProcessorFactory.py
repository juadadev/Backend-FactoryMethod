from abc import ABC, abstractmethod
from ...domain.paymentProcessor.PaymentProcessor import PaymentProcessor


class PaymentProcessorFactory(ABC):
    def get_payment_processor(self) -> PaymentProcessor:
        payment_processor = self.create_payment_processor()
        return payment_processor

    @abstractmethod
    def create_payment_processor(self) -> PaymentProcessor:
        pass
