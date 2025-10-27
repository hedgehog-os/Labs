class Chemical:
    
    hazard_levels = {
        'low', 'medium', 'high'
    }
    
    def __init__(self, name: str, formula: str, hazard_level: str) -> None:
        self.name: str = name
        self.formula: str = formula
        self.hazard_level: str = hazard_level

    @property
    def hazard_level(self):
        return self._role

    @hazard_level.setter
    def hazard_level(self, value):
        if value not in self.hazard_levels:
            raise ValueError(f'Недопустимый статус: {value}')
        self._role = value