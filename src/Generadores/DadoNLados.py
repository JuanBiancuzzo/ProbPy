from IRandom import IRandom

class DadoNLados:

    numero_minimo = 1

    def __init__(self, cantidad_lados : int, generador : IRandom):
        self.cantidad_lados = cantidad_lados
        self.generador = generador

    def GenerarElemento(self) -> int:
        return self.generador.NumeroAleatorio(DadoNLados.numero_minimo, self.cantidad_lados)
    