from Person import Person

class LabAssistant(Person):

    def __init__(self, id: int,
                 fullname: str,
                 email: str,
                 position: str,
                 lab_room: int,
                 equipment_list: list[str] = None
                 ):
        
        super().__init__(id=id,
                         fullname=fullname,
                         email=email
                         )
        
        self.position = position
        self.lab_room  = lab_room
        self.equipment_list = equipment_list