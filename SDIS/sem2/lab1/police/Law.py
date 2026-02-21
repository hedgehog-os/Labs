class Law:
    def __init__(self, article: int, severity: int = 1, desc: str = ""):
        self._article: int = article
        self._desc:str = desc
        self._severity: int = severity
        
        @property
        def severity(self):
            return self._severity
        
        @severity.setter
        def severity(self, value):
            if value > 5 or value < 1:
                raise ValueError("Incorrect severity")
            self._severity = value

    def __eq__(self, other: Law):
        if self.article == other.article:
            return True