from constants.entity_constants.entity_gender import NEUTER
from entity.base_module.base_life import BaseLife
from entity.base_module.base_lifecycle import BaseLifecycle
from entity.base_module.base_organization import BaseOrganization
from entity.origin.origin_lifecycle import OriginLifecycle


class OriginLife(BaseLife):
    def __init__(self):
        self.age: float = 0
        self.maximum_age: float = 10000
        self.gender: int = NEUTER
        self.lifecycle: BaseLifecycle = OriginLifecycle()
        self.birth_date: float = 0
        self.birth_place: str = ...
        self.productor: list[BaseLife | str] = ["sky"]
        self.name: str = "origin"

    def absorbed_energy(self, organization: BaseOrganization = None, energy_resource=None):
        super().absorbed_energy(organization, energy_resource)

    def breed(self, other_life: list[BaseLife] = None):
        super().breed(other_life)

    def death(self):
        super().death()

    def growth(self):
        super().growth()