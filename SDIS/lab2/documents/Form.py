from datetime import datetime

from typing import Any

class Form:

    def __init__(self, form_id: int,
                 path: str,
                 id: int,
                 author_id: int,
                 page_count: int,
                 fields: dict[str, Any] = None,
                 submitted_by: str = None,
                 submitted_at: datetime = None,
                 is_final: bool = False,
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

        self.fields = fields
        self.submitted_by = submitted_by
        self.submitted_at = submitted_at
        self.is_final = is_final