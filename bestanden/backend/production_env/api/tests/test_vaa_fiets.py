from django.test import TestCase
from api.Simulator.vaa_fiets import VAAFiets


class SimulatorServiceTest(TestCase):

    fixtures = ['db.json']

    def test_vaa_fiets(self):
        vaa_fiets = VAAFiets(30, 2016)
        cost, total_cost = vaa_fiets.calc_rsz_and_total_cost()
        self.assertEqual(cost, 0.78)
        self.assertEqual(total_cost, 360)

    def test_vaa_fiets_failover(self):
        vaa_fiets = VAAFiets(30, 2017)
        cost, total_cost = vaa_fiets.calc_rsz_and_total_cost()
        self.assertEqual(cost, 0.78)
        self.assertEqual(total_cost, 360)
