from datetime import datetime

class Annotation:
    def __init__(self, annotation_id: int, document_id: int, user_id: int, text: str, timestamp: datetime) -> None:
        self.annotation_id: int = annotation_id
        self.document_id: int = document_id
        self.user_id: int = user_id
        self.text: str = text
        self.timestamp: datetime = timestamp