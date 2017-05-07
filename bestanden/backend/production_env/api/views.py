from rest_framework.parsers import JSONParser
import json
from api.Simulator.bruto_netto_simulator import BrutoNettoSimulator
from api.Simulator.benefits_car_simulator import BenefitsCarSimulator
from api.Simulator.vaa_fiets import VAAFiets
from api.Simulator.vaa_technology import VAALaptopSmartphoneTablet
from api.Simulator.woon_werkverkeer_simulator import WWVSimulator
from api.Simulator.budget_voordelen import BudgetAdvantages
from api.Simulator.vaa_hospitalisation import VAAHospitalisation
from api.Simulator.vaa_socialbenefits import SocialBenefits
from api.Simulator.rsz_calculations import RSZCalculations
from api.globals.globals import Globals
from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Car
from api.models import Bike
from api.models import CalculationParameter
from api.models import Tech
from api.models import TaxVariables
from .serializers import CarSerializer
from .serializers import BikeSerializer
from .serializers import CalculationParameterSerializer
from .serializers import TechSerializer
from .serializers import TaxVariablesSerializer
from .serializers import CarVariablesSerializer
from .serializers import TechVariablesSerializer
from .serializers import BikeVariablesSerializer
from .serializers import AllowanceVariablesSerializer
from .serializers import SocialBenefitsSerializer


# Reviewer: Kim Gijbels
# Only the get is supported this way (admin supports posts, put,...)
# All objects are retrieved from the db and the serializer is used to retrieve a list
# Removed self and made method static, because pep was suggesting it
class CarList(APIView):
    @staticmethod
    def get(request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)


# Reviewer: Kim Gijbels
# Only the get is supported this way (admin supports posts, put,...)
# All objects are retrieved from the db and the serializer is used to retrieve a list
# Removed self and made method static, because pep was suggesting it
class BikeList(APIView):
    @staticmethod
    def get(request):
        cars = Bike.objects.all()
        serializer = BikeSerializer(cars, many=True)
        return Response(serializer.data)
# Reviewer: Kim Gijbels


# Question: Do we need this api?
# Removed self and request and made method static, because pep was suggesting it
class CalculationParameterList(APIView):
    @staticmethod
    def get(request):
        params = CalculationParameter.objects.all()
        serializer = CalculationParameterSerializer(params, many=True)
        return Response(serializer.data)


# Reviewer: Kim Gijbels
# Normal view (api) with only a get method
# Removed request and made method static, because pep was suggesting it
class TechList(APIView):
    @staticmethod
    def get(request):
        devices = Tech.objects.all()
        serializer = TechSerializer(devices, many=True)
        return Response(serializer.data)


# Reviewer: Kim Gijbels
# Normal view (api) with only a get method, uses filter to filter only on laptops
# Removed self and made method static, because pep was suggesting it
class LaptopList(APIView):
    @staticmethod
    def get(request):
        laptops = Tech.objects.filter(device_type='L')
        serializer = TechSerializer(laptops, many=True)
        return Response(serializer.data)


# Reviewer: Kim Gijbels
# Normal view (api) with only a get method, uses filter to filter only on smartphones
# Removed self and made method static, because pep was suggesting it
class SmartPhoneList(APIView):
    @staticmethod
    def get(request):
        phones = Tech.objects.filter(device_type='S')
        serializer = TechSerializer(phones, many=True)
        return Response(serializer.data)


# Reviewer: Kim Gijbels
# Normal view (api) with only a get method, uses filter to filter only on tablets
# Removed self and made method static, because pep was suggesting it
class TabletList(APIView):
    @staticmethod
    def get(request):
        tablets = Tech.objects.filter(device_type='T')
        serializer = TechSerializer(tablets, many=True)
        return Response(serializer.data)


# Reviewer : Robin Lycops
# Making a post request which runs brutto -> netto simulator and returns the calculated data
# for this get the data for the calculation , return the calculated data
class FipCalculator(APIView):
    parser_classes = (JSONParser,)

    @staticmethod
    def post(request):
        year = date.today().year
        data = request.data
        calculated_data = dict()

        if "income_info" in data:
            bruto_serializer = TaxVariablesSerializer(data=data["income_info"])
            bruto_serializer.is_valid()
            tax_variables = bruto_serializer.save()
            additions = 0.0
            decreases_of_budget = 0.0
            mobility_budget = 0.0
            social_budget = 0.0
            temp_budget = 0.0
            allowance = 0.0

            total_budget = BudgetAdvantages(tax_variables.bruto, 0, year).calculate_budget()

            if "car" in data:
                tax_addition, temp_budget, budget_decrease = FipCalculator.mobility_car_calc(data["car"], year,
                                                                                             tax_variables.bruto)
                additions += tax_addition
                decreases_of_budget += budget_decrease
                mobility_budget += budget_decrease

            if "bike" in data:
                tax_addition, budget_decrease = FipCalculator.mobility_bike_calc(data["bike"], year)
                additions += tax_addition
                decreases_of_budget += budget_decrease
                mobility_budget += budget_decrease

            if "tech" in data:
                tax_addition, budget_decrease = FipCalculator.tech_calc(data["tech"], year)
                additions += tax_addition
                decreases_of_budget += budget_decrease
                calculated_data['tech_budget'] = budget_decrease

            if "allowance" in data:
                vergoeding_belast_vrij, vergoeding_belast = FipCalculator.mobility_allowance_calc(data["allowance"],
                                                                                                  year)

            if "social_benefits" in data:
                budget_decrease = FipCalculator.social_benefits_calc(data["social_benefits"], year)
                decreases_of_budget += budget_decrease
                social_budget = round(budget_decrease, 2)

            if "charity" in data:
                decreases_of_budget += data["charity"]

            simulator = BrutoNettoSimulator(tax_variables, year, additions)
            simulator_no_additions = BrutoNettoSimulator(tax_variables, year)
            rsz, werk_bonus, taxable_wages, tax, tax_decreases, rsz_extra, netto = simulator.calculate_netto()
            rsz2, werk_bonus2, taxable_wages2, tax2, tax_decreases2, rsz_extra2, netto2 = \
                simulator_no_additions.calculate_netto()
            original_netto = netto2
            netto -= additions

            if temp_budget > 0:
                budget = round(temp_budget - decreases_of_budget, 2)
            else:
                budget = round(total_budget - decreases_of_budget, 2)

            end_budget_payment, total_end_budget_payment = FipCalculator().calculate_budgets(budget, total_budget, year)

            if "allowance" in data:
                # netto += vergoeding_belast + vergoeding_belast_vrij
                simulator_only_allowance = BrutoNettoSimulator(tax_variables, year, vergoeding_belast)
                rsz_allowance, werk_bonus_allowance, taxable_wages_allowance, tax_allowance, tax_decreases_allowance,\
                rsz_extra_allowance, netto_only_allowance = \
                    simulator_only_allowance.calculate_netto()

                allowance = vergoeding_belast_vrij + netto_only_allowance - original_netto

            calculated_data['rsz'] = rsz
            calculated_data['werkbonus'] = werk_bonus
            calculated_data['taxable_wages'] = taxable_wages
            calculated_data['tax'] = tax
            calculated_data['tax_decreases'] = tax_decreases
            calculated_data['rsz_extra'] = rsz_extra
            calculated_data['netto'] = round(netto, 2)
            calculated_data['netto_without_options'] = round(original_netto, 2)
            calculated_data['budget'] = budget
            calculated_data['total_budget'] = temp_budget if temp_budget > 0 else total_budget
            calculated_data['mobility_budget'] = round(mobility_budget, 2)
            calculated_data['end_budget_payment'] = end_budget_payment
            calculated_data['total_end_budget_payment'] = total_end_budget_payment
            calculated_data['social_budget'] = social_budget
            calculated_data['allowance'] = round(allowance, 2)

        return Response(calculated_data)

    @staticmethod
    def mobility_car_calc(cardata, year, bruto=0):
        car_serializer = CarVariablesSerializer(data=cardata)
        car_serializer.is_valid()
        car = car_serializer.save()
        car_simulator = BenefitsCarSimulator(year)
        vaa_car = round(car_simulator.calculate_benefits_car(car.catalog_value, car.registration_year, car.engine_type,
                                                             car.co2_car) / 12, 2)
        total_budget = BudgetAdvantages(bruto, car.lease_price, year).calculate_budget()
        budget_decrease = car_simulator.calculate_budget_decrease(car.lease_price)

        return vaa_car, total_budget, budget_decrease

    @staticmethod
    def mobility_bike_calc(bikedata, year):
        bike_serializer = BikeVariablesSerializer(data=bikedata)
        bike_serializer.is_valid()
        bike_variables = bike_serializer.save()
        bike_simulator = VAAFiets(bike_variables.lease_price, year)

        return bike_simulator.calc_rsz_and_total_cost()

    @staticmethod
    def tech_calc(techdata, year):
        tech_serializer = TechVariablesSerializer(data=techdata)
        tech_serializer.is_valid()
        tech_variables = tech_serializer.save()
        simulator = VAALaptopSmartphoneTablet(year)
        benefits = 0
        total_budget_costs = 0

        if tech_variables.laptop_value > 0:
            calculated_benefit, budget_cost = simulator.calculate_vaa_laptop(tech_variables.laptop_value)
            benefits += calculated_benefit
            total_budget_costs += budget_cost

        if tech_variables.smartphone_value > 0:
            calculated_benefit, budget_cost = simulator.calculate_vaa_smartphone(tech_variables.smartphone_value)
            benefits += calculated_benefit
            total_budget_costs += budget_cost

        if tech_variables.multimedia_value > 0:
            multimedia = Tech()
            multimedia.device_type = 'Multimedia'
            multimedia.catalog_value = tech_variables.multimedia_value
            calculated_benefit, budget_cost = simulator.calculate_vaa_tablet(multimedia, multimedia.catalog_value)
            benefits += calculated_benefit
            total_budget_costs += budget_cost

        if tech_variables.internet_value > 0:
            calculated_benefit, budget_cost = simulator.calculate_vaa_internet_home(tech_variables.internet_value)
            benefits += calculated_benefit
            total_budget_costs += budget_cost * 12

        return benefits, total_budget_costs

    @staticmethod
    def mobility_allowance_calc(allowancedata, year):
        allowance_serializer = AllowanceVariablesSerializer(data=allowancedata)
        allowance_serializer.is_valid()
        allowance = allowance_serializer.save()
        allowance_simulator = WWVSimulator(year)
        vergoeding_belast_vrij, vergoeding_belast = allowance_simulator.calculate_auto_vergoeding(allowance.days,
                                                                                                  allowance.kms)
        return vergoeding_belast_vrij, vergoeding_belast

    @staticmethod
    def social_benefits_calc(social_benefits_data, year):
        social_benefits_serializer = SocialBenefitsSerializer(data=social_benefits_data)
        social_benefits_serializer.is_valid()
        social_benefits = social_benefits_serializer.save()
        hospitalisation_p = social_benefits.hospitalisation_partner
        hospitalisation_c = social_benefits.children_hospitalisation

        cost = SocialBenefits().calculate_kinderbijslag(social_benefits.children_benefits)

        simulator = VAAHospitalisation(hospitalisation_p, hospitalisation_c, year)
        cost += simulator.calculate_hospitalisation()

        if social_benefits.retirement_saving:
            cost += SocialBenefits().calculate_pensioensparen()
        return cost

    @staticmethod
    def calculate_budgets(budget, total_budget, year):
        tax_variables = TaxVariables()
        tax_variables.bruto = budget
        tax_variables.type_worker = 'bediende'

        rsz_calculations = RSZCalculations(Globals.get_correct_calculation_parameters(year), tax_variables)
        rsz, workbonus = rsz_calculations.calculate_rsz()
        rsz += workbonus
        taxable_budget = budget - rsz
        tax_budget = taxable_budget * 0.1615
        netto_budget = taxable_budget - tax_budget

        tax_variables.bruto = total_budget
        rsz_calculations = RSZCalculations(Globals.get_correct_calculation_parameters(year), tax_variables)
        rsz, workbonus = rsz_calculations.calculate_rsz()
        rsz += workbonus
        taxable_budget = total_budget - rsz
        tax_budget = taxable_budget * 0.1615
        netto_budget_total = taxable_budget - tax_budget

        return round(netto_budget, 2), round(netto_budget_total, 2)
