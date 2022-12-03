from project.people.child import Child


class Room:
    appliances_types = ()

    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0
        self.appliances = self.generate_appliances(*self.appliances_types)


    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError(f'Expenses cannot be negative')
        self.__expenses = value

    @property
    def total_expenses(self):
        return self.expenses + self.room_cost

    def calculate_expenses(self, *args):
        result = 0
        for el in args:
            result += sum(x.get_monthly_expense() for x in el)
        self.expenses = result

    def generate_appliances(self, *appliances_types):
        total_appliances = []
        for member in range(self.members_count):
            for appliance_type in appliances_types:
                total_appliances.append(appliance_type())
        return total_appliances
