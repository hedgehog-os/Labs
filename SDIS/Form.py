from typing import Any

class Form:

    def __init__(self, form_id: int,
                 fields: dict[str, Any] = None,
                 submitted_by: str = None,
                 submitted_at: str = None,
                 is_final: bool = False
                 ):
        
        self.fields = fields
        self.submitted_by = submitted_by
        self.submitted_at = submitted_at
        self.is_final = is_final