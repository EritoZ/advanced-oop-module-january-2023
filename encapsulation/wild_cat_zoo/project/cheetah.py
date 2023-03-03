from project.animal import Animal


class Cheetah(Animal):

    def __init__(self, name: str, gender: str, age: int):
        self.money_for_care = 60
        super().__init__(name, gender, age, self.money_for_care)
