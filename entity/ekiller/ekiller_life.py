import random
import threading
import time

from common.msg import Message
from constants.msg_type_constants import BORN
from entity.base_module.base_life import BaseLife
from entity.base_module.base_organization import BaseOrganization
from colorama import Fore

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
        BaseLife.__init__(self, row_location=row_location, col_location=col_location, name=name, maximum_age=150, lock=lock, energy=200)
        self.space = space
        self.logo = Fore.RED + name

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
                self.move()
            # if this life's energy is enough, then hava a baby
            if self.energy > 400:
                self.breed()
            self.death()
            self.energy -= 20
            self.space.show_space()
            self.act_count += 1
            self.lock.release()


    def breed(self, other_life: list[BaseLife] = None):
        """
        The concrete breed logic
        """
        if 50 < self.act_count < 100:
            # ensure the coordinates are valid.
            if self.space.check_valid(self.row_location - 1, self.col_location):
                # if exists a empty location
                if isinstance(self.space.space[self.row_location - 1][self.col_location], (int, PointLife)):
                    new_life = EKillerLife(self.row_location - 1, self.col_location, str(random.randint(1, 9)),
                                           self.space, self.lock)
                    self.space.add_entity(new_life)
                    self.energy -= 300
                    self.space.client.send_information(Message(BORN, count=1))


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
            self.move()
