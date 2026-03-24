from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime
from datetime import datetime
from .database import Base

class SensorReading(Base):
    __tablename__ = "sensor_readings"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, index=True, nullable=False)
    distance_cm = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    speed_kmph = Column(Float, nullable=True)
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)
    baseline_cm = Column(Float, nullable=False)
    deviation_cm = Column(Float, nullable=False)
    pothole_detected = Column(Boolean, default=False)
