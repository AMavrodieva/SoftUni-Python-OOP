from abc import ABC, abstractmethod


class Horse(ABC):
    SPEED_MAX = 0

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not len(value.strip()) > 0:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.SPEED_MAX:
            raise ValueError(f'Horse speed is too high!')
        self.__speed = value

    @abstractmethod
    def train(self):
        pass

