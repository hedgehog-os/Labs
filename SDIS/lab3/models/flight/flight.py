from __future__ import annotations
from typing import List, TYPE_CHECKING
from exceptions.flight_exceptions import GateConflictException

if TYPE_CHECKING:
    from models.passenger.passenger import Passenger
    from models.flight.route import Route
    from models.flight.flight_schedule import FlightSchedule
    from models.flight.aircraft import Aircraft
    from models.flight.airline import Airline
    from models.infrastructure.gate import Gate

class Flight:
    def __init__(
        self,
        flight_number: str,
        airline: Airline,
        aircraft: Aircraft,
        route: Route,
        schedule: FlightSchedule,
        departure_gate: Gate,
        arrival_gate: Gate
    ) -> None:
        self.flight_number: str = flight_number
        self.airline: Airline = airline
        self.aircraft: Aircraft = aircraft
        self.route: Route = route
        self.schedule: FlightSchedule = schedule
        self.departure_gate: Gate = departure_gate
        self.arrival_gate: Gate = arrival_gate
        self.passengers: List[Passenger] = []

    def board_passenger(self, passenger: Passenger) -> None:
        self.passengers.append(passenger)

    def get_manifest(self) -> List[Passenger]:
        return self.passengers

    def is_full(self) -> bool:
        return len(self.passengers) >= self.aircraft.capacity

    def available_seats(self) -> int:
        return self.aircraft.capacity - len(self.passengers)

    def has_passenger(self, passport_number: str) -> bool:
        return any(p.passport.number == passport_number for p in self.passengers)

    def assign_gate(self, gate: Gate) -> None:
        if gate.current_flight and gate.current_flight != self:
            raise GateConflictException(gate.gate_number)
        self.departure_gate = gate
        gate.assign_flight(self)

    def get_passenger_by_name(self, name: str) -> Passenger | None:
        return next((p for p in self.passengers if p.full_name == name), None)
