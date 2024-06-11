import threading
import time

from common.msg import Message
from constants.entity_constants.entity_gender import NEUTER
from constants.msg_type_constants import DEATH
from entity.base_module.base_lifecycle import BaseLifecycle
from entity.base_module.base_organization import BaseOrganization
from colorama import Fore


class BaseLife:
    def __init__(self,
                 maximum_age: float = None,
                 gender: int = NEUTER,
                 lifecycle: BaseLifecycle = None,
                 birth_place: str = "place",
                 productor: list['BaseLife'] = None,
                 name: str = "life",
                 row_location: int = 0,
                 col_location: int = 0,
                 lock: threading.Lock = None,
                 energy: float = 0):
        self.maximum_age = maximum_age         # life's maximum age
        self.gender = gender                   # life's gender
        self.lifecycle = lifecycle             # life's lifecycle
        self.birth_time = time.time()          # when life born
        self.birth_place = birth_place         # where life born
        self.productor = productor             # who or which produce this life
        self.name = name                       # life's name
        self.row_location = row_location       # life's row index
        self.col_location = col_location       # life's column index
        self.logo = Fore.BLACK + "N"           # how this life is shown on the world
        self.death_flag = False                # whether this life is dead
        self.id = None                         # life's id
        self.energy = energy                   # life's energy in their body
        self.space = None        # Which world does this life belong to
        self.lock = lock                       # Thread lock

    def absorbed_energy(self, organization: BaseOrganization = None, energy_resource=None):
        """
        This is a function that allows this life absorb energy grom energy resource by some organization
        :param organization:
        :param energy_resource:
        """
        ...

    def breed(self, other_life: list['BaseLife'] = None):
        """
        This is a function that allows this life to reproduce another life
        :param other_life:
        :return:
        """
        ...

    def death(self):
        """
        The concrete death logic. (However, life can also die without this function)
        """
        now_time = time.time()
        if now_time - self.birth_time > self.maximum_age:
            self.death_flag = True
        if self.energy < 0:
            self.death_flag = True

    def growth(self):
        """
        This is a function that allows this life to grow
        :return:
        """
        ...

    def _find_round_location(self, life_type, step):
        """
        Look for any living things in the surrounding 3 by 3 plots
        """
        left = self.col_location - step
        top = self.row_location - step
        steps = step * 2 + 1
        for i in range(steps):
            for j in range(steps):
                if self.space.check_valid(top + i, left + j):
                    if isinstance(self.space.space[top + i][left + j], life_type):
                        return True
        return False

    def clear_life(self):
        if self.space.space[self.row_location][self.col_location] == self:
            # clear this life in the world
            self.space.space[self.row_location][self.col_location] = 0
        # and also clear this life ine world's entity list
        self.space.entities.remove(self)
        self.space.client.send_information(Message(DEATH, count=1))
        self.lock.release()


    def send_message(self):
        """
        send message to world server
        """
        ...


    def __str__(self):
        return str(self.logo)


if __name__ == '__main__':
    a = BaseLife()
