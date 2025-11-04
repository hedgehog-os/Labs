class EmergencyProtocol:
    def __init__(self, protocol_id: str, description: str, severity_level: str) -> None:
        self.protocol_id: str = protocol_id
        self.description: str = description
        self.severity_level: str = severity_level
        self.is_active: bool = False

    def activate(self) -> None:
        self.is_active = True

    def deactivate(self) -> None:
        self.is_active = False
