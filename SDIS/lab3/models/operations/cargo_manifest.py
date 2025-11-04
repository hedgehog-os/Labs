class CargoManifest:
    def __init__(self, manifest_id: str, items: list[str], total_weight_kg: float) -> None:
        self.manifest_id: str = manifest_id
        self.items: list[str] = items
        self.total_weight_kg: float = total_weight_kg

    def add_item(self, item: str, weight: float) -> None:
        self.items.append(item)
        self.total_weight_kg += weight

    def remove_item(self, item: str) -> bool:
        if item in self.items:
            self.items.remove(item)
            return True
        return False
