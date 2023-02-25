class NegativeNumberError(Exception):
    pass


def already_ordered_error(name):
    return f"Pizza {name} already prepared, and we can't make any changes!"


class PizzaDelivery:

    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        try:
            if self.ordered:
                return already_ordered_error(self.name)

            self.ingredients[ingredient] += quantity

        except KeyError:
            self.ingredients[ingredient] = quantity

        self.price += quantity * price_per_quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        try:
            if self.ordered:
                return already_ordered_error(self.name)

            elif self.ingredients[ingredient] - quantity < 0:
                raise NegativeNumberError

            self.ingredients[ingredient] -= quantity
            self.price -= quantity * price_per_quantity

        except KeyError:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

        except NegativeNumberError:
            return f"Please check again the desired quantity of {ingredient}!"

    def make_order(self):
        if self.ordered:
            return already_ordered_error(self.name)

        self.ordered = True
        ingredients_message = ', '.join([f'{ingredient}: {quantity}'
                                         for ingredient, quantity in self.ingredients.items()])

        return f"You've ordered pizza {self.name} prepared with {ingredients_message}" \
               f" and the price will be {self.price}lv."


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
