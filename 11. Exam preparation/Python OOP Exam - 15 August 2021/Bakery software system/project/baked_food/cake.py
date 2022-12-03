from project_unitest.baked_food.baked_food import BakedFood


class Cake(BakedFood):
    DEFAULT_PORTION = 245

    def __init__(self, name: str, price: float):
        super().__init__(name, self.DEFAULT_PORTION, price)

    def __repr__(self):
        return f' - {self.name}: {self.DEFAULT_PORTION:.2f}g - {self.price:.2f}lv'
