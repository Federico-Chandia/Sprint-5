class Direccion():
    calle =""
    numero=""
    ciudad=""
    provincia=""
    pais=""

    def __init__(self, direccion) -> None:
        self.calle = direccion["calle"]
        self.numero = direccion["numero"] 
        self.ciudad = direccion["ciudad"] 
        self.provincia = direccion["provincia"] 
        self.pais = direccion["pais"] 
        
    def __str__(self) -> str:
        return f"{self.calle} {self.numero}, {self.ciudad}, {self.provincia}, {self.pais}"