from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.rooms.room import Room
from project.appliances.laptop import Laptop
from project.people.child import Child


class YoungCoupleWithChildren(Room):
    default_member_count = 2
    default_room_cost = 30
    appliances_types = [TV, Fridge, Laptop]

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        budget = salary_one + salary_two
        members_count = self.default_member_count + len(children)
        super().__init__(family_name, budget, members_count)
        self.room_cost = self.default_room_cost
        self.children = list(children)
        self.calculate_expenses(self.appliances, self.children)
