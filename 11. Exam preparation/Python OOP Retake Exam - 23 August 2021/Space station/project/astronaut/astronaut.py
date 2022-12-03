from abc import ABC, abstractmethod


class Astronaut(ABC):
    DECREASE_OXYGEN = 10

    @abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not len(value.strip()) > 0:
            raise ValueError(f'Astronaut name cannot be empty string or whitespace!')
        self.__name = value

    def breathe(self):
        self.oxygen -= self.DECREASE_OXYGEN

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    def __str__(self):
        result = f"Name: {self.name}\nOxygen: {self.oxygen}\n"
        result += f"Backpack items: {', '.join(self.backpack) if len(self.backpack) > 0 else 'none'}"
        return result
