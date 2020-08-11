import time
from collections import deque

DEQUE_LIMIT = 100

#TODO: tuple specification

class LidarCom:
    def __init__(self):
        self.deque = deque(DEQUE_LIMIT)

    def add(self, tuple):
        self.deque.append(tuple)

    def is_lidar_backward_collision():
        for elem in self.deque:
            pass
        return False

    def is_lidar_forward_collision():
        for elem in self.deque:
            pass
        return False

LidarCom()