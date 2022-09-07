from src.Generadores.DadoNLados import DadoNLados
from src.IExperimentoAleatorio import IExperimentoAleatorio
from src.IElemento import IElemento
from ElementoPrueba import ElementoPrueba

class TiradaDeNDados(IExperimentoAleatorio):

    def __init__(self, cantidad_dados : int, dado : DadoNLados):
        self.dado = dado
        self.cantidad_dados = cantidad_dados

    def GenerarMovimiento(self) -> IElemento:
        valores = []
        for i in range(self.cantidad_dados):
            valores.append(self.dado.GenerarElemento())
        return ElementoPrueba(valores) 
