class Alquiler:

    def __init__(self, nombreUsuario, codigoUsuario, tiempoAlquiler, nombreInstrumento, totalPagar):
        self.nombreUsuario = nombreUsuario
        self.cedulaUsuario = codigoUsuario
        self.tiempoAlquiler = tiempoAlquiler
        self.nombreInstrumento = nombreInstrumento
        self.totalPagar = totalPagar
        self.salvamento = False

    def __str__(self):
        return f"Nombre del usuario: {self.nombreUsuario} \nCedula del usuario: {self.cedulaUsuario} \nTiempo de alquiler: {self.tiempoAlquiler} \nNombre del instrumento: {self.nombreInstrumento} \nTOTAL A PAGAR: {self.totalPagar} \nSalvamento: {self.salvamento}\n"




