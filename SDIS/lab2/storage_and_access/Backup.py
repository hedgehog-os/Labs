from datetime import datetime
from typing import Optional
from storage_and_access.Encryption import Encryption
from experiments_and_equipments.StorageDevice import StorageDevice

class Backup:
    def __init__(self,
                 backup_id: int,
                 location: str,
                 timestamp: Optional[datetime] = None,
                 size_mb: Optional[float] = None,
                 encrypted_with: Optional["Encryption"] = None,
                 storage_device: Optional["StorageDevice"] = None) -> None:
        self.backup_id: int = backup_id
        self.location: str = location
        self.timestamp: datetime = timestamp or datetime.now()
        self.size_mb: Optional[float] = size_mb

        # Ассоциации
        self.encrypted_with: Optional["Encryption"] = encrypted_with
        self.storage_device: Optional["StorageDevice"] = storage_device
