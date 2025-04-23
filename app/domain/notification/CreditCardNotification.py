from .Notification import Notification


class CreditCardNotification(Notification):
    def send_amount(self, amount: float) -> float:
        return amount
