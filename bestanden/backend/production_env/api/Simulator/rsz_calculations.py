

class RSZCalculations(object):

    def __init__(self, calc_params, tax_variables):
        self.calc_params = calc_params
        self.tax_variables = tax_variables

    def calculate_rsz_and_work_bonus(self):
        rsz, work_bonus = self.calculate_rsz()
        return rsz, work_bonus

    def calculate_rsz(self):
        rsz = \
            self.tax_variables.bruto * \
            (self.calc_params.arbeider_rsz_multiplier if self.tax_variables.type_worker == 'arbeider' else
             self.calc_params.bediende_rsz_multiplier) * self.calc_params.rsz

        work_bonus = self.work_bonus_rsz()

        return rsz - work_bonus, work_bonus

    def work_bonus_rsz(self):
        if self.tax_variables.type_worker == 'arbeider':
            if round(self.tax_variables.bruto, 2) <= self.calc_params.work_bonus_lowest_boundary:
                return self.calc_params.tax_decrease_work_bonus_arbeider_lowest
            elif round(self.tax_variables.bruto, 2) <= self.calc_params.work_bonus_highest_boundary:
                return \
                    self.calc_params.tax_decrease_work_bonus_arbeider_lowest - \
                    (self.calc_params.tax_decrease_work_bonus_arbeider_multiplier_diff *
                        (self.tax_variables.bruto - self.calc_params.work_bonus_lowest_boundary))
            else:
                return 0
        else:
            if round(self.tax_variables.bruto, 2) <= self.calc_params.work_bonus_lowest_boundary:
                return self.calc_params.tax_decrease_work_bonus_bediende_lowest
            elif round(self.tax_variables.bruto, 2) <= self.calc_params.work_bonus_highest_boundary:
                temp = \
                    self.calc_params.tax_decrease_work_bonus_bediende_lowest - \
                    (self.calc_params.tax_decrease_work_bonus_bediende_multiplier_diff *
                        (self.tax_variables.bruto - self.calc_params.work_bonus_lowest_boundary))
                return 0 if temp < 0 else temp
            else:
                return 0
