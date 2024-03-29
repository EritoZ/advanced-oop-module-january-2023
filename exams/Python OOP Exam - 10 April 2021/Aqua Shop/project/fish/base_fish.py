from abc import ABC, abstractmethod


class BaseFish(ABC):
    DEFAULT_SIZE = ...

    def __init__(self, name, species, price):
        self.name = name
        self.species = species
        self.size = self.DEFAULT_SIZE
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Fish name cannot be an empty string.")

        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        if not value:
            raise ValueError("Fish species cannot be an empty string.")

        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price cannot be equal to or below zero.")

        self.__price = value

    @abstractmethod
    def eat(self):
        ...
