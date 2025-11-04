class WeatherReport:
    UNSAFE_CONDITIONS = {"storm", "fog", "snow", "hail", "tornado"}
    EXTREME_WIND_KPH = 60.0
    EXTREME_TEMP_C = (-30.0, 45.0)

    def __init__(self, location: str, temperature_c: float, wind_kph: float, condition: str) -> None:
        self.location: str = location
        self.temperature_c: float = temperature_c
        self.wind_kph: float = wind_kph
        self.condition: str = condition.strip().lower()
        self.notes: list[str] = []
        self.is_verified: bool = False

    def is_safe_for_flight(self) -> bool:
        return (
            self.condition not in self.UNSAFE_CONDITIONS
            and self.wind_kph <= self.EXTREME_WIND_KPH
            and self.EXTREME_TEMP_C[0] <= self.temperature_c <= self.EXTREME_TEMP_C[1]
        )

    def mark_verified(self) -> None:
        self.is_verified = True

    def add_note(self, note: str) -> None:
        self.notes.append(note)

    def reset(self) -> None:
        self.notes.clear()
        self.is_verified = False

    def summary(self) -> str:
        status = "VERIFIED" if self.is_verified else "UNVERIFIED"
        safety = "SAFE" if self.is_safe_for_flight() else "UNSAFE"
        return (
            f"Weather at {self.location}: {self.temperature_c:.1f}°C, {self.wind_kph:.1f} kph wind, "
            f"{self.condition.capitalize()} — {safety}, {status}"
        )
