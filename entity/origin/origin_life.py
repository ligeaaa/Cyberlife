from entity.base_module.base_life import BaseLife
from entity.base_module.base_organization import BaseOrganization


class OriginLife(BaseLife):
    def __init__(self):
        super().__init__()

    def absorbed_energy(self, organization: BaseOrganization = None, energy_resource=None):
        super().absorbed_energy(organization, energy_resource)

    def breed(self, other_life: list[BaseLife] = None):
        super().breed(other_life)

    def death(self):
        super().death()

    def growth(self):
        super().growth()