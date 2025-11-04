from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from models.staff.pilot import Pilot
    from models.staff.flight_attendant import FlightAttendant
    from models.flight.flight import Flight

class CrewSchedule:
    def __init__(self, flight: Flight) -> None:
        self.flight: Flight = flight
        self.pilots: List[Pilot] = []
        self.attendants: List[FlightAttendant] = []

    def assign_pilot(self, pilot: Pilot) -> None:
        self.pilots.append(pilot)

    def assign_attendant(self, attendant: FlightAttendant) -> None:
        self.attendants.append(attendant)

    def is_complete(self) -> bool:
        return len(self.pilots) >= 1 and len(self.attendants) >= 2

    def get_languages(self) -> set[str]:
        return {lang for attendant in self.attendants for lang in attendant.languages}
