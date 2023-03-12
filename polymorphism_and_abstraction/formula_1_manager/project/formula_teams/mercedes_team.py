from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    def team_income(self):
        sponsors = ({1: 1000000, 3: 500000}, {5: 100000, 7: 50000})
        costs = -200000

        return sponsors, costs
