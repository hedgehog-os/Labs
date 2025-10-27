from datetime import datetime
from typing import Optional
from Sensor import Sensor

class Measurement:
    def __init__(self, value: float, unit: str, timestamp: Optional[datetime] = None, sensor: Optional[Sensor] = None) -> None:
        self.value: float = value
        self.unit: str = unit
        self.timestamp: datetime = timestamp or datetime.now()
        self.sensor: Optional[Sensor] = sensor