from .razon import Razon

class RazonAltaChequera(Razon):
    def resolver(self, cliente, evento) -> str:
        if cliente.puede_crear_chequera() == False:
            return "La cuenta no permite solicitar chequeras"
        elif evento["totalChequerasActualmente"] >=  cliente.cuenta.limite_chequeras:
            return "Se ha excedido el límite de chequeras"
        else:
            return ""