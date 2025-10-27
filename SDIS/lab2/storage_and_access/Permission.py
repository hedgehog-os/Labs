class Permission:
    def __init__(self, user_id: int, document_id: int, can_view: bool, can_edit: bool, can_delete: bool) -> None:
        self.user_id: int = user_id
        self.document_id: int = document_id
        self.can_view: bool = can_view
        self.can_edit: bool = can_edit
        self.can_delete: bool = can_delete