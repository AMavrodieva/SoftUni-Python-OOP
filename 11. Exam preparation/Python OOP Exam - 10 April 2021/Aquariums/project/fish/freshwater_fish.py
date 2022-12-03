from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    DEFAULT_SIZE = 3
    DEFAULT_AQUARIUM = 'FreshwaterAquarium'

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.DEFAULT_SIZE, price)
        self.aquarium = self.DEFAULT_AQUARIUM

    def eat(self):
        self.size += 3



