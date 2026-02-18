import random
from Citizen import Citizen

class Policeman:
    ranks = ("private", "lieutinant", "captain", "major", "colonel", "general")
    statuses = ("rest", "work")

    def __init__(self, lastname: str, rank: str, status: str):
        self.lastname: str = lastname

        @property
        def lastname(self):
            return self._name
        
        @lastname.setter
        def lastname(self, value):
            if not isinstance(value, str):
                raise TypeError("Lastname must be string")
            
            elif not value.strip():
                raise TypeError("Lastname can't be empty")
            
            elif len(value.strip()) < 2:
                raise TypeError("Lastname must contain at least 2 characters")
            
        self.rank: str = rank

        @property
        def rank(self):
            return self._rank
        
        @rank.setter
        def rank(self, value):
            if value not in self.ranks:
                raise TypeError("There is no such rank")
            
        self.status: str = status

        @property
        def status(self):
            return self._status
        
        @status.setter
        def status(self, value):
            if value not in self.statuses:
                raise TypeError("There is no such status")
            
        self.fatigue: int = 0
        self.criminal: tuple[Citizen, int] = None

    def arrest(self):
        if self.criminal:
            weights = [1 - (self.criminal[1]+ self.criminal[0]) / 10, (self.criminal[1]+ self.criminal[0]) / 10]
            arrested = random.choice([True, False], weights=weights)

            if arrested:
                self.criminal = None
                self.fatigue += 1
                return True