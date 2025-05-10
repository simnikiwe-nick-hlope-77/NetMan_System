# api/device_api.py
from fastapi import APIRouter, HTTPException
from services.device_service import DeviceService
from repositories.device_repository import DeviceRepository
from models.device import Device
from typing import List

router = APIRouter(prefix="/api/devices", tags=["Devices"])
device_service = DeviceService(DeviceRepository())

@router.get("/", response_model=List[Device])
def get_all_devices():
    return device_service.get_all_devices()

@router.post("/", response_model=Device)
def create_device(device: Device):
    try:
        return device_service.create_device(device.name, device.ip, device.type)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{device_id}", response_model=Device)
def update_device(device_id: str, device: Device):
    try:
        return device_service.update_device(device_id, device.dict())
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))