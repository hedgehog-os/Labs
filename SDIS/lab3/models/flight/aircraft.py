from __future__ import annotations

class Aircraft:
    def __init__(self, model: str, registration_number: str, capacity: int) -> None:
        self.model: str = model
        self.registration_number: str = registration_number
        self.capacity: int = capacity

    def is_valid_registration(self) -> bool:
        return self.registration_number.startswith("N") or self.registration_number[:2].isalpha()
