from datetime import datetime
from typing import Optional, List
from persons.Reviewer import Reviewer
class Draft:
    def __init__(self,
                 draft_id: int,
                 title: str,
                 author_id: int,
                 content: str,
                 created_at: Optional[datetime] = None,
                 reviewed_by: Optional[List["Reviewer"]] = None) -> None:
        self.draft_id: int = draft_id
        self.title: str = title
        self.author_id: int = author_id
        self.content: str = content
        self.created_at: datetime = created_at or datetime.now()

        # Ассоциация
        self.reviewed_by: Optional[List["Reviewer"]] = reviewed_by
