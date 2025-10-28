from typing import List

class DataSet:
    def __init__(self, dataset_id: int, name: str, source: str, records: List[dict]) -> None:
        self.dataset_id: int = dataset_id
        self.name: str = name
        self.source: str = source
        self.records: List[dict] = records