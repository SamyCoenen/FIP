from django.test import TestCase
from api.models import TaxVariables
from api.Simulator.bruto_netto_simulator import BrutoNettoSimulator


class SimulatorServiceTestChildrenTaxDecrease(TestCase):

    fixtures = ['db.json']

    def test_0_child_tax_decrease(self):
        tax_variables = TaxVariables()
        tax_variables.children = 0
        tax_variables.children_handicapped = 0
        tax_variables.family_members = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.partner_income = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        decrease = bruto_netto_simulator.decrease_childeren_under_care()

        self.assertEqual(decrease, 0)

    def test_1_child_tax_decrease(self):
        tax_variables = TaxVariables()
        tax_variables.children = 1
        tax_variables.children_handicapped = 0
        tax_variables.family_members = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.partner_income = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        decrease = bruto_netto_simulator.decrease_childeren_under_care()

        self.assertEqual(decrease, 34)

    def test_2_children_tax_decrease(self):
        tax_variables = TaxVariables()
        tax_variables.children = 2
        tax_variables.children_handicapped = 0
        tax_variables.family_members = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.partner_income = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        decrease = bruto_netto_simulator.decrease_childeren_under_care()

        self.assertEqual(decrease, 93)

    def test_3_children_tax_decrease(self):
        tax_variables = TaxVariables()
        tax_variables.children = 3
        tax_variables.children_handicapped = 0
        tax_variables.family_members = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.partner_income = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        decrease = bruto_netto_simulator.decrease_childeren_under_care()

        self.assertEqual(decrease, 248)

    def test_4_children_tax_decrease(self):
        tax_variables = TaxVariables()
        tax_variables.children = 4
        tax_variables.children_handicapped = 0
        tax_variables.family_members = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.partner_income = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        decrease = bruto_netto_simulator.decrease_childeren_under_care()

        self.assertEqual(decrease, 454)

    def test_5_children_tax_decrease(self):
        tax_variables = TaxVariables()
        tax_variables.children = 5
        tax_variables.children_handicapped = 0
        tax_variables.family_members = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.partner_income = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        decrease = bruto_netto_simulator.decrease_childeren_under_care()

        self.assertEqual(decrease, 671)

    def test_6_children_tax_decrease(self):
        tax_variables = TaxVariables()
        tax_variables.children = 6
        tax_variables.children_handicapped = 0
        tax_variables.family_members = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.partner_income = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        decrease = bruto_netto_simulator.decrease_childeren_under_care()

        self.assertEqual(decrease, 887)

    def test_7_children_tax_decrease(self):
        tax_variables = TaxVariables()
        tax_variables.children = 7
        tax_variables.children_handicapped = 0
        tax_variables.family_members = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.partner_income = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        decrease = bruto_netto_simulator.decrease_childeren_under_care()

        self.assertEqual(decrease, 1104)

    def test_8_children_tax_decrease(self):
        tax_variables = TaxVariables()
        tax_variables.children = 8
        tax_variables.children_handicapped = 0
        tax_variables.family_members = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.partner_income = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        decrease = bruto_netto_simulator.decrease_childeren_under_care()

        self.assertEqual(decrease, 1337)

    def test_9_children_tax_decrease(self):
        tax_variables = TaxVariables()
        tax_variables.children = 9
        tax_variables.children_handicapped = 0
        tax_variables.family_members = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.partner_income = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        decrease = bruto_netto_simulator.decrease_childeren_under_care()

        self.assertEqual(decrease, 1578)
