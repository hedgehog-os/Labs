from datetime import datetime
from typing import Optional, List

class Revision:
    def __init__(self,
                 revision_id: int,
                 document_id: int,
                 version_number: int,
                 editor_id: int,
                 edited_at: Optional[datetime] = None,
                 notes: Optional[str] = None,
                 previous_revision: Optional["Revision"] = None,
                 change_history: Optional[List[str]] = None) -> None:
        self.revision_id: int = revision_id
        self.document_id: int = document_id
        self.version_number: int = version_number
        self.editor_id: int = editor_id
        self.edited_at: datetime = edited_at or datetime.now()
        self.notes: Optional[str] = notes
        self.previous_revision: Optional["Revision"] = previous_revision
        self.change_history: List[str] = change_history or []
