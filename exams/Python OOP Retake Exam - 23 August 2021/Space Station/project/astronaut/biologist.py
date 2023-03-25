from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):

    DEFAULT_OXYGEN_AMOUNT = 70

    def __init__(self, name, oxygen=DEFAULT_OXYGEN_AMOUNT):
        super().__init__(name, oxygen)

    def oxygen_decrease(self):
        return 5
