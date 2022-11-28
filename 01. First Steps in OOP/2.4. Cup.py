class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def fill(self, quantity):
        free_quantity = self.size - self.quantity
        if quantity <= free_quantity:
            self.quantity += quantity
        return self.quantity

    def status(self):
        free_quantity = self.size - self.quantity
        return free_quantity


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
