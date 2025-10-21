from Person import Person
from documents.Document import Document
from datetime import datetime

class ComitteeMember(Person):
    
    roles = {
        'chair', 'reviewer', 'observer', 'secretary'
    }

    def __init__(self, id: int,
                 role: str,
                 assigned_documents: list[Document] = None,
                 approval_date: datetime = None
                 ):
        
        super().__init__(id=id)

        self.role = role
        self.assigned_documents = assigned_documents
        self.approval_date = approval_date
        
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        if value not in self.roles:
            raise ValueError(f'Недопустимый статус: {value}')
        self._role = value