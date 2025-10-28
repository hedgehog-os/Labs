from typing import List

class Insight:
    def __init__(self, insight_id: int, description: str, related_documents: List[int]) -> None:
        self.insight_id: int = insight_id
        self.description: str = description
        self.related_documents: List[int] = related_documents
