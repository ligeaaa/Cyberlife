import pickle
import random
import threading
import time

from common.client.main_client import Client
from common.get_time import get_real_time
from common.msg import Message
from common.server.main_server import Server
from entity.base_module.base_life import BaseLife
from colorama import init
import socket


class Space:
    count = 0
    save_space = []

    def __init__(self, row, column, connect=None):
        init(autoreset=True)
        self.row = row
        self.column = column
        self.connect = connect
        self.space = self._init_space()
        self.entities = []
        server_thread = threading.Thread(target=self._init_server)
        server_thread.start()
        time.sleep(1)
        client_thread = threading.Thread(target=self._init_client)
        client_thread.start()

    def _init_space(self):
        """
        Pad the space with zeros
        """
        world = []
        for i in range(self.row):
            row = []
            for j in range(self.column):
                row.append(0)
            world.append(row)
        return world

    def show_space(self):
        """
        print the world
        """
        for i in range(self.row):
            for j in range(self.column):
                print(f"{self.space[i][j]} ", end='')
            print()
        print(f"-----------{self.count}------------")
        self.count = self.count + 1
        print(self.server.data_storage)
        # Todo 设计保存逻辑
        # self.save_space.append(self)

    def add_entity(self, entity: BaseLife):
        """
        add the entity in the world
        """
        self.entities.append(entity)
        # init entity in the world
        self.space[entity.row_location][entity.col_location] = entity
        self.show_space()
        entity.start()

    def check_valid(self, target_row, target_col):
        """
        check whether the expected move([target_row, target_col]) is valid
        """
        # 判定边界
        if 0 <= target_row < len(self.space) and 0 <= target_col < len(self.space[0]):
            return True
        return False

    def _init_client(self):
        self.client = Client()

    def _init_server(self):
        self.server = Server()
        self.server.start()

    def save_to_file(self, filename):
        """
        将 Space 对象保存到文件
        """
        # 保存 Space 对象的部分属性，而不包括线程对象
        space_data = {
            'row': self.row,
            'column': self.column,
            'space': self.space,
            'entities': self.entities
        }
        with open(filename, 'wb') as f:
            pickle.dump(space_data, f)

    @classmethod
    def load_from_file(cls, filename):
        """
        从文件中加载 Space 对象
        """
        with open(filename, 'rb') as f:
            space = pickle.load(f)
        return space

    def move(self, life: BaseLife, horizontal_movement: int, vertical_movement: int):
        """
        :param life: entity
        :param horizontal_movement: The distance of movement
                                    where negative values indicate left and positive values indicate right.
        :param vertical_movement:   The distance of movement
                                    where negative values indicate down and positive values indicate up.
        :return: boolean
        """
        # random_number = random.randint(0, 3)
        # row_move, col_move = self.move_direction[random_number]
        # target_row = row_move + self.row_location
        # target_col = col_move + self.col_location
        # if self.space.check_valid(target_row, target_col):
        #     if self.space.space[target_row][target_col] == 0:
        #         self.space.space[self.row_location][self.col_location] = 0
        #         self.row_location = self.row_location + row_move
        #         self.col_location = self.col_location + col_move
        #         self.space.space[self.row_location][self.col_location] = self


