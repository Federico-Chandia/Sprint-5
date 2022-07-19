from .razon import Razon

class RazonAltaTarjetaCredito(Razon):
    def resolver(self, cliente, evento) -> str:
        if cliente.puede_crear_tarjeta_credito() == False:
            return "La cuenta no permite solicitar tarjetas de crédito"
        elif evento["totalTarjetasDeCreditoActualmente"] >=  cliente.cuenta.limite_tarjetas_credito:
            return "Se ha excedido el límite de tarjetas de crédito"
        else:
            return ""