from __future__ import annotations
from datetime import datetime

class Visa:
    def __init__(self, country: str, visa_type: str, expiration_date: str) -> None:
        self.country: str = country
        self.visa_type: str = visa_type
        self.expiration_date: str = expiration_date

    def is_valid(self, current_date: str) -> bool:
        return datetime.strptime(current_date, "%Y-%m-%d") < datetime.strptime(self.expiration_date, "%Y-%m-%d")
