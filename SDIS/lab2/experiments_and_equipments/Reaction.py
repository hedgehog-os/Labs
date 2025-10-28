from datetime import datetime
from typing import List, Optional
from experiments_and_equipments.Chemical import Chemical

class Reaction:
    def __init__(self,
                 reaction_id: int,
                 description: str,
                 reactants: Optional[List["Chemical"]] = None,
                 products: Optional[List["Chemical"]] = None,
                 conditions: Optional[str] = None,
                 recorded_at: Optional[datetime] = None) -> None:
        self.reaction_id: int = reaction_id
        self.description: str = description
        self.reactants: List["Chemical"] = reactants or []
        self.products: List["Chemical"] = products or []
        self.conditions: Optional[str] = conditions
        self.recorded_at: datetime = recorded_at or datetime.now()
