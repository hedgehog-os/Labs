from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.infrastructure.terminal import Terminal
    from models.flight.flight import Flight

class Gate:
    def __init__(self, gate_number: str, terminal: Terminal) -> None:
        self.gate_number: str = gate_number
        self.terminal: Terminal = terminal
        self.current_flight: Flight | None = None

    def assign_flight(self, flight: Flight) -> None:
        self.current_flight = flight
