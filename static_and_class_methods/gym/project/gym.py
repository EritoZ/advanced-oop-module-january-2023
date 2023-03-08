from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        message = []

        subscription_object: Subscription = next(filter(lambda x: x.id == subscription_id, self.subscriptions))

        customer_object: Customer = next(filter(lambda x: x.id == subscription_object.customer_id, self.customers))

        trainer_object: Trainer = next(filter(lambda x: x.id == subscription_object.trainer_id, self.trainers))

        plan_object: ExercisePlan = next(filter(lambda x: x.id == subscription_object.exercise_id, self.plans))

        equipment_object: Equipment = next(filter(lambda x: x.id == plan_object.equipment_id, self.equipment))

        for gym_object in (subscription_object, customer_object, trainer_object, equipment_object, plan_object):
            message.append(str(gym_object))

        return '\n'.join(message)
