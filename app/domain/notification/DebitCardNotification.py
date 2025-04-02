from .Notification import Notification


class DebitCardNotification(Notification):
    def send(self, amount: float) -> str:
        return f"Pago procesado con tarjeta de debito. Monto final: {amount:.2f}"
