class Restroom:
    def __init__(self, location: str, is_accessible: bool) -> None:
        self.location: str = location
        self.is_accessible: bool = is_accessible
        self.is_clean: bool = True

    def mark_dirty(self) -> None:
        self.is_clean = False

    def clean(self) -> None:
        self.is_clean = True
