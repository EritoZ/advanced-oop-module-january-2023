from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    @staticmethod
    def search_horse_or_jockey(name, somewhere):
        return next(filter(lambda x: x.name == name, somewhere))

    @staticmethod
    def search_race(r_type, somewhere):
        return next(filter(lambda r: r.race_type == r_type, somewhere))

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        try:
            self.search_horse_or_jockey(horse_name, self.horses)

            raise Exception(f"Horse {horse_name} has been already added!")

        except StopIteration:
            ...

        valid_horses = {'Appaloosa': Appaloosa, 'Thoroughbred': Thoroughbred}

        try:
            new_horse = valid_horses[horse_type](horse_name, horse_speed)

            self.horses.append(new_horse)

            return f"{horse_type} horse {horse_name} is added."

        except KeyError:
            ...

    def add_jockey(self, jockey_name: str, age: int):
        try:
            self.search_horse_or_jockey(jockey_name, self.jockeys)

            raise Exception(f"Jockey {jockey_name} has been already added!")

        except StopIteration:
            new_jockey = Jockey(jockey_name, age)

            self.jockeys.append(new_jockey)

            return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):

        try:
            self.search_race(race_type, self.horse_races)

            raise Exception(f"Race {race_type} has been already created!")

        except StopIteration:
            new_race = HorseRace(race_type)

            self.horse_races.append(new_race)

            return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):

        try:
            jockey_object: Jockey = self.search_horse_or_jockey(jockey_name, self.jockeys)

        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        free_horses = [horse for horse in self.horses if horse.__class__.__name__ == horse_type and not horse.is_taken]

        if not free_horses:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey_object.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        taken_horse = free_horses[-1]

        jockey_object.horse = taken_horse
        taken_horse.is_taken = True

        return f"Jockey {jockey_name} will ride the horse {taken_horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):

        try:
            searched_race: HorseRace = self.search_race(race_type, self.horse_races)

        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        try:
            searched_jockey: Jockey = self.search_horse_or_jockey(jockey_name, self.jockeys)

        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if searched_jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if searched_jockey in searched_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        searched_race.jockeys.append(searched_jockey)

        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):

        try:
            searched_race: HorseRace = self.search_race(race_type, self.horse_races)

        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        if len(searched_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner: Jockey = max(searched_race.jockeys, key=lambda j: j.horse.speed)

        return f"The winner of the {race_type} race," \
               f" with a speed of {winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."
