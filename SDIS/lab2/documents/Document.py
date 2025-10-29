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
        
    def submit(self) -> None:
        if self.status != "draft":
            raise ValueError("Документ уже отправлен или архивирован.")
        self.status = "final"

    def revise(self, revision: "Revision") -> None:
        self.revisions.append(revision)
        self.status = "draft"

    def archive(self) -> None:
        if self.status == "archived":
            raise ValueError("Документ уже в архиве.")
        self.status = "archived"

    def restore(self) -> None:
        if self.status != "archived":
            raise ValueError("Можно восстановить только архивированный документ.")
        self.status = "final"
    
    def add_tag(self, tag: str) -> None:
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag: str) -> None:
        if tag in self.tags:
            self.tags.remove(tag)

    def add_keyword(self, keyword: "Keyword") -> None:
        if self.keywords is None:
            self.keywords = []
        self.keywords.append(keyword)

    def remove_keyword(self, keyword: "Keyword") -> None:
        if self.keywords and keyword in self.keywords:
            self.keywords.remove(keyword)

    def approve(self) -> None:
        if self.status != "final":
            raise ValueError("Можно утвердить только финальный документ.")
        if self.metadata:
            self.metadata.approved = True

    def reject(self, reason: str) -> None:
        self.comments.append(Comment(
            comment_id=len(self.comments) + 1,
            document_id=self.document_id,
            user_id=self.author_id,
            content=f"Отклонено: {reason}",
            posted_at=datetime.now()
        ))
        self.status = "draft"

    def encrypt(self, method: str = "AES-256") -> None:
        if self.metadata:
            self.metadata.is_encrypted = True
            self.metadata.encryption_method = method

    def decrypt(self) -> None:
        if self.metadata and self.metadata.is_encrypted:
            self.metadata.is_encrypted = False
            self.metadata.encryption_method = None
