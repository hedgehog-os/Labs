class LocalStorage:
    def __init__(self, path: str, capacity_gb: float) -> None:
        self.path: str = path
        self.capacity_gb: float = capacity_gb