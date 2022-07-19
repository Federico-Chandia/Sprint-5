class ProcesadorHtml:
    def __init__(self):
        self.elementos= []
        

    def append(self, elemento):
        self.elementos.append(elemento)

    def crear_html(self, cliente):
        transacciones = ''
        for e in self.elementos:
            transacciones += """<ul>
                <li>{fecha}</li>
                <li>{tipoop}</li>
                <li>{estado}</li>
                <li>{monto}</li>
                <li>{razon}</li>
            </ul>""".format(
                fecha = e['fecha'],
                tipoop = e['tipo'],
                estado = e['estado'],
                monto = e['monto'],
                razon = e['razon']
            ) 

        html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        *{{
            margin: 0;
            padding: 0;
            list-style-type: none;
            box-sizing: border-box;
            font-family: 'Courier New', Courier, monospace;
        }}
        body{{
            padding: 20px;
        }}
        .tabla{{
            display: flex;
            flex-direction: column;
        }}
        .tabla >ul{{
            display: grid;
            margin: 10px 0;
            grid-template-columns: 250px 350px 250px 200px 1fr;
            justify-content: right;
        }}
        .transacciones ul{{
            display: grid;
            grid-template-columns: 250px 350px 250px 200px 1fr;
            justify-content: right;
            border-top: 1px solid blueviolet;
            border-bottom: 1px solid blueviolet;
            align-items: center;
        }}
        .transacciones ul li{{
            padding: 20px 10px ;
            border-right: 1px solid blueviolet;
            border-left: 1px solid blueviolet;
        }}
    </style>
    <title>INFORME TRANSACCIONES</title>
</head>
<body>
    <h1>Informe de transacciones</h1>
    <ul>
        <li>Nombre: {nombre}</li>
        <li>DNI: {dni}</li>
        <li>Direccion: {direccion}</li>
    </ul>
    <div class="tabla">
        <ul class="titulos">
            <li>Fecha</li>
            <li>Tipo de operacion</li>
            <li>Estado</li>
            <li>Monto</li>
            <li>Razon de rechazo</li>
        </ul>
        <div class="transacciones">
            {transacciones}
        </div>
    </div>
</body>
</html>
            """.format(
                direccion= f"{cliente.direccion.calle} {cliente.direccion.numero} {cliente.direccion.ciudad} {cliente.direccion.provincia}",
                dni=cliente.numero,
                nombre=cliente.nombre,
                transacciones = transacciones
                # agregar
            )
        archivo = open("index.html", "w")
        archivo.write(html)
        archivo.close()