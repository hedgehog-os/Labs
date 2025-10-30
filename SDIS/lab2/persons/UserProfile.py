from datetime import datetime

class ExternalExpert:
    account_statuses: set[str] = {'active', 'suspended', 'pending', 'deleted'}

    def __init__(self,
                 expert_id: int,
                 username: str,
                 email: str,
                 phone_number: str,
                 security_question: str,
                 two_factor_enabled: bool,
                 preferred_language: str,
                 timezone: str,
                 account_status: str,
                 registered_at: datetime | None = None) -> None:
        self.expert_id: int = expert_id
        self.username: str = username
        self.email: str = email
        self.phone_number: str = phone_number
        self.security_question: str = security_question
        self.two_factor_enabled: bool = two_factor_enabled
        self.preferred_language: str = preferred_language
        self.timezone: str = timezone
        self._account_status: str = ""
        self.account_status = account_status
        self.registered_at: datetime = registered_at or datetime.now()

    @property
    def account_status(self) -> str:
        return self._account_status

    @account_status.setter
    def account_status(self, value: str) -> None:
        if value not in self.account_statuses:
            raise ValueError(f"Недопустимый статус: {value}")
        self._account_status = value
