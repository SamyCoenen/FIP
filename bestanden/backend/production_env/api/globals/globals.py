from api.models import CalculationParameter, TaxScale


# Reviewer: Robin Lycops
# Parameters used over the complete app which aren't saved in the database
class Globals:
    year = 2016

    @staticmethod
    def get_correct_calculation_parameters(year):
        try:
            calc = CalculationParameter.objects.get(pk=year)
            return calc
        except CalculationParameter.DoesNotExist:
            try:
                return CalculationParameter.objects.get(pk=Globals.year)
            except CalculationParameter.DoesNotExist:
                print("No calculation parameters found in the database")
                raise

    @staticmethod
    def get_correct_tax_scales(year):
        calc = TaxScale.objects.filter(year=year)
        if calc.count() > 0:
            return calc
        else:
            calc = TaxScale.objects.filter(year=Globals.year)
            if calc.count() > 0:
                return TaxScale.objects.filter(year=Globals.year)
            else:
                print("No tax scales found in the database")
