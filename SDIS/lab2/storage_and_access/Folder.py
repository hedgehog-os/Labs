from typing import List, Optional

class Folder:
    def __init__(self, folder_id: int, name: str, parent_id: Optional[int], document_ids: List[int]) -> None:
        self.folder_id: int = folder_id
        self.name: str = name
        self.parent_id: Optional[int] = parent_id
        self.document_ids: List[int] = document_ids