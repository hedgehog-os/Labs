from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.passenger.passenger import Passenger

class CustomsDeclaration:
    def __init__(self, passenger: Passenger, declared_items: list[str], total_value_usd: float) -> None:
        self.passenger: Passenger = passenger
        self.declared_items: list[str] = declared_items
        self.total_value_usd: float = total_value_usd

    def is_required(self) -> bool:
        return self.total_value_usd > 1000
