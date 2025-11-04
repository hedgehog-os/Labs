from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.flight.aircraft import Aircraft
    from models.staff.maintenance_technician import MaintenanceTechnician

class MaintenanceLog:
    def __init__(self, aircraft: Aircraft, technician: MaintenanceTechnician, notes: str, timestamp: str) -> None:
        self.aircraft: Aircraft = aircraft
        self.technician: MaintenanceTechnician = technician
        self.notes: str = notes
        self.timestamp: str = timestamp
