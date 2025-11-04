from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.infrastructure.airport import Airport

class GroundStaff:
    def __init__(self, name: str, role: str, airport: Airport) -> None:
        self.name: str = name
        self.role: str = role
        self.airport: Airport = airport
