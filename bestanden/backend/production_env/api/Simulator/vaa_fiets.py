from api.globals.globals import Globals


# Reviewer: Robin Lycops
class VAAFiets(object):
    def __init__(self, price, year):
        self.price_bike = price

        self.calc_params = Globals.get_correct_calculation_parameters(year)

    def calc_rsz_and_total_cost(self):
        rsz = self.price_bike * self.calc_params.rsz * self.calc_params.percentage_prive_usage_bike
        return round(rsz, 2), self.price_bike * 12
