from typing import List

from project.rooms.room import Room


class Everland:

    def __init__(self):
        self.rooms: List[Room] = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0

        for room in self.rooms:

            total_consumption += room.expenses + room.room_cost

        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        message = []

        for room in self.rooms.copy():

            total_expenses = room.expenses + room.room_cost

            if room.budget >= total_expenses:
                room.budget -= total_expenses

                message.append(f"{room.family_name} paid {total_expenses:.2f}$ and have {room.budget:.2f}$"
                               f" left.")
            else:
                message.append(f"{room.family_name} does not have enough budget and must leave the hotel.")

                self.rooms.remove(room)

        return '\n'.join(message)

    def status(self):
        population = sum(room.members_count for room in self.rooms)
        message = [f'Total population: {population}']

        for room in self.rooms:

            message.append(f'{room.family_name} with {room.members_count} members. Budget:'
                           f' {room.budget:.2f}$, Expenses:'
                           f' {room.expenses:.2f}$')

            if room.children:
                for i, child in enumerate(room.children, 1):
                    message.append(f'--- Child {i} monthly cost: {child.cost * 30:.2f}$')

            appliances_monthly_costs = [appliance.get_monthly_expense() for appliance in room.appliances]

            message.append(f'--- Appliances monthly cost: {sum(appliances_monthly_costs):.2f}$')

        return '\n'.join(message)
