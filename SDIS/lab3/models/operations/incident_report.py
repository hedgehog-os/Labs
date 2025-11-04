class IncidentReport:
    def __init__(self, report_id: str, description: str, severity: str, timestamp: str) -> None:
        self.report_id: str = report_id
        self.description: str = description
        self.severity: str = severity
        self.timestamp: str = timestamp
        self.is_resolved: bool = False

    def resolve(self) -> None:
        self.is_resolved = True
