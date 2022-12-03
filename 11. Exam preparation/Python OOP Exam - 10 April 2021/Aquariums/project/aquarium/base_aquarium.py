from abc import ABC, abstractmethod
from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish
from project.decoration.decoration_repository import DecorationRepository


class BaseAquarium(ABC):

    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not len(value.strip()) > 0:
            raise ValueError(f'Aquarium name cannot be an empty string.')
        self.__name = value

    @property
    @abstractmethod
    def fish_type(self):
        pass

    def calculate_comfort(self):
        return sum(d.comfort for d in self.decorations)

    def add_fish(self, fish: BaseFish):
        if self.capacity == len(self.fish):
            return f'Not enough capacity.'
        if self.fish_type != fish.__class__.__name__:
            return "Water not suitable."
        self.fish.append(fish)
        return f'Successfully added {fish.__class__.__name__} to {self.name}.'

    def remove_fish(self, fish: BaseFish):
        if self.is_fish_exist(fish):
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def is_fish_exist(self, fish):
        for el in self.fish:
            if el.name == fish.name:
                return True
        return False

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = f"{self.name}:\n"
        fish_name = [fish.name for fish in self.fish]
        result += f"Fish: {' '.join(fish_name) if len(fish_name) > 0 else 'none'}\n"
        result += f"Decorations: {len(self.decorations)}\n"
        result += f"Comfort: {self.calculate_comfort()}\n"
        return result.strip()
