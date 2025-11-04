class ShuttleBus:
    def __init__(self, bus_id: str, route_name: str, capacity: int) -> None:
        self.bus_id: str = bus_id
        self.route_name: str = route_name
        self.capacity: int = capacity
        self.passengers_onboard: int = 0

    def board_passenger(self) -> bool:
        if self.passengers_onboard < self.capacity:
            self.passengers_onboard += 1
            return True
        return False

    def disembark_passenger(self) -> None:
        if self.passengers_onboard > 0:
            self.passengers_onboard -= 1
