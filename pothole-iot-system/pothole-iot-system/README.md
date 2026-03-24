# IoT-Based Pothole Detection System

A starter GitHub-style repository for an **IoT pothole detection project** that uses:

- **Ultrasonic sensor readings** to estimate road surface depth changes
- **GPS coordinates** to tag pothole locations
- **FastAPI** for backend ingestion and retrieval
- **SQLite + SQLAlchemy** for storage
- **Docker** for local deployment
- **A simple simulator** to mimic sensor + GPS data
- **A lightweight dashboard** to view detected potholes

## Architecture

```text
Ultrasonic Sensor + GPS
          ↓
   Microcontroller / Device
          ↓
   HTTP POST /api/v1/readings
          ↓
       FastAPI Backend
          ↓
    Detection Logic + DB
          ↓
 Dashboard / Reports / Analysis
```

## Detection Logic

A pothole is flagged when:
- the current distance is significantly larger than the rolling baseline, and
- the difference exceeds a threshold

Example:
- Normal road height reading: ~12 cm
- Sudden dip reading: ~20 cm
- Difference: 8 cm → flag as pothole if threshold is 5 cm

## Project Structure

```text
pothole-iot-system/
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── detection.py
│   └── templates/
│       └── index.html
├── simulator/
│   └── sensor_simulator.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Quick Start

### Local
```bash
pip install -r requirements.txt
uvicorn backend.app:app --reload
```

Open:
- API docs: http://127.0.0.1:8000/docs
- Dashboard: http://127.0.0.1:8000/

### Run simulator
```bash
python simulator/sensor_simulator.py
```

### Docker
```bash
docker compose up --build
```

## Main Endpoints

- `POST /api/v1/readings` → ingest sensor + GPS reading
- `GET /api/v1/potholes` → list detected potholes
- `GET /api/v1/readings` → list all readings
- `GET /health` → health check

## Example Payload

```json
{
  "device_id": "vehicle-01",
  "distance_cm": 20.4,
  "latitude": 39.7817,
  "longitude": -84.1052,
  "speed_kmph": 34.5,
  "timestamp": "2026-03-24T15:30:00"
}
```

## Interview-Friendly Explanation

This project simulates an IoT system where road-depth data from an ultrasonic sensor and position data from GPS are sent to a backend API. The backend stores each reading, compares it to a rolling baseline, and flags likely potholes when the distance jump crosses a defined threshold. The result is a simple end-to-end prototype that shows hardware-style input, backend processing, API design, storage, and dashboard visualization.
