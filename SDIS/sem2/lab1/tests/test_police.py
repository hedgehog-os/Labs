"""Unit tests for the Police Management System."""

import pytest
from police import (
    Police,
    Policeman,
    Citizen,
    Crime,
    Investigation,
    Law,
    Security,
    PoliceError,
    ZoneNotFoundError,
    PolicemanNotFoundError,
    CitizenError,
    LawError,
)


class TestLaw:
    """Tests for the Law class."""

    def test_create_law(self) -> None:
        law = Law(article=101, severity=3, desc="Theft")
        assert law.article == 101
        assert law.severity == 3
        assert law.desc == "Theft"

    def test_default_severity(self) -> None:
        law = Law(article=202)
        assert law.severity == 1

    def test_invalid_severity_low(self) -> None:
        with pytest.raises(ValueError):
            law = Law(article=303, severity=0)

    def test_invalid_severity_high(self) -> None:
        with pytest.raises(ValueError):
            law = Law(article=303, severity=6)

    def test_set_severity(self) -> None:
        law = Law(article=404)
        law.severity = 4
        assert law.severity == 4

    def test_set_invalid_severity(self) -> None:
        law = Law(article=505)
        with pytest.raises(ValueError):
            law.severity = 10

    def test_law_equality(self) -> None:
        law1 = Law(article=100, severity=2)
        law2 = Law(article=100, severity=5)
        assert law1 == law2

    def test_law_inequality(self) -> None:
        law1 = Law(article=100)
        law2 = Law(article=200)
        assert law1 != law2


class TestCitizen:
    """Tests for the Citizen class."""

    def test_create_citizen(self) -> None:
        citizen = Citizen(name="John Doe")
        assert citizen.name == "John Doe"

    def test_invalid_name_empty(self) -> None:
        with pytest.raises(ValueError):
            Citizen(name="")

    def test_invalid_name_short(self) -> None:
        with pytest.raises(ValueError):
            Citizen(name="A")

    def test_set_name(self) -> None:
        citizen = Citizen(name="Original")
        citizen.name = "Updated Name"
        assert citizen.name == "Updated Name"

    def test_set_invalid_name_type(self) -> None:
        citizen = Citizen(name="Test")
        with pytest.raises(TypeError):
            citizen.name = 123  # type: ignore


class TestPoliceman:
    """Tests for the Policeman class."""

    def test_create_policeman(self) -> None:
        policeman = Policeman(lastname="Smith", zone="Zone A")
        assert policeman.lastname == "Smith"
        assert policeman.zone == "Zone A"
        assert policeman.is_work is True
        assert policeman.fatigue == 0

    def test_invalid_lastname(self) -> None:
        with pytest.raises(ValueError):
            Policeman(lastname="A", zone="Zone A")

    def test_set_lastname(self) -> None:
        policeman = Policeman(lastname="Original", zone="Zone A")
        policeman.lastname = "Newman"
        assert policeman.lastname == "Newman"

    def test_arrest_no_assignment(self) -> None:
        policeman = Policeman(lastname="Test", zone="Zone A")
        assert policeman.arrest() is False

    def test_assign_crime(self) -> None:
        policeman = Policeman(lastname="Test", zone="Zone A")
        law = Law(article=100, severity=3)
        citizen = Citizen(name="Criminal")
        crime = Crime(suspect=citizen, description="Theft", zone="Zone A", law=law)
        policeman.assign_crime((crime, 3))
        assert policeman.has_assignment is True

    def test_recovery(self) -> None:
        policeman = Policeman(lastname="Test", zone="Zone A")
        # Simulate fatigue (would normally come from arrest attempts)
        policeman._fatigue = 5
        policeman.recovery()
        assert policeman.fatigue == 0


class TestPolice:
    """Tests for the Police class."""

    def test_create_police(self) -> None:
        police = Police()
        assert police.zones == {}

    def test_create_zone(self) -> None:
        police = Police()
        police.create_zone("Zone A")
        assert "Zone A" in police.zones

    def test_create_duplicate_zone(self) -> None:
        police = Police()
        police.create_zone("Zone A")
        with pytest.raises(PoliceError):
            police.create_zone("Zone A")

    def test_hire_policeman(self) -> None:
        police = Police()
        police.create_zone("Zone A")
        policeman = Policeman(lastname="Smith", zone="Zone A")
        police.hire(policeman, "Zone A")
        assert policeman in police.get_policemen()

    def test_hire_to_nonexistent_zone(self) -> None:
        police = Police()
        policeman = Policeman(lastname="Smith", zone="Zone A")
        with pytest.raises(ZoneNotFoundError):
            police.hire(policeman, "Zone A")

    def test_fire_policeman(self) -> None:
        police = Police()
        police.create_zone("Zone A")
        policeman = Policeman(lastname="Smith", zone="Zone A")
        police.hire(policeman, "Zone A")
        police.fire(policeman)
        assert policeman not in police.get_policemen()
        assert policeman.is_work is False

    def test_fire_nonexistent_policeman(self) -> None:
        police = Police()
        police.create_zone("Zone A")
        policeman = Policeman(lastname="Smith", zone="Zone A")
        with pytest.raises(PolicemanNotFoundError):
            police.fire(policeman)

    def test_relocate_policeman(self) -> None:
        police = Police()
        police.create_zone("Zone A")
        police.create_zone("Zone B")
        policeman = Policeman(lastname="Smith", zone="Zone A")
        police.hire(policeman, "Zone A")
        police.relocate([policeman], "Zone B")
        assert policeman.zone == "Zone B"
        assert policeman in police.get_policemen_by_zone("Zone B")

    def test_relocate_to_nonexistent_zone(self) -> None:
        police = Police()
        policeman = Policeman(lastname="Smith", zone="Zone A")
        with pytest.raises(ZoneNotFoundError):
            police.relocate([policeman], "Zone B")

    def test_get_policemen_by_zone(self) -> None:
        police = Police()
        police.create_zone("Zone A")
        policeman = Policeman(lastname="Smith", zone="Zone A")
        police.hire(policeman, "Zone A")
        policemen = police.get_policemen_by_zone("Zone A")
        assert len(policemen) == 1


class TestCrime:
    """Tests for the Crime class."""

    def test_create_crime(self) -> None:
        law = Law(article=101, severity=3)
        suspect = Citizen(name="Criminal")
        crime = Crime(suspect=suspect, description="Theft", zone="Zone A", law=law)
        assert crime.description == "Theft"
        assert crime.suspect == suspect
        assert crime.zone == "Zone A"
        assert crime.severity == 3


class TestInvestigation:
    """Tests for the Investigation class."""

    def test_investigate_empty(self) -> None:
        investigation = Investigation([])
        result = investigation.investigate()
        assert result is None

    def test_investigate_crimes(self) -> None:
        law = Law(article=101, severity=5)
        suspect = Citizen(name="Criminal")
        crime = Crime(suspect=suspect, description="Theft", zone="Zone A", law=law)
        investigation = Investigation([crime])
        # Result is probabilistic, so just check it returns correct type or None
        result = investigation.investigate()
        assert result is None or (isinstance(result, tuple) and len(result) == 2)


class TestSecurity:
    """Tests for the Security class."""

    def test_create_security(self) -> None:
        security = Security()
        assert security.level == 1.0

    def test_eval_no_crimes(self) -> None:
        security = Security()
        citizens = [Citizen(name=f"Citizen{i}") for i in range(10)]
        level = security.eval(citizens, [])
        assert level == 10.0

    def test_eval_with_crimes(self) -> None:
        security = Security()
        citizens = [Citizen(name=f"Citizen{i}") for i in range(10)]
        law = Law(article=101, severity=3)
        crimes = [
            Crime(suspect=citizens[0], description="Theft", zone="Zone A", law=law)
        ]
        level = security.eval(citizens, crimes)
        assert level == 10.0  # 10 citizens / 1 crime

    def test_decrease_security(self) -> None:
        security = Security()
        security.decrease(0.5)
        assert security.level == 0.5

    def test_increase_security(self) -> None:
        security = Security(base_level=0.5)
        security.increase(0.3)
        assert security.level == 0.8

    def test_negative_security(self) -> None:
        security = Security()
        security.decrease(10)
        assert security.level == 0.0  # Should not go below 0
