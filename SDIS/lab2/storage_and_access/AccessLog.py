from datetime import datetime
from typing import Optional

class AccessLog:

    actions = {
        'view', 'edit', 'download'
    }


    def __init__(self, user_id: int, action: str, timestamp: datetime, document_id: Optional[int] = None) -> None:
        self.user_id: int = user_id
        self.actions: str = action
        self.timestamp: datetime = timestamp
        self.document_id: Optional[int] = document_id

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        if value not in self.actions:
            raise ValueError(f'Недопустимый статус: {value}')
        self._action = value