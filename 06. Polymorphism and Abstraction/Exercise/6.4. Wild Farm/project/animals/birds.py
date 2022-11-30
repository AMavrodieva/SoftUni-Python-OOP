from project.animals.animal import Bird


class Owl(Bird):
    @property
    def allowed_food(self):
        return ['Meat']

    @property
    def weight_incremental(self):
        return 0.25

    def make_sound(self):
        return 'Hoot Hoot'


class Hen(Bird):
    @property
    def allowed_food(self):
        return ['Vegetable', 'Fruit', 'Meat', 'Seed']

    @property
    def weight_incremental(self):
        return 0.35

    def make_sound(self):
        return "Cluck"
