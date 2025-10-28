from datetime import datetime
from typing import List, Optional
from CheckList import CheckList

class Form:
    def __init__(self,
                 form_id: int,
                 title: str,
                 author_id: int,
                 created_at: Optional[datetime] = None,
                 fields: Optional[List[str]] = None,
                 checklist: Optional["CheckList"] = None) -> None:
        self.form_id: int = form_id
        self.title: str = title
        self.author_id: int = author_id
        self.created_at: datetime = created_at or datetime.now()
        self.fields: List[str] = fields or []

        # Ассоциация
        self.checklist: Optional["CheckList"] = checklist
