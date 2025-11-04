from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.flight.flight import Flight

class FlightAttendant:
    def __init__(self, name: str, languages: list[str]) -> None:
        self.name: str = name
        self.languages: list[str] = languages
        self.assigned_flights: list[Flight] = []

    def assign_to_flight(self, flight: Flight) -> None:
        self.assigned_flights.append(flight)
