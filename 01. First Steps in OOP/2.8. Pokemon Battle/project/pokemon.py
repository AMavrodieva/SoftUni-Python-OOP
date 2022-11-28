class Pokemon:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def __str__(self):
        return self.name, self.health

    def pokemon_details(self):
        return f'{self.name} with health {self.health}'
