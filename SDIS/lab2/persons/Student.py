from Person import Person
from datetime import datetime

class Student(Person):

    def __init__(self, student_id: int,
                 fullname: str,
                 email: str,
                 department: str,
                 assigned_documents: list = None,
                 activity_log: dict[str, datetime] = None
                 ):
        
        super().__init__(id=student_id,
                         fullname=fullname,
                         email=email
                         )
        
        self.department = department
        self.assigned_documents = assigned_documents
        self.activity_lof = activity_log