# IOTpotholeDetection
IoT-Based Pothole Detection System

An end-to-end IoT system designed to detect potholes using sensor data and real-time backend processing, with a scalable API architecture and dashboard visualization.

 Overview

This project simulates a real-world IoT system where:

Ultrasonic sensors measure road surface variations
GPS modules capture location data
A backend API processes incoming data
Potholes are detected using threshold-based logic
Results are stored and visualized via a dashboard

 System Architecture
Ultrasonic Sensor + GPS
          ↓
   Microcontroller / Device
          ↓
   REST API (FastAPI Backend)
          ↓
   Detection Logic + Data Pipeline
          ↓
   Database Storage (SQLite)
          ↓
   Dashboard Interface
 Key Features
 Real-time sensor data ingestion via REST APIs
 GPS-based pothole location tracking
 Threshold-based detection algorithm
 Rolling baseline computation for accuracy
 Structured data storage using SQLAlchemy
 Dashboard to visualize detected potholes
 Dockerized backend for easy deployment
 Detection Logic

A pothole is detected when:

deviation = current_distance - baseline_distance

if deviation >= threshold:
    pothole_detected = True
Baseline = rolling average of previous readings
Threshold = configurable (default: 5 cm)

 API Endpoints
POST /api/v1/readings

Send sensor + GPS data

{
  "device_id": "vehicle-01",
  "distance_cm": 20.5,
  "latitude": 39.7817,
  "longitude": -84.1052,
  "speed_kmph": 32.5,
  "timestamp": "2026-03-24T15:30:00"
}
GET /api/v1/potholes

Retrieve detected potholes

GET /api/v1/readings

Retrieve all sensor data

🛠️ Tech Stack
Backend: FastAPI
Database: SQLite + SQLAlchemy
Simulation: Python
Deployment: Docker, Uvicorn
Frontend: HTML (Jinja templates)

Running the Project
Local Setup
pip install -r requirements.txt
uvicorn backend.app:app --reload
Run Sensor Simulator
python simulator/sensor_simulator.py
Docker
docker compose up --build
 Key Learnings
Designed scalable backend APIs for IoT systems
Built data pipelines for real-time sensor processing
Implemented detection algorithms for noisy sensor data
Debugged system-level integration issues
Learned how to connect hardware-driven data with software systems
 Future Improvements
Machine learning-based pothole detection
Real-time streaming using Kafka/WebSockets
Map-based visualization (Google Maps API)
Edge computing for faster detection
