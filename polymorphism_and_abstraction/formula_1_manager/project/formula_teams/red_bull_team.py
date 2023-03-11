from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    def calculate_revenue_after_race(self, race_pos: int):
        sponsor_rewards = ({1: 1500000, 2: 800000}, {8: 20000, 10: 10000})

        reward = self.check_winnings(sponsor_rewards, race_pos)

        reward -= 250000

        self.budget += reward

        return self.status_message(reward, self.budget)
