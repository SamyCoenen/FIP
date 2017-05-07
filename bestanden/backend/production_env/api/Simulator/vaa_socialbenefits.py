

# Reviewer: Kim Gijbels
# The numbers haven't changed
class SocialBenefits(object):
    @staticmethod
    def calculate_pensioensparen():
        return 78 * 0.886 * 12

    @staticmethod
    def calculate_kinderbijslag(aantal_kinderen):
        return aantal_kinderen * 50
