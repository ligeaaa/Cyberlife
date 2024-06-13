import random


def in_probability(a: float):
    """
    :param a: the float number, 0 < a < 1
    :return: boolean
    """
    random_number = random.random()
    if random_number < a:
        return True
    return False
