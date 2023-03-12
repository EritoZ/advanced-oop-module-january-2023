from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    @staticmethod
    def find_musician(name, somewhere):
        return next(filter(lambda m: m.name == name, somewhere))

    @staticmethod
    def find_band(name, somewhere):
        return next(filter(lambda b: b.name == name, somewhere))

    @staticmethod
    def find_concert(place, somewhere):
        return next(filter(lambda c: c.place == place, somewhere))

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ("Guitarist", "Drummer", "Singer"):
            raise ValueError("Invalid musician type!")

        try:
            self.find_musician(name, self.musicians)

            raise Exception(f"{name} is already a musician!")

        except StopIteration:
            pass

        if musician_type == 'Guitarist':
            self.musicians.append(Guitarist(name, age))

        elif musician_type == 'Drummer':
            self.musicians.append(Drummer(name, age))

        else:
            self.musicians.append(Singer(name, age))

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):

        try:
            self.find_band(name, self.bands)

            raise Exception(f"{name} band is already created!")

        except StopIteration:
            self.bands.append(Band(name))

            return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):

        try:
            concert_object: Concert = self.find_concert(place, self.concerts)

            raise Exception(f"{place} is already registered for {concert_object.genre} concert!")

        except StopIteration:
            self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))

            return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):

        try:
            musician_object = self.find_musician(musician_name, self.musicians)

        except StopIteration:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            band_object: Band = self.find_band(band_name, self.bands)

        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        band_object.members.append(musician_object)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):

        try:
            band_object: Band = self.find_band(band_name, self.bands)

        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        try:
            band_member = self.find_musician(musician_name, band_object.members)

        except StopIteration:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band_object.members.remove(band_member)

        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band_object: Band = self.find_band(band_name, self.bands)

        all_members = {
            'Drummer': [],
            'Singer': [],
            'Guitarist': []
        }

        [all_members[member.__class__.__name__].append(member) for member in band_object.members]

        if not all(all_members.values()):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        needed_skills_for_concert = {
            'Rock': {
                'Drummer': {'play the drums with drumsticks'},
                'Singer': {'sing high pitch notes'},
                'Guitarist': {'play rock'}
            },
            'Metal': {
                'Drummer': {'play the drums with drumsticks'},
                'Singer': {'sing low pitch notes'},
                'Guitarist': {'play metal'}
            },
            'Jazz': {
                'Drummer': {'play the drums with drum brushes'},
                'Singer': {'sing high pitch notes', 'sing low pitch notes'},
                'Guitarist': {'play jazz'}
            }
        }

        for concert_genre in needed_skills_for_concert:
            ready_musicians = 0

            for type_musician in needed_skills_for_concert[concert_genre]:
                needed_skills = needed_skills_for_concert[concert_genre][type_musician]

                matched_skills = [needed_skills.issubset(member.skills) for member in all_members[type_musician]]

                if not all(matched_skills):
                    break

                ready_musicians += 1

            if ready_musicians == 3:
                concert_object: Concert = self.find_concert(concert_place, self.concerts)

                profit = (concert_object.audience * concert_object.ticket_price) - concert_object.expenses

                return f"{band_name} gained {profit:.2f}$ from the {concert_genre} concert in {concert_place}."

        raise Exception(f"The {band_name} band is not ready to play at the concert!")
