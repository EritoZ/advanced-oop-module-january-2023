from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:

    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        valid_comps = {"Desktop Computer": DesktopComputer, "Laptop": Laptop}

        if type_computer not in valid_comps:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        new_comp: Computer = valid_comps[type_computer](manufacturer, model)

        message = new_comp.configure_computer(processor, ram)

        self.warehouse.append(new_comp)

        return message

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        try:
            found_comp = next(filter(lambda c: c.price <= client_budget and c.processor == wanted_processor
                                               and c.ram >= wanted_ram, self.warehouse))

        except StopIteration:
            raise Exception("Sorry, we don't have a computer for you.")

        self.warehouse.remove(found_comp)

        self.profits += client_budget - found_comp.price

        return f"{found_comp} sold for {client_budget}$."
