from api.models import TaxVariables
from api.globals.globals import Globals
from api.Simulator.rsz_calculations import RSZCalculations


# Reviewer: Robin Lycops
class BrutoNettoSimulator(object):

    def __init__(self, tax_variables: TaxVariables, year, additions_no_rsz=0):
        self.payroll = Globals.get_correct_tax_scales(year)
        self.additions_no_rsz = additions_no_rsz
        self.calc_params = Globals.get_correct_calculation_parameters(year)
        self.rsz_calculator = RSZCalculations(self.calc_params, tax_variables)
        self.standard_year = Globals.year
        self.tax_variables = tax_variables
        self.total_children = self.tax_variables.children + self.tax_variables.children_handicapped * 2
        self.total_family_members_old = tax_variables.family_members_old + \
            tax_variables.family_members_old_handicapped * 2
        self.total_family_members_young = tax_variables.family_members + \
            tax_variables.family_members_handicapped * 2
        self.rent_income = \
            tax_variables.partner_income - tax_variables.partner_income * self.calc_params.rsz * \
            self.calc_params.pension_rent_multiplier if tax_variables.partner_income_pension_or_interest else 0

        self.scale = 2

        if self.tax_variables.marital_status == 'single' or self.tax_variables.marital_status == 'married' and \
           self.tax_variables.partner_income > 0 and not self.tax_variables.partner_income_pension_or_interest:
            self.scale = 1

    def calculate_netto(self):
        rsz, work_bonus = self.rsz_calculator.calculate_rsz_and_work_bonus()
        taxable_wages = round(self.tax_variables.bruto - rsz, 2) + self.additions_no_rsz

        if taxable_wages <= self.calc_params.high_income_boundary:
            tax = self.calculate_tax(taxable_wages)
            rsz_extra = self.bijzondere_bijdrage_sociale_zekerheid()
            tax_decreases = self.calculate_tax_decreases(taxable_wages, work_bonus, tax)
        else:
            tax, tax_decreases = self.calculate_tax_high_income(taxable_wages)
            rsz_extra = self.bijzondere_bijdrage_sociale_zekerheid()

        if tax_decreases > tax:
            tax_decreases = tax

        netto = self.calculate_netto_from_taxable_wages(tax, rsz_extra, tax_decreases, taxable_wages)

        return round(rsz, 2), round(work_bonus, 2), round(taxable_wages, 2), round(tax, 2), round(tax_decreases, 2), \
            round(rsz_extra, 2), round(netto, 2)

    def calculate_tax(self, taxable_wages):
        return self.get_correct_tax(taxable_wages)

    def calculate_tax_decreases(self, taxable_wages, werk_bonus, tax):
        tax_decreases = self.calculate_general_tax_decreases()
        tax_decreases = self.calculate_scale_dependent_decreases(tax_decreases)

        return self.decrease_due_to_low_income(taxable_wages, tax_decreases, tax) + \
            self.decrease_of_tax_with_work_bonus(werk_bonus)

    def calculate_scale_dependent_decreases(self, tax_decreases):
        if self.scale == 1:
            return tax_decreases + self.scale_1()
        else:
            return tax_decreases + self.scale_2()

    def calculate_general_tax_decreases(self):
        tax_decrease = self.decrease_childeren_under_care()
        tax_decrease += self.total_family_members_old * self.calc_params.tax_decrease_old_family_member
        tax_decrease += self.total_family_members_young * self.calc_params.tax_decrease_family_member

        if self.tax_variables.handicapped:
            tax_decrease += self.calc_params.tax_decrease_handicapped

        return tax_decrease

    def scale_1(self):
        tax_decrease = 0
        tax_decrease = self.decrease_other_family_cares_scale_1(tax_decrease)

        return tax_decrease

    def scale_2(self):
        tax_decrease = 0
        tax_decrease = self.decrease_other_family_cares_scale_2(tax_decrease)

        return tax_decrease

    def calculate_tax_high_income(self, taxable_wages):
        new_taxable_wages = taxable_wages // 15 * 15

        if self.scale == 1 or self.rent_income > self.calc_params.high_income_rent_boundary:
            tax = \
                self.calc_params.high_income_base_tax_scale1 + self.calc_params.high_income_multiplier_of_diff * \
                (new_taxable_wages - self.calc_params.high_income_boundary)
            tax_decrease = self.decrease_childeren_under_care()
            tax_decrease = self.decrease_other_family_cares_scale_1(tax_decrease)
            return tax, tax_decrease
        else:
            tax = \
                self.calc_params.high_income_base_tax_scale2 + self.calc_params.high_income_multiplier_of_diff * \
                (new_taxable_wages - self.calc_params.high_income_boundary)
            tax_decrease = self.decrease_childeren_under_care()
            tax_decrease = self.decrease_other_family_cares_scale_2(tax_decrease)
            return tax, tax_decrease

    def decrease_childeren_under_care(self):
        tax_decrease = 0
        if self.total_children == 1:
            tax_decrease += self.calc_params.tax_decrease_child1
        elif self.total_children == 2:
            tax_decrease += self.calc_params.tax_decrease_child2
        elif self.total_children == 3:
            tax_decrease += self.calc_params.tax_decrease_child3
        elif self.total_children == 4:
            tax_decrease += self.calc_params.tax_decrease_child4
        elif self.total_children == 5:
            tax_decrease += self.calc_params.tax_decrease_child5
        elif self.total_children == 6:
            tax_decrease += self.calc_params.tax_decrease_child6
        elif self.total_children == 7:
            tax_decrease += self.calc_params.tax_decrease_child7
        elif self.total_children >= 8:
            tax_decrease += \
                self.calc_params.tax_decrease_child8 + (self.total_children - 8) * \
                self.calc_params.tax_decrease_child8plus_multiplier

        return tax_decrease

    def decrease_other_family_cares_scale_1(self, tax_decrease):
        if self.tax_variables.marital_status == 'single':
            tax_decrease += self.calc_params.tax_decrease_single
        if (self.tax_variables.widow or
                self.tax_variables.marital_status != 'married' and self.total_children >= 1):
            tax_decrease += self.calc_params.tax_decrease_widow_or_unmarried_with_children
        if (self.tax_variables.marital_status == 'married' and self.tax_variables.partner_income <= 216 and not
                self.tax_variables.partner_income_pension_or_interest):
            tax_decrease += self.calc_params.tax_decrease_married_partner_low_income
        if (self.tax_variables.marital_status == 'married' and self.rent_income <= 432 and
                self.tax_variables.partner_income_pension_or_interest):
            tax_decrease += self.calc_params.tax_decrease_married_partner_low_rent

        return tax_decrease

    def decrease_other_family_cares_scale_2(self, tax_decrease):
        if self.tax_variables.handicapped_partner:
            tax_decrease += self.calc_params.tax_decrease_handicapped

        return tax_decrease

    def decrease_due_to_low_income(self, taxable_wages, tax_decrease, tax):
        if tax_decrease > tax:
            tax_decrease = tax
        if taxable_wages + tax_decrease <= self.calc_params.low_income_boundary:
            tax_decrease += self.calc_params.tax_decrease_low_income
        return tax_decrease

    def get_correct_tax(self, taxable_wages):
        if self.scale == 2:
            return self.get_correct_tax_scale2(taxable_wages)
        else:
            return self.get_correct_tax_scale1(taxable_wages)

    def get_correct_tax_scale1(self, taxable_wages):
        i = 0
        while i < len(self.payroll):
            if taxable_wages // 15 * 15 == self.payroll[i].bruto:
                return self.payroll[i].scale1
            i += 1
        return 0

    def get_correct_tax_scale2(self, taxable_wages):
        i = 0
        while i < len(self.payroll):
            if taxable_wages // 15 * 15 == self.payroll[i].bruto:
                return self.payroll[i].scale2
            i += 1
        return 0

    # the documentation found suggests upper bound included
    def bijzondere_bijdrage_sociale_zekerheid(self):
        bruto = round(self.tax_variables.bruto * self.calc_params.bediende_rsz_multiplier
                      if self.tax_variables.type_worker == 'bediende'
                      else self.tax_variables.bruto * self.calc_params.arbeider_rsz_multiplier, 2)

        if bruto <= self.calc_params.bijzondere_bijdrage_sz_lowest_boundary_np:
            return 0
        elif bruto <= self.calc_params.bijzondere_bijdrage_sz_lowest_boundary:
            return self.bijzondere_bijdrage_sociale_zekerheid_cat1()
        elif bruto <= self.calc_params.bijzondere_bijdrage_sz_middle_boundary:
            return self.bijzondere_bijdrage_sociale_zekerheid_cat2(bruto)
        elif bruto <= self.calc_params.bijzondere_bijdrage_sz_high_boundary:
            return self.bijzondere_bijdrage_sociale_zekerheid_cat3(bruto)
        else:
            return self.bijzondere_bijdrage_sociale_zekerheid_cat4()

    def bijzondere_bijdrage_sociale_zekerheid_cat1(self):
        if self.tax_variables.marital_status == 'married' and self.tax_variables.partner_income > 0:
            return self.calc_params.bijzondere_bijdrage_sz_married_and_income
        else:
            return 0

    def bijzondere_bijdrage_sociale_zekerheid_cat2(self, bruto):
        temp = \
            self.calc_params.bijzondere_bijdrage_sz_multiplier_middle_cat\
            * (bruto - self.calc_params.bijzondere_bijdrage_sz_lowest_boundary)
        temp = self.calc_params.bijzondere_bijdrage_sz_middle_cat_max_value \
            if temp > self.calc_params.bijzondere_bijdrage_sz_middle_cat_max_value else temp

        if self.tax_variables.marital_status == 'single' or self.tax_variables.partner_income == 0:
            return temp
        else:
            return temp \
                if temp > self.calc_params.bijzondere_bijdrage_sz_middle_cat_min_value \
                else self.calc_params.bijzondere_bijdrage_sz_middle_cat_min_value

    def bijzondere_bijdrage_sociale_zekerheid_cat3(self, bruto):
        temp = \
            self.calc_params.bijzondere_bijdrage_sz_middle_cat_max_value + \
            self.calc_params.bijzondere_bijdrage_sz_multiplier_high_cat * \
            (bruto - self.calc_params.bijzondere_bijdrage_sz_middle_boundary)

        if self.tax_variables.marital_status == 'single' or self.tax_variables.partner_income == 0:
            return temp
        else:
            return self.calc_params.bijzondere_bijdrage_sz_high_cat_max_value \
                if temp > self.calc_params.bijzondere_bijdrage_sz_high_cat_max_value else temp

    def bijzondere_bijdrage_sociale_zekerheid_cat4(self):
        if self.tax_variables.marital_status == 'single' or self.tax_variables.partner_income == 0:
            return self.calc_params.bijzondere_bijdrage_sz_highest_cat_scale1
        else:
            return self.calc_params.bijzondere_bijdrage_sz_high_cat_max_value

    def decrease_of_tax_with_work_bonus(self, work_bonus):
        return work_bonus * self.calc_params.tax_decrease_multiplier_werkbonus

    @staticmethod
    def calculate_netto_from_taxable_wages(tax, rsz_extra, tax_decrease, taxable_wages):
        if tax_decrease >= tax:
            return taxable_wages - rsz_extra
        else:
            tax -= tax_decrease
            return taxable_wages - tax - rsz_extra
