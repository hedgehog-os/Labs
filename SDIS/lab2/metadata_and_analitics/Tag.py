from typing import Optional

class Tag:
    def __init__(self, name: str, category: Optional[str] = None) -> None:
        self.name: str = name
        self.category: Optional[str] = category