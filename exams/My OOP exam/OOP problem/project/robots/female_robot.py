from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):

    _BASE_WEIGHT = 7

    def wight_increase(self):
        return 1