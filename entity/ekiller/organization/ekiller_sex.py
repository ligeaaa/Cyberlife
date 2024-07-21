import random

from common.msg import Message
from common.probability import in_probability
from constants.msg_type_constants import BORN
from entity.base_module.base_life import BaseLife
from entity.base_module.base_organization import BaseOrganization
from entity.point.point_life import PointLife


class EKillerSex(BaseOrganization):
    def __init__(self, entity):
        self.entity: BaseLife = entity
        super().__init__()

    def breed(self, life_type, other_life: list[BaseLife] = None):
        """
        The concrete breed logic
        """
        if self.entity.min_childbearing_age <= self.entity.act_count:
            probability = self.entity.calculate_fertility_probability(self.entity.act_count)
            if not in_probability(probability - 0.2):
                return
            # ensure the coordinates are valid.
            if self.entity.space.check_valid(self.entity.row_location - 1, self.entity.col_location):
                # if exists an empty location
                if isinstance(self.entity.space.space[self.entity.row_location - 1][self.entity.col_location],
                              (int, PointLife)):
                    new_life = life_type(self.entity.row_location - 1, self.entity.col_location,
                                         str(random.randint(1, 9)),
                                         self.entity.space, self.entity.lock)
                    self.entity.space.add_entity(new_life)
                    self.entity.energy -= 300
                    self.entity.space.client.send_information(Message(BORN, count=1))
