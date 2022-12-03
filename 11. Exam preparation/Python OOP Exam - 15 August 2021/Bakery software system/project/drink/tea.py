from project_unitest.drink.drink import Drink


class Tea(Drink):
    DEFAULT_PRICE = 2.50

    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, self.DEFAULT_PRICE, brand)

    def __repr__(self):
        return f' - {self.name} {self.brand} - {self.portion:.2f}ml - {self.DEFAULT_PRICE:.2f}lv'
