# tests/services/test_device_service.py
from services.device_service import DeviceService
from repositories.device_repository import DeviceRepository
from models.device import Device

class DummyRepo(DeviceRepository):
    def __init__(self):
        self.db = {}

    def save(self, device):
        self.db[device.id] = device
        return device

    def find_all(self):
        return list(self.db.values())

    def find_by_id(self, device_id):
        return self.db.get(device_id)

def test_create_device_success():
    service = DeviceService(DummyRepo())
    device = service.create_device("Router A", "192.168.1.1", "Router")
    assert device.name == "Router A"

def test_create_device_invalid_input():
    service = DeviceService(DummyRepo())
    try:
        service.create_device("", "", "")
    except ValueError as e:
        assert str(e) == "All fields are required."