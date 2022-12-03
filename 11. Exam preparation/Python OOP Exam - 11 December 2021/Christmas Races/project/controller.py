from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type == "MuscleCar" or car_type == "SportsCar":
            if self.is_car_model_exist(model):
                raise Exception(f'Car {model} is already created!')
            if car_type == "MuscleCar":
                car = MuscleCar(model, speed_limit)
            else:
                car = SportsCar(model, speed_limit)
            self.cars.append(car)
            return f'{car_type} {model} is created.'

    def create_driver(self, driver_name: str):
        if self.is_driver_exist(driver_name):
            raise Exception(f'Driver {driver_name} is already created!')
        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f'Driver {driver_name} is created.'

    def create_race(self, race_name: str):
        if self.is_race_exist(race_name):
            raise Exception(f'Race {race_name} is already created!')
        race = Race(race_name)
        self.races.append(race)
        return f'Race {race_name} is created.'

    def add_car_to_driver(self, driver_name: str, car_type: str):
        if not self.is_driver_exist(driver_name):
            raise Exception(f'Driver {driver_name} could not be found!')
        current_car = self.find_car(car_type)
        if current_car is None:
            raise Exception(f'Car {car_type} could not be found!')
        driver = self.find_driver(driver_name)
        if driver.car:
            old_model = driver.car.model
            driver.car.is_taken = False
            current_car.is_taken = True
            driver.car = current_car
            new_model = current_car.model
            driver.car.is_taken = True
            return f'Driver {driver_name} changed his car from {old_model} to {new_model}.'
        if driver.car is None:
            driver.car = current_car
            driver.car.is_taken = True
            return f'Driver {driver_name} chose the car {driver.car.model}.'

    def add_driver_to_race(self, race_name: str, driver_name: str):
        if not self.is_race_exist(race_name):
            raise Exception(f'Race {race_name} could not be found!')
        if not self.is_driver_exist(driver_name):
            raise Exception(f'Driver {driver_name} could not be found!')
        driver = self.find_driver(driver_name)
        if driver.car is None:
            raise Exception(f'Driver {driver_name} could not participate in the race!')
        race = self.find_race(race_name)
        if driver in race.drivers:
            return f'Driver {driver_name} is already added in {race_name} race.'
        race.drivers.append(driver)
        return f'Driver {driver_name} added in {race_name} race.'

    def start_race(self, race_name: str):
        if not self.is_race_exist(race_name):
            raise Exception(f'Race {race_name} could not be found!')
        race = self.find_race(race_name)
        if len(race.drivers) < 3:
            raise Exception(f'Race {race_name} cannot start with less than 3 participants!')
        list_of_participants = race.drivers.copy()
        list_of_participants.sort(key=lambda x: -x.car.speed_limit)
        result = ''
        for driver in list_of_participants[:3]:
            driver.number_of_wins += 1
            result += f'Driver {driver.name} wins the {race.name} race with a speed of {driver.car.speed_limit}.\n'
        return result.strip()

    def is_car_model_exist(self, model):
        for car in self.cars:
            if car.model == model:
                return True
        return False

    def is_driver_exist(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return True
        return False

    def is_race_exist(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return True
        return False

    def find_car(self, car_type):
        for i in range(len(self.cars)-1, -1, -1):
            if type(self.cars[i]).__name__ == car_type and not self.cars[i].is_taken:
                return self.cars[i]
        return None

    def find_driver(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver

    def find_race(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race

    # @staticmethod
    # def find_first_three_wins(race):
    #     list_of_wins = []
    #     current_race = race.co
    #     while len(list_of_wins) < 3:
    #         if not current_race.drivers:
    #             break
    #         best_driver = None
    #         best_speed = 0
    #         for driver in current_race.drivers:
    #             if driver.car.speed_limit > best_speed:
    #                 best_speed = driver.car.speed_limit
    #                 best_driver = driver
    #         list_of_wins.append(best_driver)
    #         # best_driver.number_of_wins += 1
    #         current_race.drivers.remove(best_driver)
    #     return list_of_wins






