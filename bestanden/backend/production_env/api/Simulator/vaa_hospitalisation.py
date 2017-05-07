from api.globals.globals import Globals


# Reviewer: Robin Lycops
class VAAHospitalisation(object):

    def __init__(self, partner, children, year):
        self.partner = partner
        self.children = children
        self.calculation_parameters = Globals.get_correct_calculation_parameters(year)

    def calculate_hospitalisation(self):
        cost = 0
        if self.partner:
            cost = self.calculation_parameters.hospitalisation_partner

        if self.children > 0 :
            cost += self.children * self.calculation_parameters.hospitalisation_child

        return cost
