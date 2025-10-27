from typing import List

class SecurityPolicy:
    def __init__(self, policy_id: int, name: str, rules: List[str], enforced: bool) -> None:
        self.policy_id: int = policy_id
        self.name: str = name
        self.rules: List[str] = rules
        self.enforced: bool = enforced