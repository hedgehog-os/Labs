from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.flight.aircraft import Aircraft

class FuelRecord:
    def __init__(self, aircraft: Aircraft, fuel_liters: float, timestamp: str) -> None:
        self.aircraft: Aircraft = aircraft
        self.fuel_liters: float = fuel_liters
        self.timestamp: str = timestamp
