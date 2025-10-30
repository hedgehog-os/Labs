from typing import List
from documents.Document import Document

class Supervisor:
    def __init__(self,
                 supervisor_id: int,
                 fullname: str,
                 email: str,
                 reviewed_documents: List[Document]) -> None:
        self.supervisor_id: int = supervisor_id
        self.fullname: str = fullname
        self.email: str = email
        self.reviewed_documents: List[Document] = reviewed_documents
