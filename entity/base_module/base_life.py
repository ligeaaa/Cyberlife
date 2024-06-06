import time

from constants.entity_constants.entity_gender import NEUTER
from entity.base_module.base_lifecycle import BaseLifecycle
from entity.base_module.base_organization import BaseOrganization


class BaseLife:
    def __init__(self,
                 maximum_age: float = None,
                 gender: int = NEUTER,
                 lifecycle: BaseLifecycle = None,
                 birth_place: str = "place",
                 productor: list['BaseLife'] = None,
                 name: str = "life",
                 row_location: int = 0,
                 col_location: int = 0):
        # life's maximum age
        self.maximum_age = maximum_age
        # life's gender
        self.gender = gender
        # life's lifecycle
        self.lifecycle = lifecycle
        # when life born
        self.birth_time = time.time()
        # where life born
        self.birth_place = birth_place
        # who or which produce this life
        self.productor = productor
        # life's name
        self.name = name
        self.row_location = row_location
        self.col_location = col_location

    def absorbed_energy(self, organization: BaseOrganization = None, energy_resource=None):
        """
        This is a function that allows this life absorb energy grom energy resource by some organization
        :param organization:
        :param energy_resource:
        """
        ...

    def breed(self, other_life: list['BaseLife'] = None):
        """
        This is a function that allows this life to reproduce another life
        :param other_life:
        :return:
        """
        ...

    def death(self):
        """
        This is a function that allows this life to die
        """
        ...

    def growth(self):
        """
        This is a function that allows this life to grow
        :return:
        """
        ...


if __name__ == '__main__':
    a = BaseLife()
