from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.passenger.passenger import Passenger

class SecurityOfficer:
    def __init__(self, name: str, badge_id: str) -> None:
        self.name: str = name
        self.badge_id: str = badge_id

    def inspect_passenger(self, passenger: Passenger) -> str:
        return f"Security check completed for {passenger.full_name}"
