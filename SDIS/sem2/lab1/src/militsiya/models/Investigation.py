import json
import random
from Crime import Crime

class Investigation:
    def __init__(self, path: str):
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.crimes: list[Crime] = data["crimes"]
    
    def investigate(self):
        criminals = []

        for crime in self.crimes:
            
            if crime.guilt:
                continue
            
            weights = [crime.severity / 5.0, 1 - crime.severity / 5.0]
            guilt = random.choice([True, False], weights=weights)
            if guilt:
                criminals.append((crime.suspect, crime.severity))

        return criminals
            
