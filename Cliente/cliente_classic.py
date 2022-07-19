from .cliente import Cliente
from .cuenta import Cuenta
class Classic(Cliente):

    def __init__(self, datos_cliente):
        valores = [10000,150000,0,0.01,0,0,0]     #últimos 2 valores agregados

        super().__init__(datos_cliente)
        self.cuenta = Cuenta(valores)

    def puede_crear_chequera(self) -> bool:
        return False
    def puede_crear_tarjeta_credito(self) -> bool:
        return False
    def puede_comprar_dolar(self) -> bool:
        return False