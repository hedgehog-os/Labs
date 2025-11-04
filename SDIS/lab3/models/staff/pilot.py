from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.flight.flight import Flight
    from models.flight.aircraft import Aircraft

class Pilot:
    def __init__(self, name: str, license_number: str, experience_years: int) -> None:
        self.name: str = name
        self.license_number: str = license_number
        self.experience_years: int = experience_years
        self.assigned_flights: list[Flight] = []

    def assign_flight(self, flight: Flight) -> None:
        self.assigned_flights.append(flight)

    def is_certified_for(self, aircraft: Aircraft) -> bool:
        return aircraft.model in getattr(self, "certifications", [])
