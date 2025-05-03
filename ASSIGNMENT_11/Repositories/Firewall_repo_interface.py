#Repositories/Firewall_repo_interface.py

from abc import ABC, abstractmethod
from domain.firewall import Firewall
from typing import Optional, List

class FirewallRepository(ABC):
    """
    Abstract base class that defines how the system should interact with Firewall objects.
    This ensures consistency across all implementations (e.g., in-memory, database).
    """

    @abstractmethod
    def save(self, firewall: Firewall) -> None:
        """
        Save or update a firewall object.
        If the firewall already exists, it should be overwritten.
        """
        pass

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[Firewall]:
        """
        Find a firewall by its unique ID.
        Returns the Firewall if found, else None.
        """
        pass

    @abstractmethod
    def find_all(self) -> List[Firewall]:
        """
        Return a list of all stored firewalls.
        """
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        """
        Remove a firewall by its ID.
        If it doesn't exist, do nothing.
        """
        pass