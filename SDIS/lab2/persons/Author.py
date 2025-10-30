from datetime import datetime

class Author:
    def __init__(self,
                 author_id: int,
                 fullname: str,
                 email: str,
                 document_id: int,
                 created_at: datetime) -> None:
        self.author_id: int = author_id
        self.fullname: str = fullname
        self.email: str = email
        self.document_id: int = document_id
        self.created_at: datetime = created_at
