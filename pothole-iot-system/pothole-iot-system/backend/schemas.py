from pydantic import BaseModel, Field
from datetime import datetime

class SensorReadingCreate(BaseModel):
    device_id: str = Field(..., examples=["vehicle-01"])
    distance_cm: float = Field(..., examples=[20.5])
    latitude: float = Field(..., examples=[39.7817])
    longitude: float = Field(..., examples=[-84.1052])
    speed_kmph: float | None = Field(default=None, examples=[35.2])
    timestamp: datetime

class SensorReadingResponse(BaseModel):
    id: int
    device_id: str
    distance_cm: float
    latitude: float
    longitude: float
    speed_kmph: float | None
    timestamp: datetime
    baseline_cm: float
    deviation_cm: float
    pothole_detected: bool

    class Config:
        from_attributes = True
