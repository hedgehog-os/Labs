class Elevator:
    def __init__(self, elevator_id: str, max_floor: int) -> None:
        self.elevator_id: str = elevator_id
        self.max_floor: int = max_floor
        self.current_floor: int = 0

    def move_to_floor(self, floor: int) -> bool:
        if 0 <= floor <= self.max_floor:
            self.current_floor = floor
            return True
        return False
