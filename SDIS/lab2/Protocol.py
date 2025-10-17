from datetime import datetime

class Protocol:

    def __init__(self, procedure_steps: list[str] = None,
                 safety_protocol: str = None,
                 approval_date: datetime = None,
                 expiration_date: datetime = None,
                 linked_experiment_ids: list[int] = None
                 ):
        
        self.procedure_steps = procedure_steps
        self.safety_protocol = safety_protocol
        self.approval_date = approval_date
        self.expiration_date = expiration_date
        self.linked_experiment_ids = linked_experiment_ids