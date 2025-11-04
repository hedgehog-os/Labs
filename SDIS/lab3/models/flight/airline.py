from __future__ import annotations

class Airline:
    def __init__(self, name: str, code: str, country: str) -> None:
        self.name: str = name
        self.code: str = code
        self.country: str = country

    def full_name(self) -> str:
        return f"{self.name} ({self.code})"
