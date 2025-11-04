from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.passenger.passenger import Passenger

class SecurityCheck:
    def __init__(self, checkpoint_id: str) -> None:
        self.checkpoint_id: str = checkpoint_id
        self.checked_passengers: list[str] = []

    def perform_check(self, passenger: Passenger) -> str:
        self.checked_passengers.append(passenger.full_name)
        return f"Passenger {passenger.full_name} cleared at checkpoint {self.checkpoint_id}"

    def has_been_checked(self, passenger: Passenger) -> bool:
        return passenger.full_name in self.checked_passengers
