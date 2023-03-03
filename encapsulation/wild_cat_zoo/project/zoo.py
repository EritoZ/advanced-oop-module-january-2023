from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if price >= self.__budget:
            return "Not enough budget"

        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price

        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)

        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        try:
            worker_object: Worker = next(filter(lambda x: x.name == worker_name, self.workers))

            self.workers.remove(worker_object)

            return f"{worker_name} fired successfully"

        except StopIteration:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_salaries = sum(worker.salary for worker in self.workers)

        if sum_salaries > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= sum_salaries

        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        sum_animal_care = sum(animal.money_for_care for animal in self.animals)

        if sum_animal_care > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= sum_animal_care

        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        message = []
        all_lions = [animal.__repr__() for animal in self.animals if animal.__class__.__name__ == 'Lion']
        all_tigers = [animal.__repr__() for animal in self.animals if animal.__class__.__name__ == 'Tiger']
        all_cheetahs = [animal.__repr__() for animal in self.animals if animal.__class__.__name__ == 'Cheetah']

        message.append(f'You have {len(self.animals)} animals')

        message.append(f'----- {len(all_lions)} Lions:')
        [message.append(lion) for lion in all_lions]

        message.append(f'----- {len(all_tigers)} Tigers:')
        [message.append(tiger) for tiger in all_tigers]

        message.append(f'----- {len(all_cheetahs)} Cheetahs:')
        [message.append(cheetah) for cheetah in all_cheetahs]

        return '\n'.join(message)

    def workers_status(self):
        message = []
        all_keepers = [worker.__repr__() for worker in self.workers if worker.__class__.__name__ == 'Keeper']
        all_caretakers = [worker.__repr__() for worker in self.workers if worker.__class__.__name__ == 'Caretaker']
        all_vets = [worker.__repr__() for worker in self.workers if worker.__class__.__name__ == 'Vet']

        message.append(f'You have {len(self.workers)} workers')

        message.append(f'----- {len(all_keepers)} Keepers:')
        [message.append(keeper) for keeper in all_keepers]

        message.append(f'----- {len(all_caretakers)} Caretakers:')
        [message.append(caretaker) for caretaker in all_caretakers]

        message.append(f'----- {len(all_vets)} Vets:')
        [message.append(vet) for vet in all_vets]

        return '\n'.join(message)
