from project.planet.planet_repository import PlanetRepository
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet


class SpaceStation:
    VALID_ASTRONAUT = ["Biologist", "Geodesist", "Meteorologist"]

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_mission = 0
        self.unsuccessful_mission = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in self.VALID_ASTRONAUT:
            raise Exception(f'Astronaut type is not valid!')
        if self.is_exist_astronaut(astronaut_type, name):
            return f'{name} is already added.'
        astronaut = self.create_astronaut(astronaut_type, name)
        self.astronaut_repository.astronauts.append(astronaut)
        return f"Successfully added {astronaut_type}: {astronaut.name}."

    def add_planet(self, name: str, items: str):
        result = self.planet_repository.find_by_name(name)
        if result:
            return f'{result.name} is already added.'
        planet = self.create_planet(name, items)
        self.planet_repository.planets.append(planet)
        return f'Successfully added Planet: {planet.name}.'

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f'Astronaut {astronaut.name} was retired!'

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if planet is None:
            raise Exception(f'Invalid planet name!')
        list_of_astronauts = self.choose_astronaut(5, 30)
        if len(list_of_astronauts) == 0:
            raise Exception(f'You need at least one astronaut to explore the planet!')
        participants = 0
        for astronaut in list_of_astronauts:
            if len(planet.items) == 0:
                break
            while astronaut.oxygen > 0 and len(planet.items) > 0:
                current_item = planet.items.pop()
                astronaut.backpack.append(current_item)
                astronaut.breathe()
            participants += 1

        if len(planet.items) == 0:
            self.successful_mission += 1
            return f'Planet: {planet.name} was explored. {participants} astronauts participated in collecting items.'
        else:
            self.unsuccessful_mission += 1
            return f'Mission is not completed.'

    def report(self):
        result = f'{self.successful_mission} successful missions!\n'
        result += f'{self.unsuccessful_mission} missions were not completed!\n'
        result += "Astronauts' info:" + '\n'
        for astronaut in self.astronaut_repository.astronauts:
            result += str(astronaut) + "\n"
        return result.strip()

    def is_exist_astronaut(self, astronaut_type, name):
        for astronaut in self.astronaut_repository.astronauts:
            if type(astronaut).__name__ == astronaut_type and astronaut.name == name:
                return True
        return False

    def create_astronaut(self, astronaut_type, name):
        astronaut = None
        if astronaut_type == self.VALID_ASTRONAUT[0]:
            astronaut = Biologist(name)
        elif astronaut_type == self.VALID_ASTRONAUT[1]:
            astronaut = Geodesist(name)
        elif astronaut_type == self.VALID_ASTRONAUT[2]:
            astronaut = Meteorologist(name)
        return astronaut

    @staticmethod
    def create_planet(name: str, items: str):
        pl_item = [x for x in items.split(", ")]
        planet = Planet(name)
        planet.items.extend(pl_item)
        return planet

    def choose_astronaut(self, count, min_oxygen):
        return sorted([x for x in self.astronaut_repository.astronauts if x.oxygen > min_oxygen],
                      key=lambda x: -x.oxygen)[0:count]


