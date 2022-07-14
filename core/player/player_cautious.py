from .base import BasePlayer


class PlayerCautious(BasePlayer):

    def _roles_to_payment(self, patrimony):
        if (self.money - patrimony.property_price) >= 80:
            self.paid(patrimony.property_price, patrimony.type_of_strategy)
            return True
        return False
