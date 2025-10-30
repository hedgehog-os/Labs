from datetime import datetime
from typing import List, Dict
from persons.UserProfile import UserProfile
from typing import Optional
class Student:
    def __init__(self,
                 student_id: int,
                 fullname: str,
                 email: str,
                 department: str,
                 assigned_documents: List[int] | None = None,
                 activity_log: Dict[str, datetime] | None = None,
                 profile: Optional["UserProfile"] = None) -> None:
        self.student_id: int = student_id
        self.fullname: str = fullname
        self.email: str = email
        self.department: str = department
        self.assigned_documents: List[int] = assigned_documents or []
        self.activity_log: Dict[str, datetime] = activity_log or {}

        # Ассоциация
        self.profile: Optional['UserProfile'] = profile