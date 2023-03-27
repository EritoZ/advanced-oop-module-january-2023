import unittest

from test_worker import Worker


class TestWorker(unittest.TestCase):

    def setUp(self) -> None:
        self.worker = Worker('???', 10, 1)

    def test_if_the_worker_is_initialized_with_the_correct_name_salary_and_energy(self):
        self.assertEqual(self.worker.name, '???')
        self.assertEqual(self.worker.salary, 10)
        self.assertEqual(self.worker.energy, 1)

    def test_if_the_workers_energy_is_incremented_after_the_rest_method_is_called(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 2)

    def test_if_an_error_is_raised_if_the_worker_tries_to_work_with_negative_energy_or_equal_to_0(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as message:
            self.worker.work()

        self.assertEqual(str(message.exception), 'Not enough energy.')

        self.worker.energy = -1

        with self.assertRaises(Exception) as message:
            self.worker.work()

        self.assertEqual(str(message.exception), 'Not enough energy.')

    def test_if_money_increased_after_work(self):
        self.worker.work()
        self.assertEqual(self.worker.money, 10)

    def test_if_energy_decreased_after_work(self):
        self.worker.work()
        self.assertEqual(self.worker.energy, 0)

    def test_if_get_info_works(self):
        message = f'{self.worker.name} has saved {self.worker.money} money.'
        self.assertEqual(self.worker.get_info(), message)


if __name__ == '__main__':
    unittest.main()
