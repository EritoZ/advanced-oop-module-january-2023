from project.hardware.hardware import Hardware


class PowerHardware(Hardware):

    def __init__(self, name, capacity, memory):
        super().__init__(name, 'Power', capacity, memory)
