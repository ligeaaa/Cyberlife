from entity.base_module.base_lifecycle import BaseLifecycle


class OriginLifecycle(BaseLifecycle):
    def __init__(self):
        self.lifecycle: dict = {
            "0": {"stage": 0, "name": "mature", "duration": 9000},
            "1": {"stage": 1, "name": "caducity", "duration": 1000},
            "2": {"stage": 2, "name": "death", "duration": 0}
        }
        self.stage = self.lifecycle["0"]

    def next_stage(self):
        super().next_stage()

    def check_end(self):
        super().check_end()