from django.test import TestCase
from api.models import CalculationParameter
from api.models import CarBrand
from api.models import Car
from api.models import CarCategory
from api.models import BikeBrand
from api.models import TechBrand
from api.models import Tech
from api.models import Bike


class TestModels(TestCase):
    def create_carbrand(self, name):
        return CarBrand.objects.create(name=name)

    def test_carbrand_creation(self):
        creation_brand = self.create_carbrand('testbrand')
        query_brand = CarBrand.objects.get(name='testbrand')
        self.assertTrue(isinstance(creation_brand, CarBrand))
        self.assertTrue(isinstance(query_brand, CarBrand))
        self.assertEqual(query_brand.__str__(), creation_brand.name)
        self.assertEqual(creation_brand.name, query_brand.name)

    def create_carcategory(self, name):
        return CarCategory.objects.create(name=name)

    def test_carcategory_creation(self):
        car_cat = self.create_carcategory(2)
        self.assertTrue(isinstance(car_cat, CarCategory))
        self.assertEqual(car_cat.__str__(), str(car_cat.name))

    def create_bikebrand(self, name):
        return BikeBrand.objects.create(name=name)

    def test_bikebrand_creation(self):
        creation_brand = self.create_bikebrand('testbrand')
        query_brand = self.create_bikebrand('testbrand')
        self.assertTrue(isinstance(creation_brand, BikeBrand))
        self.assertTrue(isinstance(query_brand, BikeBrand))
        self.assertEqual(query_brand.__str__(), creation_brand.name)

    def create_techbrand(self, name):
        return TechBrand.objects.create(name=name)

    def test_techbrand_creation(self):
        creation_brand = self.create_techbrand('testbrand')
        query_brand = self.create_techbrand('testbrand')
        self.assertTrue(isinstance(creation_brand, TechBrand))
        self.assertTrue(isinstance(query_brand, TechBrand))
        self.assertEqual(query_brand.__str__(), creation_brand.name)

    def create_calculationparamter(self, year, rsz, woon_werkverkeer, co2_gasoline, co2_diesel, werkbonus):
        return CalculationParameter.objects.create(id=year, rsz=rsz, woon_werkverkeer_auto=woon_werkverkeer,
                                                   co2_diesel=co2_diesel, co2_gasoline=co2_gasoline,
                                                   tax_decrease_multiplier_werkbonus=werkbonus)

    def test_calculationparameter_creation(self):
        params = self.create_calculationparamter(2016, "0.30", "0.31", 107, 89, "28.03")
        self.assertTrue(isinstance(params, CalculationParameter))
        self.assertEqual("2016", params.__str__())

    def create_car(self, brand, model, engine_type, lease_price, co2, catalog_value,
                   registration_year, category, image_url):
        return Car.objects.create(brand=brand, model=model, engine_type=engine_type, lease_price=lease_price, co2=co2,
                                  catalog_value=catalog_value, registration_year=registration_year, category=category,
                                  image_url=image_url)

    def test_car_creation(self):
        creationbrand = self.create_carbrand('Audi')
        car_cat = self.create_carcategory(2)
        car = self.create_car(creationbrand, 'A3', 'diesel', "400.20", 126, "33000", "2016-12-22", car_cat, 'nourl')
        self.assertTrue(isinstance(car, Car))
        self.assertEqual(car.__str__(), str(creationbrand.name) + ' ' + car.model)
        self.assertEqual(Car.objects.all().count(), 1)

    def create_bike(self, brand, model, electric, speed, lease_price):
        return Bike(brand=brand, model=model, electric=electric, speed=speed, lease_price=lease_price)

    def test_bike_creation(self):
        creationbrand = self.create_bikebrand('someBrand')
        bike = self.create_bike(creationbrand, 'tek', True, 0, 20)
        self.assertTrue(isinstance(bike, Bike))
        self.assertEqual(bike.__str__(), str(creationbrand.name) + ' ' + bike.model + ' 20')

    def create_tech(self, brand, model, catalog, devicetype):
        return Tech(brand=brand, model=model, catalog_value=catalog, device_type=devicetype)

    def test_tech_creation(self):
        creationbrand = self.create_techbrand('Oneplus')
        tech = self.create_tech(creationbrand, '3t', 429, 'T')
        self.assertTrue(isinstance(tech, Tech))
        self.assertEqual(tech.__str__(), str(creationbrand.name) + ' ' + tech.model)
