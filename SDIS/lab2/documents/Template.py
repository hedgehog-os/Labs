from typing import List, Optional
from Document import Document
class Template:

    formats = {
        'md', 'xml', 'json'
    }

    def __init__(self,
                 template_id: int,
                 name: str,
                 content_structure: str,
                 applicable_documents: Optional[List["Document"]] = None) -> None:
        self.template_id: int = template_id
        self.name: str = name
        self.content_structure: str = content_structure

        # Ассоциация
        self.applicable_documents: Optional[List["Document"]] = applicable_documents

    @property
    def format(self):
        return self._format

    @format.setter
    def format(self, value):
        if value not in self.formats:
            raise ValueError(f'Недопустимый формат: {value}')
        self.format = value