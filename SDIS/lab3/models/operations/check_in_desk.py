from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.passenger.passenger import Passenger

class CheckInDesk:
    def __init__(self, desk_id: str, terminal_name: str) -> None:
        self.desk_id: str = desk_id
        self.terminal_name: str = terminal_name
        self.queue: list[Passenger] = []

    def add_to_queue(self, passenger: Passenger) -> None:
        self.queue.append(passenger)

    def process_next(self) -> Passenger | None:
        return self.queue.pop(0) if self.queue else None

    def is_busy(self) -> bool:
        return len(self.queue) > 5
