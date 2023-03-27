import unittest

from project.hero import Hero


class TestHero(unittest.TestCase):

    def setUp(self):
        self.hero = Hero('joke', 2, 10, 5)
        self.joker = Hero('bad joke', 2, 6, 6)

    def test_battle_fight_yourself_error(self):
        with self.assertRaises(Exception) as error:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(error.exception))

    def test_battle_hero_has_0_health_error(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as error:
            self.hero.battle(self.joker)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(error.exception))

    def test_battle_hero_has_negative_health_error(self):
        self.hero.health = -5

        with self.assertRaises(ValueError) as error:
            self.hero.battle(self.joker)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(error.exception))

    def test_battle_enemy_hero_has_0_health_error(self):
        self.joker.health = 0

        with self.assertRaises(ValueError) as error:
            self.hero.battle(self.joker)

        self.assertEqual("You cannot fight bad joke. He needs to rest", str(error.exception))

    def test_battle_enemy_hero_has_negative_health_error(self):
        self.joker.health = -5

        with self.assertRaises(ValueError) as error:
            self.hero.battle(self.joker)

        self.assertEqual("You cannot fight bad joke. He needs to rest", str(error.exception))

    def test_battle_draw(self):
        result = self.hero.battle(self.joker)

        self.assertEqual('Draw', result)

    def test_battle_win(self):
        self.joker.level = 1
        result = self.hero.battle(self.joker)

        self.assertEqual("You win", result)
        self.assertEqual(9, self.hero.health)
        self.assertEqual(3, self.hero.level)
        self.assertEqual(10, self.hero.damage)

    def test_battle_lose(self):
        self.hero.damage = 1
        result = self.hero.battle(self.joker)

        self.assertEqual("You lose", result)
        self.assertEqual(9, self.joker.health)
        self.assertEqual(3, self.joker.level)
        self.assertEqual(11, self.joker.damage)

    def test_string_message(self):
        message = f"Hero joke: 2 lvl\n" \
               f"Health: 10\n" \
               f"Damage: 5\n"

        self.assertEqual(str(self.hero), message)


if __name__ == "__main__":
    unittest.main()
