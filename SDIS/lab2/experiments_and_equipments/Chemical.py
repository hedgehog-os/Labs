from typing import List, Optional
from experiments_and_equipments.Reaction import Reaction
class Chemical:
    def __init__(self,
                 chemical_id: int,
                 name: str,
                 formula: str,
                 concentration_molar: Optional[float] = None,
                 reactions: Optional[List["Reaction"]] = None) -> None:
        self.chemical_id: int = chemical_id
        self.name: str = name
        self.formula: str = formula
        self.concentration_molar: Optional[float] = concentration_molar

        # Ассоциация
        self.reactions: List["Reaction"] = reactions or []
