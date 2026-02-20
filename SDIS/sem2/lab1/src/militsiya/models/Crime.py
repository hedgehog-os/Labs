from Citizen import Citizen
from Law import Law
from typing import Union

class Crime:
# когда будет писаться заявление, то будет создаваться Crime, закидываться в crimes.bin 
    def __init__(self, crime: str, description: str, suspect: Citizen, law: Law, zone: Union[str, int, float], guilt: bool = False, severity: int = 1):
        self.crime: str = crime  #??
        self.description: str = description
        self.severity: int = severity
        self.suspect: Citizen = suspect
        self.law: Law = law
        self.guilt = guilt
        self.zone = zone #???

        @property
        def severity(self):
            return self._severity
        
        @severity.setter
        def severity(self, value):
            if value > 5 or value < 1:
                raise ValueError("Incorrect severity")
            self._severity = value


