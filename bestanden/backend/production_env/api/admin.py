from django.contrib import admin
from api.models import CarBrand
from api.models import Car
from api.models import CarCategory
from api.models import BikeBrand
from api.models import TechBrand
from api.models import Tech
from api.models import Bike
from api.models import CalculationParameter

# Register your models here.
admin.site.register(Car)
admin.site.register(CarBrand)
admin.site.register(CarCategory)
admin.site.register(CalculationParameter)
admin.site.register(Bike)
admin.site.register(BikeBrand)
admin.site.register(TechBrand)
admin.site.register(Tech)
