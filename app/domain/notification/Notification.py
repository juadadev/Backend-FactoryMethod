from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send_amount(self, amount: float) -> float:
        pass
