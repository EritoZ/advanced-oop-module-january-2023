from project.animals.animal import Mammal
from project.food import Food


class Mouse(Mammal):

    def make_sound(self):
        return "Squeak"

    def feed(self, food: Food):
        mouse_diet = ["Vegetable", "Fruit"]
        given_food = food.__class__.__name__

        if given_food in mouse_diet:
            self.weight += 0.1 * food.quantity
            self.food_eaten += food.quantity

        return f"{self.__class__.__name__} does not eat {given_food}!"


class Dog(Mammal):

    def make_sound(self):
        return "Woof!"

    def feed(self, food: Food):
        given_food = food.__class__.__name__

        if given_food != "Meat":
            return f"{self.__class__.__name__} does not eat {given_food}!"

        self.weight += 0.4 * food.quantity
        self.food_eaten += food.quantity


class Cat(Mammal):

    def make_sound(self):
        return "Meow"

    def feed(self, food: Food):
        cat_diet = ["Vegetable", "Meat"]
        given_food = food.__class__.__name__

        if given_food in cat_diet:
            self.weight += 0.3 * food.quantity
            self.food_eaten += food.quantity

        return f"{self.__class__.__name__} does not eat {given_food}!"


class Tiger(Mammal):

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food: Food):
        given_food = food.__class__.__name__

        if given_food != "Meat":
            return f"{self.__class__.__name__} does not eat {given_food}!"

        self.weight += 1 * food.quantity
        self.food_eaten += food.quantity
