from abc import ABC, abstractmethod
from IElemento import IElemento

class IExperimentoAleatorio(ABC):

    @abstractmethod
    def GenerarMovimiento(self) -> IElemento:
        pass

