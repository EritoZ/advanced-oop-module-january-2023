from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):

    _INITIAL_PORTION_SIZE = 245

    def __init__(self, name, price):
        super().__init__(name, self._INITIAL_PORTION_SIZE, price)
