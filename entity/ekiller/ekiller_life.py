import random
import threading
import time

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

    # move direction
    move_direction = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    def __init__(self, row_location, col_location, name, space, lock):
        threading.Thread.__init__(self)
        BaseLife.__init__(self, row_location=row_location, col_location=col_location, name=name, maximum_age=150)
        self.lock = lock
        self.space = space
        self.logo = Fore.RED + name
        self.energy = 200

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
            if self.energy < 500:
                self.hunt()
            else:
                self.move()
            if self.energy > 300:
                self.breed()
            self.death()
            self.energy -= 20
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
        if now_time - self.birth_time > 100:
            # ensure the coordinates are valid.
            if self.space.check_valid(self.row_location - 1, self.col_location):
                # if exists a empty location
                if self.space.space[self.row_location - 1][self.col_location] == 0:
                    new_life = EKillerLife(self.row_location - 1, self.col_location, str(random.randint(1, 9)),
                                           self.space, self.lock)
                    self.space.add_entity(new_life)
                    self.energy -= 300

    def death(self):
        now_time = time.time()
        if now_time - self.birth_time > self.maximum_age:
            self.space.space[self.row_location][self.col_location] = 0
            self.death_flag = True
        if self.energy < 0:
            self.death_flag = True

    def hunt(self):
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
