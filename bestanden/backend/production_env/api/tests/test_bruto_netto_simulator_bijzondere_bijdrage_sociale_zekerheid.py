from api.Simulator.bruto_netto_simulator import BrutoNettoSimulator
from django.test import TestCase
from api.models import TaxVariables


class BrutoNettoSimulatorBijzondereBijdrageSocialeZekerheid(TestCase):

    fixtures = ['db.json']

    def test_bijzondere_bijdrage_socialezekerheid_cat1_cat1_no_border_value_single_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1009.26
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'single'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)

        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()
        self.assertEqual(round(added_rsz, 2), 0)

    def test_bijzondere_bijdrage_socialezekerheid_cat1_cat1_border_value_left_single_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1013.97
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'single'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 0)

    def test_bijzondere_bijdrage_socialezekerheid_cat1_cat1_border_value_right_single_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1013.98
        tax_variables.marital_status = 'single'
        tax_variables.type_worker = 'arbeider'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 0)

    def test_bijzondere_bijdrage_socialezekerheid_cat1_cat2_no_border_value_single_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1018.52
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'single'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 0)

    def test_bijzondere_bijdrage_socialezekerheid_cat1_cat2_border_value_left_single_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1801.28
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'single'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 0)

    def test_bijzondere_bijdrage_socialezekerheid_cat1_cat2_border_value_right_single_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1801.29
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'single'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()
        self.assertEqual(round(added_rsz, 2), 0)

    def test_bijzondere_bijdrage_socialezekerheid_cat1_cat3_no_border_value_single_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1964.84
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'single'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 13.43)

    def test_bijzondere_bijdrage_socialezekerheid_cat1_cat3_border_value_left_single_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2027.94
        tax_variables.type_worker = 'arbeider'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 18.6)

    def test_bijzondere_bijdrage_socialezekerheid_cat1_cat3_border_value_right_single_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2027.95
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'single'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 18.6)

    def test_bijzondere_bijdrage_socialezekerheid_cat1_cat4_no_border_value_single_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2130.09
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'single'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 19.81)

    def test_bijzondere_bijdrage_socialezekerheid_cat1_cat4_border_value_left_single_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 5591.50
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'single'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 60.94)

    def test_bijzondere_bijdrage_socialezekerheid_cat1_cat4_border_value_right_single_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 5591.51
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'single'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 60.94)

    def test_bijzondere_bijdrage_socialezekerheid_cat1_cat1_no_border_value_married_no_income_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1009.26
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'married'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 0)

    def test_bijzondere_bijdrage_socialezekerheid_cat1_cat1_border_value_left_married_no_income_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1013.97
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'married'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 0)

    def test_bijzondere_bijdrage_socialezekerheid_cat1_cat1_border_value_right_married_no_income_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1013.98
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'married'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 0)

    def test_bijzondere_bijdrage_socialezekerheid_cat1_cat2_no_border_value_married_no_income_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1018.52
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'married'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 0)

    def test_bijzondere_bijdrage_socialezekerheid_cat1_cat2_border_value_left_married_no_income_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1801.28
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'married'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 0)

    def test_bijzondere_bijdrage_socialezekerheid_cat1_cat2_border_value_right_married_no_income_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1801.29
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'married'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 0)

    def test_bijzondere_bijdrage_socialezekerheid_cat1_cat3_no_border_value_married_no_income_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1964.84
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'married'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 13.43)

    def test_bijzondere_bijdrage_socialezekerheid_cat1_cat3_border_value_left_married_no_income_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2027.94
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'married'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 18.6)

    def test_bijzondere_bijdrage_socialezekerheid_cat1_cat3_border_value_right_married_no_income_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2027.95
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'married'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 18.6)

    def test_bijzondere_bijdrage_socialezekerheid_cat1_cat4_no_border_value_married_no_income_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2130.09
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'married'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 19.81)

    def test_bijzondere_bijdrage_socialezekerheid_cat1_cat4_border_value_left_married_no_income_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 5591.50
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'married'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 60.94)

    def test_bijzondere_bijdrage_socialezekerheid_cat1_cat4_border_value_right_married_no_income_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 5591.51
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'married'
        tax_variables.partner_income = 0
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 60.94)

    def test_bijzondere_bijdrage_socialezekerheid_cat2_cat1_no_border_value_married_income_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1009.26
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'married'
        tax_variables.partner_income = 1500
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 0)

    def test_bijzondere_bijdrage_socialezekerheid_cat2_cat1_border_value_left_married_income_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1013.97
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'married'
        tax_variables.partner_income = 1500
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 0)

    def test_bijzondere_bijdrage_socialezekerheid_cat2_cat1_border_value_right_married_income_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1013.99
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'married'
        tax_variables.partner_income = 1500
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 9.30)

    def test_bijzondere_bijdrage_socialezekerheid_cat2_cat2_no_border_value_married_income_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1018.52
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'married'
        tax_variables.partner_income = 1500
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 9.30)

    def test_bijzondere_bijdrage_socialezekerheid_cat2_cat2_border_value_left_married_income_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1801.28
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'married'
        tax_variables.partner_income = 1500
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 9.30)

    def test_bijzondere_bijdrage_socialezekerheid_cat2_cat2_border_value_right_married_income_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1801.28
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'married'
        tax_variables.partner_income = 1500
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 9.30)

    def test_bijzondere_bijdrage_socialezekerheid_cat2_cat3_no_border_value_married_income_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 1964.84
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'married'
        tax_variables.partner_income = 1500
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 13.43)

    def test_bijzondere_bijdrage_socialezekerheid_cat2_cat3_border_value_left_married_income_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2027.94
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'married'
        tax_variables.partner_income = 1500
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 18.6)

    def test_bijzondere_bijdrage_socialezekerheid_cat2_cat3_border_value_right_married_income_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2027.95
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'married'
        tax_variables.partner_income = 1500
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 18.6)

    def test_bijzondere_bijdrage_socialezekerheid_cat2_cat4_no_border_value_married_income_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 2130.09
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'married'
        tax_variables.partner_income = 1500
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 19.81)

    def test_bijzondere_bijdrage_socialezekerheid_cat2_cat4_border_value_left_married_income_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 5591.50
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'married'
        tax_variables.partner_income = 1500
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 51.64)

    def test_bijzondere_bijdrage_socialezekerheid_cat2_cat4_border_value_right_married_income_arbeider(self):
        tax_variables = TaxVariables()
        tax_variables.bruto = 5591.51
        tax_variables.type_worker = 'arbeider'
        tax_variables.marital_status = 'married'
        tax_variables.partner_income = 1500
        tax_variables.family_members_old = 0
        tax_variables.family_members = 0
        tax_variables.family_members_old_handicapped = 0
        tax_variables.family_members_handicapped = 0
        tax_variables.children = 0
        tax_variables.children_handicapped = 0

        bruto_netto_simulator = BrutoNettoSimulator(tax_variables, 2016)
        added_rsz = bruto_netto_simulator.bijzondere_bijdrage_sociale_zekerheid()

        self.assertEqual(round(added_rsz, 2), 51.64)
