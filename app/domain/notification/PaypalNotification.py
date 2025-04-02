from .Notification import Notification


class PaypalNotification(Notification):
    def send(self, amount: float) -> str:
        return f"Pago procesado con Paypal. Monto final: {amount:.2f}"
