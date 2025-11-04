from __future__ import annotations

class FlightSchedule:
    def __init__(self, departure_time: str, arrival_time: str, is_recurring: bool = False) -> None:
        self.departure_time: str = departure_time
        self.arrival_time: str = arrival_time
        self.is_recurring: bool = is_recurring

    def duration_minutes(self) -> int:
        from datetime import datetime
        fmt = "%Y-%m-%d %H:%M"
        dep = datetime.strptime(self.departure_time, fmt)
        arr = datetime.strptime(self.arrival_time, fmt)
        return int((arr - dep).total_seconds() // 60)

    def overlaps_with(self, other: FlightSchedule) -> bool:
        from datetime import datetime
        fmt = "%Y-%m-%d %H:%M"
        dep1 = datetime.strptime(self.departure_time, fmt)
        arr1 = datetime.strptime(self.arrival_time, fmt)
        dep2 = datetime.strptime(other.departure_time, fmt)
        arr2 = datetime.strptime(other.arrival_time, fmt)
        return max(dep1, dep2) < min(arr1, arr2)
