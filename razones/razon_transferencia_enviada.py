from .razon import Razon

class RazonTransferenciaEnviada(Razon):
    def resolver(self, cliente, evento) -> str:
        if evento["monto"]*(1+cliente.cuenta.costo_transferencias) > evento["saldoEnCuenta"]:
            return "Se ha excedido el saldo de la cuenta (con comisión incluída)"
        else:
            return ""