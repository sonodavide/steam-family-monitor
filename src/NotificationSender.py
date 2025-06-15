from abc import ABC, abstractmethod

class NotificationSender(ABC):
    """Abstract class for sending notifications"""
    
    @abstractmethod
    def test_notification(self) -> bool:
        """Test if notification system is working
        
        Returns:
            bool: True if test successful, False otherwise
        """
        pass