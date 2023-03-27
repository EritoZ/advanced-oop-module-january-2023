import unittest

from car_manager import Car


class TestCarManager(unittest.TestCase):

    def setUp(self) -> None:
        self.car = Car('???', 'Bugatti', 2, 10)

    def test_make(self):
        self.assertEqual(self.car.make, '???')

    def test_make_returns_error(self):
        with self.assertRaises(Exception) as context:
            self.car.make = ''

        self.assertEqual(str(context.exception), "Make cannot be null or empty!")

    def test_model(self):
        self.assertEqual(self.car.model, 'Bugatti')

    def test_model_return_error(self):
        with self.assertRaises(Exception) as context:
            self.car.model = ''

        self.assertEqual(str(context.exception), "Model cannot be null or empty!")

    def test_fuel_consumption(self):
        self.assertEqual(self.car.fuel_consumption, 2)

    def test_fuel_consumption_error_if_zero(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = 0

        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_consumption_error_if_negative(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = -10

        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity(self):
        self.assertEqual(self.car.fuel_capacity, 10)

    def test_fuel_capacity_error_if_zero(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = 0

        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_capacity_error_if_negative(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = -10

        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount(self):
        self.assertEqual(self.car.fuel_amount, 0)

    def test_fuel_amount_error_if_negative(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_amount = -10

        self.assertEqual(str(context.exception), "Fuel amount cannot be negative!")

    def test_refuel(self):
        self.car.refuel(10)

        self.assertEqual(self.car.fuel_amount, 10)

    def test_refuel_if_fuel_is_over_capacity(self):
        self.car.refuel(20)

        self.assertEqual(self.car.fuel_amount, 10)

    def test_refuel_error_if_zero(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(0)

        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_error_if_negative(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(-10)

        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")

    def test_drive(self):
        self.car.fuel_amount = 10
        self.car.drive(50)

        self.assertEqual(self.car.fuel_amount, 9)

    def test_drive_error_fuel_not_enough_for_distance(self):
        with self.assertRaises(Exception) as context:
            self.car.drive(100)

        self.assertEqual(str(context.exception), "You don't have enough fuel to drive!")


if __name__ == '__main__':
    unittest.main()
