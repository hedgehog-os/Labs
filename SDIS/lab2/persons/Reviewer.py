from datetime import datetime
from typing import List, Optional
from documents.Draft import Draft

class Reviewer:
    def __init__(self,
                 reviewer_id: int,
                 full_name: str,
                 affiliation: Optional[str] = None,
                 reviewed_drafts: Optional[List["Draft"]] = None,
                 comments: Optional[List[str]] = None,
                 last_reviewed_at: Optional[datetime] = None) -> None:
        self.reviewer_id: int = reviewer_id
        self.full_name: str = full_name
        self.affiliation: Optional[str] = affiliation
        self.reviewed_drafts: List["Draft"] = reviewed_drafts or []
        self.comments: List[str] = comments or []
        self.last_reviewed_at: Optional[datetime] = last_reviewed_at
