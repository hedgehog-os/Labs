class Escalator:
    def __init__(self, escalator_id: str, direction: str) -> None:
        self.escalator_id: str = escalator_id
        self.direction: str = direction  # "up" or "down"
        self.is_operational: bool = True

    def stop(self) -> None:
        self.is_operational = False

    def start(self) -> None:
        self.is_operational = True
