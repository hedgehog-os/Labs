class Template:

    document_types = {
        'Document', 'Report', 'Protocol', 'CheckList',
        'ExperimentLog', 'Form', 'Revision'
    }

    def __init__(self,
                 template_id: int,
                 document_type = None,
                 default_fields: list[str] = None,
                 is_draft: bool = True
                 ):
        
        self.document_type = document_type
        self.template_id = template_id
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

