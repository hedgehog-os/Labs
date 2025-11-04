from __future__ import annotations
from typing import List

class Restaurant:
    VALID_CUISINES = {
        "italian", "japanese", "chinese", "indian", "french",
        "american", "mexican", "thai", "vegetarian", "fast food"
    }

    VALID_TERMINALS = {
        "A", "B", "C", "D", "E", "International", "Domestic"
    }

    def __init__(self, name: str, cuisine_type: str, terminal_name: str) -> None:
        if cuisine_type.lower() not in self.VALID_CUISINES:
            raise ValueError(f"Invalid cuisine type: {cuisine_type}")
        if terminal_name not in self.VALID_TERMINALS:
            raise ValueError(f"Invalid terminal name: {terminal_name}")
        self.name: str = name
        self.cuisine_type: str = cuisine_type.lower()
        self.terminal_name: str = terminal_name
        self.is_open: bool = True
        self.maintenance_required: bool = False
        self.customer_log: List[str] = []
        self.menu_items: List[str] = []

    def close(self) -> None:
        self.is_open = False

    def open(self) -> None:
        self.is_open = True

    def mark_for_maintenance(self) -> None:
        self.maintenance_required = True

    def clear_maintenance(self) -> None:
        self.maintenance_required = False

    def is_operational(self) -> bool:
        return self.is_open and not self.maintenance_required

    def log_customer(self, name: str) -> None:
        self.customer_log.append(name)

    def get_customer_count(self) -> int:
        return len(self.customer_log)

    def add_menu_item(self, item: str) -> None:
        self.menu_items.append(item)

    def remove_menu_item(self, item: str) -> bool:
        if item in self.menu_items:
            self.menu_items.remove(item)
            return True
        return False

    def has_menu_item(self, item: str) -> bool:
        return item in self.menu_items

    def get_menu(self) -> List[str]:
        return self.menu_items.copy()

    def reset(self) -> None:
        self.is_open = True
        self.maintenance_required = False
        self.customer_log.clear()
        self.menu_items.clear()
