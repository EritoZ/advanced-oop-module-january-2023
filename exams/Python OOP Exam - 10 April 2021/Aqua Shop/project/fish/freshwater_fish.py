from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    DEFAULT_SIZE = 3

    def eat(self):
        self.size += 3
