from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.infrastructure.restroom import Restroom
    from models.infrastructure.lounge import Lounge

class CleaningCrew:
    def __init__(self, crew_id: str, shift: str) -> None:
        self.crew_id: str = crew_id
        self.shift: str = shift

    def clean_restroom(self, restroom: Restroom) -> None:
        restroom.clean()

    def clean_lounge(self, lounge: Lounge) -> None:
        lounge.is_clean = True
