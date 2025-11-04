from __future__ import annotations
from exceptions.ticket_exceptions import TicketAlreadyCheckedInException
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.flight.flight import Flight

class Ticket:
    def __init__(self, ticket_id: str, flight: Flight, seat: str, price: float) -> None:
        self.ticket_id: str = ticket_id
        self.flight: Flight = flight
        self.seat: str = seat
        self.price: float = price
        self.is_checked_in: bool = False

    def check_in(self) -> None:
        self.is_checked_in = True
    
    def check_in(self) -> None:
        if self.is_checked_in:
            raise TicketAlreadyCheckedInException(self.ticket_id)
        self.is_checked_in = True