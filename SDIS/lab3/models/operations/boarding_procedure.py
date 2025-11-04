from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.flight.flight import Flight
    from models.passenger.passenger import Passenger

class BoardingProcedure:
    def __init__(self, flight: Flight) -> None:
        self.flight: Flight = flight
        self.boarded_passengers: list[Passenger] = []

    def board(self, passenger: Passenger) -> None:
        self.boarded_passengers.append(passenger)

    def is_complete(self) -> bool:
        return len(self.boarded_passengers) >= len(self.flight.passengers)
