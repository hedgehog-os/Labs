from Person import Person
from datetime import datetime
from typing import Dict

class Observer(Person):
  
    def __init__(self, id: int,
                 access_logs: Dict[str, datetime],
                 last_accessed: datetime
                 ):
        
        super().__init__(id=id)

        self.access_logs = access_logs
        self.last_accessed = last_accessed