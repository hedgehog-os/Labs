from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Citizen import Citizen
    from .Law import Law

class Crime:
# когда будет писаться заявление, то будет создаваться Crime, закидываться в crimes.bin 
    def __init__(self, suspect: Citizen, description: str, zone: str, law: Law):
        self.description: str = description
        self.suspect: Citizen = suspect
        self.zone: str = zone
        self.law: Law = law

    @property
    def severity(self):
        return self.law.severity
    
    def __repr__(self):
        return f"Crime(description={self.description!r}, suspect={self.suspect!r}, zone={self.zone!r}, law={self.law!r})"
        

        


