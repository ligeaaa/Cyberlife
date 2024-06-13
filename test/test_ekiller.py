from entity.ekiller.ekiller_life import EKillerLife

try:
    import sys
    sys.path.append(r'C:\Users\NeuroXess\Desktop\gitlab\Cyberlife')
except Exception as e:
    pass

import threading
from queue import Queue

from entity.point.point_life import PointLife
from world.space import Space


def start():
    lock = threading.Lock()
    # 10 * 10 world
    space = Space(2, 10)
    space.show_space()
    point_life1 = PointLife(1, 1, "1", space, lock)
    ekiller_life1 = EKillerLife(1, 9, "1", space, lock)
    space.add_entity(point_life1)
    space.add_entity(ekiller_life1)

if __name__ == '__main__':
    start()