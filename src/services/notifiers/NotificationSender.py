from abc import ABC, abstractmethod

class NotificationSender(ABC):
    """Abstract class for sending notifications"""
    
    @abstractmethod
    def send_notification(self) -> bool:
        pass