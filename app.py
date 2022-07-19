from .Cliente import cliente_classic, cliente_gold, cliente_black
from .Razon import Razon_Alta_Chequera,Razon_Alta_Tarjeta_Credito,Razon_Compra_Dolar,Razon_Retiro_Efectivo,Razon_Transferencia_Enviada,Razon_Transferencia_Recibida
import json


def leerJSON(filename):
    try:
        archivoJson = open(filename, "r", newline="")
        datos_cliente = json.load(archivoJson)
        archivoJson.close()
    except :
      return datos_cliente


def crearCliente(datos_cliente):
    if datos_cliente["tipo"] == "BLACK":
        cliente = cliente_black(datos_cliente)
    elif datos_cliente["tipo"] == "GOLD":
        cliente = cliente_gold(datos_cliente)
    elif datos_cliente["tipo"] == "CLASSIC":
        cliente = cliente_classic(datos_cliente)
    else:
        print("Todavia no fue definido ese tipo de cliente.")
    return cliente


def procesarTransacciones(transacciones, cliente):
    transacciones_procesadas = []   
    razon = ""
    for transaccion in transacciones:
        if transaccion["estado"] == "RECHAZADA":
            if transaccion["tipo"] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
                razon = Razon_Retiro_Efectivo().resolver(cliente, transaccion)
            elif transaccion["tipo"] == "ALTA_TARJETA_CREDITO":
                razon = Razon_Alta_Tarjeta_Credito().resolver(cliente, transaccion)
            elif transaccion["tipo"] == "ALTA_CHEQUERA":
                razon = Razon_Alta_Chequera().resolver(cliente, transaccion)
            elif transaccion["tipo"] == "COMPRA_DOLAR":
                razon = Razon_Compra_Dolar().resolver(cliente, transaccion)
            elif transaccion["tipo"] == "TRANSFERENCIA_ENVIADA":
                razon = Razon_Transferencia_Enviada().resolver(cliente, transaccion)
            elif transaccion["tipo"] == "TRANSFERENCIA_RECIBIDA":
                razon = Razon_Transferencia_Recibida().resolver(cliente, transaccion)
            else:
                print("Todavia no fue definida esta transaccion.")
        else:
            razon = ""
        transacciones_procesadas.append({"fecha": transaccion["fecha"], "tipo": transaccion["tipo"], "estado":transaccion["estado"], "monto": transaccion["monto"], "razon": razon})
    return transacciones_procesadas

def procesadorHtml(cliente, transacciones_procesadas):
    listado = ""
    for transaccion in transacciones_procesadas:
        listado += f"""
        <tr>
            <td>{transaccion["fecha"]}</td>
            <td>{transaccion["tipo"]}</td>
            <td>{transaccion["estado"]}</td>
            <td>{transaccion["monto"]}</td>
            <td>{transaccion["razon"]}</td>
        </tr>
        """
    contenido = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <title>Listado de Transacciones</title>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" />
    </head>
    <body class="container align-items-center justify-content-center">
        <header class="col">
            <h1 class="row mt-3">Listado de Transacciones</h1>
        </header>
        <section  id="datosCliente">
            <div class="row">
                <hr>
                <p>Nombre: {cliente.nombre} {cliente.apellido}</p>
                <hr>
                <p>Número de cliente: {cliente.numero}</p>
                <hr>
                <p>Documento: {cliente.dni}</p>
                <hr>
                <p>Dirección: {str(cliente.direccion)}</p>
                <hr>
                <details class="mb-3">
                    <summary>Tipo de cliente: {cliente.tipoDeCliente}</summary>
                </details">
                <hr>
            </div>
        </section>
        <section id="tabla">
            <table class="table">
                <thead>
                    <tr>
                        <th>Fecha</th>
                        <th>Tipo</th>
                        <th>Estado</th>
                        <th>Monto</th>
                        <th>Razón</th>
                    </tr>
                </thead> 
                <tbody>
                    {listado}
                </tbody>    
            </table>
        </section>
    </body>
    </html>
    """
    return contenido
if __name__ == "__main__":
    archivo = "eventos\eventos_classic.json"
    datos_cliente = leerJSON(archivo)
    if not datos_cliente == None:                   
        cliente = crearCliente(datos_cliente)       
        transacciones_procesadas = procesarTransacciones(datos_cliente["transacciones"], cliente)   # Array con las transacciones procesadas
        procesadorHtml(cliente, transacciones_procesadas)