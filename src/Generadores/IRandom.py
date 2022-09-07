from abc import ABC, abstractmethod

class IRandom(ABC):

    @abstractmethod
    def NumeroAleatorio(self, min : int, max : int) -> int:
        pass