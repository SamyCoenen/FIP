from django.test import TestCase
from api.models import CalculationParameter
from api.Simulator.vaa_hospitalisation import VAAHospitalisation


# Reviewer: Robin Lycops
class SimulatorServiceTest(TestCase):

    fixtures = ['db.json']

    def test_hospitalisation_cost_partner(self):
        vaa_hospitalisation = VAAHospitalisation(True, 0, 2016)

        cost = vaa_hospitalisation.calculate_hospitalisation()

        self.assertEqual(cost, 175)

    def test_hospitalisation_cost_one_child(self):
        vaa_hospitalisation = VAAHospitalisation(False, 1, 2016)

        cost = vaa_hospitalisation.calculate_hospitalisation()

        self.assertEqual(cost, 68)

    def test_hospitalisation_cost_partner_and_child(self):
        vaa_hospitalisation = VAAHospitalisation(True, 1, 2016)

        cost = vaa_hospitalisation.calculate_hospitalisation()

        self.assertEqual(cost, 243)
