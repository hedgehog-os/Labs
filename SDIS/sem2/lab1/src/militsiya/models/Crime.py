from Citizen import Citizen
from Law import Law

class Crime:

    def __init__(self, crime: str, description: str, suspect: Citizen, law: Law, guilt: bool = False, severity: int = 1):
        self.crime: str = crime
            
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
        self.law: Law = law
        self.guilt = guilt

