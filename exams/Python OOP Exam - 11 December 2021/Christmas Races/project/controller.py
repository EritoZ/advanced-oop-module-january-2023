from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


# could be optimised with less repeated code, but I will do it later 
class Controller:

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    @staticmethod
    def __search_car(model, somewhere):
        return next(filter(lambda c: c.model == model, somewhere))

    @staticmethod
    def __search_driver_or_race(name, somewhere):
        return next(filter(lambda x: x.name == name, somewhere))

    def create_car(self, car_type: str, model: str, speed_limit: int):
        valid_types = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

        if car_type not in valid_types:
            return

        try:
            self.__search_car(model, self.cars)

            raise Exception(f"Car {model} is already created!")

        except StopIteration:
            new_car = valid_types[car_type](model, speed_limit)

            self.cars.append(new_car)

            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        try:
            self.__search_driver_or_race(driver_name, self.drivers)

            raise Exception(f"Driver {driver_name} is already created!")

        except StopIteration:

            new_driver = Driver(driver_name)

            self.drivers.append(new_driver)

            return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        try:
            self.__search_driver_or_race(race_name, self.races)

            raise Exception(f"Race {race_name} is already created!")

        except StopIteration:
            new_race = Race(race_name)

            self.races.append(new_race)

            return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        try:
            found_driver: Driver = self.__search_driver_or_race(driver_name, self.drivers)

        except StopIteration:
            raise Exception(f"Driver {driver_name} could not be found!")

        try:
            matched_car = next(filter(lambda c: c.__class__.__name__ == car_type and not c.is_taken, self.cars[::-1]))

        except StopIteration:
            raise Exception(f"Car {car_type} could not be found!")

        if found_driver.car:
            old_car = found_driver.car
            old_car.is_taken = False

            found_driver.car = matched_car
            matched_car.is_taken = True

            return f"Driver {driver_name} changed his car from {old_car.model} to {matched_car.model}."

        found_driver.car = matched_car
        matched_car.is_taken = True

        return f"Driver {driver_name} chose the car {matched_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        try:
            found_race: Race = self.__search_driver_or_race(race_name, self.races)

        except StopIteration:
            raise Exception(f"Race {race_name} could not be found!")

        try:
            found_driver: Driver = self.__search_driver_or_race(driver_name, self.drivers)

        except StopIteration:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not found_driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if found_driver in found_race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        found_race.drivers.append(found_driver)

        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        try:
            found_race: Race = self.__search_driver_or_race(race_name, self.races)

        except StopIteration:
            raise Exception(f"Race {race_name} could not be found!")

        if len(found_race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        winners = sorted(found_race.drivers, key=lambda d: -d.car.speed_limit)[:3]

        message = []

        for winner in winners:
            winner.number_of_wins += 1
            message.append(f"Driver {winner.name} wins the {race_name} race with a speed of {winner.car.speed_limit}.")

        return '\n'.join(message)
