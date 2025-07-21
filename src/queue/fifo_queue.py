from queue import Queue
from typing import Any


class FifoQueue:

    def __init__(self):
        self.__queue = Queue()

    @property
    def get_element(self):
        return self.__queue.get()

    def add_element(self, value: Any):
        self.__queue.put(value)

    def __sizeof__(self):
        return self.__queue.qsize()
