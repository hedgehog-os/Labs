from typing import List, Optional
from documents.Document import Document

class Tag:

    categories = {
        'topic', 'status', 'priority'
    }

    def __init__(self,
                 tag_id: int,
                 name: str,
                 category: Optional[str] = None,
                 applied_to: Optional[List["Document"]] = None) -> None:
        self.tag_id: int = tag_id
        self.name: str = name
        self.category: Optional[str] = category

        # Ассоциация
        self.applied_to: List["Document"] = applied_to or []

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if value not in self.categories:
            raise ValueError(f'Недопустимый статус: {value}')
        self._category = value