from abc import ABC, abstractmethod


class BaseRobot(ABC):

    _BASE_WEIGHT = ...

    def __init__(self, name, kind, price):
        self.name = name
        self.kind = kind
        self.price = price
        self.weight = self._BASE_WEIGHT

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Robot name cannot be empty!")

        self.__name = value

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        if not value.strip():
            raise ValueError("Robot kind cannot be empty!")

        self.__kind = value

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value <= 0.0:
            raise ValueError("Robot price cannot be less than or equal to 0.0!")

        self.__price = value

    @property
    @abstractmethod
    def wight_increase(self):
        ...

    def eating(self):
        self.weight += self.wight_increase()
