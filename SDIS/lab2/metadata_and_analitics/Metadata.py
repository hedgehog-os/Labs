from datetime import datetime
from typing import List, Optional

class Metadata:
    def __init__(self,
                document_id: int,
                author: str,
                created_at: datetime,
                tags: List[str],
                keywords: List[str],
                approved: bool = False,
                is_encrypted: bool = False,
                encryption_method: Optional[str] = None) -> None:
        
        self.document_id: int = document_id
        self.author: str = author
        self.created_at: datetime = created_at
        self.tags: List[str] = tags
        self.keywords: List[str] = keywords
        self.approved: bool = approved
        self.is_encrypted: bool = is_encrypted
        self.encryption_method: Optional[str] = encryption_method
