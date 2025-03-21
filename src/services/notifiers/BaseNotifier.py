from abc import ABC, abstractmethod

class BaseNotifier(ABC):
    """Abstract class for sending notifications"""
    
    @abstractmethod
    def notify(self) -> bool:
        pass