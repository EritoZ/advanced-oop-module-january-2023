class Player:

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = 'Unaffiliated'

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost

            return f"Skill {skill_name} added to the collection of the player {self.name}"

        return "Skill already added"

    def player_info(self):
        message = [
            f'Name: {self.name}',
            f'Guild: {self.guild}',
            f'HP: {self.hp}',
            f'MP: {self.mp}'
        ]

        [message.append(f'==={skill} - {mana_cost}') for skill, mana_cost in self.skills.items()]

        return '\n'.join(message)
