from __future__ import annotations
from exceptions import InvalidPassportException
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from models.passenger.passport import Passport
    from models.passenger.ticket import Ticket
    from models.passenger.baggage import Baggage
    from models.passenger.visa import Visa

class Passenger:
    def __init__(self, full_name: str, passport: Passport, ticket: Ticket) -> None:
        self.full_name: str = full_name
        self.passport: Passport = passport
        self.ticket: Ticket = ticket
        self.baggage: List[Baggage] = []

    def add_baggage(self, item: Baggage) -> None:
        self.baggage.append(item)

    def total_baggage_weight(self) -> float:
        return sum(b.weight_kg for b in self.baggage)

    def validate_passport(self, current_date: str) -> None:
        if not self.passport.is_valid(current_date):
            raise InvalidPassportException(self.passport.number)
        
    def add_visa(self, visa: Visa) -> None:
        if not hasattr(self, "visas"):
            self.visas: list[Visa] = []
        self.visas.append(visa)

    def has_valid_visa_for(self, country: str, date: str) -> bool:
        return any(v.country == country and v.is_valid(date) for v in getattr(self, "visas", []))
