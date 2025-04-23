from typing import Dict

from .Notification import Notification


class CreditCardNotification(Notification):
    def send_amount(self, amount: float) -> Dict[str, float]:
        return {"amount": amount}
