from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.passenger.ticket import Ticket
    from models.passenger.passenger import Passenger

class BoardingPass:
    def __init__(self, ticket: Ticket, passenger: Passenger, gate_number: str) -> None:
        self.ticket: Ticket = ticket
        self.passenger: Passenger = passenger
        self.gate_number: str = gate_number
        self.is_scanned: bool = False

    def scan(self) -> None:
        self.is_scanned = True
