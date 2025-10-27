from typing import List, Optional
from Device import Device

class LabRoom:
    def __init__(self, room_number: str, equipment: Optional[List[Device]] = None) -> None:
        self.room_number: str = room_number
        self.equipment: List[Device] = equipment or []