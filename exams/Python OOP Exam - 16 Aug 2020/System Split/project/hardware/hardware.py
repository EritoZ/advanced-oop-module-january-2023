import math
from abc import ABC
from typing import List

from project.software.software import Software


class Hardware(ABC):

    def __init__(self, name, hardware_type, capacity, memory):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.current_capacity = self.capacity
        self.memory = memory
        self.current_memory = self.memory
        self.software_components: List[Software] = []
            
    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        type_dict = {'HeavyHardware': value * 2, 'PowerHardware': math.floor(value * 0.25)}

        try:
            self.__capacity = type_dict[self.__class__.__name__]

        except KeyError:
            self.__capacity = value

    @property
    def memory(self):
        return self.__memory
    
    @memory.setter
    def memory(self, value):
        type_dict = {'HeavyHardware': math.floor(value * 0.75), 'PowerHardware': math.floor(value * 1.75)}

        try:
            self.__memory = type_dict[self.__class__.__name__]

        except KeyError:
            self.__memory = value

    def install(self, software: Software):
        if self.current_capacity < software.capacity_consumption or self.current_memory < software.memory_consumption:
            raise Exception("Software cannot be installed")

        self.current_capacity -= software.capacity_consumption
        self.current_memory -= software.memory_consumption

        self.software_components.append(software)

    def uninstall(self, software: Software):
        self.current_capacity += software.capacity_consumption
        self.current_memory += software.memory_consumption

        self.software_components.remove(software)
