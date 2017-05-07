from django.test import TestCase
from api.models import TaxVariables
from api.Simulator.bruto_netto_simulator import BrutoNettoSimulator


class SimulatorBrutoNettoSchaal2Arbeider(TestCase):

    fixtures = ['db.json']

    def test_calculate_bruto_netto_married_arbeider_2000bruto_partner_no_income(self):
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
        tax_variables.type_worker = 'arbeider'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 173.02)
        self.assertEqual(round(werk_bonus, 2), 109.29)
        self.assertEqual(round(taxable_wages, 2), 1826.98)
        self.assertEqual(round(tax, 2), 142.72)
        self.assertEqual(round(tax_decreases, 2), 37.09)
        self.assertEqual(round(rsz_extra, 2), 16.31)
        self.assertEqual(round(netto, 2), 1705.04)

    def test_calculate_bruto_netto_married_arbeider_2000bruto_handicapped_partner_no_income(self):
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
        tax_variables.type_worker = 'arbeider'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 173.02)
        self.assertEqual(round(werk_bonus, 2), 109.29)
        self.assertEqual(round(taxable_wages, 2), 1826.98)
        self.assertEqual(round(tax, 2), 142.72)
        self.assertEqual(round(tax_decreases, 2), 71.09)
        self.assertEqual(round(rsz_extra, 2), 16.31)
        self.assertEqual(round(netto, 2), 1739.04)

    def test_calculate_bruto_netto_married_arbeider_2000bruto_1child_partner_no_income(self):
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
        tax_variables.type_worker = 'arbeider'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 173.02)
        self.assertEqual(round(werk_bonus, 2), 109.29)
        self.assertEqual(round(taxable_wages, 2), 1826.98)
        self.assertEqual(round(tax, 2), 142.72)
        self.assertEqual(round(tax_decreases, 2), 71.09)
        self.assertEqual(round(rsz_extra, 2), 16.31)
        self.assertEqual(round(netto, 2), 1739.04)

    def test_calculate_bruto_netto_married_arbeider_2000bruto_1child_handicapped_partner_no_income(self):
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
        tax_variables.type_worker = 'arbeider'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 173.02)
        self.assertEqual(round(werk_bonus, 2), 109.29)
        self.assertEqual(round(taxable_wages, 2), 1826.98)
        self.assertEqual(round(tax, 2), 142.72)
        self.assertEqual(round(tax_decreases, 2), 130.09)
        self.assertEqual(round(rsz_extra, 2), 16.31)
        self.assertEqual(round(netto, 2), 1798.04)

    def test_calculate_bruto_married_arbeider_2000bruto_handicapped_1child_handicapped_partner_no_income(self):
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

        tax_variables.type_worker = 'arbeider'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 173.02)
        self.assertEqual(round(werk_bonus, 2), 109.29)
        self.assertEqual(round(taxable_wages, 2), 1826.98)
        self.assertEqual(round(tax, 2), 142.72)
        self.assertEqual(round(tax_decreases, 2), 142.72)
        self.assertEqual(round(rsz_extra, 2), 16.31)
        self.assertEqual(round(netto, 2), 1810.67)

    def test_calculate_bruto_netto_married_arbeider_2000bruto_1child_handicapped_and_1child_partner_no_income(self):
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
        tax_variables.type_worker = 'arbeider'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 173.02)
        self.assertEqual(round(werk_bonus, 2), 109.29)
        self.assertEqual(round(taxable_wages, 2), 1826.98)
        self.assertEqual(round(tax, 2), 142.72)
        self.assertEqual(round(tax_decreases, 2), 142.72)
        self.assertEqual(round(rsz_extra, 2), 16.31)
        self.assertEqual(round(netto, 2), 1810.67)

    def test_calculate_bruto_netto_married_arbeider_2000bruto_2children_handicapped_and_1child_partner_no_income(self):
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
        tax_variables.type_worker = 'arbeider'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 173.02)
        self.assertEqual(round(werk_bonus, 2), 109.29)
        self.assertEqual(round(taxable_wages, 2), 1826.98)
        self.assertEqual(round(tax, 2), 142.72)
        self.assertEqual(round(tax_decreases, 2), 142.72)
        self.assertEqual(round(rsz_extra, 2), 16.31)
        self.assertEqual(round(netto, 2), 1810.67)

    def test_calculate_bruto_netto_married_arbeider_2000bruto_one_family_partner_no_income(self):
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
        tax_variables.type_worker = 'arbeider'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 173.02)
        self.assertEqual(round(werk_bonus, 2), 109.29)
        self.assertEqual(round(taxable_wages, 2), 1826.98)
        self.assertEqual(round(tax, 2), 142.72)
        self.assertEqual(round(tax_decreases, 2), 71.09)
        self.assertEqual(round(rsz_extra, 2), 16.31)
        self.assertEqual(round(netto, 2), 1739.04)

    def test_calculate_bruto_netto_married_arbeider_2000bruto_1family_handicapped_partner_no_income(self):
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
        tax_variables.type_worker = 'arbeider'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 173.02)
        self.assertEqual(round(werk_bonus, 2), 109.29)
        self.assertEqual(round(taxable_wages, 2), 1826.98)
        self.assertEqual(round(tax, 2), 142.72)
        self.assertEqual(round(tax_decreases, 2), 105.09)
        self.assertEqual(round(rsz_extra, 2), 16.31)
        self.assertEqual(round(netto, 2), 1773.04)

    def test_calculate_bruto_netto_married_arbeider_2000bruto_1family_old_partner_no_income(self):
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
        tax_variables.type_worker = 'arbeider'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 173.02)
        self.assertEqual(round(werk_bonus, 2), 109.29)
        self.assertEqual(round(taxable_wages, 2), 1826.98)
        self.assertEqual(round(tax, 2), 142.72)
        self.assertEqual(round(tax_decreases, 2), 107.09)
        self.assertEqual(round(rsz_extra, 2), 16.31)
        self.assertEqual(round(netto, 2), 1775.04)

    def test_calculate_bruto_netto_married_arbeider_2000bruto_1family_old_handicapped_partner_no_income(self):
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
        tax_variables.type_worker = 'arbeider'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 173.02)
        self.assertEqual(round(werk_bonus, 2), 109.29)
        self.assertEqual(round(taxable_wages, 2), 1826.98)
        self.assertEqual(round(tax, 2), 142.72)
        self.assertEqual(round(tax_decreases, 2), 142.72)
        self.assertEqual(round(rsz_extra, 2), 16.31)
        self.assertEqual(round(netto, 2), 1810.67)

    def test_calculate_bruto_netto_married_arbeider_2000bruto_1family_old_1family_partner_no_income(self):
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
        tax_variables.type_worker = 'arbeider'

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 173.02)
        self.assertEqual(round(werk_bonus, 2), 109.29)
        self.assertEqual(round(taxable_wages, 2), 1826.98)
        self.assertEqual(round(tax, 2), 142.72)
        self.assertEqual(round(tax_decreases, 2), 141.09)
        self.assertEqual(round(rsz_extra, 2), 16.31)
        self.assertEqual(round(netto, 2), 1809.04)
