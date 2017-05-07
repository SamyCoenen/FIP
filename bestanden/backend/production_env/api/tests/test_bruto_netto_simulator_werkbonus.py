from django.test import TestCase
from api.models import TaxVariables
from api.Simulator.rsz_calculations import RSZCalculations
from api.globals.globals import Globals


class SimulatorServiceTestWerkbonus(TestCase):

    fixtures = ['db.json']

    def test_werkbonus_arbeider_schaal1_no_border_value(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1577.80
        tax_variables.type_worker = 'arbeider'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        calc_params = Globals.get_correct_calculation_parameters(Globals.year)

        rsz_calulator = RSZCalculations(calc_params, tax_variables)
        minus_rsz, work_bonus = rsz_calulator.calculate_rsz_and_work_bonus()

        self.assertEqual(round(work_bonus, 2), 209.29)

    def test_werkbonus_arbeider_schaal1_left_border_value(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1577.89
        tax_variables.type_worker = 'arbeider'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        calc_params = Globals.get_correct_calculation_parameters(Globals.year)

        rsz_calulator = RSZCalculations(calc_params, tax_variables)
        minus_rsz, work_bonus = rsz_calulator.calculate_rsz_and_work_bonus()

        self.assertEqual(round(work_bonus, 2), 209.29)

    def test_werkbonus_arbeider_schaal1_right_border_value(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1577.90
        tax_variables.type_worker = 'arbeider'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        calc_params = Globals.get_correct_calculation_parameters(Globals.year)

        rsz_calulator = RSZCalculations(calc_params, tax_variables)
        minus_rsz, work_bonus = rsz_calulator.calculate_rsz_and_work_bonus()

        self.assertEqual(round(work_bonus, 2), 209.29)

    def test_werkbonus_arbeider_schaal2_no_border_value(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1850
        tax_variables.type_worker = 'arbeider'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        calc_params = Globals.get_correct_calculation_parameters(Globals.year)

        rsz_calulator = RSZCalculations(calc_params, tax_variables)
        rsz, work_bonus = rsz_calulator.calculate_rsz_and_work_bonus()

        self.assertEqual(round(work_bonus, 2), 144.83)

    def test_werkbonus_arbeider_schaal2_left_border_value(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2461.27
        tax_variables.type_worker = 'arbeider'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        calc_params = Globals.get_correct_calculation_parameters(Globals.year)

        rsz_calulator = RSZCalculations(calc_params, tax_variables)
        rsz, work_bonus = rsz_calulator.calculate_rsz_and_work_bonus()

        self.assertEqual(round(work_bonus, 2), 0.02)

    def test_werkbonus_arbeider_schaal2_right_border_value(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2461.28
        tax_variables.type_worker = 'arbeider'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        calc_params = Globals.get_correct_calculation_parameters(Globals.year)

        rsz_calulator = RSZCalculations(calc_params, tax_variables)
        rsz, work_bonus = rsz_calulator.calculate_rsz_and_work_bonus()

        self.assertEqual(round(work_bonus, 2), 0)

    def test_werkbonus_bediende_schaal1_no_border_value(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1577.80
        tax_variables.type_worker = 'bediende'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        calc_params = Globals.get_correct_calculation_parameters(Globals.year)

        rsz_calulator = RSZCalculations(calc_params, tax_variables)
        rsz, work_bonus = rsz_calulator.calculate_rsz_and_work_bonus()

        self.assertEqual(round(work_bonus, 2), 193.79)

    def test_werkbonus_bediende_schaal1_left_border_value(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1577.89
        tax_variables.type_worker = 'bediende'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        calc_params = Globals.get_correct_calculation_parameters(Globals.year)

        rsz_calulator = RSZCalculations(calc_params, tax_variables)
        rsz, work_bonus = rsz_calulator.calculate_rsz_and_work_bonus()

        self.assertEqual(round(work_bonus, 2), 193.79)

    def test_werkbonus_bediende_schaal1_right_border_value(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1577.90
        tax_variables.type_worker = 'bediende'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        calc_params = Globals.get_correct_calculation_parameters(Globals.year)

        rsz_calulator = RSZCalculations(calc_params, tax_variables)
        rsz, work_bonus = rsz_calulator.calculate_rsz_and_work_bonus()

        self.assertEqual(round(work_bonus, 2), 193.79)

    def test_werkbonus_bediende_schaal2_no_border_value(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1850
        tax_variables.type_worker = 'bediende'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        calc_params = Globals.get_correct_calculation_parameters(Globals.year)

        rsz_calulator = RSZCalculations(calc_params, tax_variables)
        rsz, work_bonus = rsz_calulator.calculate_rsz_and_work_bonus()

        self.assertEqual(round(work_bonus, 2), 134.09)

    def test_werkbonus_bediende_schaal2_left_border_value(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2461.27
        tax_variables.type_worker = 'bediende'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        calc_params = Globals.get_correct_calculation_parameters(Globals.year)

        rsz_calulator = RSZCalculations(calc_params, tax_variables)
        rsz, work_bonus = rsz_calulator.calculate_rsz_and_work_bonus()

        self.assertEqual(round(work_bonus, 2), 0)

    def test_werkbonus_bediende_schaal2_right_border_value(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2461.28
        tax_variables.type_worker = 'bediende'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        calc_params = Globals.get_correct_calculation_parameters(Globals.year)

        rsz_calulator = RSZCalculations(calc_params, tax_variables)
        rsz, work_bonus = rsz_calulator.calculate_rsz_and_work_bonus()

        self.assertEqual(round(work_bonus, 2), 0)
