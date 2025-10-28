from datetime import datetime

class Comment:
    def __init__(self, comment_id: int, document_id: int, user_id: int, content: str, posted_at: datetime) -> None:
        self.comment_id: int = comment_id
        self.document_id: int = document_id
        self.user_id: int = user_id
        self.content: str = content
        self.posted_at: datetime = posted_at