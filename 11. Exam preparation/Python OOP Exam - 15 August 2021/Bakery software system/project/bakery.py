from project_unitest.drink.tea import Tea
from project_unitest.drink.water import Water
from project_unitest.baked_food.cake import Cake
from project_unitest.baked_food.bread import Bread
from project_unitest.table.inside_table import InsideTable
from project_unitest.table.outside_table import OutsideTable


class Bakery:
    VALID_FOOD = ["Bread", "Cake"]
    VALID_DRINK = ["Tea", "Water"]
    VALID_TABLE = ["InsideTable", "OutsideTable"]

    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not len(value.strip()) > 0:
            raise ValueError(f"Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if food_type in self.VALID_FOOD:
            if self.is_food_exist(food_type, name):
                raise Exception(f'{food_type} {name} is already in the menu!')
            food = self.create_food(food_type, name, price)
            self.food_menu.append(food)
            return f'Added {food.name} ({food_type}) to the food menu'

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if drink_type in self.VALID_DRINK:
            if self.is_drink_exist(drink_type, name):
                raise Exception(f'{drink_type} {name} is already in the menu!')
            drink = self.create_drink(drink_type, name, portion, brand)
            self.drinks_menu.append(drink)
            return f'Added {drink.name} ({drink.brand}) to the drink menu'

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type in self.VALID_TABLE:
            if self.is_table_exist(table_type, table_number):
                raise Exception(f'Table {table_number} is already in the bakery!')
            table = self.create_table(table_type, table_number, capacity)
            self.tables_repository.append(table)
            return f'Added table number {table.table_number} in the bakery'

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if table.capacity >= number_of_people and not table.is_reserved:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f'No available table for {number_of_people} people'

    def order_food(self, table_number: int, *foods):
        table = self.find_table(table_number)
        if table is None:
            return f'Could not find table {table_number}'
        available_food, not_available_food = self.food_allocation(*foods)
        foods_list = self.create_object_food(available_food)
        for food in foods_list:
            table.order_food(food)
        result = f'Table {table.table_number} ordered:\n'
        for food in foods_list:
            result += f'{food}\n'
        result += f'{self.name} does not have in the menu:\n'
        for food in not_available_food:
            result += f'{food}\n'
        return result.strip()

    def order_drink(self, table_number: int, *drinks):
        table = self.find_table(table_number)
        if table is None:
            return f'Could not find table {table_number}'
        available_drink, not_available_drink = self.drink_allocation(*drinks)
        drinks_list = self.create_object_drink(available_drink)
        for drink in drinks_list:
            table.order_drink(drink)
        result = f'Table {table.table_number} ordered:\n'
        for drink in drinks_list:
            result += f'{drink}\n'
        result += f'{self.name} does not have in the menu:\n'
        for drink in not_available_drink:
            result += f'{drink}\n'
        return result.strip()

    def leave_table(self, table_number: int):
        table = self.find_table(table_number)
        bills = table.get_bill()
        table.clear()
        self.total_income += bills
        return f'Table: {table.table_number}\nBill: {bills:.2f}'

    def get_free_tables_info(self):
        result = []
        for table in self.tables_repository:
            actual = table.free_table_info()
            if actual is not None:
                result.append(actual)
        return "\n".join(result)

    def get_total_income(self):
        return f'Total income: {self.total_income:.2f}lv'

    def is_food_exist(self, food_type, name):
        for food in self.food_menu:
            if type(food).__name__ == food_type and food.name == name:
                return True
        return False

    def is_drink_exist(self, drink_type, name):
        for drink in self.drinks_menu:
            if type(drink).__name__ == drink_type and drink.name == name:
                return True
        return False

    def is_table_exist(self, table_type, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return True
        return False

    def create_food(self, food_type, name, price):
        food = None
        if food_type == self.VALID_FOOD[0]:
            food = Bread(name, price)
        elif food_type == self.VALID_FOOD[1]:
            food = Cake(name, price)
        return food

    def create_drink(self, drink_type, name, portion, brand):
        drink = None
        if drink_type == self.VALID_DRINK[0]:
            drink = Tea(name, portion, brand)
        elif drink_type == self.VALID_DRINK[1]:
            drink = Water(name, portion, brand)
        return drink

    def create_table(self, table_type, table_number, capacity):
        table = None
        if table_type == self.VALID_TABLE[0]:
            table = InsideTable(table_number, capacity)
        if table_type == self.VALID_TABLE[1]:
            table = OutsideTable(table_number, capacity)
        return table

    def find_table(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table
        return None

    def food_allocation(self, *args):
        available_food = []
        not_available_food = []
        food_name_list = [food.name for food in self.food_menu]
        for f in args:
            if f in food_name_list:
                available_food.append(f)
            else:
                not_available_food.append(f)
        return available_food, not_available_food

    def drink_allocation(self, *args):
        available_drink = []
        not_available_drink = []
        drink_name_list = [drink.name for drink in self.drinks_menu]
        for f in args:
            if f in drink_name_list:
                available_drink.append(f)
            else:
                not_available_drink.append(f)
        return available_drink, not_available_drink

    def create_object_food(self, list_of_name):
        list_of_object = []
        for el in list_of_name:
            for food in self.food_menu:
                if el == food.name:
                    list_of_object.append(food)
        return list_of_object

    def create_object_drink(self, list_of_name):
        list_of_object = []
        for el in list_of_name:
            for drink in self.drinks_menu:
                if el == drink.name:
                    list_of_object.append(drink)
        return list_of_object
