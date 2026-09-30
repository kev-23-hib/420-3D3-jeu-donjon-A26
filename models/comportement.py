from abc import ABC, abstractclassmethod


class comportements(ABC):
    @abstractclassmethod
    def agir(self):
        pass