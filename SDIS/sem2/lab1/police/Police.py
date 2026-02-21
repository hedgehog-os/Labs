from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Policeman import Policeman

class Police:
    def __init__(self, zones = None):
        self._zones = zones or {}

        @property
        def zones(self):
            return self._zones
        
        @zones.setter
        def zones(self, value):
            self._zones = value
    
    def create_zone(self, zone: str):
        self._zones[str(zone)] = {"policemen": [], "crimes": [], "security": 1.0}

    def hire(self, policeman: Policeman, zone: str):
        self._zones[str(zone)]["policemen"].append(policeman)
        policeman._zone = zone
        
    def fire(self, policeman: Policeman):
        self._zones[policeman._zone]["policemen"].remove(policeman)

    def relocate(self, relocated_policemen: list[Policeman], target_zone: str):
        for policeman in relocated_policemen:
            self._zones[policeman._zone]["policemen"].remove(policeman)
            policeman.zone = target_zone
            self._zones[policeman._zone]["policemen"].append(policeman)

    def get_policemen(self) -> list[Policeman]:
        all_policemen = []
        for zone in self._zones.values():
            for policeman in zone["policemen"]:
                all_policemen.append(policeman)
        return all_policemen

    def add_zone(self, new_zone: str):
        self._zones[new_zone] = {"policemen": [], "crimes": [], "security": 1}
