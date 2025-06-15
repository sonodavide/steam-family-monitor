from abc import ABC, abstractmethod

class BaseErrorNotifier(ABC):
    """Abstract class for sending error notifications"""
    
    @abstractmethod
    def notify_error(self, error_message) -> None:
        pass