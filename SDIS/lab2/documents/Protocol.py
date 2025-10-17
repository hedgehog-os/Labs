from datetime import datetime

class Protocol:

    def __init__(self, path: str,
                 id: int,
                 author_id: int,
                 page_count: int,
                 procedure_steps: list[str] = None,
                 safety_protocol: str = None,
                 approval_date: datetime = None,
                 expiration_date: datetime = None,
                 linked_experiment_ids: list[int] = None,
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

        self.procedure_steps = procedure_steps
        self.safety_protocol = safety_protocol
        self.approval_date = approval_date
        self.expiration_date = expiration_date
        self.linked_experiment_ids = linked_experiment_ids