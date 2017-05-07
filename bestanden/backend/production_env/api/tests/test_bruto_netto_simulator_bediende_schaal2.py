from django.test import TestCase
from api.models import TaxVariables
from api.Simulator.bruto_netto_simulator import BrutoNettoSimulator


class BrutoNettoSimulatorTestSchaal2Bediende(TestCase):

    fixtures = ['db.json']

    def test_calculate_bruto_netto_married_bediende_2000bruto_partner_no_income(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2000.0
        tax_variables.marital_status = 'married'
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
        self.assertEqual(round(tax, 2), 148.25)
        self.assertEqual(round(tax_decreases, 2), 34.82)
        self.assertEqual(round(rsz_extra, 2), 4.15)
        self.assertEqual(round(netto, 2), 1722.2)

    def test_calculate_bruto_netto_married_bediende_2000bruto_handicapped_partner_no_income(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2000.0
        tax_variables.marital_status = 'married'
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
        self.assertEqual(round(tax, 2), 148.25)
        self.assertEqual(round(tax_decreases, 2), 68.82)
        self.assertEqual(round(rsz_extra, 2), 4.15)
        self.assertEqual(round(netto, 2), 1756.2)

    def test_calculate_bruto_netto_married_bediende_2000bruto_1child_partner_no_income(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2000.0
        tax_variables.marital_status = 'married'
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
        self.assertEqual(round(tax, 2), 148.25)
        self.assertEqual(round(tax_decreases, 2), 68.82)
        self.assertEqual(round(rsz_extra, 2), 4.15)
        self.assertEqual(round(netto, 2), 1756.2)

    def test_calculate_bruto_netto_married_bediende_2000bruto_1child_handicapped_partner_no_income(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2000.0
        tax_variables.marital_status = 'married'
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
        self.assertEqual(round(tax, 2), 148.25)
        self.assertEqual(round(tax_decreases, 2), 127.82)
        self.assertEqual(round(rsz_extra, 2), 4.15)
        self.assertEqual(round(netto, 2), 1815.2)

    def test_calculate_bruto_netto_married_bediende_2000bruto_handicapped_1child_handicapped_partner_no_income(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2000.0
        tax_variables.marital_status = 'married'
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
        self.assertEqual(round(tax, 2), 148.25)
        self.assertEqual(round(tax_decreases, 2), 148.25)
        self.assertEqual(round(rsz_extra, 2), 4.15)
        self.assertEqual(round(netto, 2), 1835.63)

    def test_calculate_bruto_netto_married_bediende_2000bruto_1child_handicapped_and_1child_partner_no_income(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2000.0
        tax_variables.marital_status = 'married'
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
        self.assertEqual(round(tax, 2), 148.25)
        self.assertEqual(round(tax_decreases, 2), 148.25)
        self.assertEqual(round(rsz_extra, 2), 4.15)
        self.assertEqual(round(netto, 2), 1835.63)

    def test_calculate_bruto_netto_married_bediende_2000bruto_2children_handicapped_and_1child_partner_no_income(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2000.0
        tax_variables.marital_status = 'married'
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
        self.assertEqual(round(tax, 2), 148.25)
        self.assertEqual(round(tax_decreases, 2), 148.25)
        self.assertEqual(round(rsz_extra, 2), 4.15)
        self.assertEqual(round(netto, 2), 1835.63)

    def test_calculate_bruto_netto_married_bediende_2000bruto_one_family(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2000.0
        tax_variables.marital_status = 'married'
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
        self.assertEqual(round(tax, 2), 148.25)
        self.assertEqual(round(tax_decreases, 2), 68.82)
        self.assertEqual(round(rsz_extra, 2), 4.15)
        self.assertEqual(round(netto, 2), 1756.2)

    def test_calculate_bruto_netto_married_bediende_2000bruto_1family_handicapped_partner_no_income(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2000.0
        tax_variables.marital_status = 'married'
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
        self.assertEqual(round(tax, 2), 148.25)
        self.assertEqual(round(tax_decreases, 2), 102.82)
        self.assertEqual(round(rsz_extra, 2), 4.15)
        self.assertEqual(round(netto, 2), 1790.2)

    def test_calculate_bruto_netto_married_bediende_2000bruto_1family_old_partner_no_income(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2000.0
        tax_variables.marital_status = 'married'
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
        self.assertEqual(round(tax, 2), 148.25)
        self.assertEqual(round(tax_decreases, 2), 104.82)
        self.assertEqual(round(rsz_extra, 2), 4.15)
        self.assertEqual(round(netto, 2), 1792.2)

    def test_calculate_bruto_netto_married_bediende_2000bruto_1family_old_handicapped_partner_no_income(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2000.0
        tax_variables.marital_status = 'married'
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
        self.assertEqual(round(tax, 2), 148.25)
        self.assertEqual(round(tax_decreases, 2), 148.25)
        self.assertEqual(round(rsz_extra, 2), 4.15)
        self.assertEqual(round(netto, 2), 1835.63)

    def test_calculate_bruto_netto_married_bediende_2000bruto_1family_old_1family_partner_no_income(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2000.0
        tax_variables.marital_status = 'married'
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
        self.assertEqual(round(tax, 2), 148.25)
        self.assertEqual(round(tax_decreases, 2), 138.82)
        self.assertEqual(round(rsz_extra, 2), 4.15)
        self.assertEqual(round(netto, 2), 1826.2)
