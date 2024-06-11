import random
import threading
import time

from common.client.main_client import Client
from common.msg import Message
from common.server.main_server import Server
from entity.base_module.base_life import BaseLife
from colorama import init
import socket


class Space:
    count = 0

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



