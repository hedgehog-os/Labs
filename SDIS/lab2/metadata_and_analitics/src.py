from datetime import datetime
from typing import List, Optional

class Metadata:
    def __init__(self, document_id: int, author: str, created_at: datetime, tags: List[str], keywords: List[str]) -> None:
        self.document_id: int = document_id
        self.author: str = author
        self.created_at: datetime = created_at
        self.tags: List[str] = tags
        self.keywords: List[str] = keywords

class Tag:
    def __init__(self, name: str, category: Optional[str] = None) -> None:
        self.name: str = name
        self.category: Optional[str] = category

class Keyword:
    def __init__(self, word: str, relevance_score: float) -> None:
        self.word: str = word
        self.relevance_score: float = relevance_score

class Statistics:
    def __init__(self, document_id: int, views: int, edits: int, comments: int) -> None:
        self.document_id: int = document_id
        self.views: int = views
        self.edits: int = edits
        self.comments: int = comments

class DataSet:
    def __init__(self, dataset_id: int, name: str, source: str, records: List[dict]) -> None:
        self.dataset_id: int = dataset_id
        self.name: str = name
        self.source: str = source
        self.records: List[dict] = records

class Chart:
    def __init__(self, chart_id: int, title: str, chart_type: str, data: dict) -> None:
        self.chart_id: int = chart_id
        self.title: str = title
        self.chart_type: str = chart_type  # e.g. "bar", "line", "pie"
        self.data: dict = data

class Summary:
    def __init__(self, document_id: int, text: str, generated_at: datetime) -> None:
        self.document_id: int = document_id
        self.text: str = text
        self.generated_at: datetime = generated_at

class Insight:
    def __init__(self, insight_id: int, description: str, related_documents: List[int]) -> None:
        self.insight_id: int = insight_id
        self.description: str = description
        self.related_documents: List[int] = related_documents

class Annotation:
    def __init__(self, annotation_id: int, document_id: int, user_id: int, text: str, timestamp: datetime) -> None:
        self.annotation_id: int = annotation_id
        self.document_id: int = document_id
        self.user_id: int = user_id
        self.text: str = text
        self.timestamp: datetime = timestamp

class Comment:
    def __init__(self, comment_id: int, document_id: int, user_id: int, content: str, posted_at: datetime) -> None:
        self.comment_id: int = comment_id
        self.document_id: int = document_id
        self.user_id: int = user_id
        self.content: str = content
        self.posted_at: datetime = posted_at
