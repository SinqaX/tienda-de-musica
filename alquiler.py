class Alquiler:
    numeroDeFactura = 1

    def __init__(self, nombreUsuario, codigoUsuario, tiempoAlquiler, nombreInstrumento, totalPagar):
        self.numeroFactura = Alquiler.numeroDeFactura
        Alquiler.numeroDeFactura += 1
        self.nombreUsuario = nombreUsuario
        self.cedulaUsuario = codigoUsuario
        self.tiempoAlquiler = tiempoAlquiler
        self.nombreInstrumento = nombreInstrumento
        self.totalPagar = totalPagar
        self.salvamento = False

    def __str__(self):
        return f"""  
    --------FACTURA N° |{self.numeroFactura}|--------   
_______________________________________
    Nombre del usuario:     {self.nombreUsuario}        
    Cedula del usuario:     {self.cedulaUsuario}        
    Tiempo de alquiler:     {self.tiempoAlquiler} dia(s)
    Nombre del instrumento: {self.nombreInstrumento}    
    Salvamento:             {self.salvamento}           
--------------------------------------
        TOTAL A PAGAR:      {self.totalPagar}"""



