from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    DEFAULT_SIZE = 5
    DEFAULT_AQUARIUM = 'SaltwaterAquarium'

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.DEFAULT_SIZE, price)
        self.aquarium = self.DEFAULT_AQUARIUM

    def eat(self):
        self.size += 2
