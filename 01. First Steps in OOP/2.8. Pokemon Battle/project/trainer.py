from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return 'This pokemon is already caught'

        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, current: str):
        for pokemon in self.pokemons:
            if pokemon.name == current:
                self.pokemons.remove(pokemon)
                return f'You have released {current}'
        return f'Pokemon is not caught'

    def trainer_data(self):
        result = ''
        result += f'Pokemon Trainer {self.name}\n'
        result += f'Pokemon count {len(self.pokemons)}\n'
        for pokemon in self.pokemons:
            result += f'- {pokemon.pokemon_details()}\n'
        return result.strip()
