from project.rooms.room import Room


class AloneOld(Room):

    _MEMBERS_COUNT = 1

    def __init__(self, family_name, pension: float):
        super().__init__(family_name, pension, self._MEMBERS_COUNT)
        self.room_cost = 10
