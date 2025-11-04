from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.flight.route import Route
    from models.flight.aircraft import Aircraft

class FlightPlan:
    def __init__(self, route: Route, aircraft: Aircraft, cruising_altitude_ft: int, estimated_duration_min: int) -> None:
        self.route: Route = route
        self.aircraft: Aircraft = aircraft
        self.cruising_altitude_ft: int = cruising_altitude_ft
        self.estimated_duration_min: int = estimated_duration_min
