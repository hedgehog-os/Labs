from datetime import datetime
from typing import Dict

class Observer:
    def __init__(self,
                 observer_id: int,
                 fullname: str,
                 email: str,
                 access_logs: Dict[str, datetime],
                 last_accessed: datetime) -> None:
        self.observer_id: int = observer_id
        self.fullname: str = fullname
        self.email: str = email
        self.access_logs: Dict[str, datetime] = access_logs
        self.last_accessed: datetime = last_accessed
