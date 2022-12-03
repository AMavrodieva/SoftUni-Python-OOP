class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        successfully_added = []
        for arg in args:
            if arg not in self.players:
                successfully_added.append(arg.name)
                self.players.append(arg)
        return f'Successfully added: {", ".join(successfully_added)}'

    def add_supply(self, *args):
        for arg in args:
            self.supplies.append(arg)

    def find_supply(self, sustenance_type):
        index = -1
        while len(self.supplies) > abs(index):
            current_supply = self.supplies[index]
            if type(current_supply).__name__ == sustenance_type:
                return self.supplies.pop(index)
            index -= 1
        if sustenance_type == "Food":
            raise Exception('There are no food supplies left!')
        if sustenance_type == "Drink":
            raise Exception('There are no drink supplies left!')

    def check_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return True

    def find_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def sustain(self, player_name: str, sustenance_type: str):
        if self.check_player(player_name) and (sustenance_type == "Food" or sustenance_type == "Drink"):
            player = self.find_player(player_name)
            if player.stamina == 100:
                return f'{player.name} have enough stamina.'
            supply = self.find_supply(sustenance_type)
            if supply:
                if player.stamina + supply.energy > 100:
                    player.stamina = 100
                else:
                    player.stamina += supply.energy
                return f'{player.name} sustained successfully with {supply.name}.'

    def check_duel(self, *args):
        result = []
        for arg in args:
            if arg.stamina == 0:
                result.append(f'Player {arg.name} does not have enough stamina.')
        return "\n".join(result)

    def duel(self, first_player_name: str, second_player_name: str):
        player = self.find_player(first_player_name)
        other = self.find_player(second_player_name)
        result = self.check_duel(player, other)
        if result:
            return result
        pl_1 = player if player.stamina < other.stamina else other
        pl_2 = player if player.stamina > other.stamina else other
        pl_2.stamina -= pl_1.stamina / 2
        if pl_2.stamina <= 0:
            pl_2.stamina = 0
            return f'Winner: {pl_1.name}'
        if pl_1.stamina - pl_2.stamina / 2 <= 0:
            pl_1.stamina = 0
            return f'Winner: {pl_2.name}'
        else:
            pl_1.stamina -= pl_2.stamina / 2
        winner_player = pl_1 if pl_1.stamina > pl_2.stamina else pl_2
        return f'Winner: {winner_player.name}'

    def next_day(self):
        for pl in self.players:
            pl.stamina = max(pl.stamina - pl.age * 2, 0)

        for pl in self.players:
            self.sustain(pl.name, "Food")
            self.sustain(pl.name, "Drink")

    def __str__(self):
        result = []
        for player in self.players:
            result.append(str(player))
        for supply in self.supplies:
            result.append(supply.details())
        return "\n".join(result)
