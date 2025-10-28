from typing import List, Optional
from storage_and_access.Backup import Backup

class StorageDevice:

    device_types = {
        "HDD", "SSD", "Cloud"
    }

    def __init__(self,
                 device_id: int,
                 name: str,
                 device_type: str,
                 capacity_mb: float,
                 location: Optional[str] = None,
                 backups: Optional[List["Backup"]] = None) -> None:
        
        self.device_id: int = device_id
        self.name: str = name
        self.device_type: str = device_type
        self.capacity_mb: float = capacity_mb
        self.location: Optional[str] = location

        # Ассоциация
        self.backups: List["Backup"] = backups or []

    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        if value not in self.device_types:
            raise ValueError(f'Недопустимый формат: {value}')
        self._device_type = value