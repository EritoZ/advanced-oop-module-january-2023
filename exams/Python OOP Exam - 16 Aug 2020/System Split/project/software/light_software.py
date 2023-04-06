from project.software.software import Software


class LightSoftware(Software):

    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, 'Light', capacity_consumption, memory_consumption)
