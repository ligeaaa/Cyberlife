from entity.base_module.base_brain import BaseBrain
from entity.base_module.base_dna import BaseDna


class BaseOrganization:
    def __init__(self):
        ...

    def construct(self, dna: BaseDna):
        ...

    def act(self, brain: BaseBrain):
        function = brain.process()
        ...
