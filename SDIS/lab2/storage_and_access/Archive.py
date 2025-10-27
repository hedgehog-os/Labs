from datetime import datetime
from typing import List

class Archive:
    def __init__(self, archive_id: int, name: str, documents: List[int], archived_at: datetime) -> None:
        self.archive_id: int = archive_id
        self.name: str = name
        self.documents: List[int] = documents
        self.archived_at: datetime = archived_at