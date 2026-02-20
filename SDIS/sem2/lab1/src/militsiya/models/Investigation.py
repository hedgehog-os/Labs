import random
from Crime import Crime

# Получает список Crime и решает кто из граждан виновен, в результате создает tuple с Crime и его опасностью
class Investigation:
    def __init__(self, crimes: list[Crime]):
        self._crimes: list[Crime] = crimes
    
    def investigate(self):
        criminals = []

        for crime in self._crimes:
            
            if crime.guilt:
                continue
            
            weights = [crime.severity / 5.0, 1 - crime.severity / 5.0]
            guilt = random.choice([True, False], weights=weights)
            if guilt:
                criminals.append((crime.suspect, crime.severity))

        return criminals
            
