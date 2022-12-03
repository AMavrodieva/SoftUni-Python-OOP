from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.rooms.room import Room
from project.appliances.laptop import Laptop


class YoungCouple(Room):
    default_members_count = 2
    default_room_cost = 20
    appliances_types = (TV, Fridge, Laptop)

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        budget = salary_one + salary_two
        super().__init__(family_name, budget, self.default_members_count)
        self.room_cost = self.default_room_cost
        self.calculate_expenses(self.appliances)
