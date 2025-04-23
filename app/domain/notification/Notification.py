from abc import ABC, abstractmethod
from typing import Dict


class Notification(ABC):
    @abstractmethod
    def send_amount(self, amount: float) -> Dict[str, float]:
        pass
