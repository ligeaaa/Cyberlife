import math
import random
import threading
import time

from entity.base_module.base_life import BaseLife
from colorama import Fore

from entity.ekiller.organization.ekiller_leg import EKillerLeg
from entity.ekiller.organization.ekiller_sex import EKillerSex
from entity.point.point_life import PointLife
from common.calculate_distance import euclidean_distance
from common.move_way import hunt_move


class EKillerLife(BaseLife, threading.Thread):
    """
    The simplest consumer life, which can only move, breed, hunt and die.
    The natural enemy of species Point Life consciously hunts species Point Life.
    """

    def __init__(self, row_location, col_location, name, space, lock):
        threading.Thread.__init__(self)
        BaseLife.__init__(self, row_location=row_location, col_location=col_location, name=name, maximum_age=80,
                          lock=lock, energy=200, min_childbearing_age=40, max_childbearing_age=70)
        self.space = space
        self.logo = Fore.RED + name
        self.leg = EKillerLeg(self)
        self.sex = EKillerSex(self)

    def run(self):
        """
        Every random 1-5s move
        """
        while True:
            random_interval = random.randint(1, 5)
            time.sleep(random_interval / self.space.time_flow_rate)
            self.lock.acquire()
            # if this life is already died
            if self.death_flag:
                self.clear_life()
                break
            # if this life's energy is not too high, then hunt
            if self.energy < 500:
                self.hunt()
            # otherwise, just move randomly
            else:
                self.leg.move(self.space)
            # if this life's energy is enough, then hava a baby
            if self.energy > 400:
                self.sex.breed(EKillerLife)
            self.death()
            self.energy -= 5
            self.space.show_space()
            self.act_count += 1
            self.lock.release()


    def hunt(self):
        """
        Find the nearest Point Life, and then try to hunt it.
        """
        # find the nearest Point Life
        nearest_point_life = None
        min_distance = None
        for entity in self.space.entities:
            if isinstance(entity, PointLife) and entity.death_flag == False:
                distance = euclidean_distance(self, entity)
                if min_distance is None:
                    min_distance = distance
                    nearest_point_life = entity
                elif min_distance > distance:
                    min_distance = distance
                    nearest_point_life = entity
        if nearest_point_life is not None:
            hunt_move(self, nearest_point_life, 3)
        else:
            self.leg.move(self.space)
