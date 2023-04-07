from abc import ABC, abstractmethod

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):

    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0

    @property
    def is_reserved(self):
        return bool(self.number_of_people)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if value not in self.range_table_numbers():
            t_index = self.__class__.__name__.index('T')
            type_table = self.__class__.__name__[:t_index]

            raise ValueError(f"{type_table} table's number must be between "
                             f"{self.range_table_numbers()[0]} and {self.range_table_numbers()[-1]} inclusive!")

        self.__table_number = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")

        self.__capacity = value

    @property
    @abstractmethod
    def range_table_numbers(self):
        ...

    def reserve(self, number_of_people: int):
        self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        bill = sum(x.price for x in self.food_orders + self.drink_orders)

        return bill

    def clear(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0

    def free_table_info(self):
        if not self.is_reserved:
            return f'''Table: {self.table_number}
Type: {self.__class__.__name__}
Capacity: {self.capacity}'''
