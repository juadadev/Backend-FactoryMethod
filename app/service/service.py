from ..factory.CreditCardFactory import CreditCardFactory
from ..factory.DebitCardFactory import DebitCardFactory
from ..factory.notification.NotificationFactory import NotificationFactory
from ..factory.paymentProcessor.PaymentProcessorFactory import PaymentProcessorFactory
from ..factory.PaypalFactory import PaypalFactory


class Service:
    def __init__(self):
        self.payment_processor_factory: PaymentProcessorFactory = None
        self.notification_factory: NotificationFactory = None

    def payAndNotify(self, payment_type: str, amount: float):
        self.configurationFactory(payment_type)

        # Procesar el pago
        payment_processor = self.payment_processor_factory.get_payment_processor()
        final_amount = payment_processor.process(amount)

        # Enviar notificación del monto final
        notification = self.notification_factory.get_notification()

        return notification.send_amount(final_amount)

    def configurationFactory(self, payment_type: str):
        if payment_type == "CREDIT_CARD":
            self.payment_processor_factory = CreditCardFactory()
            self.notification_factory = CreditCardFactory()
        elif payment_type == "DEBIT_CARD":
            self.payment_processor_factory = DebitCardFactory()
            self.notification_factory = DebitCardFactory()
        elif payment_type == "PAYPAL":
            self.payment_processor_factory = PaypalFactory()
            self.notification_factory = PaypalFactory()
        else:
            raise Exception("Método de pago no soportado")
