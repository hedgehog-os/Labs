class LostAndFoundReport:
    def __init__(self, item_description: str, location: str, timestamp: str) -> None:
        self.item_description: str = item_description
        self.location: str = location
        self.timestamp: str = timestamp
        self.is_claimed: bool = False

    def claim(self) -> None:
        self.is_claimed = True
