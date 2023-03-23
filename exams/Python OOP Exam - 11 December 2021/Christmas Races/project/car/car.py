from abc import ABC


class Car(ABC):

    SPEED_RANGE = ...

    def __init__(self, model, speed_limit):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")

        self.__model = value
        
    @property
    def speed_limit(self):
        return self.__speed_limit
    
    @speed_limit.setter
    def speed_limit(self, value):
        if value not in self.SPEED_RANGE:
            raise ValueError(f"Invalid speed limit! Must be between {self.SPEED_RANGE[0]}"
                             f" and {self.SPEED_RANGE[-1]}!")

        self.__speed_limit = value

