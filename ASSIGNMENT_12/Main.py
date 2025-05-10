# main.py

from fastapi import FastAPI
from api import device_api  # This brings in your device routes

# This line creates your FastAPI app
app = FastAPI()

# This connects the device routes to your app
app.include_router(device_api.router)

# This creates a welcome message at the root URL (just for testing)
@app.get("/")
def home():
    return {"message": "Hello from NetMan System API"}