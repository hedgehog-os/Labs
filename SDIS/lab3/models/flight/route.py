from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.infrastructure.airport import Airport

class Route:
    def __init__(self, origin: Airport, destination: Airport, distance_km: float) -> None:
        self.origin: Airport = origin
        self.destination: Airport = destination
        self.distance_km: float = distance_km

    def is_international(self) -> bool:
        return self.origin.country != self.destination.country
