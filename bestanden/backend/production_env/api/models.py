from django.db import models
import decimal
import datetime


# Reviewer: Kim Gijbels
# Model is ok, id created by Django
# We do not know which brands the company will provide, thus we cannot make a dropdownbox in the admin interface
class CarBrand(models.Model):
    name = models.CharField(max_length=100, default="")

    def __str__(self):
        return str(self.name)


# Reviewer: Kim Gijbels
# Model is ok, id is created by Django
# In this case it is possible to provide category choices, since the company has 3 categories
# These categories will be used in the Django admin interface
class CarCategory(models.Model):
    CATEGORY_CHOICES = ((1, 'Category 1'), (2, 'Category 2'), (3, 'Category 3'))

    name = models.IntegerField(choices=CATEGORY_CHOICES, default=2)

    def __str__(self):
        return str(self.name)


# Reviewer: Kim Gijbels
# Model is ok, id created by Django
# Foreign keys are placed
# All fields are required, which is good (required is by default true)
class Car(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, default="", null=True)
    model = models.CharField(max_length=100, default="")
    engine_type = models.CharField(max_length=20, default="")
    lease_price = models.FloatField(default=0)
    co2 = models.IntegerField(default=0)
    catalog_value = models.FloatField(default=0)
    registration_year = models.DateField()
    category = models.ForeignKey(CarCategory, on_delete=models.CASCADE, default="", null=True)
    image_url = models.URLField(max_length=200, blank=True, default="")  # Kan ook vervangen worden door een file

    def __str__(self):
        brandname = CarBrand.objects.get(name=self.brand)
        return str(brandname.name) + ' ' + self.model


# Reviewer: Kim Gijbels
# Model is ok, id created by Django
# Same issue as the car brands, we do not know the brands yet
class BikeBrand(models.Model):
    name = models.CharField(max_length=100, default="")

    def __str__(self):
        return str(self.name)


# Reviewer: Kim Gijbels
# Model is ok, id created by Django
# Foreign keys are placed
# All fields are required, which is good (required is by default true)
class Bike(models.Model):
    brand = models.ForeignKey(BikeBrand, on_delete=models.CASCADE, default="", null=True)
    model = models.CharField(max_length=100, default="")
    electric = models.BooleanField(default=False)
    speed = models.IntegerField(default=0)
    lease_price = models.FloatField(default=0)
    image_location = models.CharField(max_length=200, blank=True)
    image_url = models.CharField(max_length=200, blank=True)  # Kan ook vervangen worden door een file

    @property
    def bike_category(self):
        if self.lease_price <= 25:
            return 1
        elif self.lease_price <= 35:
            return 2
        elif self.lease_price <= 55:
            return 3
        elif self.lease_price <= 75:
            return 4
        elif self.lease_price <= 95:
            return 5
        else:
            return 6

    def __str__(self):
        brandname = BikeBrand.objects.get(name=self.brand)
        return str(brandname.name) + ' ' + self.model + ' ' + str(self.lease_price)


# Reviewer: Kim Gijbels
# Model is ok, id created by Django, In the seed method the id will start with 2016
# This is model is upgraded in branch bruto-netto to include more parameters and to replace decimal
# by float, because it is not possible to mix operations of float and decimal. It requires casting
# and the numbers do not have a lot of decimals, and an approximation is ok.
class CalculationParameter(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name='ID')
    rsz = models.FloatField(default=0.1307)
    woon_werkverkeer_auto = models.FloatField(default=0.3412)
    woon_werkverkeer_fiets = models.FloatField(default=0.22)
    woon_werkverkeer_auto_belast_vrij = models.IntegerField(default=380)
    co2_gasoline = models.IntegerField(default=107)
    co2_diesel = models.IntegerField(default=89)
    max_vaa_car = models.IntegerField(default=1260)
    tax_decrease_multiplier_werkbonus = models.FloatField(default=0.2803)
    pension_rent_multiplier = models.FloatField(default=0.2)
    high_income_boundary = models.IntegerField(default=7500)
    arbeider_rsz_multiplier = models.FloatField(default=1.08)
    bediende_rsz_multiplier = models.FloatField(default=1)
    tax_decrease_old_family_member = models.IntegerField(default=70)
    tax_decrease_family_member = models.IntegerField(default=34)
    tax_decrease_handicapped = models.IntegerField(default=34)
    high_income_base_tax_scale1 = models.FloatField(default=3287.26)
    high_income_multiplier_of_diff = models.FloatField(default=0.5350)
    high_income_rent_boundary = models.IntegerField(default=130)
    high_income_base_tax_scale2 = models.FloatField(default=2922.79)
    tax_decrease_child1 = models.IntegerField(default=34)
    tax_decrease_child2 = models.IntegerField(default=93)
    tax_decrease_child3 = models.IntegerField(default=248)
    tax_decrease_child4 = models.IntegerField(default=454)
    tax_decrease_child5 = models.IntegerField(default=671)
    tax_decrease_child6 = models.IntegerField(default=887)
    tax_decrease_child7 = models.IntegerField(default=1104)
    tax_decrease_child8 = models.IntegerField(default=1337)
    tax_decrease_child8plus_multiplier = models.IntegerField(default=241)
    tax_decrease_single = models.IntegerField(default=24)
    tax_decrease_widow_or_unmarried_with_children = models.IntegerField(default=34)
    tax_decrease_married_partner_low_income = models.IntegerField(default=108)
    tax_decrease_married_partner_low_rent = models.IntegerField(default=216)
    low_income_boundary = models.FloatField(default=2370.74)
    tax_decrease_low_income = models.FloatField(default=6.46)
    work_bonus_lowest_boundary = models.FloatField(default=1577.89)
    work_bonus_highest_boundary = models.FloatField(default=2461.27)
    tax_decrease_work_bonus_arbeider_lowest = models.FloatField(default=209.29)
    tax_decrease_work_bonus_arbeider_multiplier_diff = models.FloatField(default=0.2369)
    tax_decrease_work_bonus_bediende_lowest = models.FloatField(default=193.79)
    tax_decrease_work_bonus_bediende_multiplier_diff = models.FloatField(default=0.2194)
    bijzondere_bijdrage_sz_lowest_boundary_np = models.FloatField(default=1095.10)
    bijzondere_bijdrage_sz_lowest_boundary = models.FloatField(default=1945.38)
    bijzondere_bijdrage_sz_married_and_income = models.FloatField(default=9.30)
    bijzondere_bijdrage_sz_middle_boundary = models.FloatField(default=2190.18)
    bijzondere_bijdrage_sz_multiplier_middle_cat = models.FloatField(default=0.076)
    bijzondere_bijdrage_sz_middle_cat_max_value = models.FloatField(default=18.60)
    bijzondere_bijdrage_sz_middle_cat_min_value = models.FloatField(default=9.30)
    bijzondere_bijdrage_sz_high_boundary = models.FloatField(default=6038.83)
    bijzondere_bijdrage_sz_multiplier_high_cat = models.FloatField(default=0.011)
    bijzondere_bijdrage_sz_high_cat_max_value = models.FloatField(default=51.64)
    bijzondere_bijdrage_sz_highest_cat_scale1 = models.FloatField(default=60.94)
    percentage_prive_usage_bike = models.FloatField(default=0.20)
    hospitalisation_partner = models.FloatField(default=175)
    hospitalisation_child = models.FloatField(default=68)
    vaa_smartphone = models.FloatField(default=12.5)
    vaa_laptop = models.IntegerField(default=15)
    vaa_internet = models.IntegerField(default=5)
    tech_budget = models.IntegerField(default=400)
    car_cat1_lease = models.FloatField(default=435)
    car_cat2_lease = models.FloatField(default=485)
    car_cat3_lease = models.FloatField(default=585)

    def __str__(self):
        return str(self.id)


# Reviewer: Kim Gijbels
# Model is ok, id created by Django
# Same as every other brand
class TechBrand(models.Model):
    name = models.CharField(max_length=100, default="")

    def __str__(self):
        return str(self.name)


# Reviewer: Kim Gijbels
# Model is ok, id created by Django
# Foreign key in check
# Since all these devices have a lot in common, we decided to make one model of them
class Tech(models.Model):
    APPROVAL_CHOICES = (
        (u'S', u'Smartphone'),
        (u'L', u'Laptop'),
        (u'M', u'Multimedia'),
    )
    brand = models.ForeignKey(TechBrand, on_delete=models.CASCADE, default="", null=True)
    model = models.CharField(max_length=100, default="")
    catalog_value = models.IntegerField(default=0)
    device_type = models.CharField(max_length=1, choices=APPROVAL_CHOICES, default='N')

    def __str__(self):
        brandname = TechBrand.objects.get(name=self.brand)
        return str(brandname.name) + ' ' + self.model


# Reviewer: Robin Lycops
# Create Objects for taxvariables.
class TaxVariables(object):
    def __init__(self, **kwargs):
        self.bruto = decimal.Decimal(0)
        self.type_worker = ''
        self.marital_status = ''
        self.widow = False
        self.handicapped_partner = False
        self.partner_income = decimal.Decimal(0)
        self.partner_income_pension_or_interest = False
        self.handicapped = False
        self.children_handicapped = 0
        self.children = 0
        self.family_members = 0
        self.family_members_old = 0
        self.family_members_handicapped = 0
        self.family_members_old_handicapped = 0

        for field in ('bruto', 'type_worker', 'marital_status', 'handicapped_partner', 'partner_income',
                      'partner_income_pension_or_interest', 'handicapped', 'children_handicapped', 'children',
                      'family_members', 'family_members_old', 'family_members_handicapped',
                      'family_members_old_handicapped'):
            # create completely dynamic classes based on a field dictionary, get value of field or put in default None
            setattr(self, field, kwargs.get(field, None))


class CarVariables(object):
    def __init__(self, **kwargs):
        self.catalog_value = 0
        self.registration_year = datetime.date.today()
        self.engine_type = ''
        self.co2_car = 0
        self.lease_price = 0

        for field in 'catalog_value', 'registration_year', 'engine_type', 'co2_car', 'lease_price':
            # create completely dynamic classes based on a field dictionary, get value of field or put in default None
            setattr(self, field, kwargs.get(field, None))


class TechVariables(object):
    def __init__(self, **kwargs):
        self.multimedia_value = 0
        self.laptop_value = 0
        self.smartphone_value = 0
        self.internet_value = 0

        for field in 'smartphone_value', 'laptop_value', 'internet_value', 'multimedia_value':
            # create completely dynamic classes based on a field dictionary, get value of field or put in default None
            setattr(self, field, kwargs.get(field, None))


class BikeVariables(object):
    def __init__(self, **kwargs):
        self.lease_price = kwargs.get('lease_price', 0)


class AllowanceVariables(object):
    def __init__(self, **kwargs):
        self.is_selected = False
        self.days = 0
        self.kms = 0

        for field in 'is_selected', 'days', 'kms':
            # create completely dynamic classes based on a field dictionary, get value of field or put in default None
            setattr(self, field, kwargs.get(field, None))


class SocialBenefitVariables(object):
    def __init__(self, **kwargs):
        self.hospitalisation_partner = False,
        self.children_hospitalisation = 0,
        self.children_benefits = 0,
        self.retirement_saving = False

        for field in ('hospitalisation_partner', 'children_hospitalisation', 'children_benefits', 'child_benefits',
                      'retirement_saving'):
            # create completely dynamic classes based on a field dictionary, get value of field or put in default None
            setattr(self, field, kwargs.get(field, None))


class TaxScale(models.Model):
    bruto = models.IntegerField()
    scale1 = models.FloatField()
    scale2 = models.FloatField()
    year = models.IntegerField(default=2016)
