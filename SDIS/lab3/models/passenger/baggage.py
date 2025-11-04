from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.passenger.passenger import Passenger

class Baggage:
    def __init__(self, tag_number: str, weight_kg: float, is_fragile: bool) -> None:
        self.tag_number: str = tag_number
        self.weight_kg: float = weight_kg
        self.is_fragile: bool = is_fragile
        self.owner: Passenger | None = None

    def assign_owner(self, passenger: Passenger) -> None:
        self.owner = passenger

    def exceeds_limit(self, limit: float) -> bool:
        return self.weight_kg > limit
