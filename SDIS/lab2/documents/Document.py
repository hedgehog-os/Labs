from datetime import datetime
class Document:
    
    statuses = {
        'draft', 'submitted', 'under_review', 'approved',
        'rejected', 'archived', 'final', 'expired', 'deleted'
    }

    confidentiality_levels = {
        'public', 'internal', 'restricted', 
        'confidential', 'secret', 'top_secret'
    }

    def __init__(path: str,
                 self, id: int,
                 author_id: int,
                 page_count: int,
                 title: str = None,
                 desc: str = None,
                 created_at: datetime = None, 
                 updated_at: datetime = None,
                 tags :str = None,
                 keywords: str = None,
                 language: str = None,
                 word_count: int = None,
                 confidentiality_level: str = 'public',
                 status: str = 'draft',
                 ):
        
        self.document_id = id
        self.title = title
        self.description = desc
        self.created_at = created_at
        self.updated_at = updated_at
        self.author_id = author_id
        self.status = status
        self.tags = tags or []
        self.keywords = keywords or []
        self.confidentiality_level = confidentiality_level
        self.language = language
        self.page_count = page_count
        self.word_count = word_count
        self.path = path

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in self.statuses:
            raise ValueError(f'Недопустимый статус: {value}')
        self._status = value

    @property
    def confidentiality_level(self):
        return self._confidential_level

    @confidentiality_level.setter
    def confidentility_level(self, value):
        if value not in self.confidentiality_levels:
            raise ValueError(f'Недопустимый уровень конфиденциальности: {value}')
        self._confidentality_level = value
