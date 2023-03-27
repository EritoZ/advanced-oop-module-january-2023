import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal('???', 'tf?', 'gagaga')

    def test_name(self):
        self.assertEqual(self.mammal.name, '???')

    def test_type(self):
        self.assertEqual(self.mammal.type, 'tf?')

    def test_sound(self):
        self.assertEqual(self.mammal.sound, 'gagaga')

    def test_kingdom(self):
        self.assertEqual(self.mammal._Mammal__kingdom, 'animals')

    def test_make_sound(self):
        sound = "??? makes gagaga"
        self.assertEqual(self.mammal.make_sound(), sound)

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), 'animals')

    def test_info(self):
        message = '??? is of type tf?'
        self.assertEqual(self.mammal.info(), message)


if __name__ == '__main__':
    unittest.main()
