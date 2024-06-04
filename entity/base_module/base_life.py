from __future__ import annotations

from entity.base_module.base_organization import BaseOrganization


class BaseLife:
    def __init__(self):
        # life's age
        self.age = 0
        # life's maximum age
        self.maximum_age = ...
        # life's gender
        self.gender = ...
        # life's lifecycle
        self.lifecycle = ...
        # life's status in its lifecycle
        self.status = ...
        # when life born
        self.birth_date = ...
        # where life born
        self.birth_place = ...
        # who or which produce this life
        self.productor = ...
    def absorbed_energy(self, organization: BaseOrganization = None, energy_resource = None):
        """
        This is a function that allows this life absorb energy grom energy resource by some organization
        :param organization:
        :param energy_resource:
        """
        ...

    def breed(self, other_life: list[BaseLife] = None):
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
