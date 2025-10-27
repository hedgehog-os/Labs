from datetime import datetime
from typing import List

class Backup:

    locations = {
        'view', 'edit', 'download'
    }

    def __init__(self, backup_id: int, created_at: datetime, included_documents: List[int], location: str) -> None:
        self.backup_id: int = backup_id
        self.created_at: datetime = created_at
        self.included_documents: List[int] = included_documents
        self.location: str = location
    
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if value not in self.locations:
            raise ValueError(f'Недопустимый статус: {value}')
        self._location = value

    