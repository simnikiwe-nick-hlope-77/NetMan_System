#Repositories/In_memory_implementation/In_memory_firewall_repo.py

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

# repositories/inmemory/in_memory_firewall_repository.py

from domain.firewall import Firewall
from repositories.firewall_repository import FirewallRepository

class InMemoryFirewallRepository(FirewallRepository):
    """
    Stores Firewall objects in memory using a Python dictionary.
    This implementation is useful for testing or running without a real database.
    """

    def __init__(self):
        # Dictionary to store firewalls keyed by their ID (string)
        # Example: {'fw01': Firewall(...), 'fw02': Firewall(...)}
        self.firewalls = {}

    def save(self, firewall: Firewall) -> None:
        """
        Save or update a firewall in memory.
        If a firewall with the same ID exists, it will be overwritten.
        """
        self.firewalls[firewall.id] = firewall

    def find_by_id(self, id: str):
        """
        Retrieve a firewall by ID.
        Returns None if the ID doesn't exist in memory.
        """
        return self.firewalls.get(id)

    def find_all(self):
        """
        Return a list of all firewall objects currently stored in memory.
        This returns the values from the dictionary as a list.
        """
        return list(self.firewalls.values())

    def delete(self, id: str):
        """
        Delete a firewall by ID, if it exists.
        If the ID is not in the dictionary, nothing happens (safe delete).
        """
        self.firewalls.pop(id, None)