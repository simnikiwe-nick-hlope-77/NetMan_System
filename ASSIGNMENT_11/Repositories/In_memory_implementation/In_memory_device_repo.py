#Repositories/In_memory_implementation/In_memory_device_repo.py

from domain.device import Device
from repositories.device_repository import DeviceRepository

class InMemoryDeviceRepository(DeviceRepository):
    """
    Stores Device objects in a simple Python dictionary.
    """

    def __init__(self):
        self.devices = {}  # Dictionary of devices keyed by ID

    def save(self, device: Device) -> None:
        self.devices[device.id] = device  # Add or update

    def find_by_id(self, id: str):
        return self.devices.get(id)  # Get by ID or return None

    def find_all(self):
        return list(self.devices.values())  # Return all devices

    def delete(self, id: str):
        self.devices.pop(id, None)  # Remove if exists