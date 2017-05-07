from rest_framework import serializers
from api.models import CarBrand
from api.models import Car
from api.models import BikeBrand
from api.models import TechBrand
from api.models import Tech
from api.models import Bike
from api.models import CalculationParameter
from api.models import TaxVariables
from api.models import CarVariables
from api.models import TaxScale
from api.models import BikeVariables
from api.models import TechVariables
from api.models import AllowanceVariables
from api.models import SocialBenefitVariables


# Reviewer: Kim Gijbels
# Normal serializer
class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ('name',)


# Reviewer: Kim Gijbels
# brandname is used because brand is a foreignkey in Car
# Normal serializer
class CarSerializer(serializers.ModelSerializer):
    brandname = CarBrandSerializer(source='brand')

    class Meta:
        model = Car
        fields = ('brandname', 'model', 'engine_type', 'lease_price', 'co2',
                  'catalog_value', 'registration_year', 'category', 'image_url')


# Reviewer: Kim Gijbels
# Normal serializer
class BikeBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeBrand
        fields = ('name',)


# Reviewer: Kim Gijbels
class BikeSerializer(serializers.ModelSerializer):
    brandname = BikeBrandSerializer(source='brand')
    bike_category = serializers.ReadOnlyField()

    class Meta:
        model = Bike
        fields = '__all__'


# Reviewer: Kim Gijbels
# All fields are serialized
class CalculationParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalculationParameter
        fields = '__all__'


# Reviewer: Kim Gijbels
# Just a normal serializer
class TechBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechBrand
        fields = ('name',)


# Reviewer: Kim Gijbels
class TechSerializer(serializers.ModelSerializer):
    brandname = TechBrandSerializer(source='brand')

    class Meta:
        model = Tech
        fields = '__all__'


# Reviewer Robin Lycops
# Serializer made for TaxVariables objects
# update and create return complete objects instances based on the validated data
# The objects don't get saved because these aren't models!
class TaxVariablesSerializer(serializers.Serializer):
    bruto = serializers.FloatField(required=True)
    type_worker = serializers.CharField(required=True)
    marital_status = serializers.CharField(required=True)
    handicapped_partner = serializers.BooleanField()
    partner_income = serializers.FloatField()
    partner_income_pension_or_interest = serializers.BooleanField()
    handicapped = serializers.BooleanField()
    children_handicapped = serializers.IntegerField(default=0)
    children = serializers.IntegerField(default=0)
    family_members = serializers.IntegerField()
    family_members_old = serializers.IntegerField()
    family_members_handicapped = serializers.IntegerField()
    family_members_old_handicapped = serializers.IntegerField()

    # default serializer create behavior
    def create(self, validated_data):
        return TaxVariables(**validated_data)


class CarVariablesSerializer(serializers.Serializer):
    engine_type = serializers.CharField(max_length=20, default="")
    co2_car = serializers.IntegerField(default=0)
    catalog_value = serializers.FloatField(default=0)
    registration_year = serializers.DateField()
    lease_price = serializers.FloatField(default=0)

    # default serializer create behavior
    def create(self, validated_data):
        return CarVariables(**validated_data)


class TaxScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxScale
        fields = ('bruto', 'scale1', 'scale2')


class TechVariablesSerializer(serializers.Serializer):
    multimedia_value = serializers.IntegerField(default=0)
    laptop_value = serializers.IntegerField(default=0)
    smartphone_value = serializers.IntegerField(default=0)
    internet_value = serializers.IntegerField(default=0)

    # default serializer create behavior
    def create(self, validated_data):
        return TechVariables(**validated_data)


class BikeVariablesSerializer(serializers.Serializer):
    lease_price = serializers.FloatField(default=0)

    # default serializer create behavior
    def create(self, validated_data):
        return BikeVariables(**validated_data)


class AllowanceVariablesSerializer(serializers.Serializer):
    days = serializers.IntegerField(default=0)
    kms = serializers.IntegerField(default=0)

    # default serializer create behavior
    def create(self, validated_data):
        return AllowanceVariables(**validated_data)


class SocialBenefitsSerializer(serializers.Serializer):
    hospitalisation_partner = serializers.BooleanField(default=False)
    children_hospitalisation = serializers.IntegerField(default=0)
    children_benefits = serializers.IntegerField(default=0)
    retirement_saving = serializers.BooleanField(default=False)

    # default serializer create behavior
    def create(self, validated_data):
        return SocialBenefitVariables(**validated_data)
