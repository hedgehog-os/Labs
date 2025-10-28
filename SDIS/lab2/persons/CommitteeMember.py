from documents.Report import Report
from datetime import datetime
from typing import Optional, List

class CommitteeMember:

    roles = {
        'chair', 'reviewer', 'observer', 'secretary'
    }

    def __init__(self,
                 member_id: int,
                 full_name: str,
                 role: Optional[str] = None,
                 evaluated_reports: Optional[List["Report"]] = None,
                 evaluation_notes: Optional[List[str]] = None,
                 last_evaluation_date: Optional[datetime] = None) -> None:
        self.member_id: int = member_id
        self.full_name: str = full_name
        self.role: Optional[str] = role
        self.evaluated_reports: List["Report"] = evaluated_reports or []
        self.evaluation_notes: List[str] = evaluation_notes or []
        self.last_evaluation_date: Optional[datetime] = last_evaluation_date

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        if value not in self.roles:
            raise ValueError(f'Недопустимый статус: {value}')
        self._role = value