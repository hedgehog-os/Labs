from typing import List, Optional
from Measurement import Measurement

class TestCase:
    def __init__(self, case_id: int, description: str, measurements: Optional[List[Measurement]] = None) -> None:
        self.case_id: int = case_id
        self.description: str = description
        self.measurements: List[Measurement] = measurements or []