"""
Technically the scheduler is an iterator over url object list
It can be further extended with different schedule policy
"""
from abc import ABC, abstractmethod


class Scheduler(ABC):
    """
    An iterator which decide the sequence of url download
    """
    def __init__(self, url_list):
        self.url_list = url_list
        self.index = 0

    def __iter__(self):
        return self

    @abstractmethod
    def __next__(self):
        pass


class FIFOScheduler(Scheduler):
    """
    A primitive FIFO Scheduler (mainly serves as an example)
    """
    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.url_list):
            url = self.url_list[self.index]
            self.index += 1
            return url

        raise StopIteration
