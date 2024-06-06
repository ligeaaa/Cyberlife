import random
import threading
import time

from entity.base_module.base_life import BaseLife
from entity.base_module.base_organization import BaseOrganization


class PointLife(BaseLife, threading.Thread):
    move_direction = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    def __init__(self, row_location, col_location, name, space, lock):
        threading.Thread.__init__(self)
        BaseLife.__init__(self)
        self.row_location = row_location
        self.col_location = col_location
        self.name = name
        self.lock = lock
        self.space = space

    def run(self):
        while True:
            # 生成1到5之间的随机整数
            random_interval = random.randint(1, 5)
            time.sleep(random_interval)
            self.lock.acquire()
            self.move()
            self.lock.release()

    def move(self):
        random_number = random.randint(0, 3)
        row_move, col_move = self.move_direction[random_number]
        if self.check_move(row_move, col_move):
            self.space.space[self.row_location][self.col_location] = 0
            self.row_location = self.row_location + row_move
            self.col_location = self.col_location + col_move
            self.space.space[self.row_location][self.col_location] = self.name
            self.space.show_space()

    def check_move(self, row_move, col_move):
        target_row = row_move + self.row_location
        target_col = col_move + self.col_location
        # 判定边界
        if 0 < target_row < len(self.space.space) and 0 < target_col < len(self.space.space[0]):
            # 判定是否有障碍
            if self.space.space[target_row][target_col] == 0:
                return True
        return False
