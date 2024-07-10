from entity.base_module.base_dna import BaseDna


class PointDna(BaseDna):
    def __init__(self):
        BaseDna.__init__(self)
        self.dna_count = None
        self.dnas = {
            "leg": None,
            "brain": None,
            "stomach": None,
            "mouth": None,
            "sex": None,
            "base": None
        }