from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    def calculate_revenue_after_race(self, race_pos: int):
        sponsor_rewards = ({1: 1000000, 3: 500000}, {5: 100000, 7: 50000})

        reward = self.check_winnings(sponsor_rewards, race_pos)

        reward -= 200000

        self.budget += reward

        return self.status_message(reward, self.budget)