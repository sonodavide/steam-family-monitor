from abc import ABC, abstractmethod

class UpdateFetcher(ABC):
    """Abstract class for fetching updates"""
    
    @abstractmethod
    def test_connection(self) -> bool:
        """Test if update fetching system is working
        
        Returns:
            bool: True if test successful, False otherwise
        """
        pass