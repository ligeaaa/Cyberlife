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
    space = Space(10, 30, death_and_born_statics)
    space.show_space()
    point_life1 = PointLife(1, 1, "1", space, lock, death_and_born_statics)
    point_life2 = PointLife(2, 2, "2", space, lock, death_and_born_statics)
    point_life3 = PointLife(3, 3, "3", space, lock, death_and_born_statics)
    point_life4 = PointLife(4, 4, "4", space, lock, death_and_born_statics)
    point_life5 = PointLife(5, 5, "5", space, lock, death_and_born_statics)
    space.add_entity(point_life1)
    space.add_entity(point_life2)
    space.add_entity(point_life3)
    space.add_entity(point_life4)
    space.add_entity(point_life5)

if __name__ == '__main__':
    start()