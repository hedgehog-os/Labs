class CheckList:

    def __init__(self, checklist_items: list = None,
                 is_complete: bool = False,
                 last_checked: str = None,
                 linked_procedure_ids: dict = None
                 ):
        
        self.checklist_items = checklist_items
        self.is_complete = is_complete
        self.last_checked = last_checked
        self.linked_procedure_ids = linked_procedure_ids