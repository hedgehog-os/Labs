from Person import Person
from datetime import datetime

class ExternalExpert(Person):
  
    account_statuses = {
        'active', 'suspended', 'pending', 'deleted'
    }

    def __init__(self, id: int,
                 username: str,
                 email: str,
                 phone_number: str,
                 security_question: str,
                 two_factore_enabled: bool,
                 prefered_language: str,
                 timezone: str,
                 account_status: str
                 ):
        
        super().__init__(id=id, fullname=username, email=email)

        self.phone_number = phone_number
        self.security_question = security_question
        self.two_factore_enabled = two_factore_enabled
        self.prefered_language = prefered_language
        self.timezone = timezone
        self.account_status = account_status

    @property
    def account_status(self):
        return self._role

    @account_status.setter
    def account_status(self, value):
        if value not in self.account_statuses:
            raise ValueError(f'Недопустимый статус: {value}')
        self._role = value