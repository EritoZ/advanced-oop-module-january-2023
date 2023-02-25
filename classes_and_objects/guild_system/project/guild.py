from project.player import Player


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        if player.guild != 'Unaffiliated':
            return f"Player {player.name} is in another guild."

        player.guild = self.name
        self.players.append(player)

        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        try:
            player_object: Player = next(filter(lambda x: x.name == player_name, self.players))

            self.players.remove(player_object)
            player_object.guild = 'Unaffiliated'

            return f"Player {player_name} has been removed from the guild."

        except StopIteration:

            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        message = [
            f'Guild: {self.name}'
        ]

        [message.append(player.player_info()) for player in self.players]

        return '\n'.join(message)


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())