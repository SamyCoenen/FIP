from api.globals.globals import Globals


# Reviewer: Kim
# Everything ok
class WWVSimulator(object):

    def __init__(self, year):
        self.calculation_parameters = Globals.get_correct_calculation_parameters(year)

    # parameters:
    # days: days of going to work with the bike per week
    # kms: kms from home to work (single)
    def calculate_fiets_vergoeding(self, days_per_week, kms):
        return 2 * kms * self.get_workingdays(days_per_week) * self.calculation_parameters.woon_werkverkeer_fiets

    # returns: waarde van autovergoeding per maand (niet belast) en waarde van autovergoeding per maand (belastbaar)
    def calculate_auto_vergoeding(self, days, kms):
        vergoeding = self.get_workingdays(days) * 2 * kms * self.calculation_parameters.woon_werkverkeer_auto * 12

        if vergoeding > self.calculation_parameters.woon_werkverkeer_auto_belast_vrij:
            return \
                round(self.calculation_parameters.woon_werkverkeer_auto_belast_vrij, 2), \
                round((vergoeding - self.calculation_parameters.woon_werkverkeer_auto_belast_vrij), 2)
        else:
            return round(vergoeding, 2),  0

    # berekent dagen dat er gewerkt wordt per maand
    @staticmethod
    def get_workingdays(days_per_week):
        if days_per_week >= 4:
            return days_per_week * 4 + 2
        else:
            return days_per_week * 4 + 1
