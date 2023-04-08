from abc import ABC


class BaseService(ABC):

    _DEFAULT_CAPACITY = ...

    def __init__(self, name):
        self.name = name
        self.capacity = self._DEFAULT_CAPACITY
        self.robots = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Service name cannot be empty!")

        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Service capacity cannot be less than or equal to 0!")

        self.__capacity = value

    def details(self):
        s_right_index = self.__class__.__name__.rindex('S')
        first_name = self.__class__.__name__[:s_right_index]

        return f'''{self.name} {first_name} Service:
Robots: {" ".join(r.name for r in self.robots) if self.robots else 'none'}'''
