import unittest
from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):

    def setUp(self):
        self.vehicle = Vehicle(10, 100)

    def test_default_fuel_consumption(self):
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)

    def test_drive(self):
        self.vehicle.drive(4)

        self.assertEqual(self.vehicle.fuel, 5)

    def test_drive_error(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(10)

        self.assertEqual(str(context.exception), "Not enough fuel")

    def test_refuel(self):
        self.vehicle.fuel = 5
        self.vehicle.refuel(4)

        self.assertEqual(self.vehicle.fuel, 9)

    def test_refuel_error(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(10)

        self.assertEqual(str(context.exception), "Too much fuel")

    def test_str_method(self):
        message = f"The vehicle has 100 horse power with 10 fuel left and 1.25 fuel consumption"

        self.assertEqual(str(self.vehicle), message)


if __name__ == "__main__":
    unittest.main()
