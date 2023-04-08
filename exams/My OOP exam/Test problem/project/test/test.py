from project.tennis_player import TennisPlayer
import unittest


class TestTennisPlayer(unittest.TestCase):

    def setUp(self) -> None:
        self.player = TennisPlayer('dani', 20, 100.0)

    def test_init(self):
        self.assertEqual(self.player.name, 'dani')
        self.assertEqual(self.player.age, 20)
        self.assertEqual(self.player.points, 100.0)
        self.assertEqual(self.player.wins, [])

    def test_name_error(self):
        with self.assertRaises(ValueError) as er:
            self.player.name = '1'

        self.assertEqual(str(er.exception), "Name should be more than 2 symbols!")

    def test_name_error_equal(self):
        with self.assertRaises(ValueError) as er:
            self.player.name = '12'

        self.assertEqual(str(er.exception), "Name should be more than 2 symbols!")

    def test_age_error(self):
        with self.assertRaises(ValueError) as er:
            self.player.age = 5

        self.assertEqual(str(er.exception), "Players must be at least 18 years of age!")

    def test_age_error_equal(self):
        self.player.age = 18

        self.assertEqual(self.player.age, 18)

    def test_add_win(self):
        self.player.add_new_win('?')

        self.assertEqual(self.player.wins, ['?'])

    def test_win_exists(self):
        self.player.add_new_win('?')
        message = self.player.add_new_win('?')

        self.assertEqual(message, "? has been already added to the list of wins!")

    def test_player_is_better_dunder(self):
        new_player = TennisPlayer('Mas', 20, 5)

        message = self.player < new_player

        self.assertEqual('dani is a better player than Mas', message)

    def test_player_is_not_better_dunder(self):
        new_player = TennisPlayer('Mas', 20, 120)

        message = self.player < new_player

        self.assertEqual('Mas is a top seeded player and he/she is better than dani', message)

    def test_str_no_wins_dunder(self):
        message = str(self.player)

        self.assertEqual(f"Tennis Player: dani\n"
                         f"Age: 20\n"
                         f"Points: 100.0\n"
                         f"Tournaments won: ", message)

    def test_str_with_one_win_dunder(self):
        self.player.add_new_win('?')
        message = str(self.player)

        self.assertEqual(f"Tennis Player: dani\n"
                         f"Age: 20\n"
                         f"Points: 100.0\n"
                         f"Tournaments won: ?", message)

    def test_str_with_multiple_wins_dunder(self):
        self.player.add_new_win('?')
        self.player.add_new_win('!')
        message = str(self.player)

        self.assertEqual(f"Tennis Player: dani\n"
                         f"Age: 20\n"
                         f"Points: 100.0\n"
                         f"Tournaments won: ?, !", message)


if __name__ == '__main__':
    unittest.main()
