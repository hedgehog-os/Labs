from datetime import datetime

class Summary:
    def __init__(self, document_id: int, text: str, generated_at: datetime) -> None:
        self.document_id: int = document_id
        self.text: str = text
        self.generated_at: datetime = generated_at