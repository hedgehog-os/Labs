from Device import Device

class Sensor:
    def __init__(self, sensor_id: int, type: str, device: Device) -> None:
        self.sensor_id: int = sensor_id
        self.type: str = type
        self.device: Device = device