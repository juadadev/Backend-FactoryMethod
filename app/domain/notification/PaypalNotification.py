"""PaypalNotification class.

Clase en concreta de notificación de PayPal.
"""

from .Notification import Notification


class PaypalNotification(Notification):
    def send_amount(self, amount: float) -> dict[str, float]:
        """Envía una cantidad de dinero a través de PayPal.

        Args:
            amount (float): La cantidad de dinero a enviar.

        Returns:
            dict[str, float]: Un diccionario con la cantidad enviada.

        """
        return {'amount': amount}
