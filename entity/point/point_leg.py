import random

from entity.base_module.base_organization import BaseOrganization


class PointLeg(BaseOrganization):
    def __init__(self, entity):
        self.entity = entity
        # move direction
        super().__init__()
        self.move_direction = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

    def move(self, space):
        """
        The concrete move logic
        :return:
        """
        random_number = random.randint(0, 3)
        row_move, col_move = self.move_direction[random_number]
        space.move_life(self.entity, row_move, col_move)
