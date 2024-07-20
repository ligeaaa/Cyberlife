import random

from common.msg import Message
from constants.msg_type_constants import BORN
from entity.base_module.base_life import BaseLife
from entity.base_module.base_organization import BaseOrganization


class PointSex(BaseOrganization):
    def __init__(self, entity):
        self.entity: BaseLife = entity
        super().__init__()

    def breed(self, life_type, other_life: list[BaseLife] = None):
        # if this entity has lived for sometime
        if self.entity.min_childbearing_age < self.entity.act_count:
            # find round location and ensure the coordinates are valid.
            if self.entity._find_round_location(life_type, 1) and self.entity.space.check_valid(
                    self.entity.row_location - 1, self.entity.col_location):
                # if exists a empty location
                if self.entity.space.space[self.entity.row_location - 1][self.entity.col_location] == 0:
                    new_point_life = life_type(self.entity.row_location - 1, self.entity.col_location,
                                               str(random.randint(1, 9)), self.entity.space, self.entity.lock)
                    self.entity.space.add_entity(new_point_life)
                    self.entity.energy -= 10
                    self.entity.space.client.send_information(Message(BORN, count=1))
