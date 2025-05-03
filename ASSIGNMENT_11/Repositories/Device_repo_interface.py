#Repositories/Device_repo_interafce.py

from repositories.repository import Repository
from domain.device import Device 

class DeviceRepository(Repository[Device, str]):
    """
    This is the specific interface for handling Device objects.
    It inherits all the methods from the generic Repository.
    Specifying that this repository deals with Device objects that use string IDs.
    """
    pass  # No need to add anything now — it's just linking Device to the generic idea