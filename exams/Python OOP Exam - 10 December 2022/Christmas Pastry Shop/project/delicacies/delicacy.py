from abc import ABC


class Delicacy(ABC):

    PORTION = ...

    def __init__(self, name, price: float):
        self.name = name
        self.portion = self.PORTION
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be null or whitespace!")

        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price cannot be less or equal to zero!")

        self.__price = value

    def details(self):
        return f"{self.__class__.__name__} {self.name}: {self.portion}g - {self.price:.2f}lv."
