from typing import List, Optional
from experiments_and_equipments.TestCase import TestCase

class Procedure:
    def __init__(self,
                 procedure_id: int,
                 name: str,
                 steps: List[str],
                 expected_outcome: Optional[str] = None,
                 used_in: Optional[List["TestCase"]] = None) -> None:
        self.procedure_id: int = procedure_id
        self.name: str = name
        self.steps: List[str] = steps
        self.expected_outcome: Optional[str] = expected_outcome

        # Ассоциация
        self.used_in: List["TestCase"] = used_in or []
