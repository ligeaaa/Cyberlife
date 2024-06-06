import random
import threading
import time

from entity.base_module.base_life import BaseLife


class Space:
    count = 0

    def __init__(self, row, column, connect=None):
        self.row = row
        self.column = column
        self.connect = connect
        self.space = self._init_space()
        self.entities = []

    def _init_space(self):
        world = []
        for i in range(self.row):
            row = []
            for j in range(self.column):
                row.append(0)
            world.append(row)
        return world

    def show_space(self):
        for i in range(self.row):
            for j in range(self.column):
                print(f"{self.space[i][j]} ", end='')
            print()
        print(f"-----------{self.count}------------")
        self.count = self.count + 1

    def add_entity(self, entity: BaseLife):
        self.entities.append(entity)
        self.space[entity.row_location][entity.col_location] = entity.name
        self.show_space()


    def init_world(self):
        for entity in self.entities:
            # self.start(entity)
            entity.start()

    # def start(self, entity):
    #     while True:
    #         # 生成1到5之间的随机整数
    #         random_interval = random.randint(1, 5)
    #         print(f"等待 {random_interval} 秒...")
    #         time.sleep(random_interval)
    #
    #         self.move()




