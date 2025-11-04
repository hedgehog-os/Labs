class Lounge:
    def __init__(self, name: str, capacity: int, is_vip: bool = False) -> None:
        self.name: str = name
        self.capacity: int = capacity
        self.is_vip: bool = is_vip
        self.current_occupancy: int = 0

    def admit_guest(self) -> bool:
        if self.current_occupancy < self.capacity:
            self.current_occupancy += 1
            return True
        return False
