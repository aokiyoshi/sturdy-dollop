from pydantic import BaseModel

class Doctor(BaseModel):
    name: str

class Locations(BaseModel):
    doctor: Doctor
    latitude: float
    longitude: float
    distance: int
    timestamp: int
