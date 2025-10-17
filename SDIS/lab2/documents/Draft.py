from datetime import datetime

class Draft:

    def __init__(self, linked_template_ids: list[int],
                 author_id: int,
                 is_draft: bool = True,
                 created_at: datetime = None,
                 ):
        
        self.linked_template_ids = linked_template_ids
        self.author_id = author_id
        self.is_draft = is_draft
        self.created_at = created_at