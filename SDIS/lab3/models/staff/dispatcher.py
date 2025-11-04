from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.flight.flight import Flight

class Dispatcher:
    def __init__(self, name: str, dispatch_id: str) -> None:
        self.name: str = name
        self.dispatch_id: str = dispatch_id

    def dispatch_flight(self, flight: Flight) -> str:
        return f"Dispatcher {self.name} dispatched flight {flight.flight_number}"
