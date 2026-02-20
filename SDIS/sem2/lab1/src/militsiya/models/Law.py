class Law:
    def __init__(self, article: int, desc: str = ""):
        self.article: int = article
        self.desc:str = desc
        
        
    def __eq__(self, other: Law):
        if self.article == other.article:
            return True