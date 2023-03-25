from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):

    DEFAULT_OXYGEN_AMOUNT = 50

    def __init__(self, name, oxygen=DEFAULT_OXYGEN_AMOUNT):
        super().__init__(name, oxygen)