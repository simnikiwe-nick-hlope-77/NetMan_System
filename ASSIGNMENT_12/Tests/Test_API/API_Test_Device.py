# tests/api/test_device_api.py
from fastapi.testclient import TestClient
from main import app  # assuming your FastAPI app is in main.py

client = TestClient(app)

def test_create_device_endpoint():
    response = client.post("/api/devices/", json={
        "name": "Switch 1",
        "ip": "10.0.0.2",
        "type": "Switch",
        "id": "dummy-id"  # needed if using Device model as input
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Switch 1"