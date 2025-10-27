from datetime import datetime
from typing import List, Optional
from Procedure import Procedure
from TestCase import TestCase

class Experiment:
    def __init__(self, experiment_id: int, title: str, procedure: Procedure, start_date: Optional[datetime] = None) -> None:
        self.experiment_id: int = experiment_id
        self.title: str = title
        self.procedure: Procedure = procedure
        self.start_date: datetime = start_date or datetime.now()
        self.test_cases: List[TestCase] = []