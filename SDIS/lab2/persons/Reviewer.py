from Person import Person
from documents.Document import Document

class Reviewer(Person):

    def __init__(self, id: int,
                 review_rating: int = None,
                 review_text: str = None,
                 comment_text: str = None
                 ):
        
        super().__init__(id=id)

        self.review_rating = review_rating
        self.review_text = review_text
        self.comment_text = comment_text
        