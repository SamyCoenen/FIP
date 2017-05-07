from api.globals.globals import Globals


class BudgetAdvantages(object):

    def __init__(self, bruto, lease_budget, year):
        self.bruto = bruto
        self.thirteenth_month = bruto * 1.08
        self.lease = lease_budget * 12
        self.calc_param = Globals.get_correct_calculation_parameters(year)

    def calculate_budget(self):
        return self.thirteenth_month + self.lease + self.calc_param.tech_budget + 330
