from typing import List

class LabAssistant:
    def __init__(self,
                 assistant_id: int,
                 fullname: str,
                 email: str,
                 position: str,
                 lab_room: int,
                 equipment_list: List[str] | None = None) -> None:
        self.assistant_id: int = assistant_id
        self.fullname: str = fullname
        self.email: str = email
        self.position: str = position
        self.lab_room: int = lab_room
        self.equipment_list: List[str] = equipment_list or []
