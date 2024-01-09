class Venta:

    def __init__(self, cedulaCliente, nombreInstrumento, fecha, totalPagar):
        self.cedulaCliente = cedulaCliente
        self.nombreInstrumento = nombreInstrumento
        self.fecha = fecha
        self.productos = []
        self.totalPagar = totalPagar

    def generarFacturaVenta(self,):
        pass

class VentaSeparado(Venta):

    def __init__(self, nombreCliente, nombreInstrumento, fecha, cantidad, totalPagar, abono):
        super().__init__(nombreCliente, nombreInstrumento, fecha, cantidad, totalPagar)
        self.abono = 0


