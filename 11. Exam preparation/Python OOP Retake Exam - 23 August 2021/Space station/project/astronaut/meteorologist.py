from project_unitest.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    DEFAULT_OXYGEN = 90
    DECREASE_OXYGEN = 15

    def __init__(self, name: str):
        super().__init__(name, self.DEFAULT_OXYGEN)
