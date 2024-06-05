class BaseLifecycle:
    def __init__(self):
        self.lifecycle: dict = ...
        self.stage = self.lifecycle["0"]

    def next_stage(self):
        self.stage = self.lifecycle[self.stage["stage"]]


    def check_end(self):
        ...