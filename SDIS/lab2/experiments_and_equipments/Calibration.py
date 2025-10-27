from datetime import datetime

class Calibration:
    def __init__(self, calibration_id: int, date: datetime, technician: str, notes: str) -> None:
        self.calibration_id: int = calibration_id
        self.date: datetime = date
        self.technician: str = technician
        self.notes: str = notes