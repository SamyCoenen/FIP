from django.test import TestCase
from api.models import TaxVariables
from api.Simulator.rsz_calculations import RSZCalculations
from api.globals.globals import Globals


class SimulatorServiceTestRsz(TestCase):

    fixtures = ['db.json']

    def test_calculate_rsz_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2000
        tax_variables.type_worker = 'arbeider'
        tax_variables.children = 0
        tax_variables.children_handicapped = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.partner_income = 0

        calc_params = Globals.get_correct_calculation_parameters(Globals.year)

        rsz_calulator = RSZCalculations(calc_params, tax_variables)
        rsz, werk_bonus = rsz_calulator.calculate_rsz_and_work_bonus()

        self.assertEqual(round(rsz + werk_bonus, 2), 282.31)

    def test_calculate_rsz_bediende(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2000
        tax_variables.type_worker = 'bediende'
        tax_variables.children = 0
        tax_variables.children_handicapped = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.partner_income = 0

        calc_params = Globals.get_correct_calculation_parameters(Globals.year)

        rsz_calulator = RSZCalculations(calc_params, tax_variables)
        rsz, werk_bonus = rsz_calulator.calculate_rsz_and_work_bonus()

        self.assertEqual(round(rsz + werk_bonus, 2), 261.40)
