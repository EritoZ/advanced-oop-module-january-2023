from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):

    _MEMBERS_COUNT = 2

    def __init__(self, family_name, pension_one: float, pension_two: float):
        super().__init__(family_name, pension_one + pension_two, self._MEMBERS_COUNT)
        self.room_cost = 15
        self.appliances = [TV(), Fridge(), Stove()] * self.members_count
        self.calculate_expenses(self.appliances)
