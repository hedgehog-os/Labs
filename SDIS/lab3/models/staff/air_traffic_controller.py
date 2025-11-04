from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.flight.flight import Flight

class AirTrafficController:
    def __init__(self, name: str, control_tower_id: str) -> None:
        self.name: str = name
        self.control_tower_id: str = control_tower_id
        self.active_flights: list[Flight] = []

    def authorize_takeoff(self, flight: Flight) -> str:
        self.active_flights.append(flight)
        return f"Flight {flight.flight_number} authorized for takeoff by {self.name}"

    def release_flight(self, flight: Flight) -> None:
        self.active_flights = [f for f in self.active_flights if f != flight]
