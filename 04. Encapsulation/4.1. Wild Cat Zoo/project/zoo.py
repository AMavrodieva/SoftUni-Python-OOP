from project.animals import Animal
from project.worker import Worker
from project.lion import Lion
from project.tiger import Tiger
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.vet import Vet
from project.caretaker import Caretaker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if len(self.animals) == self.__animal_capacity:
            return f'Not enough space for animal'
        if price > self.__budget:
            return f'Not enough budget'
        self.animals.append(animal)
        self.__budget -= price
        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return f'Not enough space for worker'
        self.workers.append(worker)
        return f'{worker.name} the {worker.__class__.__name__} hired successfully'

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        needed_sum = sum(w.salary for w in self.workers)
        if needed_sum <= self.__budget:
            self.__budget -= needed_sum
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return f'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        needed_sum = sum(animals.money_for_care for animals in self.animals)
        if needed_sum <= self.__budget:
            self.__budget -= needed_sum
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        return f'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        list_lion = [repr(animal) for animal in self.animals if isinstance(animal, Lion)]
        result += f'----- {len(list_lion)} Lions:\n' + "\n".join(list_lion) + "\n"
        list_tiger = [repr(animal) for animal in self.animals if isinstance(animal, Tiger)]
        result += f'----- {len(list_tiger)} Tigers:\n' + "\n".join(list_tiger) + "\n"
        list_cheetah = [repr(animal) for animal in self.animals if isinstance(animal, Cheetah)]
        result += f'----- {len(list_cheetah)} Cheetahs:\n' + "\n".join(list_cheetah)
        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        list_keepers = [repr(worker) for worker in self.workers if isinstance(worker, Keeper)]
        result += f'----- {len(list_keepers)} Keepers:\n' + "\n".join(list_keepers) + "\n"
        list_caretakers = [repr(worker) for worker in self.workers if isinstance(worker, Caretaker)]
        result += f'----- {len(list_caretakers)} Caretakers:\n' + "\n".join(list_caretakers) + "\n"
        list_vets = [repr(worker) for worker in self.workers if isinstance(worker, Vet)]
        result += f'----- {len(list_vets)} Vets:\n' + "\n".join(list_vets)
        return result

