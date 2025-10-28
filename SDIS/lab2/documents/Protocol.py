from datetime import datetime
from typing import List, Optional
from persons.Supervisor import Supervisor
class Protocol:
    def __init__(self,
                 protocol_id: int,
                 title: str,
                 author_id: int,
                 created_at: Optional[datetime] = None,
                 steps: Optional[List[str]] = None,
                 reviewed_by: Optional[List["Supervisor"]] = None) -> None:
        self.protocol_id: int = protocol_id
        self.title: str = title
        self.author_id: int = author_id
        self.created_at: datetime = created_at or datetime.now()
        self.steps: List[str] = steps or []

        # Ассоциации
        self.reviewed_by: Optional[List["Supervisor"]] = reviewed_by
