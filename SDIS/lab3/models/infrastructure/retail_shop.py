class RetailShop:
    def __init__(self, name: str, category: str, terminal_name: str) -> None:
        self.name: str = name
        self.category: str = category  # e.g. "electronics", "clothing"
        self.terminal_name: str = terminal_name
        self.is_open: bool = True

    def close(self) -> None:
        self.is_open = False

    def open(self) -> None:
        self.is_open = True
