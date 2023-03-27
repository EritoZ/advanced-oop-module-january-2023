from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class Bakery:

    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty string or white space!")

        self.__name = value

    @staticmethod
    def search_food_or_drink_by_name(name, somewhere):
        return next(filter(lambda x: x.name == name, somewhere))

    @staticmethod
    def search_table_by_number(number, somewhere):
        return next(filter(lambda t: t.table_number == number, somewhere))

    def add_food(self, food_type: str, name: str, price: float):

        try:
            matched_food: BakedFood = self.search_food_or_drink_by_name(name, self.food_menu)

            raise Exception(f"{matched_food.__class__.__name__} {name} is already in the menu!")

        except StopIteration:
            ...

        types = {'Bread': Bread, 'Cake': Cake}

        new_food = types[food_type](name, price)

        self.food_menu.append(new_food)

        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):

        try:
            matched_drink: Drink = self.search_food_or_drink_by_name(name, self.drinks_menu)

            raise Exception(f"{matched_drink.__class__.__name__} {name} is already in the menu!")

        except StopIteration:
            ...

        types = {'Tea': Tea, 'Water': Water}

        new_drink = types[drink_type](name, portion, brand)

        self.drinks_menu.append(new_drink)

        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):

        try:
            self.search_table_by_number(table_number, self.tables_repository)

            raise Exception(f"Table {table_number} is already in the bakery!")

        except StopIteration:
            ...

        types = {'InsideTable': InsideTable, 'OutsideTable': OutsideTable}

        new_table = types[table_type](table_number, capacity)

        self.tables_repository.append(new_table)

        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        try:
            matched_table: Table = next(filter(lambda t: not t.is_reserved and t.capacity >= number_of_people,
                                        self.tables_repository))

            matched_table.reserve(number_of_people)

            return f"Table {matched_table.table_number} has been reserved for {number_of_people} people"

        except StopIteration:
            return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        try:
            matched_table: Table = self.search_table_by_number(table_number, self.tables_repository)

        except StopIteration:
            return f"Could not find table {table_number}"

        found_food = [f'Table {table_number} ordered:']
        not_found_food = [f'{self.name} does not have in the menu:']

        for food_name in args:
            try:
                matched_food: BakedFood = self.search_food_or_drink_by_name(food_name, self.food_menu)

                matched_table.order_food(matched_food)
                found_food.append(str(matched_food))

            except StopIteration:
                not_found_food.append(food_name)

        return '\n'.join(found_food + not_found_food)

    def order_drink(self, table_number: int, *args):
        try:
            matched_table: Table = self.search_table_by_number(table_number, self.tables_repository)

        except StopIteration:
            return f"Could not find table {table_number}"

        found_drinks = [f'Table {table_number} ordered:']
        not_found_drinks = [f'{self.name} does not have in the menu:']

        for drink_name in args:
            try:
                matched_drink: Drink = self.search_food_or_drink_by_name(drink_name, self.drinks_menu)

                matched_table.order_drink(matched_drink)
                found_drinks.append(str(matched_drink))

            except StopIteration:
                not_found_drinks.append(drink_name)

        return '\n'.join(found_drinks + not_found_drinks)

    def leave_table(self, table_number: int):
        found_table: Table = self.search_table_by_number(table_number, self.tables_repository)
        bill = found_table.get_bill()

        self.total_income += bill
        found_table.clear()

        return f'''Table: {table_number}
Bill: {bill:.2f}'''

    def get_free_tables_info(self):
        tables_info = (table.free_table_info() for table in self.tables_repository if table.free_table_info())

        return '\n'.join(tables_info)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
