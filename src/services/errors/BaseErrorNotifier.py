from abc import ABC, abstractmethod

class BaseErrorNotifier(ABC):
    """Abstract class for sending notifications"""
    
    @abstractmethod
    def notify_error(self) -> bool:
        pass