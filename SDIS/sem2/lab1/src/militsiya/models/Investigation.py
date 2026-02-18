from Policeman import Policeman
from Crime import Crime

class Investigation:
    def __init__(self, policeman: Policeman, crime: Crime):
        self.policeman: Policeman = policeman
        self.crime: Crime = crime