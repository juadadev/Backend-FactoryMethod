from abc import ABC, abstractmethod

from ...domain.notification.Notification import Notification


class NotificationFactory(ABC):
    def get_notification(self) -> Notification:
        notification = self.create_notification()
        return notification

    @abstractmethod
    def create_notification(self) -> Notification:
        pass
