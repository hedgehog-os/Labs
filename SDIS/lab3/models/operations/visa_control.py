from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.passenger.passenger import Passenger
    from models.passenger.visa import Visa

class VisaControl:
    def __init__(self, country: str) -> None:
        self.country: str = country

    def verify(self, passenger: Passenger) -> bool:
        for visa in getattr(passenger, "visas", []):
            if visa.country == self.country and visa.is_valid("2025-11-04"):
                return True
        return False
