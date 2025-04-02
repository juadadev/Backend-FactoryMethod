from .notification.NotificationFactory import NotificationFactory
from .paymentProcessor.PaymentProcessorFactory import PaymentProcessorFactory
from ..domain.notification.Notification import Notification
from ..domain.paymentProcessor.PaymentProcessor import PaymentProcessor
from ..domain.notification.PaypalNotification import PaypalNotification
from ..domain.paymentProcessor.PaypalProcessor import PaypalProcessor


class PaypalFactory(NotificationFactory, PaymentProcessorFactory):
    def create_notification(self) -> Notification:
        return PaypalNotification()

    def create_payment_processor(self) -> PaymentProcessor:
        return PaypalProcessor()
