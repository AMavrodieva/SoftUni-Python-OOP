from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove

from project.rooms.room import Room


class OldCouple(Room):
    default_members_count = 2
    default_room_cost = 15
    appliances_types = (TV, Fridge, Stove)

    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        budget = pension_one + pension_two
        super().__init__(family_name, budget, self.default_members_count)
        self.room_cost = self.default_room_cost
        self.calculate_expenses(self.appliances)
