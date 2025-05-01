from ..domain.notification.CreditCardNotification import CreditCardNotification
from ..domain.notification.Notification import Notification
from ..domain.paymentProcessor.CreditCardProcessor import CreditCardProcessor
from ..domain.paymentProcessor.PaymentProcessor import PaymentProcessor
from .notification.NotificationFactory import NotificationFactory
from .paymentProcessor.PaymentProcessorFactory import PaymentProcessorFactory


class CreditCardFactory(NotificationFactory, PaymentProcessorFactory):
    def create_notification(self) -> Notification:
        return CreditCardNotification()

    def create_payment_processor(self) -> PaymentProcessor:
        return CreditCardProcessor()
