from Form import Form

from typing import List, Optional

class CheckList:
    def __init__(self,
                 checklist_id: int,
                 title: str,
                 items: List[str],
                 form: Optional["Form"] = None,
                 checklist_items: list = None,
                 is_complete: bool = False,
                 ) -> None:
        self.checklist_id: int = checklist_id
        self.title: str = title
        self.items: List[str] = items
        self.checklist_items: List[str] = checklist_items
        self.is_complete: bool = is_complete

        # Ассоциация
        self.form: Optional["Form"] = form
