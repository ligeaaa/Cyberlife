import os
import pickle
import sys
import threading
import time

from common.client.main_client import Client
from common.server.main_server import Server
from entity.base_module.base_life import BaseLife
from colorama import init


def check_data_empty(space: list):
    while True:
        flag = True
        for row in space:
            for value in row:
                if value != 0:
                    flag = False
                    break
        if flag:
            print(f"{time.time()}: NO LIFE IN SPACE")
        time.sleep(1)


class Space:
    count = 0
    save_space = []

    def __init__(self, row, column, connect=False, time_flow_rate=1):
        init(autoreset=True)
        self.row = row
        self.column = column
        self.connect = connect
        self.time_flow_rate = time_flow_rate
        self.space = self._init_space()
        self.entities = []
        self.old_time = time.time()
        server_thread = threading.Thread(target=self._init_server)
        server_thread.start()
        time.sleep(1)
        client_thread = threading.Thread(target=self._init_client)
        client_thread.start()

        # Thread used to check whether all entity died
        check_thread = threading.Thread(target=check_data_empty, args=(self.space,))
        check_thread.daemon = True
        check_thread.start()

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
        # don't show space too quick
        if time.time() - self.old_time < 1:
            return
        else:
            if sys.stdin.isatty():
                if os.name == 'nt':
                    _ = os.system('cls')
                else:
                    _ = os.system('clear')
            self.old_time = time.time()

        # Todo pref, do not use loop, but print it at once
        for i in range(self.row):
            for j in range(self.column):
                print(f"{self.space[i][j]} ", end='')
            print()
        print(f"-----------{self.count}------------")
        self.count = self.count + 1
        print(self.server.data_storage)
        # Todo save important data about space and entites
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

    def move_life(self, life: BaseLife, vertical_movement: int, horizontal_movement: int):
        """
        :param life: entity
        :param horizontal_movement: The distance of movement
                                    where negative values indicate left and positive values indicate right.
        :param vertical_movement:   The distance of movement
                                    where negative values indicate down and positive values indicate up.
        :return: boolean
        """
        if life not in self.entities:
            return False
        row_location = life.row_location
        col_location = life.col_location
        target_row = vertical_movement + row_location
        target_col = horizontal_movement + col_location
        if self.check_valid(target_row, target_col):
            if self.space[target_row][target_col] == 0:
                self.space[row_location][col_location] = 0
                life.row_location = life.row_location + vertical_movement
                life.col_location = life.col_location + horizontal_movement
                self.space[target_row][target_col] = life
        self.show_space()

    def _get_wrapped_position(self, x, y):
        """
        Get the wrapped position to handle the boundary conditions
        """
        wrapped_x = x % self.row
        wrapped_y = y % self.column
        return wrapped_x, wrapped_y

    def get_value(self, x, y):
        """
        Get the value at the position (x, y) with wrapping around the edges
        """
        wrapped_x, wrapped_y = self._get_wrapped_position(x, y)
        return self.space[wrapped_x][wrapped_y]

    def set_value(self, x, y, value):
        """
        Set the value at the position (x, y) with wrapping around the edges
        """
        wrapped_x, wrapped_y = self._get_wrapped_position(x, y)
        self.space[wrapped_x][wrapped_y] = value


if __name__ == "__main__":
    # Example usage
    space = Space(5, 5)
    space.show_space()
