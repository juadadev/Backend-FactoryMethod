from .Notification import Notification


class PaypalNotification(Notification):
    def send_amount(self, amount: float) -> float:
        return amount
