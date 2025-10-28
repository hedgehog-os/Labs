from typing import List, Optional
from Measurement import Measurement
from experiments_and_equipments.Procedure import Procedure
from datetime import datetime

class TestCase:
    def __init__(self,
                 testcase_id: int,
                 name: str,
                 description: str,
                 created_at: Optional[datetime] = None,
                 procedure: Optional["Procedure"] = None,
                 measurements: Optional[List[Measurement]] = None) -> None:
        self.testcase_id: int = testcase_id
        self.name: str = name
        self.description: str = description
        self.created_at: datetime = created_at or datetime.now()

        # Ассоциация
        self.procedure: Optional["Procedure"] = procedure
        self.measurements: Optional[List[Measurement]] = measurements