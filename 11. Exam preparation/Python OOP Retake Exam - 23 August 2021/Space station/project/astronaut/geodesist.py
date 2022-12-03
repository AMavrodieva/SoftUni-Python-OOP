from project_unitest.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    DEFAULT_OXYGEN = 50

    def __init__(self, name: str):
        super().__init__(name, self.DEFAULT_OXYGEN)
