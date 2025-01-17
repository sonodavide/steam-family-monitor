from abc import ABC, abstractmethod

class UpdateFetcher(ABC):
    """Abstract class for fetching updates"""
    
    @abstractmethod
    def fetchUpdates(self) -> list['ParsedUserResult']:
        pass