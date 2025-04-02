from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, amount: float) -> str:
        pass
