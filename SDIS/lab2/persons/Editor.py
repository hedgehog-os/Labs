class Editor:
    def __init__(self,
                 editor_id: int,
                 fullname: str,
                 email: str,
                 editor_notes: str,
                 revision_number: int,
                 change_history: str) -> None:
        self.editor_id: int = editor_id
        self.fullname: str = fullname
        self.email: str = email
        self.editor_notes: str = editor_notes
        self.revision_number: int = revision_number
        self.change_history: str = change_history
