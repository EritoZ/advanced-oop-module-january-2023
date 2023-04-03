from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):

    def __init__(self, family_name, salary_one: float, salary_two: float, *children):
        self._MEMBERS_COUNT = 2 + len(children)
        super().__init__(family_name, salary_one + salary_two, self._MEMBERS_COUNT)
        self.children = list(children)
        self.room_cost = 30
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count
        self.calculate_expenses(self.children, self.appliances)
