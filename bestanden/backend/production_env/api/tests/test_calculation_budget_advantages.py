from django.test import TestCase
from api.Simulator.budget_voordelen import BudgetAdvantages


class SimulatorServiceTestCalculateBudget(TestCase):

    fixtures = ['db.json']

    def test_calculate_budget(self):

        budget_calculator = BudgetAdvantages(2000, 485, 2016)
        budget = budget_calculator.calculate_budget()

        self.assertEqual(round(budget, 2), 8710)
