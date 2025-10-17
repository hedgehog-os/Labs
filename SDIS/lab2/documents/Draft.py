from datetime import datetime
from Document import Document
from datetime import datetime

class Draft(Document):

    def __init__(self, linked_template_ids: list[int],
                 id: int,
                 path: str,
                 author_id: int,
                 page_count: int,
                 created_at: datetime = None, 
                 is_draft: bool = True,
                 title: str = None,
                 desc: str = None,
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
        
        self.linked_template_ids = linked_template_ids
        self.author_id = author_id
        self.is_draft = is_draft
        self.created_at = created_at