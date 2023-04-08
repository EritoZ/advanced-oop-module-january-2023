from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:

    def __init__(self):
        self.robots = []
        self.services = []

    @property
    def _valid_services(self):
        return {"MainService": MainService, "SecondaryService": SecondaryService}

    @property
    def _valid_robots(self):
        return {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    @staticmethod
    def _find_robot_or_service_by_name(name, somewhere):
        return next(filter(lambda x: x.name == name, somewhere))

    def add_service(self, service_type: str, name: str):
        try:
            new_service = self._valid_services[service_type](name)

            self.services.append(new_service)

            return f"{service_type} is successfully added."

        except KeyError:
            raise Exception("Invalid service type!")

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        try:
            new_robot = self._valid_robots[robot_type](name, kind, price)

            self.robots.append(new_robot)

            return f"{robot_type} is successfully added."

        except KeyError:
            raise Exception("Invalid robot type!")

    def add_robot_to_service(self, robot_name: str, service_name: str):
        found_robot: BaseRobot = self._find_robot_or_service_by_name(robot_name, self.robots)
        found_service: BaseService = self._find_robot_or_service_by_name(service_name, self.services)

        valid_robot_services = {'MaleRobot': 'MainService', 'FemaleRobot': 'SecondaryService'}

        if valid_robot_services[found_robot.__class__.__name__] != found_service.__class__.__name__:
            return "Unsuitable service."

        if found_service.capacity == len(found_service.robots):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(found_robot)
        found_service.robots.append(found_robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        found_service: BaseService = self._find_robot_or_service_by_name(service_name, self.services)

        try:
            found_robot: BaseRobot = self._find_robot_or_service_by_name(robot_name, found_service.robots)

            found_service.robots.remove(found_robot)
            self.robots.append(found_robot)

            return f"Successfully removed {robot_name} from {service_name}."

        except StopIteration:
            raise Exception("No such robot in this service!")

    def feed_all_robots_from_service(self, service_name: str):
        found_service: BaseService = self._find_robot_or_service_by_name(service_name, self.services)

        [robot.eating() for robot in found_service.robots]

        return f"Robots fed: {len(found_service.robots)}."

    def service_price(self, service_name: str):
        found_service: BaseService = self._find_robot_or_service_by_name(service_name, self.services)

        total_price = sum(r.price for r in found_service.robots)

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        services_details = [s.details() for s in self.services]

        return '\n'.join(services_details)
    