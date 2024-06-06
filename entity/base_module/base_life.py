from __future__ import annotations

from entity.base_module.base_lifecycle import BaseLifecycle
from entity.base_module.base_organization import BaseOrganization


class BaseLife:
    def __init__(self):
        # life's age
        self.age: float = 0
        # life's maximum age
        self.maximum_age: float = ...
        # life's gender
        self.gender: int = ...
        # life's lifecycle
        self.lifecycle: BaseLifecycle = ...
        # when life born
        self.birth_date: float = ...
        # where life born
        self.birth_place: str = ...
        # who or which produce this life
        self.productor: list[BaseLife] = ...
        # life's name
        self.name: str = ...
        self.row_location = ...
        self.col_location = ...

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


if __name__ == '__main__':
    a = BaseLife()

