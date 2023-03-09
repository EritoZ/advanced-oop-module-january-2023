from project.customer import Customer
from project.dvd import DVD


class MovieWorld:

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer_object: Customer = next(filter(lambda c: c.id == customer_id, self.customers))
        customer_name = customer_object.name

        dvd_object: DVD = next(filter(lambda d: d.id == dvd_id, self.dvds))
        dvd_name = dvd_object.name

        if dvd_object in customer_object.rented_dvds:
            return f"{customer_name} has already rented {dvd_name}"

        if dvd_object.is_rented:
            return "DVD is already rented"

        if customer_object.age < dvd_object.age_restriction:
            return f"{customer_name} should be at least {dvd_object.age_restriction} to rent this movie"

        dvd_object.is_rented = True
        customer_object.rented_dvds.append(dvd_object)

        return f"{customer_name} has successfully rented {dvd_object.name}"

    def return_dvd(self, customer_id, dvd_id):
        try:
            customer_object: Customer = next(filter(lambda c: c.id == customer_id, self.customers))
            customer_name = customer_object.name

            dvd_object: DVD = next(filter(lambda d: d.id == dvd_id, customer_object.rented_dvds))

            customer_object.rented_dvds.remove(dvd_object)
            dvd_object.is_rented = False

            return f"{customer_name} has successfully returned {dvd_object.name}"

        except StopIteration:
            return f"{customer_name} does not have that DVD"

    def __repr__(self):
        message = [str(customer) for customer in self.customers]
        message.extend(str(dvd) for dvd in self.dvds)

        return '\n'.join(message)
