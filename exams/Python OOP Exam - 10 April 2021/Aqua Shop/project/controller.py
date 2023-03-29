from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:

    def __init__(self):
        self.decorations_repository: DecorationRepository = DecorationRepository()
        self.aquariums = []

    @staticmethod
    def find_aquarium_by_name(name, somewhere):
        return next(filter(lambda a: a.name == name, somewhere))

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        valid_types = {"FreshwaterAquarium": FreshwaterAquarium, "SaltwaterAquarium": SaltwaterAquarium}

        try:
            new_aquarium = valid_types[aquarium_type](aquarium_name)

            self.aquariums.append(new_aquarium)

            return f"Successfully added {aquarium_type}."

        except KeyError:
            return "Invalid aquarium type."

    def add_decoration(self, decoration_type: str):
        valid_types = {"Ornament": Ornament, "Plant": Plant}

        try:
            new_decor = valid_types[decoration_type]()

            self.decorations_repository.add(new_decor)

            return f"Successfully added {decoration_type}."

        except KeyError:
            return "Invalid decoration type."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        try:
            found_aquarium: BaseAquarium = self.find_aquarium_by_name(aquarium_name, self.aquariums)

        except StopIteration:
            return

        found_decor = self.decorations_repository.find_by_type(decoration_type)

        if not found_decor:
            return f"There isn't a decoration of type {decoration_type}."

        self.decorations_repository.remove(found_decor)
        found_aquarium.add_decoration(found_decor)

        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        try:
            found_aquarium: BaseAquarium = self.find_aquarium_by_name(aquarium_name, self.aquariums)

        except StopIteration:
            return

        try:
            valid_types = {"FreshwaterFish": FreshwaterFish, "SaltwaterFish": SaltwaterFish}

            new_fish = valid_types[fish_type](fish_name, fish_species, price)

        except KeyError:
            return f"There isn't a fish of type {fish_type}."

        return found_aquarium.add_fish(new_fish)

    def feed_fish(self, aquarium_name: str):
        try:
            found_aquarium: BaseAquarium = self.find_aquarium_by_name(aquarium_name, self.aquariums)

        except StopIteration:
            return

        found_aquarium.feed()

        return f"Fish fed: {len(found_aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        try:
            found_aquarium: BaseAquarium = self.find_aquarium_by_name(aquarium_name, self.aquariums)

        except StopIteration:
            return

        sum_price_decors = sum(decor.price for decor in found_aquarium.decorations)
        sum_price_fish = sum(fish.price for fish in found_aquarium.fish)

        return f"The value of Aquarium {aquarium_name} is {sum_price_decors + sum_price_fish:.2f}."

    def report(self):
        return '\n'.join(str(aquarium) for aquarium in self.aquariums)
