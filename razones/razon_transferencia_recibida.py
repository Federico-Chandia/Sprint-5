from .razon import Razon

class RazonTransferenciaRecibida(Razon):
    def resolver(self, cliente, evento) -> str:
        if evento["monto"] > cliente.cuenta.limite_transferencia_recibida and cliente.cuenta.limite_transferencia_recibida != -1:   #-1 referencia a los clientes black
            return "Se ha excedido límite de transferencia sin aviso"
        else:
            return ""