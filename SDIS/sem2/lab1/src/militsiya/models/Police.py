import json
from Policeman import Policeman

class Police:
    def __init__(self, path: str):
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.policemen: list[Policeman] = data["policemen"]
            self.history: list[str] = data["history"]
    
    def history(self):
        return self.history
    
    def hire(self, policeman: Policeman):
        self.policemen.append(policeman)
        self.history.append(f"Hired policeman {policeman.lastname}")
        
    def fire(self, policeman: Policeman):
        self.policemen.remove(policeman)
        self.history.append(f"Fired policeman {policeman.lastname}")

