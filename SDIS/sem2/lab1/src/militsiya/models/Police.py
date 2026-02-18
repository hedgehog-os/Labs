import json
from Policeman import Policeman

class Police:
    def __init__(self, policemen: list[Policeman]):
        self.policemen: list[Policeman] = policemen

    
    def history(path: str):
        with open(path, 'r', encoding='utf-8') as file:
            history = json.load(file)
        return history
    
    def hire(policeman: Policeman):
        policeman.append(policeman)
        