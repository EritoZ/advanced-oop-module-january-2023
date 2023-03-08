from project.room import Room


class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)
        self.guests += room.guests

    def search_room(self, room_number):
        try:
            room_object = next(filter(lambda x: x.number == room_number, self.rooms))

            return room_object

        except StopIteration:
            pass

    def take_room(self, room_number, people):

        room_object: Room = self.search_room(room_number)

        room_status = room_object.take_room(people)

        if room_status is not None:
            return room_status

        self.guests += room_object.guests

    def free_room(self, room_number):

        room_object: Room = self.search_room(room_number)

        room_guests = room_object.guests

        room_status = room_object.free_room()

        if room_status is not None:
            return room_status

        self.guests -= room_guests

    def status(self):
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]

        return f'''Hotel {self.name} has {self.guests} total guests
Free rooms: {', '.join(free_rooms)}
Taken rooms: {', '.join(taken_rooms)}'''
