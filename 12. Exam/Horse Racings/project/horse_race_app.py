from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey
from project.horse_race import HorseRace


class HorseRaceApp:
    VALID_HORSE_TYPE = ["Appaloosa", "Thoroughbred"]

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type in self.VALID_HORSE_TYPE:
            if self.is_horse_exist(horse_type, horse_name):
                raise Exception(f'Horse {horse_name} has been already added!')
        horse = self.create_horse(horse_type, horse_name, horse_speed)
        if horse:
            self.horses.append(horse)
            return f'{horse_type} horse {horse.name} is added.'

    def add_jockey(self, jockey_name: str, age: int):
        if self.is_jockey_exist(jockey_name):
            raise Exception(f"Jockey {jockey_name} has been already added!")
        jockey = Jockey(jockey_name, age)
        if jockey:
            self.jockeys.append(jockey)
            return f"Jockey {jockey.name} is added."

    def create_horse_race(self, race_type: str):
        if self.is_race_exist(race_type):
            raise Exception(f"Race {race_type} has been already created!")
        race = HorseRace(race_type)
        if race:
            self.horse_races.append(race)
            return f"Race {race.race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.find_jockey(jockey_name)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        horse = self.find_horse(horse_type)
        if horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jockey.horse is not None:
            return f'Jockey {jockey.name} already has a horse.'
        horse.is_taken = True
        jockey.horse = horse
        return f'Jockey {jockey.name} will ride the horse {jockey.horse.name}.'

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        if not self.is_race_exist(race_type):
            raise Exception(f'Race {race_type} could not be found!')
        race = self.find_race(race_type)
        if not self.is_jockey_exist(jockey_name):
            raise Exception(f'Jockey {jockey_name} could not be found!')
        jockey = self.find_jockey(jockey_name)
        if jockey:
            if jockey.horse is None:
                raise Exception(f'Jockey {jockey.name} cannot race without a horse!')
            if jockey in race.jockeys:
                return f"Jockey {jockey.name} has been already added to the {race.race_type} race."
            race.jockeys.append(jockey)
            return f'Jockey {jockey.name} added to the {race.race_type} race.'

    def start_horse_race(self, race_type: str):
        if not self.is_race_exist(race_type):
            raise Exception(f"Race {race_type} could not be found!")
        race = self.find_race(race_type)
        if len(race.jockeys) < 2:
            raise Exception(f'Horse race {race.race_type} needs at least two participants!')
        winner = sorted(race.jockeys, key=lambda x: -x.horse.speed)[0]
        return f"The winner of the {race.race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."

    def is_horse_exist(self, horse_type, horse_name):
        for horse in self.horses:
            if horse.__class__.__name__ == horse_type:
                if horse.name == horse_name:
                    return True
        return False

    def is_jockey_exist(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return True
        return False

    def is_race_exist(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return True
        return False

    def create_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse = None
        if horse_type == self.VALID_HORSE_TYPE[0]:
            horse = Appaloosa(horse_name, horse_speed)
        elif horse_type == self.VALID_HORSE_TYPE[1]:
            horse = Thoroughbred(horse_name, horse_speed)
        return horse

    def find_horse(self, horse_type):
        for ind in range(len(self.horses)-1, -1, -1):
            horse = self.horses[ind]
            if horse.__class__.__name__ == horse_type:
                if not horse.is_taken:
                    return horse
        return None

    def find_jockey(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey
        return None

    def find_race(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race
        return None
