from __future__ import annotations
from datetime import datetime

class Passport:
    def __init__(self, number: str, nationality: str, expiration_date: str) -> None:
        self.number: str = number
        self.nationality: str = nationality
        self.expiration_date: str = expiration_date

    def is_valid(self, current_date: str) -> bool:
        return datetime.strptime(current_date, "%Y-%m-%d") < datetime.strptime(self.expiration_date, "%Y-%m-%d")
