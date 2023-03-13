from project.delicacies.gingerbread import Gingerbread

from project.delicacies.stolen import Stolen

from project.booths.open_booth import OpenBooth

from project.booths.private_booth import PrivateBooth

from project.booths.booth import Booth


class ChristmasPastryShopApp:

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    @staticmethod
    def find_delicacy(name, location):
        return next(filter(lambda d: d.name == name, location))

    @staticmethod
    def find_booth(number, location):
        return next(filter(lambda b: b.booth_number == number, location))

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        valid_delicacies = ('Gingerbread', 'Stolen')

        if type_delicacy not in valid_delicacies:
            raise ValueError(f"{type_delicacy} is not on our delicacy menu!")

        try:
            self.find_delicacy(name, self.delicacies)

            raise Exception(f"{name} already exists!")

        except StopIteration:

            if type_delicacy == 'Gingerbread':
                new_delicacy = Gingerbread(name, price)

            else:
                new_delicacy = Stolen(name, price)

            self.delicacies.append(new_delicacy)

            return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        valid_booths = ('Open Booth', 'Private Booth')

        if type_booth not in valid_booths:
            raise Exception(f"{type_booth} is not a valid booth!")

        try:
            self.find_booth(booth_number, self.booths)

            raise Exception(f"Booth number {booth_number} already exists!")

        except StopIteration:

            if type_booth == 'Open Booth':
                new_booth = OpenBooth(booth_number, capacity)

            else:
                new_booth = PrivateBooth(booth_number, capacity)

            self.booths.append(new_booth)

            return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):

        try:
            # do not touch this
            found_booth: Booth = next(
                filter(lambda b: not b.is_reserved and b.capacity >= number_of_people, self.booths))

            found_booth.reserve(number_of_people)

            return f"Booth {found_booth.booth_number} has been reserved for {number_of_people} people."

        except StopIteration:
            raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        try:
            found_booth: Booth = self.find_booth(booth_number, self.booths)

        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")

        try:
            found_delicacy = self.find_delicacy(delicacy_name, self.delicacies)

        except StopIteration:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        found_booth.delicacy_orders.append(found_delicacy)

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):

        found_booth: Booth = self.find_booth(booth_number, self.booths)

        orders_profit = [order.price for order in found_booth.delicacy_orders]

        total_profit = sum(orders_profit) + found_booth.price_for_reservation

        self.income += total_profit

        found_booth.price_for_reservation = 0
        found_booth.delicacy_orders.clear()
        found_booth.is_reserved = False

        return f'''Booth {booth_number}:
Bill: {total_profit:.2f}lv.'''

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
