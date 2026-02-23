"""Citizen module representing civilians in the system."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Crime import Crime
    from .Law import Law


class CitizenError(Exception):
    """Base exception for citizen-related errors."""
    pass


class Citizen:
    """Represents a citizen who can report crimes and interact with police."""

    def __init__(self, name: str) -> None:
        self._name: str = name
        # Validate name on initialization
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not name.strip():
            raise ValueError("Name cannot be empty")
        if len(name.strip()) < 2:
            raise ValueError("Name must contain at least 2 characters")

    @property
    def name(self) -> str:
        """Return the citizen's name."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Set the citizen's name with validation."""
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not value.strip():
            raise ValueError("Name cannot be empty")
        if len(value.strip()) < 2:
            raise ValueError("Name must contain at least 2 characters")
        self._name = value.strip()

    def submit_application(
        self,
        suspect: Citizen,
        description: str,
        zone: str,
        law: Law
    ) -> Crime:
        """
        Submit a crime report against a suspect.
        
        Args:
            suspect: The citizen suspected of committing a crime.
            description: Description of the incident.
            zone: The zone where the crime occurred.
            law: The law that was broken.
            
        Returns:
            Crime: A new Crime object.
        """
        from .Crime import Crime
        return Crime(
            suspect=suspect,
            description=description,
            zone=zone,
            law=law
        )

    def __repr__(self) -> str:
        return f"Citizen(name={self._name!r})"

    def __str__(self) -> str:
        return f"Citizen: {self._name}"
