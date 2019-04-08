from abc import ABC, abstractmethod


class Instrument(ABC):
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def play(self):
        pass
