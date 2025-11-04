from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.flight.aircraft import Aircraft

class MaintenanceTechnician:
    def __init__(self, name: str, specialization: str) -> None:
        self.name: str = name
        self.specialization: str = specialization

    def inspect_aircraft(self, aircraft: Aircraft) -> str:
        return f"{self.name} inspected aircraft {aircraft.registration_number} ({aircraft.model})"
