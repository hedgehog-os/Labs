from typing import Optional, List
from storage_and_access.Backup import Backup
class Encryption:

    methods = {
        "AES", "RSA", "ChaCha20"
    }

    algorithms = {
        "CBC", "GCM", "OAEP"
    }

    def __init__(self,
                 encryption_id: int,
                 method: str,
                 key_length: int,
                 algorithm: str,
                 applied_to: Optional[List["Backup"]] = None) -> None:
        self.encryption_id: int = encryption_id
        self.method: str = method
        self.key_length: int = key_length
        self.algorithm: str = algorithm

        # Ассоциация
        self.applied_to: List["Backup"] = applied_to or []

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, value):
        if value not in self.methods:
            raise ValueError(f'Недопустимый формат: {value}')
        self._method = value

    @property
    def algorithm(self):
        return self._algorithm

    @algorithm.setter
    def algorithm(self, value):
        if value not in self.algorithms:
            raise ValueError(f'Недопустимый формат: {value}')
        self._algorithm = value