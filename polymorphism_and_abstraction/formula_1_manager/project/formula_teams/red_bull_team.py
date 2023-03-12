from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    def team_income(self):
        sponsors = ({1: 1500000, 2: 800000}, {8: 20000, 10: 10000})

        costs = -250000

        return sponsors, costs
