from project.horse_specification.horse import Horse


class Thoroughbred (Horse):
    SPEED_MAX = 140
    DEFAULT_INCREASE_SPEED = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        if self.speed + self.DEFAULT_INCREASE_SPEED > self.SPEED_MAX:
            self.speed = self.SPEED_MAX
        else:
            self.speed += self.DEFAULT_INCREASE_SPEED
