from abc import ABC


class Astronaut(ABC):

    DEFAULT_OXYGEN_AMOUNT = ...

    def __init__(self, name, oxygen=DEFAULT_OXYGEN_AMOUNT):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")

        self.__name = value

    def oxygen_decrease(self):
        return 10

    def breathe(self):
        self.oxygen -= self.oxygen_decrease()

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
