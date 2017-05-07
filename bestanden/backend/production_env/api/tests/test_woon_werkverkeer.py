from django.test import TestCase
from api.Simulator.woon_werkverkeer_simulator import WWVSimulator
from api.models import CalculationParameter


class WoonWerkVerkeerTest(TestCase):
    def setUp(self):
        CalculationParameter.objects.create(id=2016, woon_werkverkeer_auto=0.3412, woon_werkverkeer_fiets=0.22,
                                            woon_werkverkeer_auto_belast_vrij=380).save()
        self.wwvSimulator = WWVSimulator(2016)

    def test_calculate_fiets_20KM_1DAY(self):
        vergoeding = self.wwvSimulator.calculate_fiets_vergoeding(1, 20)
        self.assertEqual(44, vergoeding)

    def test_calculate_fiets_20KM_2DAYS(self):
        vergoeding = self.wwvSimulator.calculate_fiets_vergoeding(4, 20)
        self.assertEqual(158.4, vergoeding)

    def test_calculate_fiets_20KM_5DAYS(self):
        vergoeding = self.wwvSimulator.calculate_fiets_vergoeding(5, 20)
        self.assertEqual(193.6, vergoeding)

    def test_calculate_auto_20KM_1DAY(self):
        vergoeding = self.wwvSimulator.calculate_auto_vergoeding(1, 20)
        self.assertEqual((round(380, 2), round(438.88, 2)), vergoeding)

    def test_calculate_auto_5KM_1DAY(self):
        vergoeding = self.wwvSimulator.calculate_auto_vergoeding(1, 5)
        self.assertEqual((round(204.72, 2), 0), vergoeding)
