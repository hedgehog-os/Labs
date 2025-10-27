from Chemical import Chemical

class Sample:
    def __init__(self, sample_id: int, chemical: Chemical, volume_ml: float) -> None:
        self.sample_id: int = sample_id
        self.chemical: Chemical = chemical
        self.volume_ml: float = volume_ml