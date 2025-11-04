class WeatherReport:
    def __init__(self, location: str, temperature_c: float, wind_kph: float, condition: str) -> None:
        self.location: str = location
        self.temperature_c: float = temperature_c
        self.wind_kph: float = wind_kph
        self.condition: str = condition  # e.g. "Clear", "Rain", "Fog"

    def is_safe_for_flight(self) -> bool:
        return self.condition.lower() not in {"storm", "fog", "snow"}
