from .Notification import Notification


class CreditCardNotification(Notification):
    def send_amount(self, amount: float) -> dict[str, float]:
        return {'amount': amount}
