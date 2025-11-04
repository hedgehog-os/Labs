from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.passenger.passenger import Passenger

class CustomsOfficer:
    def __init__(self, name: str, officer_id: str) -> None:
        self.name: str = name
        self.officer_id: str = officer_id

    def inspect_passenger(self, passenger: Passenger) -> str:
        return f"Customs inspection completed for {passenger.full_name}"
