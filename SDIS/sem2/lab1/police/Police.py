from Policeman import Policeman
from typing import Union

class Police:
    def __init__(self, zones = None):
        self._zones = zones or {}

        @property
        def zones(self):
            return self._zones
        
        @zones.setter
        def zones(self, value):
            self._zones = value
    
    def create_zone(self, zone: Union[str, int, float]):
        self._zones[str(zone)] = {"policemen": [], "crimes": [], "security": 1.0}

    def hire(self, policeman: Policeman, zone: Union[str, int, float]):
        self._zones[str(zone)]["policemen"].append(policeman)
        policeman.zone = zone
        
    def fire(self, policeman: Policeman):
        self._zones[policeman.zone()]["policemen"].remove(policeman)

    def relocate(self, relocated_policemen: list[Policeman], target_zone: Union[str, int, float]):
        for policeman in relocated_policemen:
            self._zones[policeman.zone()]["policemen"].remove(policeman)
            policeman.zone = target_zone
            self._zones[policeman.zone()]["policemen"].append(policeman)


