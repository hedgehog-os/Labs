class Runway:
    def __init__(self, identifier: str, length_meters: int, is_active: bool = True) -> None:
        self.identifier: str = identifier
        self.length_meters: int = length_meters
        self.is_active: bool = is_active

    def close(self) -> None:
        self.is_active = False

    def open(self) -> None:
        self.is_active = True
