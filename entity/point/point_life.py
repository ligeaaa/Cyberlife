import random
import threading
import time

from entity.base_module.base_life import BaseLife
from entity.base_module.base_organization import BaseOrganization
from colorama import Fore

class PointLife(BaseLife, threading.Thread):
    """
    The simplest life, which can only move, breed and die.
    Producers
    """

    # move direction
    move_direction = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    def __init__(self, row_location, col_location, name, space, lock):
        threading.Thread.__init__(self)
        BaseLife.__init__(self, row_location=row_location, col_location=col_location, name=name, maximum_age=50)
        self.lock = lock
        self.space = space
        self.logo = Fore.GREEN + name

    def run(self):
        """
        Every random 1-5s move
        :return:
        """
        while True:
            random_interval = random.randint(1, 5)
            time.sleep(random_interval)
            self.lock.acquire()
            if self.death_flag:
                if self.space.space[self.row_location][self.col_location] == self:
                    self.space.space[self.row_location][self.col_location] = 0
                self.space.entities.remove(self)
                self.lock.release()
                break
            self.move()
            self.breed()
            self.death()
            self.lock.release()

    def move(self):
        """
        The concrete move logic
        :return:
        """
        random_number = random.randint(0, 3)
        row_move, col_move = self.move_direction[random_number]
        target_row = row_move + self.row_location
        target_col = col_move + self.col_location
        if self.space.check_valid(target_row, target_col):
            if self.space.space[target_row][target_col] == 0:
                self.space.space[self.row_location][self.col_location] = 0
                self.row_location = self.row_location + row_move
                self.col_location = self.col_location + col_move
                self.space.space[self.row_location][self.col_location] = self
                self.space.show_space()

    def breed(self, other_life: list[BaseLife] = None):
        now_time = time.time()
        # if this entity has lived for 20 seconds
        if now_time - self.birth_time > 35:
            # find round location and ensure the coordinates are valid.
            if self._find_round_location() and self.space.check_valid(self.row_location - 1, self.col_location):
                # if exists a empty location
                if self.space.space[self.row_location - 1][self.col_location] == 0:
                    new_point_life = PointLife(self.row_location - 1, self.col_location, str(random.randint(1, 9)), self.space, self.lock)
                    self.space.add_entity(new_point_life)

    def death(self):
        now_time = time.time()
        if now_time - self.birth_time > self.maximum_age:
            self.death_flag = True

    def _find_round_location(self):
        """
        Look for any living things in the surrounding 3 by 3 plots
        """
        left = self.col_location - 1
        top = self.row_location - 1
        step = 3
        for i in range(step):
            for j in range(step):
                if self.space.check_valid(top + i, left + j):
                    if isinstance(self.space.space[top + i][left + j], PointLife):
                        return True
        return False

