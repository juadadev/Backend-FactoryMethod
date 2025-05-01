from .Notification import Notification


class DebitCardNotification(Notification):
    def send_amount(self, amount: float) -> dict[str, float]:
        return {'amount': amount}
