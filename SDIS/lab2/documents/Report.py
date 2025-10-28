from datetime import datetime
from typing import List, Optional
from persons.CommitteeMember import CommitteeMember
from metadata_and_analitics.Chart import Chart
from metadata_and_analitics.Summary import Summary

class Report:
    def __init__(self,
                 report_id: int,
                 title: str,
                 author_id: int,
                 created_at: Optional[datetime] = None,
                 charts: Optional[List["Chart"]] = None,
                 summary: Optional["Summary"] = None,
                 reviewed_by: Optional[List["CommitteeMember"]] = None) -> None:
        self.report_id: int = report_id
        self.title: str = title
        self.author_id: int = author_id
        self.created_at: datetime = created_at or datetime.now()

        # Ассоциации
        self.charts: List["Chart"] = charts or []
        self.summary: Optional["Summary"] = summary
        self.reviewed_by: Optional[List["CommitteeMember"]] = reviewed_by
