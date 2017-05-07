from django.test import TestCase
from api.models import TaxVariables
from api.Simulator.bruto_netto_simulator import BrutoNettoSimulator


class SimulatorServiceTestBrutoNettoSchaal1Bediende(TestCase):

    fixtures = ['db.json']

    def test_calculate_bruto_netto_single_bediende_2000bruto(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2000.0
        tax_variables.marital_status = 'single'
        tax_variables.handicapped = False
        tax_variables.partner_income = 0
        tax_variables.partner_income_pension_or_interest = False
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0
        tax_variables.type_worker = 'bediende'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 160.22)
        self.assertEqual(round(werk_bonus, 2), 101.18)
        self.assertEqual(round(taxable_wages, 2), 1839.78)
        self.assertEqual(round(tax, 2), 359.78)
        self.assertEqual(round(tax_decreases, 2), 58.82)
        self.assertEqual(round(rsz_extra, 2), 4.15)
        self.assertEqual(round(netto, 2), 1534.67)

    def test_calculate_bruto_netto_single_bediende_2000bruto_handicapped(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2000.0
        tax_variables.marital_status = 'single'
        tax_variables.handicapped = True
        tax_variables.partner_income = 0
        tax_variables.partner_income_pension_or_interest = False
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0
        tax_variables.type_worker = 'bediende'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 160.22)
        self.assertEqual(round(werk_bonus, 2), 101.18)
        self.assertEqual(round(taxable_wages, 2), 1839.78)
        self.assertEqual(round(tax, 2), 359.78)
        self.assertEqual(round(tax_decreases, 2), 92.82)
        self.assertEqual(round(rsz_extra, 2), 4.15)
        self.assertEqual(round(netto, 2), 1568.67)

    def test_calculate_bruto_netto_single_bediende_2000bruto_not_handicapped_1child(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2000.0
        tax_variables.marital_status = 'single'
        tax_variables.handicapped = False
        tax_variables.partner_income = 0
        tax_variables.partner_income_pension_or_interest = False
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 1
        tax_variables.children_handicapped = 0
        tax_variables.type_worker = 'bediende'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 160.22)
        self.assertEqual(round(werk_bonus, 2), 101.18)
        self.assertEqual(round(taxable_wages, 2), 1839.78)
        self.assertEqual(round(tax, 2), 359.78)
        self.assertEqual(round(tax_decreases, 2), 126.82)
        self.assertEqual(round(rsz_extra, 2), 4.15)
        self.assertEqual(round(netto, 2), 1602.67)

    def test_calculate_bruto_netto_single_bediende_2000bruto_not_handicapped_1child_handicapped(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2000.0
        tax_variables.marital_status = 'single'
        tax_variables.handicapped = False
        tax_variables.partner_income = 0
        tax_variables.partner_income_pension_or_interest = False
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 1
        tax_variables.type_worker = 'bediende'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 160.22)
        self.assertEqual(round(werk_bonus, 2), 101.18)
        self.assertEqual(round(taxable_wages, 2), 1839.78)
        self.assertEqual(round(tax, 2), 359.78)
        self.assertEqual(round(tax_decreases, 2), 185.82)
        self.assertEqual(round(rsz_extra, 2), 4.15)
        self.assertEqual(round(netto, 2), 1661.67)

    def test_calculate_bruto_netto_single_bediende_2000bruto_handicapped_1child_handicapped(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2000.0
        tax_variables.marital_status = 'single'
        tax_variables.handicapped = True
        tax_variables.partner_income = 0
        tax_variables.partner_income_pension_or_interest = False
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 1
        tax_variables.type_worker = 'bediende'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 160.22)
        self.assertEqual(round(werk_bonus, 2), 101.18)
        self.assertEqual(round(taxable_wages, 2), 1839.78)
        self.assertEqual(round(tax, 2), 359.78)
        self.assertEqual(round(tax_decreases, 2), 219.82)
        self.assertEqual(round(rsz_extra, 2), 4.15)
        self.assertEqual(round(netto, 2), 1695.67)

    def test_calculate_bruto_netto_single_bediende_2000bruto_1child_handicapped_and_1child(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2000.0
        tax_variables.marital_status = 'single'
        tax_variables.handicapped = False
        tax_variables.partner_income = 0
        tax_variables.partner_income_pension_or_interest = False
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 1
        tax_variables.children_handicapped = 1
        tax_variables.type_worker = 'bediende'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 160.22)
        self.assertEqual(round(werk_bonus, 2), 101.18)
        self.assertEqual(round(taxable_wages, 2), 1839.78)
        self.assertEqual(round(tax, 2), 359.78)
        self.assertEqual(round(tax_decreases, 2), 340.82)
        self.assertEqual(round(rsz_extra, 2), 4.15)
        self.assertEqual(round(netto, 2), 1816.67)

    def test_calculate_bruto_netto_single_bediende_2000bruto_2child_handicapped_and_1child_no_family(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2000.0
        tax_variables.marital_status = 'single'
        tax_variables.handicapped = False
        tax_variables.partner_income = 0
        tax_variables.partner_income_pension_or_interest = False
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 1
        tax_variables.children_handicapped = 2
        tax_variables.type_worker = 'bediende'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 160.22)
        self.assertEqual(round(werk_bonus, 2), 101.18)
        self.assertEqual(round(taxable_wages, 2), 1839.78)
        self.assertEqual(round(tax, 2), 359.78)
        self.assertEqual(round(tax_decreases, 2), 359.78)
        self.assertEqual(round(rsz_extra, 2), 4.15)
        self.assertEqual(round(netto, 2), 1835.63)

    def test_calculate_bruto_netto_single_bediende_2000bruto_one_family(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2000.0
        tax_variables.marital_status = 'single'
        tax_variables.handicapped = False
        tax_variables.partner_income = 0
        tax_variables.partner_income_pension_or_interest = False
        tax_variables.family_members_old = 0
        tax_variables.family_members = 1
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0
        tax_variables.type_worker = 'bediende'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 160.22)
        self.assertEqual(round(werk_bonus, 2), 101.18)
        self.assertEqual(round(taxable_wages, 2), 1839.78)
        self.assertEqual(round(tax, 2), 359.78)
        self.assertEqual(round(tax_decreases, 2), 92.82)
        self.assertEqual(round(rsz_extra, 2), 4.15)
        self.assertEqual(round(netto, 2), 1568.67)

    def test_calculate_bruto_netto_single_bediende_2000bruto_not_handicapped_no_children_1family_handicapped(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2000.0
        tax_variables.marital_status = 'single'
        tax_variables.handicapped = False
        tax_variables.partner_income = 0
        tax_variables.partner_income_pension_or_interest = False
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 1
        tax_variables.children = 0
        tax_variables.children_handicapped = 0
        tax_variables.type_worker = 'bediende'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 160.22)
        self.assertEqual(round(werk_bonus, 2), 101.18)
        self.assertEqual(round(taxable_wages, 2), 1839.78)
        self.assertEqual(round(tax, 2), 359.78)
        self.assertEqual(round(tax_decreases, 2), 126.82)
        self.assertEqual(round(rsz_extra, 2), 4.15)
        self.assertEqual(round(netto, 2), 1602.67)

    def test_calculate_bruto_netto_single_bediende_2000bruto_1family_old(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2000.0
        tax_variables.marital_status = 'single'
        tax_variables.handicapped = False
        tax_variables.partner_income = 0
        tax_variables.partner_income_pension_or_interest = False
        tax_variables.family_members_old = 1
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0
        tax_variables.type_worker = 'bediende'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 160.22)
        self.assertEqual(round(werk_bonus, 2), 101.18)
        self.assertEqual(round(taxable_wages, 2), 1839.78)
        self.assertEqual(round(tax, 2), 359.78)
        self.assertEqual(round(tax_decreases, 2), 128.82)
        self.assertEqual(round(rsz_extra, 2), 4.15)
        self.assertEqual(round(netto, 2), 1604.67)

    def test_calculate_bruto_netto_single_bediende_2000bruto_1family_old_handicapped(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2000.0
        tax_variables.marital_status = 'single'
        tax_variables.handicapped = False
        tax_variables.partner_income = 0
        tax_variables.partner_income_pension_or_interest = False
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 1
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0
        tax_variables.type_worker = 'bediende'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 160.22)
        self.assertEqual(round(werk_bonus, 2), 101.18)
        self.assertEqual(round(taxable_wages, 2), 1839.78)
        self.assertEqual(round(tax, 2), 359.78)
        self.assertEqual(round(tax_decreases, 2), 198.82)
        self.assertEqual(round(rsz_extra, 2), 4.15)
        self.assertEqual(round(netto, 2), 1674.67)

    def test_calculate_bruto_netto_single_bediende_2000bruto_1family_old_1family(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2000.0
        tax_variables.marital_status = 'single'
        tax_variables.handicapped = False
        tax_variables.partner_income = 0
        tax_variables.partner_income_pension_or_interest = False
        tax_variables.family_members_old = 1
        tax_variables.family_members = 1
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0
        tax_variables.type_worker = 'bediende'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 160.22)
        self.assertEqual(round(werk_bonus, 2), 101.18)
        self.assertEqual(round(taxable_wages, 2), 1839.78)
        self.assertEqual(round(tax, 2), 359.78)
        self.assertEqual(round(tax_decreases, 2), 162.82)
        self.assertEqual(round(rsz_extra, 2), 4.15)
        self.assertEqual(round(netto, 2), 1638.67)
