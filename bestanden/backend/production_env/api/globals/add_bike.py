import json
from api.models import BikeBrand, Bike, TaxScale

with open('C:/users/Kim/Downloads/brand.json') as data_file:
    data = json.load(data_file)

print(data[0]['id'])

i = 0
while i < len(data):
    bike_brands = BikeBrand.objects.create(id=data[i]['id'], name=data[i]['name'])
    i += 1


with open('C:/users/Kim/Downloads/bikes.json') as data_file:
    data = json.load(data_file)

print(int(data[i]['brand']))

brands = []
i = 0
while i < len(data):
    brands.append(BikeBrand.objects.get(pk=int(data[i]['brand'])))
    if str(data[i]['lease_price']).rfind(',') > 0:
        temp = str(data[i]['lease_price']).replace(',', '.')
        print(temp)
        data[i]['lease_price'] = float(temp)
    i += 1

i = 0
while i < len(data):
    electric = False
    if data[i]['model'].rfind('E-') > 0:
        electric = True
    bikes = Bike.objects.create(brand=brands[i], model=data[i]['model'], lease_price=data[i]['lease_price'],
                                image_location=data[i]['image_location'], image_url=data[i]['image_url'],
                                electric=electric)
    i += 1


with open('api/globals/bedrijfsvoorheffing_schalen_2016_copy.txt') as data_file:
    data = json.load(data_file)

print(data[0]['scale1'])

i = 0
while i < len(data):
    scales = TaxScale.objects.create(year=2016, bruto=data[i]['bruto'], scale1=data[i]['scale1'],
                                     scale2=data[i]['scale2'])
    i += 1
