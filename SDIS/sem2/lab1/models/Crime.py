from Citizen import Citizen
from Law import Law

class Crime:
# когда будет писаться заявление, то будет создаваться Crime, закидываться в crimes.bin 
    def __init__(self, suspect: Citizen, description: str, law: Law):
        self.description: str = description
        self.suspect: Citizen = suspect
        self.law: Law = law

        @property
        def severity(self):
            return self.law.severity
        

        


