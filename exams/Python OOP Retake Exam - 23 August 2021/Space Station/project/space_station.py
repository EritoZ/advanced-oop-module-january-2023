from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.unsuccessful_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        found_astro = self.astronaut_repository.find_by_name(name)

        if found_astro:
            return f"{name} is already added."

        valid_types = {"Biologist": Biologist, "Geodesist": Geodesist, "Meteorologist": Meteorologist}

        try:
            new_astronaut = valid_types[astronaut_type](name)

            self.astronaut_repository.add(new_astronaut)

            return f"Successfully added {astronaut_type}: {name}."

        except KeyError:
            raise Exception("Astronaut type is not valid!")

    def add_planet(self, name: str, items: str):
        found_planet = self.planet_repository.find_by_name(name)

        if found_planet:
            return f"{name} is already added."

        new_planet = Planet(name)

        items = items.split(", ")

        new_planet.items = items

        self.planet_repository.add(new_planet)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        found_astro = self.astronaut_repository.find_by_name(name)

        if not found_astro:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(found_astro)

        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):

        for astro in self.astronaut_repository.astronauts:
            astro.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        found_planet: Planet = self.planet_repository.find_by_name(planet_name)

        if not found_planet:
            raise Exception("Invalid planet name!")

        suitable_astros = [astro for astro in self.astronaut_repository.astronauts if astro.oxygen > 30]

        if not suitable_astros:
            raise Exception("You need at least one astronaut to explore the planet!")

        suitable_astros = sorted(suitable_astros, key=lambda a: -a.oxygen)

        useful_astros = 0

        for astro in suitable_astros[:5]:
            useful_astros += 1

            while astro.oxygen > 0:
                found_item = found_planet.items.pop()

                astro.backpack.append(found_item)

                astro.breathe()

                if not found_planet.items:
                    self.successful_missions += 1
                    return f"Planet: {planet_name} was explored. {useful_astros}" \
                           f" astronauts participated in collecting items."

        if found_planet.items:
            self.unsuccessful_missions += 1
            return "Mission is not completed."

    def report(self):
        message = [f'{self.successful_missions} successful missions!',
                   f'{self.unsuccessful_missions} missions were not completed!',
                   'Astronauts\' info:']

        for astro in self.astronaut_repository.astronauts:
            message.append(f'Name: {astro.name}')
            message.append(f'Oxygen: {astro.oxygen}')
            message.append(f'Backpack items: {", ".join(astro.backpack) if astro.backpack else "none"}')

        return '\n'.join(message)
