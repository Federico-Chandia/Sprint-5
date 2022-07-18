from .razon import Razon

class RazonRetiroEfectivo(Razon):
    def resolver(self,cliente, evento) -> str:
        if evento["monto"] > cliente.cuenta.limite_extraccion_diario or evento["monto"] > evento["cupoDiarioRestante"]:
            return "El monto a retirar excede el límite de extracción diario"
        elif abs(evento["saldoEnCuenta"] - evento["monto"]) > cliente.cuenta.saldo_descubierto_disponible:
            return "El retiro excede el saldo descubierto disponible"
        else:
            return ""