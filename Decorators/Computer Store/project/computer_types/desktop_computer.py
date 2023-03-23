from project.computer_types.computer import Computer


class DesktopComputer(Computer):

    def eligible_processors(self):
        return {'AMD Ryzen 7 5700G': 500, 'Intel Core i5-12600K': 600, 'Apple M1 Max': 1800}

    def max_ram(self):
        # 128
        return 6

    def type_comp(self):
        return 'desktop computer'
