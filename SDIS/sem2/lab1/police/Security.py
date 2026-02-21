from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Crime import Crime
    from .Citizen import Citizen

class Security:
    def __init__(self):
        self.level: int = 1

    def eval(self, citizens: list[Citizen], crimes: list[Crime]):
        return len(citizens) / len(crimes)
