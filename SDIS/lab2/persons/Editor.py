from Person import Person
from documents.Document import Document
from datetime import datetime

class Editor(Person):
    
    def __init__(self, id: int,
                 edtor_notes: str,
                 revision_number: int,
                 chnge_history: str
                 ):
        
        super().__init__(id=id)

        self.edtor_notes = edtor_notes
        self.revision_number = revision_number
        self.chnge_history = chnge_history

        
    