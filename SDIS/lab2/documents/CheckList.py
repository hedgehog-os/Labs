from Document import Document
from datetime import datetime

class CheckList(Document):

    def __init__(self, id: int,
                 page_count: int,
                 author_id: int,
                 path: str,
                 checklist_items: list = None,
                 is_complete: bool = False,
                 last_checked: str = None,
                 linked_procedure_ids: dict = None,
                 title: str = None,
                 desc: str = None,
                 created_at: datetime = None, 
                 updated_at: datetime = None,
                 tags :str = None,
                 keywords: str = None,
                 language: str = None,
                 word_count: int = None,
                 confidentiality_level: str = 'public',
                 status: str = 'draft'
                 ):
        
        super().__init__(
                 id=id,
                 author_id=author_id,
                 page_count=page_count,
                 path=path,
                 title=title,
                 desc=desc,
                 created_at=created_at, 
                 updated_at=updated_at,
                 tags=tags,
                 keywords=keywords,
                 language=language,
                 word_count=word_count,
                 confidentiality_level=confidentiality_level,
                 status=status
                 )
        
        self.checklist_items = checklist_items
        self.is_complete = is_complete
        self.last_checked = last_checked
        self.linked_procedure_ids = linked_procedure_ids