from typing import List, Optional
from Calibration import Calibration

class Device:
    def __init__(self, device_id: int, name: str, calibration: Optional[Calibration] = None) -> None:
        self.device_id: int = device_id
        self.name: str = name
        self.calibration: Optional[Calibration] = calibration