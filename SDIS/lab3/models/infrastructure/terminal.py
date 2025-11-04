from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from models.infrastructure.gate import Gate

class Terminal:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.gates: List[Gate] = []

    def add_gate(self, gate: Gate) -> None:
        self.gates.append(gate)
