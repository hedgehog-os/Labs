from Citizen import Citizen

class Criminal:
    crimes = ("theft", "fighting", "fraude", "murder")

    def __init__(self, crime: str, name: str, description: str, suspect: Citizen, severity: int = 1):
        self.crime: str = crime

        @property
        def crime(self):
            return self._crime
        
        @crime.setter
        def crime(self, value):
            if value not in self.crimes:
                raise TypeError("There is no such status")
            
        self.name: str = name

        @property
        def name(self):
            return self._name
        
        @name.setter
        def name(value):
            if not isinstance(value, str):
                raise TypeError("Name must be string")
            
            elif not value.strip():
                raise TypeError("Name can't be empty")
            
            elif len(value.strip()) < 2:
                raise TypeError("Name must contain at least 2 characters")
            
        self.description: str = description

        self.severity: int = severity

        @property
        def severity(self):
            return self._severity
        
        @severity.setter
        def severity(value):
            if value > 5 or value < 1:
                raise ValueError("Incorrect severity")

        self.suspect: Citizen = suspect

