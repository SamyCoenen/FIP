from django.test import TestCase
from api.Simulator.vaa_socialbenefits import SocialBenefits


class TestSocialBenefits(TestCase):
    def test_pensioensparen_monthly(self):
        pensioensparen = SocialBenefits.calculate_pensioensparen()

        self.assertEqual(829.296, pensioensparen)

    def test_kinderbijslag_1child(self):
        bijslag = SocialBenefits.calculate_kinderbijslag(1)

        self.assertEqual(50, bijslag)

    def test_kinderbijslag_2children(self):
        bijslag = SocialBenefits.calculate_kinderbijslag(2)

        self.assertEqual(100, bijslag)
