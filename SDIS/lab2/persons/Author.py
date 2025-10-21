from Person import Person
from datetime import datetime

class Author(Person):
  
    def __init__(self, id: int,
                 fullname: str,
                 document_id: int,
                 created_at: datetime
                 ):
        
        super().__init__(id=id,
                         fullname=fullname)

        self.document_id = document_id
        self.created_at = created_at