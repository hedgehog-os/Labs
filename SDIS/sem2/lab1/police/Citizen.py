from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Crime import Crime
    from .Law import Law

class Citizen:
    def __init__(self, name: str):
        self._name: str = name

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
            
    def submit_application(self, suspect: Citizen, description: str, law: Law) -> Crime:
        return Crime(suspect=suspect, description=description, law=law)
    
    def __repr__(self):
        return f"Citizen(name={self._name!r})"