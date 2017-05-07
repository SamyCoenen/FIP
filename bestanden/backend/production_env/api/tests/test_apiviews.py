from django.urls import reverse
from rest_framework.test import APITestCase
import json
from api.models import CalculationParameter
from api.models import CarBrand
from api.models import Car
from api.models import CarCategory
from api.models import BikeBrand
from api.models import TechBrand
from api.models import Tech
from api.models import Bike


class ApiViewTests(APITestCase):
    fixtures = ['db.json']

    def setUp(self):
        carbrand = CarBrand.objects.create(name='carbrandtest')
        carcat = CarCategory.objects.create(name=2)
        bikebrand = BikeBrand.objects.create(name='bikebrandtest')
        techbrand = TechBrand.objects.create(name='techbrandtest')
        Car.objects.create(brand=carbrand, model='cartestmodel', engine_type='diesel', lease_price="400.20", co2=126,
                           catalog_value="33000", registration_year="2016-12-22", category=carcat,
                           image_url='nourl')
        Bike(brand=bikebrand, model='tek', electric=True, speed=20, lease_price=20)
        Tech(brand=techbrand, model='oneplus', catalog_value=439, device_type='S')
        Tech(brand=techbrand, model='y200', catalog_value=439, device_type='L')
        Tech(brand=techbrand, model='x300', catalog_value=439, device_type='T')

    def test_laptoplist(self):
        url = reverse('laptops')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), len(Tech.objects.filter(device_type='L')))

    def test_smartphonelist(self):
        url = reverse('smartphones')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), len(Tech.objects.filter(device_type='S')))

    def test_tabletlist(self):
        url = reverse('tablets')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), len(Tech.objects.filter(device_type='T')))

    def test_carlist(self):
        url = reverse('cars')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), len(Car.objects.all()))

    def test_bikelist(self):
        url = reverse('bikes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), len(Bike.objects.all()))

    def test_techlist(self):
        url = reverse('tech')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), len(Tech.objects.all()))

    def test_calculationparameterlist(self):
        url = reverse('calcparams')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), len(CalculationParameter.objects.all()))

    def test_fip_calculator_no_options(self):
        url = reverse('calculator')

        data = {"income_info": {"bruto": 2000, "type_worker": "arbeider", "marital_status": "single",
                                "handicapped_partner": False, "partner_income": 0,
                                "partner_income_pension_or_interest": False, "handicapped": False,
                                "children_handicapped": 0, "children": 0, "family_members": 0, "family_members_old": 0,
                                "family_members_handicapped": 0, "family_members_old_handicapped": 0}}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)

        response_data_expected = {"rsz_extra": 16.31, "tax": 352.78, "tax_decreases": 61.09, "taxable_wages": 1826.98,
                                  "rsz": 173.02, "werkbonus": 109.29, "netto": 1518.98, "budget": 2890,
                                  "end_budget_payment": 2106.54, "total_end_budget_payment": 2106.54,
                                  "total_budget": 2890, "mobility_budget": 0, "netto_without_options": 1518.98,
                                  'social_budget': 0, 'allowance': 0}

        self.assertJSONEqual(json.dumps(response.data), json.dumps(response_data_expected))

    def test_fip_calculator_all_options_but_car(self):
        url = reverse('calculator')

        data = {"income_info": {"bruto": 2000, "type_worker": "arbeider", "marital_status": "single",
                                "handicapped_partner": False, "partner_income": 0,
                                "partner_income_pension_or_interest": False, "handicapped": False,
                                "children_handicapped": 0, "children": 0, "family_members": 0, "family_members_old": 0,
                                "family_members_handicapped": 0, "family_members_old_handicapped": 0},
                "bike": {"lease_price": 20}, "tech": {"smartphone_value": 400, "laptop_value": 1000,
                                                      "multimedia_value": 600, "internet_value": 25},
                "allowance": {"days": 5, "kms": 20}}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)

        response_data_expected = {"werkbonus": 109.29, "netto": 1462.94, "tax": 408.82, "tax_decreases": 61.09,
                                  "rsz_extra": 16.31, "taxable_wages": 1938.42, "rsz": 173.02, "budget": 350,
                                  "end_budget_payment": 255.12, "total_end_budget_payment": 2106.54,
                                  "total_budget": 2890, "mobility_budget": 240, "netto_without_options": 1518.98,
                                  "tech_budget": 2300, 'social_budget': 0, 'allowance': 1978.23}

        self.assertJSONEqual(json.dumps(response.data), json.dumps(response_data_expected))

    def test_fip_calculator_all_options(self):
        url = reverse('calculator')

        data = {"income_info": {"bruto": 2000, "type_worker": "arbeider", "marital_status": "single",
                                "handicapped_partner": False, "partner_income": 0,
                                "partner_income_pension_or_interest": False, "handicapped": False,
                                "children_handicapped": 0, "children": 0, "family_members": 0, "family_members_old": 0,
                                "family_members_handicapped": 0, "family_members_old_handicapped": 0},
                "bike": {"lease_price": 20}, "tech": {"smartphone_value": 400, "laptop_value": 1000,
                                                      "multimedia_value": 600, "internet_value": 25},
                "allowance": {"days": 5, "kms": 20},
                "car": {"engine_type": "diesel", "co2_car": 135, "catalog_value": 26000,
                        "registration_year": "2017-01-18", "lease_price": 437},
                "social_benefits": {"hospitalisation_partner": True, "children_hospitalisation": 2,
                                    "children_benefits": 2, "retirement_saving": True}}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)

        response_data_expected = {"werkbonus": 109.29, "netto": 1378.87, "tax": 492.89, "tax_decreases": 61.09,
                                  "rsz_extra": 16.31, "rsz": 173.02, "taxable_wages": 2125.99, "budget": -1466.3,
                                  "end_budget_payment": -1068.8, "total_end_budget_payment": 2106.54,
                                  "total_budget": 8134, "mobility_budget": 6060, "netto_without_options": 1518.98,
                                  'tech_budget': 2300, 'social_budget': 1240.3, 'allowance': 1978.23}

        self.assertJSONEqual(json.dumps(response.data), json.dumps(response_data_expected))
