from ..domain.notification.DebitCardNotification import DebitCardNotification
from ..domain.notification.Notification import Notification
from ..domain.paymentProcessor.DebitCardProcessor import DebitCardProcessor
from ..domain.paymentProcessor.PaymentProcessor import PaymentProcessor
from .notification.NotificationFactory import NotificationFactory
from .paymentProcessor.PaymentProcessorFactory import PaymentProcessorFactory


class DebitCardFactory(NotificationFactory, PaymentProcessorFactory):
    def create_notification(self) -> Notification:
        return DebitCardNotification()

    def create_payment_processor(self) -> PaymentProcessor:
        return DebitCardProcessor()
