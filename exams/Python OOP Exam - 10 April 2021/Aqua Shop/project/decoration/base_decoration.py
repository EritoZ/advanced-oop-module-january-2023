from abc import ABC


class BaseDecoration(ABC):
    COMFORT = ...
    PRICE = ...

    def __init__(self):
        self.comfort = self.COMFORT
        self.price = self.PRICE
