from datetime import datetime

class Template:

    document_types = {
        'Document', 'Report', 'Protocol', 'CheckList',
        'ExperimentLog', 'Form', 'Revision'
    }

    def __init__(self,
                 path: str,
                 id: int,
                 author_id: int,
                 document_type = None,
                 default_fields: list[str] = None,
                 is_draft: bool = True,
                 title: str = None,
                 desc: str = None,
                 created_at: datetime = None, 
                 updated_at: datetime = None,
                 tags :str = None,
                 ):
        
        super().__init__(
                 id=id,
                 author_id=author_id,
                 path=path,
                 title=title,
                 desc=desc,
                 created_at=created_at, 
                 updated_at=updated_at,
                 tags=tags,
                 )

        self.document_type = document_type
        self.default_fields = default_fields
        self.is_draft = is_draft

    @property
    def document_type(self):
        return self._document_type

    @document_type.setter
    def document_type(self, value):
        if value not in self.document_types:
            raise ValueError(f'Недопустимый статус: {value}')
        self._document_type = value

