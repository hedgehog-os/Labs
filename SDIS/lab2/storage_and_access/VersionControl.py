from typing import List

class VersionControl:
    def __init__(self, document_id: int, versions: List[str], current_version: str) -> None:
        self.document_id: int = document_id
        self.versions: List[str] = versions
        self.current_version: str = current_version