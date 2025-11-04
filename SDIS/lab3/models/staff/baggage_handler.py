from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.passenger.baggage import Baggage

class BaggageHandler:
    def __init__(self, name: str, shift: str) -> None:
        self.name: str = name
        self.shift: str = shift
        self.handled_baggage: list[Baggage] = []

    def load_baggage(self, baggage: Baggage) -> None:
        self.handled_baggage.append(baggage)
