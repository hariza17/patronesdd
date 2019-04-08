from abc import ABCMeta, abstractmethod


class Prototype(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def clone(self):
        pass
