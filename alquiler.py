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
        return f"-----Numero de Factura {self.numeroFactura}----- \nNombre del usuario: {self.nombreUsuario} \nCedula del usuario: {self.cedulaUsuario} \nTiempo de alquiler: {self.tiempoAlquiler} dia(s) \nNombre del instrumento: {self.nombreInstrumento} \nSalvamento: {self.salvamento} \nTOTAL A PAGAR: {self.totalPagar}\n"



