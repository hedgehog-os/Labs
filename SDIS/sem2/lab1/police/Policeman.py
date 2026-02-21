import random
from . import Crime

from typing import Union

# Пресекает правонарушение, смотрит какие граждане виновны и арестует
class Policeman:

    def __init__(self, lastname: str, zone: Union[str, int, float], is_work: bool = True):
        self._lastname: str = lastname
        self._zone: Union[str, int, float] = zone
        self._is_work: bool = is_work
        self._fatigue: int = 0
        self._criminal: tuple[Crime, int] = None

        @property
        def zone(self):
            return self._zone
        
        @zone.setter
        def zone(self, value):
            self._zone = value
        
        @property
        def lastname(self):
            return self._lastname
        
        @lastname.setter
        def lastname(self, value):
            if not isinstance(value, str):
                raise TypeError("Lastname must be string")
            
            elif not value.strip():
                raise ValueError("Lastname can't be empty")
            
            elif len(value.strip()) < 2:
                raise ValueError("Lastname must contain at least 2 characters")
            
            self._lastname = value.strip()
            
        @property
        def is_work(self):
            return self._is_work
        
        @is_work.setter
        def is_work(self, value):
            self._is_work = value

    def arrest(self) -> bool:
        if self._criminal:
            weights = [1 - (self._fatigue + self._criminal[1]) / 20, (self._fatigue + self._criminal[1]) / 20]
            arrested = random.choices([True, False], weights=weights)[0]

            if arrested:
                self._criminal = None
                self._fatigue += 1
                return True
            
            else:
                self._fatigue += 1
                return False

    def assign_crime(self, criminal: tuple[Crime, int]):
        self._criminal = criminal

    def recovery(self):
        self._fatigue = 0

