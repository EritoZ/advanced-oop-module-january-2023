from abc import ABC, abstractmethod


class Computer(ABC):

    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value: str):
        if not value or value.isspace():
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value or value.isspace():
            raise ValueError("Model name cannot be empty.")

        self.__model = value

    @property
    @abstractmethod
    def eligible_processors(self):
        ...

    @property
    def eligible_rams(self):
        rams = [2]

        [rams.append(rams[-1] * 2) for _ in range(self.max_ram())]

        return rams

    @property
    @abstractmethod
    def max_ram(self):
        ...

    @property
    @abstractmethod
    def type_comp(self):
        ...

    def configure_computer(self, processor: str, ram: int):

        if processor not in self.eligible_processors():
            raise ValueError(f"{processor} is not compatible with {self.type_comp()} {self.manufacturer} {self.model}!")

        if ram not in self.eligible_rams:
            raise ValueError(f"{ram}GB RAM is not compatible with {self.type_comp()} {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price = (self.eligible_rams.index(ram) + 1) * 100 + self.eligible_processors()[processor]

        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
