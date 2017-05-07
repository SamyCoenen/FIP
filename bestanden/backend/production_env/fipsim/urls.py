"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.csrf import csrf_protect
from api.views import CarList
from api.views import BikeList
from api.views import TabletList
from api.views import LaptopList
from api.views import SmartPhoneList
from api.views import TechList
from api.views import CalculationParameterList
from api.views import FipCalculator
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/cars$', csrf_protect(CarList.as_view()), name='cars'),
    url(r'^api/bikes$', csrf_protect(BikeList.as_view()), name='bikes'),
    url(r'^api/laptops$', csrf_protect(LaptopList.as_view()), name='laptops'),
    url(r'^api/smartphones$', csrf_protect(SmartPhoneList.as_view()), name='smartphones'),
    url(r'^api/tablets$', csrf_protect(TabletList.as_view()), name='tablets'),
    url(r'^api/tech$', csrf_protect(TechList.as_view()), name='tech'),
    url(r'^api/calculations$', csrf_protect(CalculationParameterList.as_view()), name='calcparams'),
    url(r'^$', csrf_protect(FipCalculator.as_view()), name='calculator'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
