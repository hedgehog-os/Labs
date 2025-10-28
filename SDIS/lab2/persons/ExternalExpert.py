from datetime import datetime
from typing import List, Optional
from documents.ExperimentLog import ExperimentLog

class ExternalExpert:
    def __init__(self,
                 expert_id: int,
                 full_name: str,
                 field_of_expertise: Optional[str] = None,
                 comments: Optional[List[str]] = None,
                 commented_logs: Optional[List["ExperimentLog"]] = None,
                 last_commented_at: Optional[datetime] = None) -> None:
        self.expert_id: int = expert_id
        self.full_name: str = full_name
        self.field_of_expertise: Optional[str] = field_of_expertise
        self.comments: List[str] = comments or []
        self.commented_logs: List["ExperimentLog"] = commented_logs or []
        self.last_commented_at: Optional[datetime] = last_commented_at
