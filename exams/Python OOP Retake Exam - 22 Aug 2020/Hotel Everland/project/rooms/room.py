from abc import ABC, abstractmethod


class Room(ABC):

    _MEMBERS_COUNT = ...

    def __init__(self, family_name, budget: float, members_count):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.appliances = []
        self.expenses = 0
        self.room_cost = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")

        self.__expenses = value

    def calculate_expenses(self, *args):
        total_sum = 0

        for lst in args:
            total_sum += sum(el.cost for el in lst)

        total_sum_month = total_sum * 30

        self.expenses = total_sum_month
