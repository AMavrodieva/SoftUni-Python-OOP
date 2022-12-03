from project.rooms.room import Room
from project.appliances.tv import TV


class AloneYoung(Room):
    default_member_count = 1
    default_room_cost = 10
    appliances_types = (TV,)

    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, self.default_member_count)
        self.room_cost = self.default_room_cost
        self.calculate_expenses(self.appliances)
