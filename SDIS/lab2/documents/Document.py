from datetime import datetime
from typing import List, Optional
from metadata_and_analitics.Metadata import Metadata
from Attachment import Attachment
from Revision import Revision
from Template import Template
from metadata_and_analitics.Comment import Comment
from metadata_and_analitics.Keyword import Keyword

class Document:

    statuses = {
        'draft', 'final', 'archived'
    }

    def __init__(self,
                 document_id: int,
                 title: str,
                 author_id: int,
                 created_at: Optional[datetime] = None,
                 tags: Optional[List[str]] = None,
                 status: str = "draft",
                 metadata: Optional["Metadata"] = None,
                 attachments: Optional[List["Attachment"]] = None,
                 revisions: Optional[List["Revision"]] = None,
                 comments: Optional[List["Comment"]] = None,
                 template: Optional["Template"] = None,
                 keywords: Optional[List["Keyword"]] = None) -> None:
        self.document_id: int = document_id
        self.title: str = title
        self.author_id: int = author_id
        self.created_at: datetime = created_at or datetime.now()
        self.tags: List[str] = tags or []
        self.status: str = status

        # Ассоциации
        self.metadata: Optional["Metadata"] = metadata
        self.attachments: List["Attachment"] = attachments or []
        self.revisions: List["Revision"] = revisions or []
        self.comments: List["Comment"] = comments or []
        self.template: Optional["Template"] = template
        self.keywords: Optional[List["Keyword"]] = keywords

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in self.statuses:
            raise ValueError(f'Недопустимый статус: {value}')
        self._status = value