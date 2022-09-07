import imp
from IRandom import IRandom

class ValorFijo(IRandom):

    def __init__(self, valor_fijo : int):
        self.valor_fijo = valor_fijo

    def NumeroAleatorio(self, min : int, max : int) -> int:
        return self.valor_fijo