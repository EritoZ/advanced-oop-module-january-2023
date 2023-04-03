from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):

    _MEMBERS_COUNT = 1

    def __init__(self, family_name, salary: float):
        super().__init__(family_name, salary, self._MEMBERS_COUNT)
        self.room_cost = 10
        self.appliances = [TV()] * self.members_count
        self.calculate_expenses(self.appliances)
