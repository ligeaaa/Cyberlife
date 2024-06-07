import random

from entity.base_module.base_life import BaseLife


def hunt_move(a: BaseLife, b: BaseLife, step):
    """
    a life moves towards b life by step steps
    :param a: the host life
    :param b: the target life
    """
    for _ in range(step):
        if b.death_flag:
            return
        direction_row = b.row_location - a.row_location
        direction_col = b.col_location - a.col_location

        target_row = a.row_location
        target_col = a.col_location

        if direction_row != 0:
            target_row = a.row_location + random.choice([0, 1]) if direction_row > 0 else a.row_location + random.choice([-1, 0])
        if direction_col != 0:
            target_col = a.col_location + random.choice([0, 1]) if direction_col > 0 else a.col_location + random.choice([-1, 0])

        if a.row_location != target_row or a.col_location != target_col:
            if isinstance(a.space.space[target_row][target_col], type(b)):
                a.energy += b.energy / 2
                a.space.space[target_row][target_col] = 0
                b.death_flag = True
            if a.space.space[target_row][target_col] == 0:
                a.space.space[a.row_location][a.col_location] = 0
                a.row_location = target_row
                a.col_location = target_col
                a.space.space[target_row][target_col] = a
                a.space.show_space()


def random_move(a: BaseLife, step):
    ...