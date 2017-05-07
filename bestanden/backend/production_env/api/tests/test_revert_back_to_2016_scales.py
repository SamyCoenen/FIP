from django.test import TestCase
from api.models import TaxVariables
from api.Simulator.bruto_netto_simulator import BrutoNettoSimulator


class SimulatorServiceTestRevertTo2016Scales(TestCase):

    fixtures = ['db.json']

    def test_revert_back_to_2016_scales_when_scales_of_year_not_found(self):
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

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 50000)
        rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = bruto_netto_simulator.calculate_netto()

        self.assertEqual(round(rsz, 2), 173.02)
        self.assertEqual(round(werk_bonus, 2), 109.29)
        self.assertEqual(round(taxable_wages, 2), 1826.98)
        self.assertEqual(round(tax, 2), 352.78)
        self.assertEqual(round(tax_decreases, 2), 61.09)
        self.assertEqual(round(rsz_extra, 2), 16.31)
        self.assertEqual(round(netto, 2), 1518.98)
