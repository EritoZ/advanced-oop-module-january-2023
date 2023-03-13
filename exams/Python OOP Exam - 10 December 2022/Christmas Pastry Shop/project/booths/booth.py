from abc import ABC, abstractmethod


class Booth(ABC):

    def __init__(self, booth_number: int, capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders = []
        self.price_for_reservation = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Capacity cannot be a negative number!")

        self.__capacity = value

    @property
    def price_for_reservation(self):
        return self.__price_for_reservation

    @price_for_reservation.setter
    def price_for_reservation(self, value):
        self.is_reserved = True
        self.__price_for_reservation = value

    @property
    @abstractmethod
    def price(self):
        pass

    def reserve(self, number_of_people: int):
        price_reservation = number_of_people * self.price()

        self.price_for_reservation = price_reservation
