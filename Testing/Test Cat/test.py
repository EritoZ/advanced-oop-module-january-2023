import unittest

from test_cat import Cat


class TestCat(unittest.TestCase):

    def setUp(self) -> None:
        self.cat = Cat('?')

    def test_cat_gets_fatter(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_cat_is_fed(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_panics_if_tried_to_feed_when_already_fed(self):
        self.cat.eat()

        with self.assertRaises(Exception) as context:
            self.cat.eat()

        self.assertEqual(str(context.exception), 'Already fed.')

    def test_cat_cannot_sleep_error(self):
        with self.assertRaises(Exception) as context:
            self.cat.sleep()

        self.assertEqual(str(context.exception), 'Cannot sleep while hungry')

    def test_cat_if_not_sleepy_after_sleep(self):
        self.cat.sleepy = True
        self.cat.fed = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
