from project_unitest.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    DEFAULT_OXYGEN = 70
    DECREASE_OXYGEN = 5

    def __init__(self, name: str):
        super().__init__(name, self.DEFAULT_OXYGEN)

