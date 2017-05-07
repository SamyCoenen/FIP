from api.globals.globals import Globals


# Reviewer: Robin Lycops
class VAALaptopSmartphoneTablet(object):

    def __init__(self, year, tech_devices=None, catalog_value=0):
        self.calc_parameters = Globals.get_correct_calculation_parameters(year)
        self.tech_devices = tech_devices
        self.catalog_value = catalog_value

    def calculate_vaa(self):
        vaa_belast = 0
        vaa_total_cost = 0
        i = 0
        while i < len(self.tech_devices):
            if self.tech_devices[i].device_type == 'Smartphone':
                vaa_belast_temp, vaa_total_cost_temp = self.calculate_vaa_smartphone()
            elif self.tech_devices[i].device_type == 'Laptop':
                vaa_belast_temp, vaa_total_cost_temp = self.calculate_vaa_laptop()
            else:
                vaa_belast_temp, vaa_total_cost_temp = self.calculate_vaa_tablet(self.tech_devices[i])
            vaa_total_cost += self.tech_devices[i].catalog_value
            vaa_belast += vaa_belast_temp
            i += 1

        return round(vaa_belast, 2), round(vaa_total_cost, 2)

    def calculate_vaa_smartphone(self, product_value=0):
        if product_value == 0:
            return self.calc_parameters.vaa_smartphone, self.catalog_value
        else:
            return self.calc_parameters.vaa_smartphone, product_value

    def calculate_vaa_laptop(self, product_value=0):
        if product_value == 0:
            return self.calc_parameters.vaa_laptop, self.catalog_value
        else:
            return self.calc_parameters.vaa_laptop, product_value

    def calculate_vaa_tablet(self, device, product_value=0):
        if product_value == 0:
            return device.catalog_value * self.calc_parameters.rsz, self.catalog_value
        else:
            return device.catalog_value * self.calc_parameters.rsz, product_value

    # Reviewer: Kim Gijbels
    def calculate_vaa_internet_home(self, product_value=0):
        if product_value == 0:
            return self.calc_parameters.vaa_internet, self.catalog_value
        else:
            return self.calc_parameters.vaa_internet, product_value
