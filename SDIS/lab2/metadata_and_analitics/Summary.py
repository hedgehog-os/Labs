from documents.Report import Report
from datetime import datetime
from typing import Optional

class Summary:
    def __init__(self,
                 summary_id: int,
                 content: str,
                 generated_at: Optional[datetime] = None,
                 report: Optional["Report"] = None) -> None:
        self.summary_id: int = summary_id
        self.content: str = content
        self.generated_at: datetime = generated_at or datetime.now()

        # Ассоциация
        self.report: Optional["Report"] = report
