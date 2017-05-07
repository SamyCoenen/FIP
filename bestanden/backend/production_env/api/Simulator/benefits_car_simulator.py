import datetime
from math import floor
from api.globals.globals import Globals


class BenefitsCarSimulator(object):

    def __init__(self, year):
        self.calculation_parameters = Globals.get_correct_calculation_parameters(year)

    # Reviewer: Kim Gijbels
    # Question: get of parameter of 2016
    # But the algorithm seems ok, verified on:
    # http://www.voordeelalleaardberekenen.be/
    @staticmethod
    def get_co2percentage_for_cartype(enginetype, co2_car, calc_params):
        co2_percentage = 0
        if enginetype == 'diesel':
            co2_percentage = (5.5 + (co2_car - calc_params.co2_diesel) * 0.1) / 100
        elif enginetype == 'benzine' or enginetype == 'lpg' or enginetype == 'aardgas':
            co2_percentage = (5.5 + (co2_car - calc_params.co2_gasoline) * 0.1) / 100
        if co2_percentage < 0.04:
            return 0.04
        elif co2_percentage > 0.18:
            return 0.18
        else:
            return round(co2_percentage, 4)

    # Reviewer: Kim Gijbels
    # Algorithm verified on:
    # https://www.dragintra.com/pdf/vaa/2012-10-01-voordeel-van-alle-aard-bedrijfswagens.pdf
    def get_catalog_value(self, catalog_value, registration_year, today=datetime.date.today()):
        years_diff = self.get_years_diff(registration_year, today)
        if years_diff >= 5:
            return round(catalog_value * 0.7, 2)
        else:
            return round((1 - years_diff * 0.06) * catalog_value, 2)

    # Reviewer: Kim Gijbels
    # Checks how many full years the car has been registered
    @staticmethod
    def get_years_diff(registration_year, today=datetime.date.today()):
        if registration_year > today:
            return 0
        else:
            days_diff = today - registration_year
            years_diff = floor(days_diff.days / 365)

            return years_diff

    # Reviewer: Kim Gijbels
    # Algorithm verified on:
    # http://www.voordeelalleaardberekenen.be/
    # Gebruiksduur is calculated in the adjusted_catalog_value
    def calculate_benefits_car(
            self, catalog_value, registration_year, enginetype, co2_car, today=datetime.date.today()):

        co2_percent = self.get_co2percentage_for_cartype(enginetype, co2_car, self.calculation_parameters)
        adjusted_catalog_value = self.get_catalog_value(catalog_value, registration_year, today)
        benefits = round(adjusted_catalog_value * co2_percent * 6 / 7, 2)

        if benefits < self.calculation_parameters.max_vaa_car:
            benefits = self.calculation_parameters.max_vaa_car

        return benefits

    def calculate_budget_decrease(self, lease):
        if lease <= self.calculation_parameters.car_cat1_lease:
            return self.calculation_parameters.car_cat1_lease * 12
        elif lease <= self.calculation_parameters.car_cat2_lease:
            return self.calculation_parameters.car_cat2_lease * 12
        else:
            return self.calculation_parameters.car_cat3_lease * 12
