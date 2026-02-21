from . import Crime, Citizen


class Security:
    def __init__(self):
        self.level: int = 1

    def eval(self, citizens: list[Citizen], crimes: list[Crime]):
        return len(citizens) / len(crimes)
