from abc import ABC, abstractmethod


class FormulaTeam(ABC):

    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = value

    @abstractmethod
    def team_income(self):
        pass

    def calculate_revenue_after_race(self, race_pos: int):
        sponsor_rewards, reward = self.team_income()

        reward += self.check_winnings(sponsor_rewards, race_pos)

        self.budget += reward

        return self.status_message(reward, self.budget)

    @staticmethod
    def check_winnings(sponsor_rewards, race_pos):
        reward = 0

        for sponsor in sponsor_rewards:
            for position in sponsor:

                if position >= race_pos:
                    reward += sponsor[position]
                    break

        return reward

    @staticmethod
    def status_message(revenue, current_budget):
        return f"The revenue after the race is { revenue }$. Current budget { current_budget }$"
