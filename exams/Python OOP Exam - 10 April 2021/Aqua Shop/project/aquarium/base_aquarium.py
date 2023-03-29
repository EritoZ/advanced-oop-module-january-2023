from abc import ABC

from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):
    DEFAULT_CAPACITY = ...

    def __init__(self, name):
        self.name = name
        self.capacity = self.DEFAULT_CAPACITY
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Aquarium name cannot be an empty string.")

        self.__name = value

    def calculate_comfort(self):
        sum_comfort = sum(dec.comfort for dec in self.decorations)

        return sum_comfort

    def add_fish(self, fish: BaseFish):
        if self.capacity == len(self.fish):
            return "Not enough capacity."

        correct_aquariums_for_fishes = {'FreshwaterFish': 'FreshwaterAquarium', 'SaltwaterFish': 'SaltwaterAquarium'}
        type_fish = fish.__class__.__name__

        if self.__class__.__name__ != correct_aquariums_for_fishes[type_fish]:
            return "Water not suitable."

        self.fish.append(fish)

        return f"Successfully added {type_fish} to {self.name}."

    def remove_fish(self, fish: BaseFish):
        try:
            self.fish.remove(fish)

        except ValueError:
            return

    def add_decoration(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        [fish.eat() for fish in self.fish]

    def __str__(self):
        message = [f'{self.name}:', f'Fish: {" ".join(fish.name for fish in self.fish) if self.fish else "none"}',
                   f'Decorations: {len(self.decorations)}', f'Comfort: {self.calculate_comfort()}']

        return '\n'.join(message)
