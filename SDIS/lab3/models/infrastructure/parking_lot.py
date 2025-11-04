class ParkingLot:
    def __init__(self, lot_id: str, capacity: int) -> None:
        self.lot_id: str = lot_id
        self.capacity: int = capacity
        self.occupied: int = 0

    def park_vehicle(self) -> bool:
        if self.occupied < self.capacity:
            self.occupied += 1
            return True
        return False

    def release_vehicle(self) -> None:
        if self.occupied > 0:
            self.occupied -= 1
