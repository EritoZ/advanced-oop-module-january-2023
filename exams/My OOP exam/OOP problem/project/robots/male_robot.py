from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):

    _BASE_WEIGHT = 9

    def wight_increase(self):
        return 3
