from datetime import datetime
from typing import List, Optional
from persons.ExternalExpert import ExternalExpert

class ExperimentLog:
    def __init__(self,
                 log_id: int,
                 experiment_id: int,
                 author_id: int,
                 entries: List[str],
                 created_at: Optional[datetime] = None,
                 comments: Optional[List["ExternalExpert"]] = None) -> None:
        self.log_id: int = log_id
        self.experiment_id: int = experiment_id
        self.author_id: int = author_id
        self.entries: List[str] = entries
        self.created_at: datetime = created_at or datetime.now()

        # Ассоциации
        self.comments: Optional[List["ExternalExpert"]] = comments
