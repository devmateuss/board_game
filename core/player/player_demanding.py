from .base import BasePlayer


class PlayerDemanding(BasePlayer):

    def _roles_to_payment(self, patrimony):
        if patrimony.rental_price > 50:
            self.paid(patrimony.property_price, patrimony.type_of_strategy)
            return True
        return False
