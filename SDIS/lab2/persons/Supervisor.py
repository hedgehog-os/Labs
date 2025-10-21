from Person import Person
from documents.Document import Document

class Supervisor(Person):

    def __init__(self, student_id: int,
                 fullname: str,
                 email: str,
                 reviewed_documents: list[Document],
                 supervisor_id: int
                 ):
        
        super().__init__(id=student_id,
                         fullname=fullname,
                         email=email
                         )
        
        self.reviewed_documents  = reviewed_documents
        self.supervisor_id = supervisor_id