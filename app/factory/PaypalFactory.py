from ..domain.notification.Notification import Notification
from ..domain.notification.PaypalNotification import PaypalNotification
from ..domain.paymentProcessor.PaymentProcessor import PaymentProcessor
from ..domain.paymentProcessor.PaypalProcessor import PaypalProcessor
from .notification.NotificationFactory import NotificationFactory
from .paymentProcessor.PaymentProcessorFactory import PaymentProcessorFactory


class PaypalFactory(NotificationFactory, PaymentProcessorFactory):
    def create_notification(self) -> Notification:
        return PaypalNotification()

    def create_payment_processor(self) -> PaymentProcessor:
        return PaypalProcessor()
