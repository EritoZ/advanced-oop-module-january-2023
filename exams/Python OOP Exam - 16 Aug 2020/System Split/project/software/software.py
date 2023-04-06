import math
from abc import ABC


class Software(ABC):

    def __init__(self, name, software_type, capacity_consumption, memory_consumption):
        self.name = name
        self.software_type = software_type
        self.capacity_consumption = capacity_consumption
        self.memory_consumption = memory_consumption

    @property
    def capacity_consumption(self):
        return self.__capacity_consumption

    @capacity_consumption.setter
    def capacity_consumption(self, value):
        type_dict = {'LightSoftware': math.floor(value * 1.5), 'ExpressSoftware': value}

        try:
            self.__capacity_consumption = type_dict[self.__class__.__name__]

        except KeyError:
            self.__capacity_consumption = value

    @property
    def memory_consumption(self):
        return self.__memory_consumption

    @memory_consumption.setter
    def memory_consumption(self, value):
        type_dict = {'LightSoftware': math.floor(value * 0.5), 'ExpressSoftware': value * 2}

        try:
            self.__memory_consumption = type_dict[self.__class__.__name__]

        except KeyError:
            self.__memory_consumption = value
