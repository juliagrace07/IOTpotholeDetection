import random
import time
from datetime import datetime, timezone
import requests

API_URL = "http://127.0.0.1:8000/api/v1/readings"
DEVICE_ID = "vehicle-01"

def generate_reading():
    base_distance = random.uniform(11.5, 13.5)

    # Occasionally simulate a pothole
    if random.random() < 0.25:
        distance = base_distance + random.uniform(5.5, 10.0)
    else:
        distance = base_distance + random.uniform(-0.5, 0.8)

    return {
        "device_id": DEVICE_ID,
        "distance_cm": round(distance, 2),
        "latitude": round(39.758 + random.uniform(-0.02, 0.02), 6),
        "longitude": round(-84.191 + random.uniform(-0.02, 0.02), 6),
        "speed_kmph": round(random.uniform(20, 45), 2),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

if __name__ == "__main__":
    print("Sending simulated sensor data to backend...")
    for _ in range(20):
        payload = generate_reading()
        response = requests.post(API_URL, json=payload, timeout=5)
        print(response.status_code, response.json())
        time.sleep(1)
