from .razon import Razon

class RazonCompraDolar(Razon):
    def resolver(self, cliente, evento) -> str:
        if cliente.puede_comprar_dolar() == False:
            return "La cuenta no permite realizar compra de dólares"
        elif evento["monto"] > evento["saldoEnCuenta"]:
            return "Se ha excedido el saldo de la cuenta"
        else:
            return ""