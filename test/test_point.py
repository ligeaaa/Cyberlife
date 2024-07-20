import random

# try:
#     import sys
#     sys.path.append(r'C:\Users\NeuroXess\Desktop\gitlab\Cyberlife')
# except Exception as e:
#     pass

from common.get_time import get_real_time
from entity.ekiller.ekiller_life import EKillerLife

import threading

from entity.point.point_life import PointLife
from world.space import Space


def start():
    lock = threading.Lock()
    # 10 * 10 world
    row = 10
    column = 10
    space = Space(row, column, time_flow_rate=10)
    # for i in range(5):
    #     a = random.randint(0, row - 2)
    #     b = random.randint(0, column - 2)
    #     point_life = PointLife(a, b, "1", space, lock)
    #     point_life2 = PointLife(a + 1, b, "1", space, lock)
    #     space.add_entity(point_life)
    #     space.add_entity(point_life2)
    point_life = PointLife(5, 5, "1", space, lock)
    space.add_entity(point_life)
    space.show_space()

if __name__ == '__main__':
    start()
