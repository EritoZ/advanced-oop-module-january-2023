from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    DEFAULT_SIZE = 5

    def eat(self):
        self.size += 2
