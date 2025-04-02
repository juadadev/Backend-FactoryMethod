from .notification.NotificationFactory import NotificationFactory
from .paymentProcessor.PaymentProcessorFactory import PaymentProcessorFactory
from ..domain.notification.Notification import Notification
from ..domain.paymentProcessor.PaymentProcessor import PaymentProcessor
from ..domain.notification.DebitCardNotification import DebitCardNotification
from ..domain.paymentProcessor.DebitCardProcessor import DebitCardProcessor


class DebitCardFactory(NotificationFactory, PaymentProcessorFactory):
    def create_notification(self) -> Notification:
        return DebitCardNotification()

    def create_payment_processor(self) -> PaymentProcessor:
        return DebitCardProcessor()
