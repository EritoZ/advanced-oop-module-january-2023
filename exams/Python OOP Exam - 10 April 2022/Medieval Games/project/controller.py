from collections import deque

from project.player import Player
from project.supply.supply import Supply


class Controller:

    def __init__(self):
        self.players = []
        self.supplies = []

    @staticmethod
    def __find_player(name, somewhere):
        return next(filter(lambda p: p.name == name, somewhere))

    def add_player(self, *args):
        message = []

        for player in args:
            if player not in self.players:
                self.players.append(player)
                message.append(player.name)

        return f"Successfully added: {', '.join(message)}"

    def add_supply(self, *args):
        new_supplies = list(args)

        self.supplies.extend(new_supplies)

    def sustain(self, player: str or Player, sustenance_type: str):

        if isinstance(player, str):

            try:
                player = self.__find_player(player, self.players)

            except StopIteration:
                return

        if sustenance_type not in ("Food", "Drink"):
            return

        if not player.need_sustenance:
            return f"{player.name} have enough stamina."

        reversed_supplies = self.supplies[::-1]

        try:
            found_supply: Supply = next(filter(lambda s: s.__class__.__name__ == sustenance_type, reversed_supplies))

        except StopIteration:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        im_too_tired_to_think_var_name = found_supply.energy

        if player.stamina + im_too_tired_to_think_var_name > 100:
            im_too_tired_to_think_var_name = 100 - player.stamina

        player.stamina += im_too_tired_to_think_var_name

        reverse_index_found_supply = reversed_supplies.index(found_supply)

        self.supplies.pop(len(self.supplies) - 1 - reverse_index_found_supply)

        return f"{player.name} sustained successfully with {found_supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__find_player(first_player_name, self.players)
        second_player = self.__find_player(second_player_name, self.players)

        both_players = (first_player, second_player)

        message = [f"Player {player.name} does not have enough stamina." for player in both_players
                   if not player.stamina]

        if message:
            return '\n'.join(message)

        both_players = deque(sorted(both_players, key=lambda p: p.stamina))

        for _ in range(2):
            result = both_players[1].stamina - both_players[0].stamina * 0.5

            if result <= 0:
                both_players[1].stamina = 0

                return f"Winner: {both_players[0].name}"

            both_players[1].stamina = result

            both_players.rotate()

        winner = max(both_players, key=lambda x: x.stamina)

        return f"Winner: {winner.name}"

    def next_day(self):

        for player in self.players:
            stamina_result = player.stamina - player.age * 2

            if stamina_result < 0:
                stamina_result = 0

            player.stamina = stamina_result

            self.sustain(player, 'Food')
            self.sustain(player, 'Drink')

    def __str__(self):
        message = [str(x) for x in self.players]

        message.extend(x.details() for x in self.supplies)

        return '\n'.join(message)
