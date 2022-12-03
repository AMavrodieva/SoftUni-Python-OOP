from abc import ABC, abstractmethod
from project_unitest.baked_food.baked_food import BakedFood
from project_unitest.drink.drink import Drink


class Table(ABC):
    @abstractmethod
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError(f'Capacity has to be greater than 0!')
        self.__capacity = value

    def reserve(self, number_of_people: int):
        self.number_of_people += number_of_people
        self.is_reserved = True

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        result = sum([drink.price for drink in self.drink_orders])
        result += sum([baked_food.price for baked_food in self.food_orders])
        return result

    def clear(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            result = f"""Table: {self.table_number}
Type: {self.__class__.__name__}
Capacity: {self.capacity}"""
            return result
        return None
