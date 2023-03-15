from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:

    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.receipt_id = 1

    @staticmethod
    def search_client(phone_number, somewhere):
        return next(filter(lambda c: c.phone_number == phone_number, somewhere))

    def check_status_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def register_client(self, client_phone_number: str):

        try:
            self.search_client(client_phone_number, self.clients_list)

            raise Exception("The client has already been registered!")

        except StopIteration:

            new_client = Client(client_phone_number)

            self.clients_list.append(new_client)

            return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        meals_type = ("Starter", "MainDish", "Dessert")

        [self.menu.append(meal) for meal in meals if meal.__class__.__name__ in meals_type]

    def show_menu(self):

        self.check_status_menu()

        menu_details = '\n'.join([meal.details() for meal in self.menu])

        return menu_details

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):

        self.check_status_menu()

        try:
            current_client = self.search_client(client_phone_number, self.clients_list)

        except StopIteration:
            current_client = Client(client_phone_number)
            self.clients_list.append(current_client)

        ordered_meals = [meal for meal in self.menu if meal.name in meal_names_and_quantities]

        if len(ordered_meals) < len(meal_names_and_quantities):
            not_found = tuple(set(meal_names_and_quantities).difference(meal.name for meal in ordered_meals))

            raise Exception(f"{not_found[0]} is not on the menu!")

        for meal in ordered_meals:
            if meal_names_and_quantities[meal.name] > meal.quantity:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal.name}!")

        meal_types = {"Starter": Starter, "MainDish": MainDish, "Dessert": Dessert}

        for meal in ordered_meals:
            quantity = meal_names_and_quantities[meal.name]

            what_meal = meal_types[meal.__class__.__name__](meal.name, meal.price, quantity)

            current_client.shopping_cart.append(what_meal)
            current_client.bill += meal.price * quantity
            meal.quantity -= quantity

        return f"Client {client_phone_number} successfully ordered" \
               f" {', '.join([meal.name for meal in current_client.shopping_cart])} for {current_client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        current_client: Client = self.search_client(client_phone_number, self.clients_list)

        if not current_client.shopping_cart:
            raise Exception("There are no ordered meals!")

        client_orders_dict = {meal.name: meal.quantity for meal in current_client.shopping_cart}

        for meal in self.menu:
            if meal.name in client_orders_dict:
                meal.quantity += client_orders_dict[meal.name]

        current_client.shopping_cart = []
        current_client.bill = 0.0

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        current_client: Client = self.search_client(client_phone_number, self.clients_list)

        if not current_client.shopping_cart:
            raise Exception("There are no ordered meals!")

        message = f"Receipt #{self.receipt_id} with total amount of {current_client.bill:.2f} was successfully paid for" \
                  f" {client_phone_number}."

        self.receipt_id += 1

        current_client.bill = 0.0
        current_client.shopping_cart = []

        return message

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
