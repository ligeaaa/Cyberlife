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
from world.statics import DeathAndBreedStatics


def start():
    lock = threading.Lock()
    death_and_born_statics = DeathAndBreedStatics()
    # 10 * 10 world
    space = Space(10, 30)
    space.show_space()
    point_life1 = PointLife(1, 1, "1", space, lock)
    point_life2 = PointLife(2, 2, "2", space, lock)
    point_life3 = PointLife(3, 3, "3", space, lock)
    point_life4 = PointLife(4, 4, "4", space, lock)
    point_life5 = PointLife(5, 5, "5", space, lock)
    ekiller_life1 = EKillerLife(9, 9, "1", space, lock)
    space.add_entity(point_life1)
    space.add_entity(point_life2)
    space.add_entity(point_life3)
    space.add_entity(point_life4)
    space.add_entity(point_life5)
    space.add_entity(ekiller_life1)

if __name__ == '__main__':
    start()