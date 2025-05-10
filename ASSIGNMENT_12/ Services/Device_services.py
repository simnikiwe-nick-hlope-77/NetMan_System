# services/device_service.py
from repositories.device_repository import DeviceRepository
from models.device import Device
from uuid import uuid4

class DeviceService:
    def __init__(self, device_repo: DeviceRepository):
        self.device_repo = device_repo

    def create_device(self, name: str, ip: str, type: str) -> Device:
        if not ip or not name or not type:
            raise ValueError("All fields are required.")
        device = Device(id=str(uuid4()), name=name, ip=ip, type=type)
        return self.device_repo.save(device)

    def get_all_devices(self):
        return self.device_repo.find_all()

    def update_device(self, device_id: str, data: dict):
        device = self.device_repo.find_by_id(device_id)
        if not device:
            raise ValueError("Device not found")
        device.name = data.get("name", device.name)
        device.ip = data.get("ip", device.ip)
        device.type = data.get("type", device.type)
        return self.device_repo.save(device)