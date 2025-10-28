class Statistics:
    def __init__(self, document_id: int, views: int, edits: int, comments: int) -> None:
        self.document_id: int = document_id
        self.views: int = views
        self.edits: int = edits
        self.comments: int = comments