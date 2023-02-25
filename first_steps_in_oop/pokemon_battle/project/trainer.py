from pokemon_battle.project.pokemon import Pokemon


class Trainer:

    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):

        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.name} with health {pokemon.health}"
        else:
            return "This pokemon_battle is already caught"

    def release_pokemon(self, pokemon_name: str):

        try:
            found_pokemon = [pokemon_object for pokemon_object in self.pokemons
                             if pokemon_name == pokemon_object.name][0]

            self.pokemons.remove(found_pokemon)

            return f"You have released {pokemon_name}"

        except IndexError:
            return "Pokemon is not caught"

    def trainer_data(self):
        message = [
            f'Pokemon Trainer {self.name}',
            f'Pokemon count {len(self.pokemons)}',
            '\n'.join([f'- {pokemon.pokemon_details()}' for pokemon in self.pokemons])
        ]

        return '\n'.join(message)


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())