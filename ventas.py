class Venta:

    def __init__(self, cedulaCliente, fecha, totalPagar):
        self.cedulaCliente = cedulaCliente
        # self.nombreInstrumento = nombreInstrumento -----> BORRAR, YA HAY PRODUCTOS
        self.fecha = fecha
        self.productos = []
        self.totalPagar = totalPagar

    def generarFacturaVenta(self,):
        pass
class VentaSeparado(Venta):

    def __init__(self, nombreCliente, fecha, totalPagar, abono):
        super().__init__(nombreCliente, fecha, totalPagar, abono)
        self.abono = 0
    


