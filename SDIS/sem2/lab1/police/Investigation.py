from __future__ import annotations

import random

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Crime import Crime

# Получает список Crime и решает кто из граждан виновен, в результате создает tuple с Crime и его опасностью
class Investigation:
    def __init__(self, crime: Crime):
        self._crime: list[Crime] = crime
    
    def investigate(self) -> tuple:
        for crime in self._crime:
            
            weights = [crime.severity / 5.0, 1 - crime.severity / 5.0]
            guilt = random.choices([True, False], weights=weights)[0]
            if guilt:
                criminal = ((crime.suspect, crime.law._severity))
                return criminal
            
