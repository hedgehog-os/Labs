from __future__ import annotations

class SpecialAssistanceRequest:
    def __init__(self, request_type: str, description: str, is_confirmed: bool = False) -> None:
        self.request_type: str = request_type  # e.g. "wheelchair", "visual aid", "language support"
        self.description: str = description
        self.is_confirmed: bool = is_confirmed

    def confirm(self) -> None:
        self.is_confirmed = True
