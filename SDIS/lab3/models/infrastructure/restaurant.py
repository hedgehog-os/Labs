class Restaurant:
    def __init__(self, name: str, cuisine_type: str, terminal_name: str) -> None:
        self.name: str = name
        self.cuisine_type: str = cuisine_type
        self.terminal_name: str = terminal_name
        self.is_open: bool = True

    def close(self) -> None:
        self.is_open = False

    def open(self) -> None:
        self.is_open = True
