import math

from entity.base_module.base_life import BaseLife


def euclidean_distance(a: BaseLife, b: BaseLife) -> float:
    """
    The method used to calculate the Euclidean distance between two organisms
    """
    a_row = a.row_location
    a_col = a.col_location
    b_row = b.row_location
    b_col = b.col_location
    distance = math.sqrt(math.pow((a_row - b_row), 2) + math.pow((a_col - b_col), 2))
    return distance
