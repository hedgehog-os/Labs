from datetime import datetime

class Student:

    def __init__(self, student_id: int,
                 fullname: str,
                 email: str,
                 department: str,
                 assigned_documents: list,
                 activity_log: dict[str, datetime]
                 ):
        
        self.student_id = student_id
        self.fullname = fullname
        self.email = email
        self.department = department
        self.assigned_documents = assigned_documents
        self.activity_lof = activity_log