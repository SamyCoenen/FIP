from django.test import TestCase
from api.models import TaxVariables
from api.Simulator.bruto_netto_simulator import BrutoNettoSimulator


class SimulatorServiceTestBrutoNettoSchaal1Arbeider(TestCase):

    fixtures = ['db.json']

    def test_calculate_bruto_netto_single_arbeider_2000bruto(self):
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
        tax_variables.type_worker = 'arbeider'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 173.02)
        self.assertEqual(round(werk_bonus, 2), 109.29)
        self.assertEqual(round(taxable_wages, 2), 1826.98)
        self.assertEqual(round(tax, 2), 352.78)
        self.assertEqual(round(tax_decreases, 2), 61.09)
        self.assertEqual(round(rsz_extra, 2), 16.31)
        self.assertEqual(round(netto, 2), 1518.98)

    def test_calculate_bruto_netto_single_arbeider_2000bruto_handicapped(self):
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
        tax_variables.type_worker = 'arbeider'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 173.02)
        self.assertEqual(round(werk_bonus, 2), 109.29)
        self.assertEqual(round(taxable_wages, 2), 1826.98)
        self.assertEqual(round(tax, 2), 352.78)
        self.assertEqual(round(tax_decreases, 2), 95.09)
        self.assertEqual(round(rsz_extra, 2), 16.31)
        self.assertEqual(round(netto, 2), 1552.98)

    def test_calculate_bruto_netto_single_arbeider_2000bruto_1child(self):
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
        tax_variables.type_worker = 'arbeider'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 173.02)
        self.assertEqual(round(werk_bonus, 2), 109.29)
        self.assertEqual(round(taxable_wages, 2), 1826.98)
        self.assertEqual(round(tax, 2), 352.78)
        self.assertEqual(round(tax_decreases, 2), 129.09)
        self.assertEqual(round(rsz_extra, 2), 16.31)
        self.assertEqual(round(netto, 2), 1586.98)

    def test_calculate_bruto_netto_single_arbeider_2000bruto_1child_handicapped_no_family(self):
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
        tax_variables.type_worker = 'arbeider'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 173.02)
        self.assertEqual(round(werk_bonus, 2), 109.29)
        self.assertEqual(round(taxable_wages, 2), 1826.98)
        self.assertEqual(round(tax, 2), 352.78)
        self.assertEqual(round(tax_decreases, 2), 188.09)
        self.assertEqual(round(rsz_extra, 2), 16.31)
        self.assertEqual(round(netto, 2), 1645.98)

    def test_calculate_bruto_netto_single_arbeider_2000bruto_handicapped_1child_handicapped(self):
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
        tax_variables.type_worker = 'arbeider'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 173.02)
        self.assertEqual(round(werk_bonus, 2), 109.29)
        self.assertEqual(round(taxable_wages, 2), 1826.98)
        self.assertEqual(round(tax, 2), 352.78)
        self.assertEqual(round(tax_decreases, 2), 222.09)
        self.assertEqual(round(rsz_extra, 2), 16.31)
        self.assertEqual(round(netto, 2), 1679.98)

    def test_calculate_bruto_netto_single_arbeider_2000bruto_1child_handicapped_and_1child(self):
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
        tax_variables.type_worker = 'arbeider'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 173.02)
        self.assertEqual(round(werk_bonus, 2), 109.29)
        self.assertEqual(round(taxable_wages, 2), 1826.98)
        self.assertEqual(round(tax, 2), 352.78)
        self.assertEqual(round(tax_decreases, 2), 343.09)
        self.assertEqual(round(rsz_extra, 2), 16.31)
        self.assertEqual(round(netto, 2), 1800.98)

    def test_calculate_bruto_netto_single_arbeider_2000bruto_2children_handicapped_and_1child(self):
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
        tax_variables.type_worker = 'arbeider'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 173.02)
        self.assertEqual(round(werk_bonus, 2), 109.29)
        self.assertEqual(round(taxable_wages, 2), 1826.98)
        self.assertEqual(round(tax, 2), 352.78)
        self.assertEqual(round(tax_decreases, 2), 352.78)
        self.assertEqual(round(rsz_extra, 2), 16.31)
        self.assertEqual(round(netto, 2), 1810.67)

    def test_calculate_bruto_netto_single_arbeider_2000bruto_one_family(self):
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
        tax_variables.type_worker = 'arbeider'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 173.02)
        self.assertEqual(round(werk_bonus, 2), 109.29)
        self.assertEqual(round(taxable_wages, 2), 1826.98)
        self.assertEqual(round(tax, 2), 352.78)
        self.assertEqual(round(tax_decreases, 2), 95.09)
        self.assertEqual(round(rsz_extra, 2), 16.31)
        self.assertEqual(round(netto, 2), 1552.98)

    def test_calculate_bruto_netto_single_arbeider_2000bruto_1family_handicapped(self):
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
        tax_variables.type_worker = 'arbeider'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 173.02)
        self.assertEqual(round(werk_bonus, 2), 109.29)
        self.assertEqual(round(taxable_wages, 2), 1826.98)
        self.assertEqual(round(tax, 2), 352.78)
        self.assertEqual(round(tax_decreases, 2), 129.09)
        self.assertEqual(round(rsz_extra, 2), 16.31)
        self.assertEqual(round(netto, 2), 1586.98)

    def test_calculate_bruto_netto_single_arbeider_2000bruto_1family_old(self):
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
        tax_variables.type_worker = 'arbeider'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 173.02)
        self.assertEqual(round(werk_bonus, 2), 109.29)
        self.assertEqual(round(taxable_wages, 2), 1826.98)
        self.assertEqual(round(tax, 2), 352.78)
        self.assertEqual(round(tax_decreases, 2), 131.09)
        self.assertEqual(round(rsz_extra, 2), 16.31)
        self.assertEqual(round(netto, 2), 1588.98)

    def test_calculate_bruto_netto_single_arbeider_2000bruto_1family_old_handicapped(self):
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
        tax_variables.type_worker = 'arbeider'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 173.02)
        self.assertEqual(round(werk_bonus, 2), 109.29)
        self.assertEqual(round(taxable_wages, 2), 1826.98)
        self.assertEqual(round(tax, 2), 352.78)
        self.assertEqual(round(tax_decreases, 2), 201.09)
        self.assertEqual(round(rsz_extra, 2), 16.31)
        self.assertEqual(round(netto, 2), 1658.98)

    def test_calculate_bruto_netto_single_arbeider_2000bruto_1family_old_1family(self):
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
        tax_variables.type_worker = 'arbeider'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 173.02)
        self.assertEqual(round(werk_bonus, 2), 109.29)
        self.assertEqual(round(taxable_wages, 2), 1826.98)
        self.assertEqual(round(tax, 2), 352.78)
        self.assertEqual(round(tax_decreases, 2), 165.09)
        self.assertEqual(round(rsz_extra, 2), 16.31)
        self.assertEqual(round(netto, 2), 1622.98)
