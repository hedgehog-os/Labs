class Officer:
    ranks = ("private", "lieutinant", "captain", "major", "colonel", "general")
    specializations = ("investigation", "patrol", "district police officer", "operative")
    statuses = ("sick", "wickend", "vocation")

    def __init__(self, lastname: str, rank: str, specialization: str, status: str):
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
            
        self.specialization: str = specialization

        @property
        def specialization(self):
            return self._specialization
        
        @specialization.setter
        def specialization(self, value):
            if value not in self.specializations:
                raise TypeError("There is no such specialization")
            
        self.status: str = status

        @property
        def status(self):
            return self._status
        
        @status.setter
        def status(self, value):
            if value not in self.statuses:
                raise TypeError("There is no such status")
            
        self.fatigue: int = 0

