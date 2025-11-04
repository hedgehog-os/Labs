class InformationKiosk:
    def __init__(self, kiosk_id: str, location: str) -> None:
        self.kiosk_id: str = kiosk_id
        self.location: str = location
        self.is_active: bool = True

    def deactivate(self) -> None:
        self.is_active = False

    def activate(self) -> None:
        self.is_active = True
