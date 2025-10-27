class Encryption:
    def __init__(self, method: str, key: str, enabled: bool) -> None:
        self.method: str = method  # e.g. "AES-256"
        self.key: str = key
        self.enabled: bool = enabled