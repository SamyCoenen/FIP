from django.test import TestCase
from api.models import TaxVariables
from api.Simulator.bruto_netto_simulator import BrutoNettoSimulator


class SimulatorServiceTestHighIncome(TestCase):

    fixtures = ['db.json']

    def test_scale1_income_7500_should_not_be_high_income(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 8627.63
        tax_variables.marital_status = 'single'
        tax_variables.handicapped = False
        tax_variables.partner_income = 0
        tax_variables.partner_income_pension_or_interest = False
        tax_variables.children_handicapped = 0
        tax_variables.children = 0
        tax_variables.family_members = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.type_worker = 'bediende'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 1127.63)
        self.assertEqual(round(werk_bonus, 2), 0)
        self.assertEqual(round(taxable_wages, 2), 7500)
        self.assertEqual(round(tax, 2), 3287.26)
        self.assertEqual(round(tax_decreases, 2), 24)
        self.assertEqual(round(rsz_extra, 2), 60.94)
        self.assertEqual(round(netto, 2), 4175.8)

    def test_scale1_income_7500_right_boundary(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 8627.64
        tax_variables.marital_status = 'single'
        tax_variables.handicapped = False
        tax_variables.partner_income = 0
        tax_variables.partner_income_pension_or_interest = False
        tax_variables.children_handicapped = 0
        tax_variables.children = 0
        tax_variables.family_members = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.type_worker = 'bediende'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 1127.63)
        self.assertEqual(round(werk_bonus, 2), 0)
        self.assertEqual(round(taxable_wages, 2), 7500.01)
        self.assertEqual(round(tax, 2), 3287.26)
        self.assertEqual(round(tax_decreases, 2), 24)
        self.assertEqual(round(rsz_extra, 2), 60.94)
        self.assertEqual(round(netto, 2), 4175.81)

    def test_scale1_income_7500_no_boundary(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 8950
        tax_variables.marital_status = 'single'
        tax_variables.handicapped = False
        tax_variables.partner_income = 0
        tax_variables.partner_income_pension_or_interest = False
        tax_variables.children_handicapped = 0
        tax_variables.children = 0
        tax_variables.family_members = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.type_worker = 'bediende'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 1169.77)
        self.assertEqual(round(werk_bonus, 2), 0)
        self.assertEqual(round(taxable_wages, 2), 7780.23)
        self.assertEqual(round(tax, 2), 3431.71)
        self.assertEqual(round(tax_decreases, 2), 24)
        self.assertEqual(round(rsz_extra, 2), 60.94)
        self.assertEqual(round(netto, 2), 4311.58)

    def test_scale1_income_7500_right_boundary_one_child(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 8627.64
        tax_variables.marital_status = 'single'
        tax_variables.handicapped = False
        tax_variables.partner_income = 0
        tax_variables.partner_income_pension_or_interest = False
        tax_variables.children_handicapped = 0
        tax_variables.children = 1
        tax_variables.family_members = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.type_worker = 'bediende'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 1127.63)
        self.assertEqual(round(werk_bonus, 2), 0)
        self.assertEqual(round(taxable_wages, 2), 7500.01)
        self.assertEqual(round(tax, 2), 3287.26)
        self.assertEqual(round(tax_decreases, 2), 92)
        self.assertEqual(round(rsz_extra, 2), 60.94)
        self.assertEqual(round(netto, 2), 4243.81)

    def test_scale2_income_7500_should_not_be_high_income(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 8627.63
        tax_variables.marital_status = 'married'
        tax_variables.handicapped = False
        tax_variables.partner_income = 0
        tax_variables.partner_income_pension_or_interest = False
        tax_variables.children_handicapped = 0
        tax_variables.children = 0
        tax_variables.family_members = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.type_worker = 'bediende'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 1127.63)
        self.assertEqual(round(werk_bonus, 2), 0)
        self.assertEqual(round(taxable_wages, 2), 7500)
        self.assertEqual(round(tax, 2), 2922.79)
        self.assertEqual(round(tax_decreases, 2), 0)
        self.assertEqual(round(rsz_extra, 2), 60.94)
        self.assertEqual(round(netto, 2), 4516.27)

    def test_scale2_income_7500_right_boundary(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 8627.64
        tax_variables.marital_status = 'married'
        tax_variables.handicapped = False
        tax_variables.partner_income = 0
        tax_variables.partner_income_pension_or_interest = False
        tax_variables.children_handicapped = 0
        tax_variables.children = 0
        tax_variables.family_members = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.type_worker = 'bediende'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 1127.63)
        self.assertEqual(round(werk_bonus, 2), 0)
        self.assertEqual(round(taxable_wages, 2), 7500.01)
        self.assertEqual(round(tax, 2), 2922.79)
        self.assertEqual(round(tax_decreases, 2), 0)
        self.assertEqual(round(rsz_extra, 2), 60.94)
        self.assertEqual(round(netto, 2), 4516.28)

    def test_scale2_income_7500_no_boundary(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 8950
        tax_variables.marital_status = 'married'
        tax_variables.handicapped = False
        tax_variables.partner_income = 0
        tax_variables.partner_income_pension_or_interest = False
        tax_variables.children_handicapped = 0
        tax_variables.children = 0
        tax_variables.family_members = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.type_worker = 'bediende'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 1169.77)
        self.assertEqual(round(werk_bonus, 2), 0)
        self.assertEqual(round(taxable_wages, 2), 7780.23)
        self.assertEqual(round(tax, 2), 3067.24)
        self.assertEqual(round(tax_decreases, 2), 0)
        self.assertEqual(round(rsz_extra, 2), 60.94)
        self.assertEqual(round(netto, 2), 4652.05)

    def test_scale2_income_7500_right_boundary_one_child(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 8627.64
        tax_variables.marital_status = 'married'
        tax_variables.handicapped = False
        tax_variables.partner_income = 0
        tax_variables.partner_income_pension_or_interest = False
        tax_variables.children_handicapped = 0
        tax_variables.children = 1
        tax_variables.family_members = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.type_worker = 'bediende'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 1127.63)
        self.assertEqual(round(werk_bonus, 2), 0)
        self.assertEqual(round(taxable_wages, 2), 7500.01)
        self.assertEqual(round(tax, 2), 2922.79)
        self.assertEqual(round(tax_decreases, 2), 34)
        self.assertEqual(round(rsz_extra, 2), 60.94)
        self.assertEqual(round(netto, 2), 4550.28)
