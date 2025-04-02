from .notification.NotificationFactory import NotificationFactory
from .paymentProcessor.PaymentProcessorFactory import PaymentProcessorFactory
from ..domain.notification.Notification import Notification
from ..domain.paymentProcessor.PaymentProcessor import PaymentProcessor
from ..domain.notification.CreditCardNotification import CreditCardNotification
from ..domain.paymentProcessor.CreditCardProcessor import CreditCardProcessor


class CreditCardFactory(NotificationFactory, PaymentProcessorFactory):
    def create_notification(self) -> Notification:
        return CreditCardNotification()

    def create_payment_processor(self) -> PaymentProcessor:
        return CreditCardProcessor()
