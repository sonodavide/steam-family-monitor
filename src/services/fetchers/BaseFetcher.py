from abc import ABC, abstractmethod

class BaseFetcher(ABC):
    """Abstract class for fetching updates"""
    
    @abstractmethod
    def fetch(self) -> list['ParsedUserResult']:
        pass