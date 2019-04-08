from abc import ABC, abstractmethod


class Orchestra(ABC):
    @abstractmethod
    def create_instrument(self):
        pass
