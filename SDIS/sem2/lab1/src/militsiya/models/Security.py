import json
from Crime import Crime
from Citizen import Citizen

class Security:
    def __init__(self, path):
        self.level: int = 1
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.crimes: list[Crime] = data["crimes"]
            self.citizens: list[Citizen] = data["citizens"]

    def eval(self):
        return len(self.citizens) / len(self.crimes)
    
    def update(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.crimes: list[Crime] = data["crimes"]
            self.citizens: list[Citizen] = data["citizens"]