from collections import defaultdict, deque

WINDOW_SIZE = 5
POTHOLE_THRESHOLD_CM = 5.0

class RollingBaselineDetector:
    def __init__(self, window_size: int = WINDOW_SIZE, threshold_cm: float = POTHOLE_THRESHOLD_CM):
        self.window_size = window_size
        self.threshold_cm = threshold_cm
        self.history = defaultdict(lambda: deque(maxlen=self.window_size))

    def evaluate(self, device_id: str, distance_cm: float) -> tuple[float, float, bool]:
        readings = self.history[device_id]

        if readings:
            baseline = sum(readings) / len(readings)
        else:
            baseline = distance_cm

        deviation = distance_cm - baseline
        pothole_detected = deviation >= self.threshold_cm

        readings.append(distance_cm)
        return round(baseline, 2), round(deviation, 2), pothole_detected
