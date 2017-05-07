from django.test import TestCase
from api.models import Tech
from api.Simulator.vaa_technology import VAALaptopSmartphoneTablet


class SimulatorServiceVAATechnology(TestCase):

    fixtures = ['db.json']

    def test_vaa_laptop(self):
        laptop = Tech()
        laptop.device_type = 'Laptop'
        laptop.catalog_value = 800
        devices = [laptop]
        vaa_laptop = VAALaptopSmartphoneTablet(2016, devices)

        cost, total_cost = vaa_laptop.calculate_vaa()

        self.assertEqual(cost, 15)
        self.assertEqual(total_cost, 800)

    def test_vaa_smarthphone(self):
        smartphone = Tech()
        smartphone.device_type = 'Smartphone'
        smartphone.catalog_value = 400
        devices = [smartphone]
        vaa_smartphone = VAALaptopSmartphoneTablet(2016, devices)

        cost, total_cost = vaa_smartphone.calculate_vaa()

        self.assertEqual(cost, 12.5)
        self.assertEqual(total_cost, 400)

    def test_vaa_tablet(self):
        tablet = Tech()
        tablet.device_type = 'Tablet'
        tablet.catalog_value = 400
        devices = [tablet]
        vaa_tablet = VAALaptopSmartphoneTablet(2016, devices)

        cost, total_cost = vaa_tablet.calculate_vaa()

        self.assertEqual(cost, 52.28)
        self.assertEqual(total_cost, 400)

    def test_all_three_devices(self):
        laptop = Tech()
        laptop.catalog_value = 800
        laptop.device_type = 'Laptop'

        smartphone = Tech()
        smartphone.catalog_value = 400
        smartphone.device_type = 'Smartphone'

        tablet = Tech()
        tablet.device_type = 'Tablet'
        tablet.catalog_value = 400

        devices = [laptop, smartphone, tablet]

        vaa_devices = VAALaptopSmartphoneTablet(2016, devices)
        cost, total_cost = vaa_devices.calculate_vaa()

        self.assertEqual(cost, 79.78)
        self.assertEqual(total_cost, 1600)

    def test_vaa_internet(self):
        internet = VAALaptopSmartphoneTablet(2016, [], 15)
        vergoed, cost = internet.calculate_vaa_internet_home()

        self.assertEqual(5, vergoed)
        self.assertEqual(cost, 15)
