from datetime import datetime
from typing import List

class Metadata:
    def __init__(self, document_id: int, author: str, created_at: datetime, tags: List[str], keywords: List[str]) -> None:
        self.document_id: int = document_id
        self.author: str = author
        self.created_at: datetime = created_at
        self.tags: List[str] = tags
        self.keywords: List[str] = keywords