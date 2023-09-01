from typing import Union

from fastapi import FastAPI
from models import Doctor, Locations

app = FastAPI()

# Создать нового доктора
@app.post("/create_doctor/")
async def create_doctor(doctor: Doctor):
    # Save the doctor in the database or perform other operations
    return doctor

# Get a specific doctor by ID
@app.get("/doctors/{doctor_id}")
async def get_doctor(doctor_id: int):
    # Retrieve the doctor from the database or perform other operations
    return {"doctor_id": doctor_id, "name": "Doctor Name"}

# Update a specific doctor by ID
@app.put("/doctors/{doctor_id}")
async def update_doctor(doctor_id: int, doctor: Doctor):
    # Update the doctor in the database or perform other operations
    return {"message": f"Doctor {doctor_id} updated successfully"}

# Delete a specific doctor by ID
@app.delete("/doctors/{doctor_id}")
async def delete_doctor(doctor_id: int):
    # Delete the doctor from the database or perform other operations
    return {"message": f"Doctor {doctor_id} deleted successfully"}

# Create a new location
@app.post("/locations/")
async def create_location(location: Locations):
    # Save the location in the database or perform other operations
    return {"message": "Location created successfully"}

# Get a specific location by ID
@app.get("/locations/{location_id}")
async def get_location(location_id: int):
    # Retrieve the location from the database or perform other operations
    return {"location_id": location_id, "latitude": 0.0, "longitude": 0.0}

# Update a specific location by ID
@app.put("/locations/{location_id}")
async def update_location(location_id: int, location: Locations):
    # Update the location in the database or perform other operations
    return {"message": f"Location {location_id} updated successfully"}

# Delete a specific location by ID
@app.delete("/locations/{location_id}")
async def delete_location(location_id: int):
    # Delete the location from the database or perform other operations
    return {"message": f"Location {location_id} deleted successfully"}