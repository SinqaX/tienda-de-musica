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

    def __init__(self, nombreCliente, fecha, cantidad, totalPagar):
        super().__init__(nombreCliente, fecha, cantidad, totalPagar)
        self.abono = 0


