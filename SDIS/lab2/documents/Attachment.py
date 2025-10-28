from Document import Document        
from datetime import datetime
from typing import Optional

class Attachment:

    formats = {
        'pdf', 'docx', 'txt', 'md','html',
        'xlsx', 'csv', 'json', 'xml',
        'latex', 'py', 'cpp'
    }


    def __init__(self,
                 attachment_id: int,
                 filename: str,
                 filetype: str,
                 uploaded_at: Optional[datetime] = None,
                 document: Optional["Document"] = None,
                 format: str = None) -> None:
        
        self.attachment_id: int = attachment_id
        self.filename: str = filename
        self.filetype: str = filetype
        self.uploaded_at: datetime = uploaded_at or datetime.now()
        self.format: str = format

        # Ассоциация
        self.document: Optional["Document"] = document

    @property
    def format(self):
        return self._format

    @format.setter
    def format(self, value):
        if value not in self.formats:
            raise ValueError(f'Недопустимый формат: {value}')
        self.format = value