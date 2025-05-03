# repositories/repository.py

from typing import TypeVar, Generic, List, Optional
from abc import ABC, abstractmethod

# T is the type of object (like Device, User)
# ID is the type of identifier (like str or int)
T = TypeVar('T')
ID = TypeVar('ID')

class Repository(ABC, Generic[T, ID]):
    """
    A generic interface (or template) for any kind of repository.
    This helps us define a common set of methods for storing and retrieving objects,
    no matter what kind of object it is.
    """

    @abstractmethod
    def save(self, entity: T) -> None:
        """
        Save or update an object.
        If the object already exists, update it.
        If not, add it.
        """
        pass

    @abstractmethod
    def find_by_id(self, id: ID) -> Optional[T]:
        """
        Get a single object by its ID.
        If the object doesn't exist, return None.
        """
        pass

    @abstractmethod
    def find_all(self) -> List[T]:
        """
        Get all the objects stored in the repository.
        """
        pass

    @abstractmethod
    def delete(self, id: ID) -> None:
        """
        Delete an object by its ID.
        If it doesn't exist, nothing happens.
        """
        pass