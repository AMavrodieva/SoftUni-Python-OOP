from project.decoration.decoration_repository import DecorationRepository
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    VALID_AQUARIUMS = ["FreshwaterAquarium", "SaltwaterAquarium"]
    VALID_DECORATION = ["Ornament", "Plant"]
    VALID_TYPE_FISH = ["FreshwaterFish", "SaltwaterFish"]

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.VALID_AQUARIUMS:
            return f'Invalid aquarium type.'
        aquarium = self.create_aquarium(aquarium_type, aquarium_name)
        self.aquariums.append(aquarium)
        return f'Successfully added {aquarium_type}.'

    def add_decoration(self, decoration_type: str):
        if decoration_type not in self.VALID_DECORATION:
            return 'Invalid decoration type.'
        decoration = self.create_decoration(decoration_type)
        self.decorations_repository.add(decoration)
        return f'Successfully added {decoration_type}.'

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        result = self.decorations_repository.find_by_type(decoration_type)
        if result == "None":
            return f"There isn't a decoration of type {decoration_type}."
        aquarium = self.is_aquarium_exist(aquarium_name)
        if aquarium:
            aquarium.add_decoration(result)
            self.decorations_repository.remove(result)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in self.VALID_TYPE_FISH:
            return f"There isn't a fish of type {fish_type}."
        aquarium = self.is_aquarium_exist(aquarium_name)
        fish = self.create_fish(fish_type, fish_name, fish_species, price)
        if aquarium:
            return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.is_aquarium_exist(aquarium_name)
        if aquarium:
            aquarium.feed()
            fed_count = len(aquarium.fish)
            return f"Fish fed: {fed_count}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.is_aquarium_exist(aquarium_name)
        if aquarium:
            decoration_sum = sum(d.price for d in aquarium.decorations)
            fish_sum = sum(f.price for f in aquarium.fish)
            total = decoration_sum + fish_sum
            return f'The value of Aquarium {aquarium_name} is {total:.2f}.'

    def report(self):
        result = ""
        for aquarium in self.aquariums:
            result += str(aquarium) + "\n"
        return result.strip()

    def create_aquarium(self, aquarium_type, aquarium_name):
        aquarium = None
        if aquarium_type == self.VALID_AQUARIUMS[0]:
            aquarium = FreshwaterAquarium(aquarium_name)
        elif aquarium_type == self.VALID_AQUARIUMS[1]:
            aquarium = SaltwaterAquarium(aquarium_name)
        return aquarium

    def create_decoration(self, decoration_type):
        decoration = None
        if decoration_type == self.VALID_DECORATION[0]:
            decoration = Ornament()
        elif decoration_type == self.VALID_DECORATION[1]:
            decoration = Plant()
        return decoration

    def is_aquarium_exist(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium
        return None

    def create_fish(self, fish_type: str, fish_name: str, fish_species: str, price: float):
        fish = None
        if fish_type == self.VALID_TYPE_FISH[0]:
            fish = FreshwaterFish(fish_name, fish_species, price)
        elif fish_type == self.VALID_TYPE_FISH[1]:
            fish = SaltwaterFish(fish_name, fish_species, price)
        return fish
