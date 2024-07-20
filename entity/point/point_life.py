import random
import threading
import time

from common.msg import Message
from constants.msg_type_constants import BORN
from entity.base_module.base_life import BaseLife
from colorama import Fore

from entity.point.organization.point_leg import PointLeg
from entity.point.organization.point_sex import PointSex


class PointLife(BaseLife, threading.Thread):
    """
    The simplest life, which can only move, breed and die.
    Producers
    """

    def __init__(self, row_location, col_location, name, space, lock):
        threading.Thread.__init__(self)
        BaseLife.__init__(self, row_location=row_location, col_location=col_location, name=name, maximum_age=50,
                          lock=lock, energy=200, min_childbearing_age=10, max_childbearing_age=50)
        self.space = space
        self.logo = Fore.GREEN + name
        self.leg = PointLeg(self)
        self.sex = PointSex(self)



    def run(self):
        """
        Every random 1-5s move
        :return:
        """
        while True:
            random_interval = random.randint(1, 5)
            time.sleep(random_interval / self.space.time_flow_rate)
            self.lock.acquire()
            if self.death_flag:
                self.clear_life()
                break
            self.leg.move(self.space)
            self.sex.breed(PointLife)
            self.death()
            self.energy -= 1
            self.send_message()
            self.space.show_space()
            self.act_count += 1
            self.lock.release()


    def avoid(self):
        ...

