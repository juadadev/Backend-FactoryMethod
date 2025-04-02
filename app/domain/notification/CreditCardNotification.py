from .Notification import Notification


class CreditCardNotification(Notification):
    def send(self, amount: float) -> str:
        return f"Pago procesado con tarjeta de crédito. Monto final: {amount:.2f}"
