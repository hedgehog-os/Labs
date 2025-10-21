from Person import Person
from datetime import datetime

class ExternalExpert(Person):
  
    def __init__(self, id: int,
                 comment_text: str,
                 comment_date: datetime,
                 annotation_text: str
                 ):
        
        super().__init__(id=id)

        self.comment_text = comment_text
        self.comment_date = comment_date
        self.annotation_text = annotation_text