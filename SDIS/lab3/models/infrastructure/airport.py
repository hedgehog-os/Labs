from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from models.infrastructure.terminal import Terminal
    from models.staff.ground_staff import GroundStaff

class Airport:
    def __init__(self, code: str, name: str, city: str, country: str) -> None:
        self.code: str = code
        self.name: str = name
        self.city: str = city
        self.country: str = country
        self.terminals: List[Terminal] = []
        self.staff: List[GroundStaff] = []

    def add_terminal(self, terminal: Terminal) -> None:
        self.terminals.append(terminal)

    def assign_staff(self, staff: GroundStaff) -> None:
        self.staff.append(staff)
