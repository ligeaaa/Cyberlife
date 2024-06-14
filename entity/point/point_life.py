import random
import threading
import time

from common.msg import Message
from constants.msg_type_constants import BORN
from entity.base_module.base_life import BaseLife
from entity.base_module.base_organization import BaseOrganization
from colorama import Fore

class PointLife(BaseLife, threading.Thread):
    """
    The simplest life, which can only move, breed and die.
    Producers
    """

    def __init__(self, row_location, col_location, name, space, lock):
        threading.Thread.__init__(self)
        BaseLife.__init__(self, row_location=row_location, col_location=col_location, name=name, maximum_age=50, lock=lock, energy=200)
        self.space = space
        self.logo = Fore.GREEN + name

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
            self.move()
            self.breed()
            self.death()
            self.energy -= 1
            self.send_message()
            self.space.show_space()
            self.act_count += 1
            self.lock.release()


    def breed(self, other_life: list[BaseLife] = None):
        # if this entity has lived for 20 seconds
        if 10 < self.act_count:
            # find round location and ensure the coordinates are valid.
            if self._find_round_location(PointLife, 1) and self.space.check_valid(self.row_location - 1, self.col_location):
                # if exists a empty location
                if self.space.space[self.row_location - 1][self.col_location] == 0:
                    new_point_life = PointLife(self.row_location - 1, self.col_location, str(random.randint(1, 9)), self.space, self.lock)
                    self.space.add_entity(new_point_life)
                    self.energy -= 10
                    self.space.client.send_information(Message(BORN, count=1))

    def avoid(self):





        ...

