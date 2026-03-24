from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .models import SensorReading
from .schemas import SensorReadingCreate
from .detection import RollingBaselineDetector

app = FastAPI(title="IoT Pothole Detection API", version="1.0.0")
templates = Jinja2Templates(directory="backend/templates")
detector = RollingBaselineDetector()

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request, db: Session = Depends(get_db)):
    potholes = db.query(SensorReading).filter(SensorReading.pothole_detected == True).order_by(SensorReading.id.desc()).all()
    return templates.TemplateResponse("index.html", {"request": request, "potholes": potholes})

@app.post("/api/v1/readings")
def create_reading(payload: SensorReadingCreate, db: Session = Depends(get_db)):
    baseline_cm, deviation_cm, pothole_detected = detector.evaluate(
        device_id=payload.device_id,
        distance_cm=payload.distance_cm
    )

    reading = SensorReading(
        device_id=payload.device_id,
        distance_cm=payload.distance_cm,
        latitude=payload.latitude,
        longitude=payload.longitude,
        speed_kmph=payload.speed_kmph,
        timestamp=payload.timestamp,
        baseline_cm=baseline_cm,
        deviation_cm=deviation_cm,
        pothole_detected=pothole_detected,
    )
    db.add(reading)
    db.commit()
    db.refresh(reading)

    return {
        "message": "Reading stored successfully",
        "reading_id": reading.id,
        "baseline_cm": baseline_cm,
        "deviation_cm": deviation_cm,
        "pothole_detected": pothole_detected,
    }

@app.get("/api/v1/readings")
def list_readings(db: Session = Depends(get_db)):
    readings = db.query(SensorReading).order_by(SensorReading.id.desc()).all()
    return readings

@app.get("/api/v1/potholes")
def list_potholes(db: Session = Depends(get_db)):
    potholes = db.query(SensorReading).filter(SensorReading.pothole_detected == True).order_by(SensorReading.id.desc()).all()
    return potholes
