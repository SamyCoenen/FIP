from django.test import TestCase
from api.Simulator.benefits_car_simulator import BenefitsCarSimulator
import datetime


# Create your tests here.
# car benefits are based on the simulator: https://www.sd.be/carcostcalculator/Default.aspx?lang=nl
class VaaAutoTest(TestCase):

    fixtures = ['db.json']

    def setUp(self):
        self.benefitsCarSimulator = BenefitsCarSimulator(2016)

    # Test dieselwagens
    def test_calculate_benefits_car_no_aging_diesel(self):
        benefits = self.benefitsCarSimulator.calculate_benefits_car(33751, datetime.date(2016, 12, 22), 'diesel', 126,
                                                                    datetime.date(2016, 12, 22))
        self.assertEqual(2661.51, benefits)
        adjust_catalog = self.benefitsCarSimulator.get_catalog_value(33751, datetime.date(2016, 12, 22),
                                                                     datetime.date(2016, 12, 22))
        self.assertEqual(33751, adjust_catalog)
        years_diff = self.benefitsCarSimulator.get_years_diff(datetime.date(2016, 12, 22), datetime.date(2016, 12, 22))
        self.assertEqual(0, years_diff)

    def test_calculate_benefits_car_no_aging_diesel_negative_registration_year(self):
        benefits = self.benefitsCarSimulator.calculate_benefits_car(33751, datetime.date(2017, 12, 22), 'diesel', 126,
                                                                    datetime.date(2016, 12, 22))
        self.assertEqual(2661.51, benefits)

    def test_calculate_benefits_car_age_1year_diesel(self):
        years_diff = self.benefitsCarSimulator.get_years_diff(datetime.date(2016, 12, 22), datetime.date(2017, 12, 22))
        self.assertEqual(1, years_diff)
        adjust_catalog = self.benefitsCarSimulator.get_catalog_value(33751, datetime.date(2016, 12, 22),
                                                                     datetime.date(2017, 12, 22))
        self.assertEqual(31725.94, adjust_catalog)
        benefits = self.benefitsCarSimulator.calculate_benefits_car(33751, datetime.date(2016, 12, 22), 'diesel', 126,
                                                                    datetime.date(2017, 12, 22))
        self.assertEqual(2501.82, benefits)

    def test_calculate_benefits_car_age_6year_diesel(self):
        years_diff = self.benefitsCarSimulator.get_years_diff(datetime.date(2016, 12, 22), datetime.date(2022, 12, 22))
        self.assertEqual(6, years_diff)
        adjust_catalog = self.benefitsCarSimulator.get_catalog_value(33751, datetime.date(2016, 12, 22),
                                                                     datetime.date(2022, 12, 22))
        self.assertEqual(23625.7, adjust_catalog)
        benefits = self.benefitsCarSimulator.calculate_benefits_car(33751, datetime.date(2016, 12, 22), 'diesel', 126,
                                                                    datetime.date(2022, 12, 22))
        self.assertEqual(1863.06, benefits)

    def test_calculate_benefits_car_age_5year_diesel(self):
        years_diff = self.benefitsCarSimulator.get_years_diff(datetime.date(2016, 12, 22), datetime.date(2021, 12, 22))
        self.assertEqual(5, years_diff)
        adjust_catalog = self.benefitsCarSimulator.get_catalog_value(33751, datetime.date(2016, 12, 22),
                                                                     datetime.date(2021, 12, 22))
        self.assertEqual(23625.7, adjust_catalog)
        benefits = self.benefitsCarSimulator.calculate_benefits_car(33751, datetime.date(2016, 12, 22), 'diesel', 126,
                                                                    datetime.date(2022, 12, 22))
        self.assertEqual(1863.06, benefits)

    def test_calculate_benefits_car_no_aging_diesel_highco2(self):
        benefits = self.benefitsCarSimulator.calculate_benefits_car(33751, datetime.date(2016, 12, 22), 'diesel', 300,
                                                                    datetime.date(2016, 12, 22))
        self.assertEqual(5207.30, benefits)

    def test_calculate_benefits_car_no_aging_diesel_lowco2(self):
        benefits = self.benefitsCarSimulator.calculate_benefits_car(33751, datetime.date(2016, 12, 22), 'diesel', 89,
                                                                    datetime.date(2016, 12, 22))
        self.assertEqual(1591.12, benefits)

    def test_calculate_benefits_car_no_aging_diesel_lowco2_below_reference_co2(self):
        benefits = self.benefitsCarSimulator.calculate_benefits_car(33751, datetime.date(2016, 12, 22), 'diesel', 70,
                                                                    datetime.date(2016, 12, 22))
        self.assertEqual(1260, benefits)

    def test_calculate_benefits_car_age_5year_diesel_highco2(self):
        benefits = self.benefitsCarSimulator.calculate_benefits_car(33751, datetime.date(2016, 12, 22), 'diesel', 300,
                                                                    datetime.date(2021, 12, 22))
        self.assertEqual(3645.11, benefits)

    # Test benzine
    def test_calculate_benefits_car_no_aging_benzine(self):
        benefits = self.benefitsCarSimulator.calculate_benefits_car(33751, datetime.date(2016, 12, 22), 'benzine', 126,
                                                                    datetime.date(2016, 12, 22))
        self.assertEqual(2140.78, benefits)
        years_diff = self.benefitsCarSimulator.get_years_diff(datetime.date(2016, 12, 22), datetime.date(2016, 12, 22))
        self.assertEqual(0, years_diff)
        adjust_catalog = self.benefitsCarSimulator.get_catalog_value(33751, datetime.date(2016, 12, 22),
                                                                     datetime.date(2016, 12, 22))
        self.assertEqual(33751, adjust_catalog)

    def test_calculate_benefits_car_age_1year_benzine(self):
        years_diff = self.benefitsCarSimulator.get_years_diff(datetime.date(2016, 12, 22), datetime.date(2017, 12, 22))
        self.assertEqual(1, years_diff)
        adjust_catalog = self.benefitsCarSimulator.get_catalog_value(33751, datetime.date(2016, 12, 22),
                                                                     datetime.date(2017, 12, 22))
        self.assertEqual(31725.94, adjust_catalog)
        benefits = self.benefitsCarSimulator.calculate_benefits_car(33751, datetime.date(2016, 12, 22), 'benzine', 126,
                                                                    datetime.date(2017, 12, 22))
        self.assertEqual(2012.33, benefits)

    def test_calculate_benefits_car_age_6year_benzine(self):
        years_diff = self.benefitsCarSimulator.get_years_diff(datetime.date(2016, 12, 22), datetime.date(2022, 12, 22))
        self.assertEqual(6, years_diff)
        adjust_catalog = self.benefitsCarSimulator.get_catalog_value(33751, datetime.date(2016, 12, 22),
                                                                     datetime.date(2022, 12, 22))
        self.assertEqual(23625.7, adjust_catalog)
        benefits = self.benefitsCarSimulator.calculate_benefits_car(33751, datetime.date(2016, 12, 22), 'benzine', 126,
                                                                    datetime.date(2022, 12, 22))
        self.assertEqual(1498.54, benefits)

    def test_calculate_benefits_car_age_5year_benzine(self):
        years_diff = self.benefitsCarSimulator.get_years_diff(datetime.date(2016, 12, 22), datetime.date(2021, 12, 22))
        self.assertEqual(5, years_diff)
        adjust_catalog = self.benefitsCarSimulator.get_catalog_value(33751, datetime.date(2016, 12, 22),
                                                                     datetime.date(2021, 12, 22))
        self.assertEqual(23625.7, adjust_catalog)
        benefits = self.benefitsCarSimulator.calculate_benefits_car(33751, datetime.date(2016, 12, 22), 'benzine', 126,
                                                                    datetime.date(2021, 12, 22))
        self.assertEqual(1498.54, benefits)

    def test_calculate_benefits_car_no_aging_benzine_highco2(self):
        benefits = self.benefitsCarSimulator.calculate_benefits_car(33751, datetime.date(2016, 12, 22), 'benzine', 300,
                                                                    datetime.date(2016, 12, 22))
        self.assertEqual(5207.30, benefits)

    def test_calculate_benefits_car_age_5year_benzine_highco2(self):
        benefits = self.benefitsCarSimulator.calculate_benefits_car(33751, datetime.date(2016, 12, 22), 'benzine', 300,
                                                                    datetime.date(2021, 12, 22))
        self.assertEqual(3645.11, benefits)

    def test_calculate_benefits_car_no_aging_benzine_lowco2(self):
        benefits = self.benefitsCarSimulator.calculate_benefits_car(33751, datetime.date(2016, 12, 22), 'benzine', 107,
                                                                    datetime.date(2016, 12, 22))
        self.assertEqual(1591.12, benefits)

    def test_calculate_benefits_car_no_aging_benzine_lowco2_below_reference_co2(self):
        benefits = self.benefitsCarSimulator.calculate_benefits_car(33751, datetime.date(2016, 12, 22), 'benzine', 70,
                                                                    datetime.date(2016, 12, 22))
        self.assertEqual(1260, benefits)

    # Test electric
    def test_calculate_benefits_car_no_aging_electric(self):
        benefits = self.benefitsCarSimulator.calculate_benefits_car(33751, datetime.date(2016, 12, 22), 'electric', 126,
                                                                    datetime.date(2016, 12, 22))
        # voordeel alle aard mag niet lager gaan dan 1260/jaar dus gebruik indien het lager gaat 1260
        # self.assertEqual(1157.18, benefits)
        self.assertEqual(1260, benefits)
        years_diff = self.benefitsCarSimulator.get_years_diff(datetime.date(2016, 12, 22), datetime.date(2016, 12, 22))
        self.assertEqual(0, years_diff)
        adjust_catalog = self.benefitsCarSimulator.get_catalog_value(33751, datetime.date(2016, 12, 22),
                                                                     datetime.date(2016, 12, 22))
        self.assertEqual(33751, adjust_catalog)

    def test_calculate_benefits_car_age_1year_electric(self):
        years_diff = self.benefitsCarSimulator.get_years_diff(datetime.date(2016, 12, 22), datetime.date(2017, 12, 22))
        self.assertEqual(1, years_diff)
        adjust_catalog = self.benefitsCarSimulator.get_catalog_value(33751, datetime.date(2016, 12, 22),
                                                                     datetime.date(2017, 12, 22))
        self.assertEqual(31725.94, adjust_catalog)
        benefits = self.benefitsCarSimulator.calculate_benefits_car(33751, datetime.date(2016, 12, 22), 'electric', 126,
                                                                    datetime.date(2017, 12, 22))
        # voordeel alle aard mag niet lager gaan dan 1260/jaar dus gebruik indien het lager gaat 1260
        # self.assertEqual(1087.75, benefits)
        self.assertEqual(1260, benefits)

    def test_calculate_benefits_car_age_6year_electric(self):
        years_diff = self.benefitsCarSimulator.get_years_diff(datetime.date(2016, 12, 22), datetime.date(2022, 12, 22))
        self.assertEqual(6, years_diff)
        adjust_catalog = self.benefitsCarSimulator.get_catalog_value(33751, datetime.date(2016, 12, 22),
                                                                     datetime.date(2022, 12, 22))
        self.assertEqual(23625.7, adjust_catalog)
        benefits = self.benefitsCarSimulator.calculate_benefits_car(33751, datetime.date(2016, 12, 22), 'electric', 126,
                                                                    datetime.date(2022, 12, 22))
        # voordeel alle aard mag niet lager gaan dan 1260/jaar dus gebruik indien het lager gaat 1260
        # self.assertEqual(810.02, benefits)
        self.assertEqual(1260, benefits)

    def test_calculate_benefits_car_age_5year_electric(self):
        years_diff = self.benefitsCarSimulator.get_years_diff(datetime.date(2016, 12, 22), datetime.date(2021, 12, 22))
        self.assertEqual(5, years_diff)
        adjust_catalog = self.benefitsCarSimulator.get_catalog_value(33751, datetime.date(2016, 12, 22),
                                                                     datetime.date(2021, 12, 22))
        self.assertEqual(23625.7, adjust_catalog)
        benefits = self.benefitsCarSimulator.calculate_benefits_car(33751, datetime.date(2016, 12, 22), 'electric', 126,
                                                                    datetime.date(2021, 12, 22))
        # voordeel alle aard mag niet lager gaan dan 1260/jaar dus gebruik indien het lager gaat 1260
        # self.assertEqual(810.02, benefits)
        self.assertEqual(1260, benefits)

    def test_calculate_benefits_car_no_aging_electric_lowco2(self):
        benefits = self.benefitsCarSimulator.calculate_benefits_car(33751, datetime.date(2016, 12, 22), 'electric', 70,
                                                                    datetime.date(2016, 12, 22))
        # voordeel alle aard mag niet lager gaan dan 1260/jaar dus gebruik indien het lager gaat 1260
        # self.assertEqual(1157.18, benefits)
        self.assertEqual(1260, benefits)

    def test_calculate_benefits_car_no_aging_electric_highco2(self):
        benefits = self.benefitsCarSimulator.calculate_benefits_car(33751, datetime.date(2016, 12, 22), 'electric', 300,
                                                                    datetime.date(2016, 12, 22))
        # voordeel alle aard mag niet lager gaan dan 1260/jaar dus gebruik indien het lager gaat 1260
        # self.assertEqual(1157.18, benefits)
        self.assertEqual(1260, benefits)

    def test_calculate_benefits_car_age_5year_electric_lowco2(self):
        benefits = self.benefitsCarSimulator.calculate_benefits_car(33751, datetime.date(2016, 12, 22), 'electric', 70,
                                                                    datetime.date(2021, 12, 22))
        # voordeel alle aard mag niet lager gaan dan 1260/jaar dus gebruik indien het lager gaat 1260
        # self.assertEqual(810.02, benefits)
        self.assertEqual(1260, benefits)

    def test_calculate_benefits_car_age_5year_electric_highco2(self):
        benefits = self.benefitsCarSimulator.calculate_benefits_car(33751, datetime.date(2016, 12, 22), 'electric', 300,
                                                                    datetime.date(2021, 12, 22))
        # voordeel alle aard mag niet lager gaan dan 1260/jaar dus gebruik indien het lager gaat 1260
        # self.assertEqual(810.02, benefits)
        self.assertEqual(1260, benefits)

    def test_calculate_benefits_car_age_5year_electric_highco2_negative_registration_year(self):
        benefits = self.benefitsCarSimulator.calculate_benefits_car(33751, datetime.date(2017, 12, 22), 'electric', 300,
                                                                    datetime.date(2016, 12, 22))
        # voordeel alle aard mag niet lager gaan dan 1260/jaar dus gebruik indien het lager gaat 1260
        # self.assertEqual(810.02, benefits)
        self.assertEqual(1260, benefits)

    def test_calculate_budget_decrease_lease_cat1_less(self):
        budget_decrease = self.benefitsCarSimulator.calculate_budget_decrease(434)

        self.assertEqual(5220, budget_decrease)

    def test_calculate_budget_decrease_lease_cat1(self):
        budget_decrease = self.benefitsCarSimulator.calculate_budget_decrease(435)

        self.assertEqual(5220, budget_decrease)

    def test_calculate_budget_decrease_lease_cat2_less(self):
        budget_decrease = self.benefitsCarSimulator.calculate_budget_decrease(484)

        self.assertEqual(5820, budget_decrease)

    def test_calculate_budget_decrease_lease_cat2(self):
        budget_decrease = self.benefitsCarSimulator.calculate_budget_decrease(485)

        self.assertEqual(5820, budget_decrease)

    def test_calculate_budget_decrease_lease_cat3_less(self):
        budget_decrease = self.benefitsCarSimulator.calculate_budget_decrease(584)

        self.assertEqual(7020, budget_decrease)

    def test_calculate_budget_decrease_lease_cat3(self):
        budget_decrease = self.benefitsCarSimulator.calculate_budget_decrease(585)

        self.assertEqual(7020, budget_decrease)
