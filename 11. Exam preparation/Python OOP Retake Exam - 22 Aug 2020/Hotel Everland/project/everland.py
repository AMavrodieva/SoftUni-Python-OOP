from project.rooms.room import Room
from project.rooms.alone_old import AloneOld


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum(room.total_expenses for room in self.rooms)
        return f'Monthly consumptions: {total_consumption:.2f}$.'

    def pay(self):
        result = []
        removed_room = []
        for room in self.rooms:
            removed_room = []
            if room.budget >= room.total_expenses:
                new_budget = room.budget - room.total_expenses
                result.append(f'{room.family_name} paid {room.total_expenses:.2f}$ and have {new_budget:.2f}$ left.')
                room.budget -= room.total_expenses
            else:
                result.append(f'{room.family_name} does not have enough budget and must leave the hotel.')
                removed_room.append(room)
        for room in removed_room:
            self.rooms.remove(room)
        return "\n".join(result)

    def status(self):
        all_people_in_the_hotel = sum(room.members_count for room in self.rooms)
        result = f'Total population: {all_people_in_the_hotel}\n'
        for room in self.rooms:
            room_expenses = room.total_expenses - room.room_cost
            result += f'{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room_expenses:.2f}$\n'
            room_other_expenses = room.room_cost
            for ind, child in enumerate(room.children):
                child_expenses = child.get_monthly_expense()
                result += f'--- Child {ind+1} monthly cost: {child_expenses:.2f}$\n'
                room_other_expenses += child_expenses
            result += f'--- Appliances monthly cost: {room.total_expenses - room_other_expenses:.2f}$\n'
        return result.strip()
