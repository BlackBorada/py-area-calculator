from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self, name) -> None:
        self.name = name

    @abstractmethod
    def area(self):
        raise NotImplementedError