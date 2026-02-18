class Citizen:
    def __init__(self, name: str, address: str):
        self.name: str = name

        @property
        def name(self):
            return self._name
        
        @name.setter
        def name(value):
            if not isinstance(value, str):
                raise TypeError("Name must be string")
            
            elif not value.strip():
                raise TypeError("Name can't be empty")
            
            elif len(value.strip()) < 2:
                raise TypeError("Name must contain at least 2 characters")
            
            self.address = address